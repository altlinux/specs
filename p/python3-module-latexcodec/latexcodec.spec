%define oname latexcodec

%def_with check
%def_with docs

Name: python3-module-%oname
Version: 3.0.0
Release: alt1

Summary: A lexer and codec to work with LaTeX code in Python
License: MIT
Group: Development/Python3
Url: https://pypi.org/project/latexcodec
Vcs: https://github.com/mcmtroffaes/latexcodec.git
BuildArch: noarch

Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-setuptools
BuildRequires: python3-module-wheel
%if_with docs
BuildRequires: python3-module-sphinx
%endif

%if_with check
BuildRequires: python3-module-pytest
%endif

%py3_provides %oname

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
%pyproject_build

%install
%pyproject_install

%if_with docs
export PYTHONPATH=$PWD
%make -C doc pickle
%make -C doc html
cp -fR doc/_build/pickle %buildroot%python3_sitelibdir/%oname/
%endif

%check
%pyproject_run_pytest -v

%files
%doc README.*
%python3_sitelibdir/%oname
%python3_sitelibdir/%{pyproject_distinfo %oname}
%if_with docs
%doc doc/_build/html
%exclude %python3_sitelibdir/%oname/pickle

%files pickles
%dir %python3_sitelibdir/%oname/
%python3_sitelibdir/%oname/pickle
%endif


%changelog
* Fri Mar 08 2024 Anton Vyatkin <toni@altlinux.org> 3.0.0-alt1
- New version 3.0.0.

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

