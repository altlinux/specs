Name: python3-module-metno
Version: 0.5.0
Release: alt1

Summary: Python library to talk to the met.no api
License: MIT
Group: Development/Python
Url: https://pypi.org/project/PyMetno/

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
%doc LICENSE README.*
%python3_sitelibdir/metno
%python3_sitelibdir/PyMetno-%version-*-info

%changelog
* Mon Jan 13 2020 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.5.0-alt1
- initial
