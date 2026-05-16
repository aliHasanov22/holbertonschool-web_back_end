const sinon = require("sinon");
const assert = require("assert");
const sendPaymentRequestToAPI = require("./5-payment");

describe("sendPaymentRequestToAPI", function () {
  let consoleSpy;

  beforeEach(function () {
    consoleSpy = sinon.spy(console, "log");
  });

  afterEach(function () {
    consoleSpy.restore();
  });

  it("logs the total for 100 and 20", function () {
    sendPaymentRequestToAPI(100, 20);
    assert.strictEqual(consoleSpy.calledOnceWithExactly("The total is: 120"), true);
  });

  it("logs the total for 10 and 10", function () {
    sendPaymentRequestToAPI(10, 10);
    assert.strictEqual(consoleSpy.calledOnceWithExactly("The total is: 20"), true);
  });
});