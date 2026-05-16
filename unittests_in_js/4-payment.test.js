const sinon = require("sinon");
const assert = require("assert");
const Utils = require("./utils");
const sendPaymentRequestToApi = require("./4-payment");

describe("sendPaymentRequestToApi", function () {
  afterEach(function () {
    sinon.restore();
  });

  it("stubs Utils.calculateNumber and logs the total", function () {
    const stub = sinon.stub(Utils, "calculateNumber").returns(10);
    const spy = sinon.spy(console, "log");

    sendPaymentRequestToApi(100, 20);

    assert.strictEqual(stub.calledOnceWithExactly("SUM", 100, 20), true);
    assert.strictEqual(spy.calledOnceWithExactly("The total is: 10"), true);
  });
});