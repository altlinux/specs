%define oname testtools

%def_with python3

Name: python-module-%oname
Version: 0.9.8
Release: alt1.2
Summary: extensions to the Python standard library's unit testing framework

Group: Development/Python
License: MIT
Url: http://pypi.python.org/pypi/testtools

Source: %name-%version.tar
Packager: Vladimir Lettiev <crux@altlinux.ru>

BuildArch: noarch
BuildRequires: python-module-setuptools
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel python3-module-distribute
%endif

%description
testtools is a set of extensions to the Python standard library's unit
testing framework. These extensions have been derived from years of
experience with unit testing in Python and come from many different
sources.

%if_with python3
%package -n python3-module-%oname
Summary: extensions to the Python 3 standard library's unit testing framework
Group: Development/Python3
%add_python3_req_skip twisted

%description -n python3-module-%oname
testtools is a set of extensions to the Python standard library's unit
testing framework. These extensions have been derived from years of
experience with unit testing in Python and come from many different
sources.
%endif

%prep
%setup -q
%if_with python3
rm -rf ../python3
cp -a . ../python3
%endif

%build
%python_build
%if_with python3
pushd ../python3
%python3_build
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
%python_sitelibdir/testtools*
%doc HACKING LICENSE MANUAL NEWS README

%if_with python3
%files -n python3-module-%oname
%doc HACKING LICENSE MANUAL NEWS README
%python3_sitelibdir/*
%endif

%changelog
* Thu Apr 12 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.9.8-alt1.2
- Added module for Python 3 (bootstrap)

* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.9.8-alt1.1
- Rebuild with Python-2.7

* Mon Jan 10 2011 Vladimir Lettiev <crux@altlinux.ru> 0.9.8-alt1
- New version 0.9.8

* Mon Oct 18 2010 Vladimir Lettiev <crux@altlinux.ru> 0.9.7-alt1
- New version 0.9.7

* Mon Sep 20 2010 Vladimir Lettiev <crux@altlinux.ru> 0.9.6-alt1
- initial build

