Name: python3-module-url-normalize
Version: 1.4.3
Release: alt1

Summary: URI Normalization function
License: MIT
Group: Development/Python
Url: https://pypi.org/project/url-normalize/

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
%python3_sitelibdir/url_normalize
%python3_sitelibdir/url_normalize-%version-*-info

%changelog
* Fri Mar 18 2022 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.4.3-alt1
- 1.4.3 released

* Tue Jul 21 2020 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.4.2-alt1
- initial
