%define oname css-parser

Name: python3-module-css-parser
Version: 1.0.8
Release: alt1

Summary: A CSS Cascading Style Sheets library for Python

Group: Development/Python3
License: LGPL
Url: https://pypi.python.org/pypi/css-parser

# Source-url: %__pypi_url %oname
Source: %name-%version.tar

BuildArch: noarch

# optional
%add_python3_req_skip google.appengine.api

BuildRequires(pre): rpm-build-intro >= 2.2.5
BuildRequires(pre): rpm-build-python3

%description
A Python package to parse and build CSS Cascading Style Sheets. DOM only, not
any rendering facilities!

%package doc
Summary: Documentation for CSS Cascading Style Sheets library for Python
Group: Development/Documentation

%description doc
A Python package to parse and build CSS Cascading Style Sheets. DOM only, not
any rendering facilities!

This package contains documentation for %name.

%prep
%setup

%build
%python3_build_debug

%install
%python3_install
%python3_prune

%files
%python3_sitelibdir_noarch/*

%changelog
* Fri Dec 30 2022 Vitaly Lipatov <lav@altlinux.ru> 1.0.8-alt1
- new version 1.0.8 (with rpmrb script)

* Mon Apr 04 2022 Vitaly Lipatov <lav@altlinux.ru> 1.0.7-alt1
- new version 1.0.7 (with rpmrb script)

* Sun Nov 08 2020 Vitaly Lipatov <lav@altlinux.ru> 1.0.6-alt1
- new version 1.0.6 (with rpmrb script)

* Sun Nov 08 2020 Vitaly Lipatov <lav@altlinux.ru> 1.0.4-alt2
- build python3 package separately

* Fri Feb 01 2019 Vitaly Lipatov <lav@altlinux.ru> 1.0.4-alt1
- initial build for ALT Sisyphus
  (a fork of the cssutils project based on version 1.0.2)
