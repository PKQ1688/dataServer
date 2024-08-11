import os
from dotenv import load_dotenv
from apify_client import ApifyClient

load_dotenv()

# Initialize the ApifyClient with your API token
client = ApifyClient(os.getenv("APIFY_TOKEN"))

# Prepare the Actor input
run_input = {
    "runMode": "DEVELOPMENT",
    "startUrls": [{ "url": "https://crawlee.dev" }],
    "keepUrlFragments": False,
    "linkSelector": "a[href]",
    "globs": [{ "glob": "https://crawlee.dev/*/*" }],
    "pseudoUrls": [],
    "excludes": [{ "glob": "/**/*.{png,jpg,jpeg,pdf}" }],
    "pageFunction": """// The function accepts a single argument: the \"context\" object.
// For a complete list of its properties and functions,
// see https://apify.com/apify/web-scraper#page-function 
async function pageFunction(context) {
    // This statement works as a breakpoint when you're trying to debug your code. Works only with Run mode: DEVELOPMENT!
    // debugger; 

    // jQuery is handy for finding DOM elements and extracting data from them.
    // To use it, make sure to enable the \"Inject jQuery\" option.
    const $ = context.jQuery;
    const pageTitle = $('title').first().text();
    const h1 = $('h1').first().text();
    const first_h2 = $('h2').first().text();
    const random_text_from_the_page = $('p').first().text();


    // Print some information to actor log
    context.log.info(`URL: ${context.request.url}, TITLE: ${pageTitle}`);

    // Manually add a new page to the queue for scraping.
   await context.enqueueRequest({ url: 'http://www.example.com' });

    // Return an object with the data extracted from the page.
    // It will be stored to the resulting dataset.
    return {
        url: context.request.url,
        pageTitle,
        h1,
        first_h2,
        random_text_from_the_page
    };
}""",
    "injectJQuery": True,
    "proxyConfiguration": { "useApifyProxy": True },
    "proxyRotation": "RECOMMENDED",
    "initialCookies": [],
    "useChrome": False,
    "headless": True,
    "ignoreSslErrors": False,
    "ignoreCorsAndCsp": False,
    "downloadMedia": True,
    "downloadCss": True,
    "maxRequestRetries": 3,
    "maxPagesPerCrawl": 0,
    "maxResultsPerCrawl": 0,
    "maxCrawlingDepth": 0,
    "maxConcurrency": 50,
    "pageLoadTimeoutSecs": 60,
    "pageFunctionTimeoutSecs": 60,
    "waitUntil": ["networkidle2"],
    "preNavigationHooks": """// We need to return array of (possibly async) functions here.
// The functions accept two arguments: the \"crawlingContext\" object
// and \"gotoOptions\".
[
    async (crawlingContext, gotoOptions) => {
        // ...
    },
]
""",
    "postNavigationHooks": """// We need to return array of (possibly async) functions here.
// The functions accept a single argument: the \"crawlingContext\" object.
[
    async (crawlingContext) => {
        // ...
    },
]""",
    "breakpointLocation": "NONE",
    "closeCookieModals": False,
    "maxScrollHeightPixels": 5000,
    "debugLog": False,
    "browserLog": False,
    "customData": {},
}

# Run the Actor and wait for it to finish
run = client.actor("moJRLRc85AitArpNN").call(run_input=run_input)

# Fetch and print Actor results from the run's dataset (if there are any)
for item in client.dataset(run["defaultDatasetId"]).iterate_items():
    print(item)