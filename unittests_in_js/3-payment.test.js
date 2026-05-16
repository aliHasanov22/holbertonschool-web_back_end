const sinon = require("sinon");
const assert = require("assert");
const Utils = require("./utils");
const sendPaymentRequestToApi = require("./3-payment");

describe("sendPaymentRequestToApi", function () {
  it("calls Utils.calculateNumber with the right arguments", function () {
    const spy = sinon.spy(Utils, "calculateNumber");

    sendPaymentRequestToApi(100, 20);

    assert.strictEqual(spy.calledOnceWithExactly("SUM", 100, 20), true);
    spy.restore();
  });
});