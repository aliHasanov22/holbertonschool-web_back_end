const request = require("request");
const { expect } = require("chai");

describe("Index page", function () {
  it("returns status code 200", function (done) {
    request.get("http://localhost:7865", (err, res) => {
      expect(res.statusCode).to.equal(200);
      done(err);
    });
  });

  it("returns the expected body", function (done) {
    request.get("http://localhost:7865", (err, res, body) => {
      expect(body).to.equal("Welcome to the payment system");
      done(err);
    });
  });

  it("returns the correct content type", function (done) {
    request.get("http://localhost:7865", (err, res) => {
      expect(res.headers["content-type"]).to.include("text/html");
      done(err);
    });
  });
});