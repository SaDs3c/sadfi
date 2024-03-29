# sadfi  

### (SADSEC Wi-Fi)

sadfi is a Python package that allows access to the last Wi-Fi scan information on Termux using the `termux-wifi-scaninfo` command. It provides a simple command-line interface to display Wi-Fi scan results in a tabular format.

## Installation

You can install sadfi using `pip`:

```bash
pip install sadfi

```

**More:** Ensure that you have the `termux-wifi-scaninfo` command available on your Termux environment.

## Usage

After installation, you can use sadfi by running the following command:

```bash
sadfi
```

This will display a table with information about the last Wi-Fi scan.

## Example Output
```sql
------------------------------------------------------------
This SadSec tool allows access to all last Wi-Fi scan information.

+------------+-------------------+-----------+------+
| SSID       | BSSID             | Frequency | RSSI |
+------------+-------------------+-----------+------+
| TestSSID   | 00:11:22:33:44:55 | 2412      | -55  |
+------------+-------------------+-----------+------+
```

##  Dependencies
- tabulate: Used for formatting and displaying data in tabular form.

## Contributing

If you would like to contribute to sadfi, feel free to open an issue or submit a pull request on the [GitHub repository](https://github.com/SaDs3c/sadfi)

## License

This project is licensed under the [MIT License](https://github.com/SaDs3c/sadfi/blob/main/LICENSE) - see the LICENSE file for details.
