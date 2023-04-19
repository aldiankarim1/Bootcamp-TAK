const request_url = require("supertest")("https://restful-booker.herokuapp.com");
const assert = require("chai").expect;

describe("User", function () {
    it("Success Create User", async function () {
        const body = {
            firstname : "Aldian",
            lastname : "Karim",
            totalprice : 5000,
            depositpaid : true,
            bookingdates : {
                checkin : "2023-04-16",
                checkout : "2023-04-17"
            },
            additionalneeds : "Breakfast"
        }

        const response = await request_url
            .post("/booking")
            .set('Accept', 'application/json')
            .send(body);

            assert(response.statusCode).to.eql(200);
            assert(response.body.booking.firstname).to.eql("Aldian");
            assert(response.body.booking.lastname).to.eql("Karim");
            assert(response.body.booking.totalprice).to.eql(5000);
            assert(response.body.booking.depositpaid).to.eql(true);
            assert(response.body.booking.bookingdates.checkin).to.eql("2023-04-16");
            assert(response.body.booking.bookingdates.checkout).to.eql("2023-04-17");
            assert(response.body.booking.additionalneeds).to.eql("Breakfast");
    })
    it("Success Get All Data ID", async function () {

        const response = await request_url
            .get("/booking")
            .set('Accept', 'application/json')
            .send();
            assert(response.statusCode).to.eql(200);
    })
    it("Success Get Data by ID", async function () {

        const response = await request_url
            .get("/booking/1")
            .set('Accept', 'application/json')
            .send();
            assert(response.statusCode).to.eql(200);
    })
    it("Create Booking with firstname empty", async () => {
        const body = {
            firstname : "",
            lastname : "Karim",
            totalprice : 5000,
            depositpaid : true,
            bookingdates : {
                checkin : "2023-04-16",
                checkout : "2023-04-17"
            },
            additionalneeds : "Breakfast"
        }

        const response = await request_url
            .post("/booking")
            .set('Accept', 'application/json')
            .send(body);

            assert(response.statusCode).to.eql(200);
            assert(response.body.booking.firstname).to.eql("");
            assert(response.body.booking.lastname).to.eql("Karim");
            assert(response.body.booking.totalprice).to.eql(5000);
            assert(response.body.booking.depositpaid).to.eql(true);
            assert(response.body.booking.bookingdates.checkin).to.eql("2023-04-16");
            assert(response.body.booking.bookingdates.checkout).to.eql("2023-04-17");
            assert(response.body.booking.additionalneeds).to.eql("Breakfast");
    })
    it("Create Booking with lastname empty", async () => {
        const body = {
            firstname : "Aldian",
            lastname : "",
            totalprice : 5000,
            depositpaid : true,
            bookingdates : {
                checkin : "2023-04-16",
                checkout : "2023-04-17"
            },
            additionalneeds : "Breakfast"
        }

        const response = await request_url
            .post("/booking")
            .set('Accept', 'application/json')
            .send(body);

            assert(response.statusCode).to.eql(200);
            assert(response.body.booking.firstname).to.eql("Aldian");
            assert(response.body.booking.lastname).to.eql("");
            assert(response.body.booking.totalprice).to.eql(5000);
            assert(response.body.booking.depositpaid).to.eql(true);
            assert(response.body.booking.bookingdates.checkin).to.eql("2023-04-16");
            assert(response.body.booking.bookingdates.checkout).to.eql("2023-04-17");
            assert(response.body.booking.additionalneeds).to.eql("Breakfast");
    })
    it("Create Booking with totalprice is empty", async () => {
        const body = {
            firstname : "Aldian",
            lastname : "Karim",
            totalprice : "",
            depositpaid : true,
            bookingdates : {
                checkin : "2023-04-16",
                checkout : "2023-04-17"
            },
            additionalneeds : "Breakfast"
        }

        const response = await request_url
            .post("/booking")
            .set('Accept', 'application/json')
            .send(body);

            assert(response.statusCode).to.eql(200);
            assert(response.body.booking.firstname).to.eql("Aldian");
            assert(response.body.booking.lastname).to.eql("Karim");
            assert(response.body.booking.totalprice).to.eql(null);
            assert(response.body.booking.depositpaid).to.eql(true);
            assert(response.body.booking.bookingdates.checkin).to.eql("2023-04-16");
            assert(response.body.booking.bookingdates.checkout).to.eql("2023-04-17");
            assert(response.body.booking.additionalneeds).to.eql("Breakfast");
    })
    it("Create Booking with depositpaid empty", async () => {
        const body = {
            firstname : "Aldian",
            lastname : "Karim",
            totalprice : 5000,
            depositpaid : "",
            bookingdates : {
                checkin : "2023-04-16",
                checkout : "2023-04-17"
            },
            additionalneeds : "Breakfast"
        }

        const response = await request_url
            .post("/booking")
            .set('Accept', 'application/json')
            .send(body);

            assert(response.statusCode).to.eql(200);
            assert(response.body.booking.firstname).to.eql("Aldian");
            assert(response.body.booking.lastname).to.eql("Karim");
            assert(response.body.booking.totalprice).to.eql(5000);
            assert(response.body.booking.depositpaid).to.eql(false);
            assert(response.body.booking.bookingdates.checkin).to.eql("2023-04-16");
            assert(response.body.booking.bookingdates.checkout).to.eql("2023-04-17");
            assert(response.body.booking.additionalneeds).to.eql("Breakfast");
    })
    it("Create Booking with checkin empty", async () => {
        const body = {
            firstname : "Aldian",
            lastname : "Karim",
            totalprice : 5000,
            depositpaid : true,
            bookingdates : {
                checkin : "",
                checkout : "2023-04-17"
            },
            additionalneeds : "Breakfast"
        }

        const response = await request_url
            .post("/booking")
            .set('Accept', 'application/json')
            .send(body);

            assert(response.statusCode).to.eql(200);
            assert(response.body.booking.firstname).to.eql("Aldian");
            assert(response.body.booking.lastname).to.eql("Karim");
            assert(response.body.booking.totalprice).to.eql(5000);
            assert(response.body.booking.depositpaid).to.eql(true);
            assert(response.body.booking.bookingdates.checkin).to.eql("0NaN-aN-aN");
            assert(response.body.booking.bookingdates.checkout).to.eql("2023-04-17");
            assert(response.body.booking.additionalneeds).to.eql("Breakfast");
    })
    it("Create Booking with checkout empty", async () => {
        const body = {
            firstname : "Aldian",
            lastname : "Karim",
            totalprice : 5000,
            depositpaid : true,
            bookingdates : {
                checkin : "2023-04-16",
                checkout : ""
            },
            additionalneeds : "Breakfast"
        }

        const response = await request_url
            .post("/booking")
            .set('Accept', 'application/json')
            .send(body);

            assert(response.statusCode).to.eql(200);
            assert(response.body.booking.firstname).to.eql("Aldian");
            assert(response.body.booking.lastname).to.eql("Karim");
            assert(response.body.booking.totalprice).to.eql(5000);
            assert(response.body.booking.depositpaid).to.eql(true);
            assert(response.body.booking.bookingdates.checkin).to.eql("2023-04-16");
            assert(response.body.booking.bookingdates.checkout).to.eql("0NaN-aN-aN");
            assert(response.body.booking.additionalneeds).to.eql("Breakfast");
    })
    it("Create Booking with additionalneeds empty", async () => {
        const body = {
            firstname : "Aldian",
            lastname : "Karim",
            totalprice : 5000,
            depositpaid : true,
            bookingdates : {
                checkin : "2023-04-16",
                checkout : "2023-04-17"
            },
            additionalneeds : ""
        }

        const response = await request_url
            .post("/booking")
            .set('Accept', 'application/json')
            .send(body);

            assert(response.statusCode).to.eql(200);
            assert(response.body.booking.firstname).to.eql("Aldian");
            assert(response.body.booking.lastname).to.eql("Karim");
            assert(response.body.booking.totalprice).to.eql(5000);
            assert(response.body.booking.depositpaid).to.eql(true);
            assert(response.body.booking.bookingdates.checkin).to.eql("2023-04-16");
            assert(response.body.booking.bookingdates.checkout).to.eql("2023-04-17");
            assert(response.body.booking.additionalneeds).to.eql("");
    })
    it("Success Get Data by ID 1", async function () {

        const response = await request_url
            .get("/booking/1")
            .set('Accept', 'application/json')
            .send();
            assert(response.statusCode).to.eql(200);
    })
})