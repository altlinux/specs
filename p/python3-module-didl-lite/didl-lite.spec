Name: python3-module-didl-lite
Version: 1.2.4
Release: alt1

Summary: DIDL-Lite (Digital Item Declaration Language) tools for Python
License: Apache-2.0
Group: Development/Python
Url: https://pypi.org/project/python-didl-lite/

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
%doc LICENSE.* README.*
%python3_sitelibdir/didl_lite
%python3_sitelibdir/python_didl_lite-%version-*-info

%changelog
* Tue Jan 21 2020 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.2.4-alt1
- initial

