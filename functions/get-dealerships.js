//used public cloudant actions

// const { CloudantV1 } = require('@ibm-cloud/cloudant');

// Cloudant_URL =
//   'https://a49f770b-c876-45fc-8b2b-0f7706b7dbea-bluemix.cloudantnosqldb.appdomain.cloud';
// Cloudant_APIKEY = '-0rrs2ZF5O5dqEFi2hTFGrpEY152sjUYfYZtgJy5d_CR';

// function main(params) {
//   const service = CloudantV1.newInstance({
//     serviceName: 'Cloudant',
//   });

//   service.getAllDbs().then((response) => {
//     console.log(response.result);
//   });
// }

// function main(params) {
//   const cloudant = Cloudant({
//     url: params.COUCH_URL,
//     plugins: { iamauth: { iamApiKey: params.IAM_API_KEY } },
//   });

//   let dealerships = getAllDealerships(cloudant);
//   return dealerships;
// }

// function getAllDealerships(cloudant) {
//   return new Promise((resolve, reject) => {
//     cloudant.db
//       .use('dealerships')
//       .list({ include_docs: true })
//       .then((body) => {
//         resolve({ rows: body.rows });
//       })
//       .catch((err) => {
//         reject({ err: err });
//       });
//   });
// }
