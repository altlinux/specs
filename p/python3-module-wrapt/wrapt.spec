%define oname wrapt

%def_with check

Name: python3-module-%oname
Version: 1.15.0
Release: alt1
Summary: A Python module for decorators, wrappers and monkey patching
License: BSD
Group: Development/Python3
Url: https://pypi.python.org/pypi/wrapt

# https://github.com/GrahamDumpleton/wrapt
Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3 rpm-macros-sphinx3
BuildRequires: python3-devel python3-module-pytest
BuildRequires: python3-module-sphinx
BuildRequires: python3-module-sphinx_rtd_theme

%py3_provides %oname

%description
The aim of the wrapt module is to provide a transparent object proxy for
Python, which can be used as the basis for the construction of function
wrappers and decorator functions.

%package pickles
Summary: Pickles for %oname
Group: Development/Python3

%description pickles
The aim of the wrapt module is to provide a transparent object proxy for
Python, which can be used as the basis for the construction of function
wrappers and decorator functions.

This package contains pickles for %oname.

%package docs
Summary: Documentation for %oname
Group: Development/Documentation
BuildArch: noarch

%description docs
The aim of the wrapt module is to provide a transparent object proxy for
Python, which can be used as the basis for the construction of function
wrappers and decorator functions.

This package contains documentation for %oname.

%prep
%setup

%prepare_sphinx3 .
ln -s ../objects.inv docs/

%build
%add_optflags -fno-strict-aliasing
%python3_build_debug

%install
%python3_install

%make SPHINXBUILD="sphinx-build-3" -C docs pickle
%make SPHINXBUILD="sphinx-build-3" -C docs html

cp -fR docs/_build/pickle %buildroot%python3_sitelibdir/%oname/

%check
export PYTHONPATH=%buildroot%python3_sitelibdir
py.test3

%files
%doc README.rst
%python3_sitelibdir/%oname
%python3_sitelibdir/*.egg-info
%exclude %python3_sitelibdir/*/pickle

%files pickles
%python3_sitelibdir/*/pickle

%files docs
%doc docs/_build/html blog

%changelog
* Mon Feb 27 2023 Grigory Ustinov <grenka@altlinux.org> 1.15.0-alt1
- Automatically updated to 1.15.0.

* Thu May 12 2022 Grigory Ustinov <grenka@altlinux.org> 1.14.1-alt1
- Automatically updated to 1.14.1.

* Tue Mar 15 2022 Grigory Ustinov <grenka@altlinux.org> 1.14.0-alt1
- Automatically updated to 1.14.0.

* Tue Feb 08 2022 Grigory Ustinov <grenka@altlinux.org> 1.13.3-alt1
- Build new version.
- Enable check.

* Mon Feb 08 2021 Grigory Ustinov <grenka@altlinux.org> 1.12.1-alt2
- Disable check for python3.9.

* Sat Aug 01 2020 Grigory Ustinov <grenka@altlinux.org> 1.12.1-alt1
- Build new version.
- Drop specsubst scheme.
- Drop python2 support.

* Wed Jun 19 2019 Grigory Ustinov <grenka@altlinux.org> 1.11.2-alt1
- Build new version.

* Sun Jan 20 2019 Grigory Ustinov <grenka@altlinux.org> 1.11.1-alt1
- Build new version.

* Fri Jan 11 2019 Grigory Ustinov <grenka@altlinux.org> 1.11.0-alt1
- Build new version.

* Thu May 10 2018 Grigory Ustinov <grenka@altlinux.org> 1.10.11-alt2
- Fix provides for docs part.

* Thu Apr 26 2018 Grigory Ustinov <grenka@altlinux.org> 1.10.11-alt1
- Build new version.
- Tranfer package to subst-packaging system.

* Thu Mar 22 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 1.9.0-alt2.git20140822.1.1.1.1
- (NMU) Rebuilt with python-3.6.4.

* Tue Jul 11 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 1.9.0-alt2.git20140822.1.1.1
- Fixed build spec

* Mon May 23 2016 Ivan Zakharyaschev <imz@altlinux.org> 1.9.0-alt1.git20140822.1.1.1
- BR: sphinx_rtd_theme (the theme is optional since sphinx-1.4.1).

* Thu Mar 17 2016 Ivan Zakharyaschev <imz@altlinux.org> 1.9.0-alt1.git20140822.1.1
- (NMU) rebuild with python3-3.5 & rpm-build-python3-0.1.10
  (for ABI dependence and new python3(*) reqs)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 1.9.0-alt1.git20140822.1
- NMU: Use buildreq for BR.

* Sat Nov 08 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.9.0-alt1.git20140822
- Initial build for Sisyphus

