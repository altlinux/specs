%define oname fyzz

Name: python-module-%oname
Version: 0.1.0
Release: alt2.1
Summary: SPARQL parser
License: LGPLv2
Group: Development/Python
BuildArch: noarch
Url: https://pypi.python.org/pypi/fyzz/

Source: %name-%version.tar
Patch1: %oname-%version-alt-unittest.patch

BuildRequires: python-module-setuptools python-module-yapps2
BuildRequires: python-module-logilab-common

%description
SPARQL parser written in Python using yapps.

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR

%description tests
SPARQL parser written in Python using yapps.

This package contains tests for %oname.

%prep
%setup
%patch1 -p2

%build
%python_build_debug

%install
%python_install

%check
export PYTHONPATH=%buildroot%python_sitelibdir
for i in test/*.py; do
	python $i
done

%files
%doc ChangeLog doc/*
%python_sitelibdir/*
%exclude %python_sitelibdir/*/test

%files tests
%python_sitelibdir/*/test

%changelog
* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 0.1.0-alt2.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Wed Nov 22 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 0.1.0-alt2
- Fixed tests.

* Wed Nov 05 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1.0-alt1
- Initial build for Sisyphus

