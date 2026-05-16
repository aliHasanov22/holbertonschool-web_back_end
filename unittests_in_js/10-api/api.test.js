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

describe("Cart page", function () {
  it("returns status code 200 when id is a number", function (done) {
    request.get("http://localhost:7865/cart/12", (err, res) => {
      expect(res.statusCode).to.equal(200);
      done(err);
    });
  });

  it("returns the expected body when id is a number", function (done) {
    request.get("http://localhost:7865/cart/12", (err, res, body) => {
      expect(body).to.equal("Payment methods for cart 12");
      done(err);
    });
  });

  it("returns 404 when id is not a number", function (done) {
    request.get("http://localhost:7865/cart/hello", (err, res) => {
      expect(res.statusCode).to.equal(404);
      done(err);
    });
  });
});

describe("Available payments", function () {
  it("returns status code 200", function (done) {
    request.get("http://localhost:7865/available_payments", (err, res) => {
      expect(res.statusCode).to.equal(200);
      done(err);
    });
  });

  it("returns the expected object", function (done) {
    request.get("http://localhost:7865/available_payments", (err, res, body) => {
      expect(JSON.parse(body)).to.deep.equal({
        payment_methods: {
          credit_cards: true,
          paypal: false,
        },
      });
      done(err);
    });
  });
});

describe("Login", function () {
  it("returns status code 200", function (done) {
    request.post(
      {
        url: "http://localhost:7865/login",
        json: { userName: "Betty" },
      },
      (err, res) => {
        expect(res.statusCode).to.equal(200);
        done(err);
      }
    );
  });

  it("returns the expected body", function (done) {
    request.post(
      {
        url: "http://localhost:7865/login",
        json: { userName: "Betty" },
      },
      (err, res, body) => {
        expect(body).to.equal("Welcome Betty");
        done(err);
      }
    );
  });
});