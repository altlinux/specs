%define oname metafone

Name: python3-module-%oname
Version: 0.5
Release: alt2

Summary: A Python implementation of the double metaphone algorithms
License: BSD
Group: Development/Python3
Url: https://pypi.python.org/pypi/Metafone/
BuildArch: noarch

# https://github.com/al45tair/metaphone.git
Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-nose python3-module-six


%description
A Python implementation of the double metaphone algorithms.

This is a fork of the Metaphone package, with added Unicode support.

%package tests
Summary: Tests for %oname
Group: Development/Python3
Requires: %name = %EVR
%py3_requires six

%description tests
A Python implementation of the double metaphone algorithms.

This is a fork of the Metaphone package, with added Unicode support.

This package contains tests for %oname.

%prep
%setup

%build
export LC_ALL=en_US.UTF-8
%python3_build_debug

%install
%python3_install

%check
%__python3 setup.py test

%files
%doc *.rst
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*/tests

%files tests
%python3_sitelibdir/*/tests


%changelog
* Mon Feb 10 2020 Andrey Bychkov <mrdrew@altlinux.org> 0.5-alt2
- Build for python2 disabled.

* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 0.5-alt1.git20150216.1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.5-alt1.git20150216.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Mon Mar 02 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.5-alt1.git20150216
- Initial build for Sisyphus

