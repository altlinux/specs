Name: asus-numberpad-driver
Version: 6.3.1
Release: alt1

Summary: Linux feature-rich configurable driver for Asus numberpad
License: GPL-2.0
Group: Other
URL: https://github.com/asus-linux-drivers/asus-numberpad-driver

BuildArch: noarch

Source: %name-%version.tar
Patch: deps-alt-fix.patch

AutoProv: no
AutoReq: no

%description
Maintained feature-rich linux driver for NumberPad(2.0) on Asus laptops.
NumberPad(2.0) is illuminated numeric keypad integrated to touchpad which
appears when is done tap on top right corner of touchpad for atleast 1s
by default (configurable) or slide gesture from top right/left corner
to the center, the left shows calc app aswell (configurable).

%prep
%setup
%patch -p1

%build

%install

mkdir -p %buildroot%_datadir/%name-install/

cp -r $PWD/* %buildroot%_datadir/%name-install/

%files
%doc README.*
%dir %_datadir/%name-install/
%_datadir/%name-install/

%changelog
* Sat Aug 03 2024 Anton Vyatkin <toni@altlinux.org> 6.3.1-alt1
- Initial build for Sisyphus.
