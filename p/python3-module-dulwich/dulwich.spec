%define oname dulwich
Name: python3-module-%oname
Version: 0.8.2
Release: alt1.git20120327
Summary: Python Git Library
License: GPLv2+
Group: Development/Python3
Url: https://github.com/eberle1080/dulwich-py3k
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools

%py3_provides %oname

%description
Simple Python implementation of the Git file formats and protocols.
Dulwich is the place where Mr. and Mrs. Git live in one of the Monty
Python sketches.

All functionality is available in pure Python, but (optional) C
extensions are also available for better performance.

%package tests
Summary: Tests for dulwich
Group: Development/Python3
Requires: %name = %version-%release

%description tests
Simple Python implementation of the Git file formats and protocols.
Dulwich is the place where Mr. and Mrs. Git live in one of the Monty
Python sketches.

All functionality is available in pure Python, but (optional) C
extensions are also available for better performance.

This package contains tests for dulwich.

%prep
%setup

%build
%python3_build

%install
%python3_install

pushd %buildroot%_bindir
for i in $(ls); do
	mv $i $i.py3
done
popd

%files
%doc AUTHORS COPYING HACKING NEWS README docs/*.txt docs/tutorial
%_bindir/*
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*/tests

%files tests
%python3_sitelibdir/*/tests

%changelog
* Thu Jul 31 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.8.2-alt1.git20120327
- Initial build for Sisyphus

