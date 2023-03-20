%define oname dotenv

Name: python3-module-%oname
Version: 1.0.0
Release: alt1

Summary: Reads the key-value pair from .env file and adds them to environment variable.

License: BSD-3-Clause
Group: Development/Python
Url: https://github.com/theskumar/python-dotenv

Source: %name-%version.tar
BuildArch: noarch

AutoReqProv: nopython
%define __python %nil

BuildRequires(pre): rpm-build-python3
BuildRequires: python3(setuptools)
BuildRequires: python3(wheel)

%description
Reads the key-value pair from .env file and adds them to environment
variable. It is great for managing app settings during development
and in production using 12-factor principles.

%prep
%setup -n %name-%version

%build
# We don't support IPython for now (requires additional dependencies)
rm -f src/dotenv/ipython.py
%pyproject_build

%install
%pyproject_install

%files
%_bindir/%oname
%python3_sitelibdir/%oname/
%python3_sitelibdir/python_%oname-%version.dist-info/*

%changelog
* Mon Mar 20 2023 Vladimir Didenko <cow@altlinux.org> 1.0.0-alt1
- new version

* Tue Feb 14 2023 Vladimir Didenko <cow@altlinux.org> 0.21.1-alt1
- new version

* Mon Sep 5 2022 Vladimir Didenko <cow@altlinux.org> 0.21.0-alt1
- new version

* Tue Mar 29 2022 Vladimir Didenko <cow@altlinux.org> 0.20.0-alt1
- new version

* Mon Dec 6 2021 Vladimir Didenko <cow@altlinux.org> 0.19.2-alt1
- new version

* Fri Jul 30 2021 Vladimir Didenko <cow@altlinux.org> 0.19.0-alt1
- new version

* Wed May 26 2021 Vladimir Didenko <cow@altlinux.org> 0.17.1-alt1
- new version

* Mon Apr 12 2021 Vladimir Didenko <cow@altlinux.org> 0.17.0-alt1
- new version

* Mon Dec 21 2020 Vladimir Didenko <cow@altlinux.org> 0.15.0-alt1
- new version

* Fri Jul 3 2020 Vladimir Didenko <cow@altlinux.org> 0.14.0-alt1
- new version

* Wed Mar 11 2020 Vladimir Didenko <cow@altlinux.org> 0.12.0-alt1
- initial build for Sisyphus
