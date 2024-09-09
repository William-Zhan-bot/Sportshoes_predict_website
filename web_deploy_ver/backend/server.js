const express = require("express");
const path = require("path");
const { spawn } = require("child_process");
const { error } = require("console");
const app = express();

// 設定port
const port = process.env.PORT || 3000;
app.listen(port, () => {
  console.log(`PORT IS RUNNING ON ${port}`);
});

// middleware 
app.set("views", "/opt/render/project/src/web_deploy_ver/frontend/views/");
app.set("view engine", "ejs");
// 靜態檔案
const public = path.join(__dirname, "..", "frontend", "public");
app.use(express.static(public));

// 設定 req res
app.get("/", (req, res) => {
  const filePath = path.join(__dirname, "..", "frontend", "index.html");
  res.sendFile(filePath);
});

// deploy_test
app.get("/test", (req, res) => {
  res.send("deploy test ok!");
});

// 導入Python模組 設置async promise
const executepred = async (script, args) => {
  console.log("start predicting");

  const arguments = args.map((arg) => arg.toString());

  const aipy = path.join(__dirname, "..", "backend", "predict.py");
  console.log(aipy);

  const py = spawn("python", [aipy, ...arguments]);

  const result = await new Promise((resolve, reject) => {
    let output;

    // get output from script
    py.stdout.on("data", (data) => {
      console.log("Here");
      console.log(data);
      output = JSON.parse(data);
      console.log(output);
    });

    // err
    py.stderr.on("data", (data) => {
      console.error(`[python] Error occured: ${data}`);
      reject(`ERROR occured in ${script}`);
    });

    py.on("exit", (code) => {
      console.log(`child process exited with code ${code}`);
      resolve(output);
    });
  });
  return result;
};

// 預測結果
app.get("/result", async (req, res) => {
  try {
    const aipy = path.join(__dirname, "..", "backend", "predict.py");
    let query = req.query;
    console.log(query);
    const result = await executepred("python", [
      query.brand,
      query.size,
      query.gender,
      query.type,
      query.color,
      query.material,
    ]);
    res.render("result.ejs", { result: result, data: query });
    console.log("predict success", result);
  } catch (err) {
    console.log("err");
    console.log(err);
    res.status(500).json({ error: error });
  }
});
