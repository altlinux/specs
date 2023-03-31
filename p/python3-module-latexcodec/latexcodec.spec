%define oname latexcodec

Name: python3-module-%oname
Version: 2.0.1
Release: alt2

Summary: A lexer and codec to work with LaTeX code in Python
License: MIT
Group: Development/Python3
Url: https://pypi.python.org/pypi/latexcodec
BuildArch: noarch

# https://github.com/mcmtroffaes/latexcodec.git
Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-coverage
BuildRequires: python3-module-sphinx python3-module-six
BuildRequires: python3-module-pytest

%py3_provides %oname
%py3_requires six


%description
A lexer and codec to work with LaTeX code in Python.

%package pickles
Summary: Pickles for %oname
Group: Development/Python3

%description pickles
A lexer and codec to work with LaTeX code in Python.

This package contains pickles for %oname.

%prep
%setup

sed -i 's|sphinx-build|sphinx-build-3|' doc/Makefile

%build
%python3_build

%install
%python3_install

export PYTHONPATH=$PWD
%make -C doc pickle
%make -C doc html
cp -fR doc/_build/pickle %buildroot%python3_sitelibdir/%oname/

%check
export PYTHONPATH=$PWD
py.test-3

%files
%doc *.rst doc/_build/html
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*/pickle

%files pickles
%python3_sitelibdir/*/pickle


%changelog
* Fri Mar 31 2023 Anton Vyatkin <toni@altlinux.org> 2.0.1-alt2
- Fix BuildRequires.

* Tue Mar 30 2021 Grigory Ustinov <grenka@altlinux.org> 2.0.1-alt1
- Build new version.

* Fri Dec 06 2019 Andrey Bychkov <mrdrew@altlinux.org> 1.0.7-alt1
- Version updated to 1.0.7
- python2 disabled

* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 1.0.5-alt1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Thu Sep 28 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 1.0.5-alt1
- Updated to upstream version 1.0.5.

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 1.0.2-alt1.a1.git20150826.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 1.0.2-alt1.a1.git20150826.1
- NMU: Use buildreq for BR.

* Mon Aug 31 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0.2-alt1.a1.git20150826
- Initial build for Sisyphus

