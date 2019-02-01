%define oname css-parser
%def_with python3

Name: python-module-css-parser
Version: 1.0.4
Release: alt1

Summary: A CSS Cascading Style Sheets library for Python

Group: Development/Python
License: LGPL
Url: https://pypi.python.org/pypi/css-parser

# Source-url: https://pypi.io/packages/source/c/%oname/%oname-%version.tar.gz
Source: %name-%version.tar

BuildArch: noarch

# Automatically added by buildreq on Tue Jun 01 2010 (-bi)
BuildRequires: python-module-mechanize python-module-setuptools python-modules-encodings

# optional
%add_python_req_skip google.appengine.api
%add_python3_req_skip google.appengine.api

%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools
%endif


%description
A Python package to parse and build CSS Cascading Style Sheets. DOM only, not
any rendering facilities!

%package -n python3-module-%oname
Summary: CSS Cascading Style Sheets library for Python
Group: Development/Python3

%description -n python3-module-%oname
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

#pushd %buildroot%_bindir
#for i in $(ls); do
#	mv $i $i.py3
#done
#popd
%endif


rm -rf %buildroot%python_sitelibdir_noarch/%oname/tests/
rm -rf %buildroot%python3_sitelibdir_noarch/%oname/tests/


%files
%doc PKG-INFO
%if_without python3
#_bindir/*
%endif
%python_sitelibdir_noarch/*

%if_with python3
%files -n python3-module-%oname
#_bindir/*
%python3_sitelibdir_noarch/*
%endif

#files doc
#doc examples

%changelog
* Fri Feb 01 2019 Vitaly Lipatov <lav@altlinux.ru> 1.0.4-alt1
- initial build for ALT Sisyphus
  (a fork of the cssutils project based on version 1.0.2)
