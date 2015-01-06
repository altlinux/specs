%define oname cssutils

%def_disable check

Name: python3-module-%oname
Version: 1.0
Release: alt1
Summary: A CSS Cascading Style Sheets library for Python
License: LGPLv2.1+
Group: Development/Python3
Url: https://pypi.python.org/pypi/cssutils/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar
BuildArch: noarch

BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools-tests
BuildPreReq: python3-module-mock python-tools-2to3

%py3_provides %oname

%description
A Python package to parse and build CSS Cascading Style Sheets. DOM
only, not any rendering facilities!

%package tests
Summary: Tests for %oname
Group: Development/Python3
Requires: %name = %EVR

%description tests
A Python package to parse and build CSS Cascading Style Sheets. DOM
only, not any rendering facilities!

This package contains tests for %oname.

%prep
%setup

find -type f -name '*.py' -exec 2to3 -w -n '{}' +

%build
%python3_build_debug

%install
%python3_install

pushd %buildroot%_bindir
for i in $(ls); do
	mv $i $i.py3
done
popd

%check
python3 setup.py test

%files
%doc *.txt examples sheets
%_bindir/*
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*/tests

%files tests
%python3_sitelibdir/*/tests

%changelog
* Tue Jan 06 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0-alt1
- Initial build for Sisyphus

