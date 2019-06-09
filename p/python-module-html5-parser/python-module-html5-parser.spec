%define modulename html5-parser
%def_with check
%def_with python3

Name: python-module-html5-parser
Version: 0.4.6
Release: alt1

Summary: Fast C based HTML 5 parsing for python

Url: https://github.com/kovidgoyal/html5-parser
License: ASL 2.0
Group: Development/Python


Packager: Vitaly Lipatov <lav@altlinux.ru>

# Source-url: https://github.com/kovidgoyal/html5-parser/archive/v%version.tar.gz
Source: %name-%version.tar

BuildRequires(pre): rpm-build-intro >= 2.1.4
BuildRequires: python-devel python-module-setuptools

BuildRequires: libxml2-devel
%if_with check
BuildRequires: python-module-lxml python-module-BeautifulSoup4
%endif

%if_with python3
BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel python3-module-setuptools
%if_with check
BuildRequires: python3-module-lxml python3-module-BeautifulSoup4
%endif
%endif

#setup_python_module %modulename

%description
A fast, standards compliant, C based, HTML 5 parser for python.
Over thirty times as fast as pure python based parsers, such as html5lib.

Based on Google gumbo-parser C library.

%package -n python3-module-html5-parser
Summary: Fast C based HTML 5 parsing for python 3
Group: Development/Python3

%description -n python3-module-html5-parser
A fast, standards compliant, C based, HTML 5 parser for python.
Over thirty times as fast as pure python based parsers, such as html5lib.

Based on Google gumbo-parser C library.

%prep
%setup
%python3_dirsetup

%build
%python_build_debug
%python3_dirbuild_debug

%install
%python_install
%python3_dirinstall

%check
%python_test
%python3_dirtest

%files
%doc README.rst
%python_sitelibdir/*

%if_with python3
%files -n python3-module-html5-parser
%doc README.rst
%python3_sitelibdir/*
%endif


%changelog
* Sun Jun 09 2019 Vitaly Lipatov <lav@altlinux.ru> 0.4.6-alt1
- new version 0.4.6 (with rpmrb script)

* Sat Jun 30 2018 Vitaly Lipatov <lav@altlinux.ru> 0.4.5-alt1
- new version 0.4.5 (with rpmrb script)
- cleanup spec (use python3_dir* macros from rpm-build-intro)

* Thu Mar 22 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 0.4.4-alt1.1
- (NMU) Rebuilt with python-3.6.4.

* Sun Oct 01 2017 Vitaly Lipatov <lav@altlinux.ru> 0.4.4-alt1
- initial build for ALT Sisyphus

