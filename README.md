# tap-netsuite

[Singer](https://www.singer.io/) tap that extracts data from a [NetSuite](https://www.netsuite.com/) database and produces JSON-formatted data following the [Singer spec](https://github.com/singer-io/getting-started/blob/master/SPEC.md).

```bash
$ python3 -m venv env/tap-netsuite
$ source env/tap-netsuite/bin/activate
$ pip install .
$ tap-netsuite --config config.json --discover
$ tap-netsuite --config config.json --properties properties.json --state state.json
```

# Quickstart

## Install the tap

```
> pip install tap-netsuite
```

## Create a Config file
#### Token Based Authentication
```
{
  "ns_account":"netsuite_account_id",
  "ns_consumer_key":"netsuite_consumer_key",
  "ns_consumer_secret":"netsuite_consumer_secret",
  "ns_token_key":"netsuite_token_key",
  "ns_token_secret" :"netsuite_token_secret",
  "select_fields_by_default": true,
  "is_sandbox": true / false,
  "start_date": "2019-09-02T00:00:00Z"
}
```
The `ns_account` is your account Id. This can be found under Setup -> Company -> Company Information. Look for Account Id. Note "_SB" is for Sandbox account.

The `ns_consumer_key`, `ns_consumer_secret`, `ns_token_key` and `ns_token_secret` keys are your TBA Authentication keys for SOAP connection. Visit the [NetSuite documentation](https://support.cazoomi.com/hc/en-us/articles/360010093392-How-to-Setup-NetSuite-Token-Based-Authentication-as-Authentication-Type).

The `start_date` is used by the tap as a bound on SOAP requests when searching for records.  This should be an [RFC3339](https://www.ietf.org/rfc/rfc3339.txt) formatted date-time, like "2018-01-08T00:00:00Z". For more details, see the [Singer best practices for dates](https://github.com/singer-io/getting-started/blob/master/BEST_PRACTICES.md#dates).

The `is_sandbox` should always be set to "false" if you are connecting Production account of NetSuite. Set it to "true" if you want to connect to SandBox acccount.

When new fields are discovered in NetSuite objects, the `select_fields_by_default` key describes whether or not the tap will select those fields by default.

## Run Discovery

To run discovery mode, execute the tap with the config file.

```
> tap-netsuite --config config.json --discover > properties.json
```

## Sync Data

To sync data, select fields in the `properties.json` output and run the tap.

```
> tap-netsuite --config config.json --properties properties.json [--state state.json]
```
