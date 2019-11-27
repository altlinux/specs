%define oname rebus

Name: python3-module-%oname
Version: 0.2
Release: alt2

Summary: Generate base64-encoded strings consisting of alphanumeric symbols only
License: GPLv2.0/LGPLv2.1
Group: Development/Python3
Url: https://pypi.python.org/pypi/rebus/
BuildArch: noarch

# https://github.com/barseghyanartur/rebus.git
Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-six

%py3_provides %oname
%py3_requires six


%description
Generate base64-encoded strings consisting of alphanumeric symbols only.

%package tests
Summary: Tests for %oname
Group: Development/Python3
Requires: %name = %EVR

%description tests
Generate base64-encoded strings consisting of alphanumeric symbols only.

This package contains tests for %oname.

%prep
%setup

%build
%python3_build_debug

%install
%python3_install

%check
export PYTHONPATH=$PWD/src
%__python3 setup.py test
%__python3 src/rebus/tests.py -v

%files
%doc *.rst docs/*.rst*
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*/tests.*
%exclude %python3_sitelibdir/*/*/tests.*

%files tests
%python3_sitelibdir/*/tests.*
%python3_sitelibdir/*/*/tests.*


%changelog
* Wed Nov 27 2019 Andrey Bychkov <mrdrew@altlinux.org> 0.2-alt2
- python2 disabled

* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 0.2-alt1.git20140314.1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.2-alt1.git20140314.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Tue Feb 17 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.2-alt1.git20140314
- Initial build for Sisyphus

