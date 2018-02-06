%define _unpackaged_files_terminate_build 1
BuildRequires: unzip
%define oname zLOG
Name: python-module-%oname
Version: 3.0
Release: alt1.1
Summary: A general logging facility
License: ZPLv2.1
Group: Development/Python
Url: https://pypi.python.org/pypi/zLOG/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/zopefoundation/zLOG.git
Source0: https://pypi.python.org/packages/ac/2a/36bf03a74327e6a158914c980403114c678a8d2ce1159a742d1ec94d5d92/%{oname}-%{version}.zip
BuildArch: noarch

BuildPreReq: python-module-setuptools python-module-zconfig-tests

%py_provides %oname

%description
This package provides a general logging facility that, at this point, is
just a small shim over Python's logging module. Therefore, unless you
need to support a legacy package from the Zope 2 world, you're probably
better off using Python's logging module.

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR

%description tests
This package provides a general logging facility that, at this point, is
just a small shim over Python's logging module. Therefore, unless you
need to support a legacy package from the Zope 2 world, you're probably
better off using Python's logging module.

This package contains tests for %oname.

%prep
%setup -q -n %{oname}-%{version}

%build
%python_build_debug

%install
%python_install

%check
export PYTHONPATH=$PWD/src
python setup.py test

%files
%doc *.txt
%python_sitelibdir/*
%exclude %python_sitelibdir/*/tests

%files tests
%python_sitelibdir/*/tests

%changelog
* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 3.0-alt1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Wed Jan 11 2017 Igor Vlasenko <viy@altlinux.ru> 3.0-alt1
- automated PyPI update

* Thu Aug 27 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.12.0-alt1.git20141220
- New snapshot

* Thu Oct 16 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.12.0-alt1.git20130313
- Snapshot from git

* Sat Oct 11 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.12.0-alt1
- Initial build for Sisyphus

