%define _unpackaged_files_terminate_build 1
%define oname dulwich
Name: python3-module-%oname
Version: 0.16.3
Release: alt1
Summary: Python Git Library
License: GPLv2+
Group: Development/Python3
Url: https://github.com/eberle1080/dulwich-py3k
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source0: https://pypi.python.org/packages/9e/d7/8fb5b952ad14f27f7ab1bbe17db7860fe99c3c3e5d08de0bea3a161389a0/%{oname}-%{version}.tar.gz

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
%setup -q -n %{oname}-%{version}

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
%doc AUTHORS COPYING NEWS docs/*.txt docs/tutorial PKG-INFO README.md examples
%_bindir/*
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*/tests

%files tests
%python3_sitelibdir/*/tests

%changelog
* Wed Jan 18 2017 Igor Vlasenko <viy@altlinux.ru> 0.16.3-alt1
- automated PyPI update

* Thu Mar 17 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.8.2-alt1.git20120327.1
- (NMU) rebuild with python3-3.5 & rpm-build-python3-0.1.10
  (for ABI dependence and new python3(*) reqs)

* Thu Jul 31 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.8.2-alt1.git20120327
- Initial build for Sisyphus

