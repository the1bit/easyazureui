# Easy Azure UI 

## Versions

* latest, 19.08.01: Very first release

## Background 

I wanted to create a small Python based webUI for Azure management. This soulution uses Azure Rest-APi calls.

## Features

* Login to azure via Service Principal
* Get available Subscriptions
* List VMs in default Subscription
* List resource groups in default Subscription

## Pre-requisites

### Azure Service principal

```
az ad sp create-for-rbac --name easyui-prod --query '{"client_id": appId, "secret": password, "tenant": tenant}'

```

*Store the secred on a safe place*

### External configuration file which contains Azure related information

* filename: config.json
* example: 

```
{
  "tenant": "<your-tenant-id-in-Azure>",
  "authority_url": "https://login.microsoftonline.com/",
  "default_subscription": "<subcription-id-in-Azure>",
  "client_id": "<SP-client-id>",
  "client_secret": "<SP-secret>",
  "resource": "https://management.azure.com/"
}

```

*Put a configuration file to a well known path*

## Installation

### Linux

1. Pull image

```
docker pull the1bit/easyazureui
```

2. Navigate to configuration file directory
3. Create container from image

```
docker container run --mount type=bind,source=$(pwd),destination=/easyui/EasyAzureUI1/config -d -p 5555:5555 the1bit/easyazureui
```


### Window with WSL - PowerShell!!!! not from WSL
1. Pull image

```
docker pull the1bit/easyazureui
```

2. Navigate to configuration file directory
3. Create container from image

```
docker container run --mount type=bind,source=$(pwd),destination=/easyui/EasyAzureUI1/config -d -p 5555:5555 the1bit/easyazureui
```

## Contact

* [the1bit - Tibor Kiss](https://iam.the1bit.hu)
* [Webpage/Blog](https://the1bit.hu)
* [Facebook](https://www.facebook.com/the1bit)
* [Twitter](https://twitter.com/the1bit)
* **[Pateron](https://www.patreon.com/user?u=22504194)**
* [Instagram](http://instagram.com/the1bit)


