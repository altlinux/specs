%define oname logilab-doctools

%def_without python3

Name: python-module-%oname
Version: 0.4.2
Release: alt2.1
Summary: Tools used at Logilab to make documents
License: GPL
Group: Development/Python
Url: https://pypi.python.org/pypi/logilab-doctools/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: fop xsltproc
BuildPreReq: python-devel python-module-setuptools
BuildPreReq: python-module-pybill python-module-Reportlab
BuildPreReq: python-module-lxml python-module-logilab-common
BuildPreReq: python-module-doctools
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools
BuildPreReq: python3-module-Reportlab
BuildPreReq: python3-module-lxml python3-module-logilab-common
BuildPreReq: python3-module-doctools python-tools-2to3
%endif

%py_provides logilab.doctools
Requires: fop xsltproc
%py_requires logilab.common pybill

%description
Set of tools to help transforming documents in various formats.

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR

%description tests
Set of tools to help transforming documents in various formats.

This package contains tests for %oname.

%if_with python3
%package -n python3-module-%oname
Summary: Tools used at Logilab to make documents
Group: Development/Python3
Requires: fop xsltproc
%py3_provides logilab.doctools
%py3_requires logilab.common

%description -n python3-module-%oname
Set of tools to help transforming documents in various formats.

%package -n python3-module-%oname-tests
Summary: Tests for %oname
Group: Development/Python3
Requires: python3-module-%oname = %EVR

%description -n python3-module-%oname-tests
Set of tools to help transforming documents in various formats.

This package contains tests for %oname.
%endif

%prep
%setup

%if_with python3
cp -fR . ../python3
find ../python3 -type f -name '*.py' -exec 2to3 -w -n '{}' +
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

rm -f doc/makefile

%check
python setup.py test
%if_with python3
pushd ../python3
python3 setup.py test
popd
%endif

%files
%doc ChangeLog README doc/* examples
%_bindir/*
%python_sitelibdir/logilab/doctools
%python_sitelibdir/*.egg-info
%exclude %python_sitelibdir/logilab/doctools/test

%files tests
%python_sitelibdir/logilab/doctools/test

%if_with python3
%files -n python3-module-%oname
%doc ChangeLog README doc/* examples
%python3_sitelibdir/logilab/doctools
%python3_sitelibdir/*.egg-info
%exclude %python3_sitelibdir/logilab/doctools/test

%files -n python3-module-%oname-tests
%python3_sitelibdir/logilab/doctools/test
%endif

%changelog
* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 0.4.2-alt2.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Tue Mar 03 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.4.2-alt2
- Fixed build

* Sat Nov 01 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.4.2-alt1
- Initial build for Sisyphus

