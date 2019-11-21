%define oname pytest-oot

Name: python3-module-%oname
Version: 0.2.6
Release: alt2

Summary: Run object-oriented tests in a simple format
License: Free
Group: Development/Python3
Url: https://pypi.python.org/pypi/pytest-oot/
BuildArch: noarch

Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-pytest

%py3_provides pytest_oot


%description
Run object-oriented tests in a simple format.

%prep
%setup

%build
%python3_build_debug

%install
%python3_install

%check
%__python3 setup.py test

%files
%doc PKG-INFO example
%python3_sitelibdir/*
%exclude %python3_sitelibdir/example


%changelog
* Thu Nov 21 2019 Andrey Bychkov <mrdrew@altlinux.org> 0.2.6-alt2
- python2 disabled

* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 0.2.6-alt1.1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.2.6-alt1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Fri Jan 02 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.2.6-alt1
- Version 0.2.6

* Thu Jan 01 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.2.1-alt1
- Initial build for Sisyphus

