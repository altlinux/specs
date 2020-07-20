Name: python3-module-ppadb
Version: 0.2.6
Release: alt1

Summary: Anoter ADB shell implemented in Python
License: MIT
Group: Development/Python
Url: https://pypi.org/project/ppadb/

Source0: %name-%version-%release.tar

BuildArch: noarch
BuildRequires: rpm-build-python3 python3-module-setuptools

%description
%summary

%prep
%setup

%build
%python3_build

%install
%python3_install

%files
%python3_sitelibdir/ppadb
%python3_sitelibdir/pure_python_adb-%version-*-info

%changelog
* Mon Jul 20 2020 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.2.6-alt1
- initial
