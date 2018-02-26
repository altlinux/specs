%define oname FlashBlock
%define chromium_extensionsdir %_datadir/chromium-browser/extensions

Name: chromium-browser-flashblock
Version: 0.9.23
Release: alt2

Summary: FlashBlock for Chrome. Block them all, or be selective with the embedded whitelist manager

License: BSD
Group: Networking/WWW
Url: https://chrome.google.com/extensions/detail/gofhjkjmkpinhpoiabjplobcaignabnl

BuildArch: noarch

Packager: Vitaly Lipatov <lav@altlinux.ru>

Source: %name-%version.tar

%description
The extension automatically blocks flash content on webpages.  Each flash
element is being replaced with a placeholder that allows you to load only
selected elements on a given page.  You can also manage a whitelist of
allowed websites via a configuration panel.

Usage:
For enable to all users set CHROMIUM_FLAGS="--load-extension=%chromium_extensionsdir/%oname" in
/etc/chromium-browser/default config file.
Allows only one extension :(

See also http://bugs.etersoft.ru/show_bug.cgi?id=4920

%prep
%setup

%install
install -d %buildroot%chromium_extensionsdir/%oname/
cp -a * %buildroot%chromium_extensionsdir/%oname/

%files
%dir %chromium_extensionsdir/
%chromium_extensionsdir/%oname/

%changelog
* Mon Feb 01 2010 Vitaly Lipatov <lav@altlinux.ru> 0.9.23-alt2
- build as noarch

* Mon Feb 01 2010 Vitaly Lipatov <lav@altlinux.ru> 0.9.23-alt1
- initial build for ALT Linux Sisyphus
