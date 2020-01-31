Name: python3-module-netort
Version: 0.7.6
Release: alt1

License: LGPLv2
Group: Development/Python
Url: http://github.com/yandex-load/netort

Summary: common library for yandex-load org

# Source-url: https://github.com/yandex-load/netort/archive/v%version.tar.gz
Packager: Vitaly Lipatov <lav@altlinux.ru>

Source: %name-%version.tar

BuildArch: noarch

BuildRequires(pre): rpm-build-python3 rpm-build-intro
BuildRequires: python3-module-setuptools

%py3_use pandas >= 0.23.0

# for a time
%add_python3_req_skip yandextank.plugins.Phantom.reader

%description
This is a library of common components for performance testing tools
(YandexTank, Volta, etc.).

%prep
%setup
# obsoleted path
%__subst "s|requests.packages.urllib3.exceptions|urllib3.exceptions|" netort/data_manager/clients/luna*.py

%build
%python3_build

%install
%python3_install
# too specific
rm -fv %buildroot%python3_sitelibdir/netort/usb_devices.py

%files
%_bindir/phout_upload
%python3_sitelibdir/*

%changelog
* Fri Jan 31 2020 Vitaly Lipatov <lav@altlinux.ru> 0.7.6-alt1
- initial build for ALT Sisyphus (python3 version)
