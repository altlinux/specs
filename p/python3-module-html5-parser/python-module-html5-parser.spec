%define oname html5-parser

# obsoleted tests
%def_without check

Name: python3-module-html5-parser
Version: 0.4.7
Release: alt2

Summary: Fast C based HTML 5 parsing for python

Url: https://github.com/kovidgoyal/html5-parser
License: ASL 2.0
Group: Development/Python3


Packager: Vitaly Lipatov <lav@altlinux.ru>

# Source-url: %__pypi_url %oname
Source: %name-%version.tar

BuildRequires(pre): rpm-build-intro >= 2.2.4
BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel python3-module-setuptools

BuildRequires: libxml2-devel

%if_with check
BuildRequires: python3-module-lxml python3-module-beautifulsoup4
%endif

%description
A fast, standards compliant, C based, HTML 5 parser for python.
Over thirty times as fast as pure python based parsers, such as html5lib.

Based on Google gumbo-parser C library.

%prep
%setup

%build
%python3_build_debug

%install
%python3_install
%python3_prune

%check
%python3_test

%files
%doc README.rst
%python3_sitelibdir/*

%changelog
* Sun Nov 08 2020 Vitaly Lipatov <lav@altlinux.ru> 0.4.7-alt2
- build python3 package separately, cleanup spec

* Sun Jun 30 2019 Vitaly Lipatov <lav@altlinux.ru> 0.4.7-alt1
- new version 0.4.7 (with rpmrb script)

* Sun Jun 09 2019 Vitaly Lipatov <lav@altlinux.ru> 0.4.6-alt1
- new version 0.4.6 (with rpmrb script)

* Sat Jun 30 2018 Vitaly Lipatov <lav@altlinux.ru> 0.4.5-alt1
- new version 0.4.5 (with rpmrb script)
- cleanup spec (use python3_dir* macros from rpm-build-intro)

* Thu Mar 22 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 0.4.4-alt1.1
- (NMU) Rebuilt with python-3.6.4.

* Sun Oct 01 2017 Vitaly Lipatov <lav@altlinux.ru> 0.4.4-alt1
- initial build for ALT Sisyphus

