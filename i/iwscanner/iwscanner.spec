Name: iwscanner
Version: 0.2.4
Release: alt1

Summary: iwScanner is a wireless scanner for linux with an easy to use graphic interface.

Group: Networking/Other
License: LGPL
Url: http://kuthulu.com/iwscanner/

Packager: Vitaly Lipatov <lav@altlinux.ru>

Source: http://kuthulu.com/iwscanner/%name-%version.tar

BuildArch: noarch

# Automatically added by buildreq on Sun Jan 22 2012
# optimized out: python-base python-module-peak python-modules-compiler
BuildRequires: python-module-mwlib python-module-paste

# needs iwlist
Requires: wireless-tools

Requires: python-module-pygtk-libglade

%description
iwScanner is a wireless scanner for linux with an easy to use graphic interface.

%prep
%setup

%install
mkdir -p %buildroot/%python_sitelibdir/%name/ %buildroot/%_bindir/
install -m644 *.py *.glade* *.png %buildroot/%python_sitelibdir/%name/
cat >%buildroot/%_bindir/%name <<EOF
#!/bin/sh
cd %python_sitelibdir/%name/
python iwscanner.py
EOF
chmod 755 %buildroot/%_bindir/%name

%files
%doc README
%_bindir/%name
%python_sitelibdir/%name/

%changelog
* Sun Jan 22 2012 Vitaly Lipatov <lav@altlinux.ru> 0.2.4-alt1
- initial build for ALT Linux Sisyphus
