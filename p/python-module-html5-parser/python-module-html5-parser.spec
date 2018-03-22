%def_without check
%def_with python3

%define modulename bleach
Name: python-module-html5-parser
Version: 0.4.4
Release: alt1.1

Summary: Fast C based HTML 5 parsing for python

Url: https://github.com/kovidgoyal/html5-parser
License: ASL 2.0
Group: Development/Python


Packager: Vitaly Lipatov <lav@altlinux.ru>

# Source-url: https://github.com/kovidgoyal/html5-parser/archive/v%version.tar.gz
Source: %name-%version.tar

BuildRequires: python-dev python-module-setuptools

BuildRequires: libxml2-devel

%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools
%endif

#setup_python_module %modulename

%description
A fast, standards compliant, C based, HTML 5 parser for python.
Over thirty times as fast as pure python based parsers, such as html5lib.

%package -n python3-module-html5-parser
Summary: Fast C based HTML 5 parsing for python 3
Group: Development/Python3

%description -n python3-module-html5-parser
A fast, standards compliant, C based, HTML 5 parser for python.
Over thirty times as fast as pure python based parsers, such as html5lib.


%prep
%setup

%if_with python3
cp -fR . ../python3
%endif

%build
%python_build_debug

%if_with python3
pushd ../python3
%python3_build_debug
popd
%endif

%install
%python_install

%if_with python3
pushd ../python3
%python3_install
popd
%endif

%files
%doc README.rst
%python_sitelibdir/*

%if_with python3
%files -n python3-module-html5-parser
%doc README.rst
%python3_sitelibdir/*
%endif


%changelog
* Thu Mar 22 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 0.4.4-alt1.1
- (NMU) Rebuilt with python-3.6.4.

* Sun Oct 01 2017 Vitaly Lipatov <lav@altlinux.ru> 0.4.4-alt1
- initial build for ALT Sisyphus

