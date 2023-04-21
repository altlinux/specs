%define oname pamqp

%def_without docs

%def_with check

Name: python3-module-%oname
Version: 3.2.1
Release: alt1

Summary: RabbitMQ Focused AMQP low-level library
License: BSD-3-Clause
Group: Development/Python3
Url: https://pypi.python.org/pypi/pamqp/
Vcs: https://github.com/gmr/pamqp.git

Source: %name-%version.tar

BuildArch: noarch

BuildRequires(pre): rpm-build-python3
%if_with docs
BuildRequires(pre): rpm-macros-sphinx3
BuildRequires: python3-module-sphinx
BuildRequires: python3-module-sphinx-autodoc-typehints
%endif

%py3_provides %oname

%description
pamqp is a pure-python AMQP 0-9-1 frame encoder and decoder. The aim is
to create a client agnostic python encoder and decoder for general
purpose use.

%if_with docs
%package pickles
Summary: Pickles for %oname
Group: Development/Python3

%description pickles
pamqp is a pure-python AMQP 0-9-1 frame encoder and decoder. The aim is
to create a client agnostic python encoder and decoder for general
purpose use.

This package contains pickles for %oname.

%package docs
Summary: Documentation for %oname
Group: Development/Documentation
BuildArch: noarch

%description docs
pamqp is a pure-python AMQP 0-9-1 frame encoder and decoder. The aim is
to create a client agnostic python encoder and decoder for general
purpose use.

This package contains documentation for %oname.
%endif

%prep
%setup

%build
%python3_build

%if_with docs
export PYTHONPATH="$PWD"
sphinx-build-3 docs pickle
sphinx-build-3 docs html
%endif

%install
%python3_install

%if_with docs
cp -fR docs/_build/pickle %buildroot%python3_sitelibdir/%oname/
%endif

%check
%tox_create_default_config
%tox_check

%files
%doc *.rst LICENSE
%python3_sitelibdir/%oname
%python3_sitelibdir/%oname-%version-*.egg-info
%if_with docs
%exclude %python3_sitelibdir/*/pickle

%files pickles
%dir %python3_sitelibdir/%oname
%python3_sitelibdir/*/pickle

%files docs
%doc docs/_build/html/*
%endif

%changelog
* Thu Apr 13 2023 Anton Vyatkin <toni@altlinux.org> 3.2.1-alt1
- (NMU) New version 3.2.1.

* Fri Oct 23 2020 Stanislav Levin <slev@altlinux.org> 1.6.1-alt3
- Dropped dependency on coveralls.

* Sat Aug 01 2020 Grigory Ustinov <grenka@altlinux.org> 1.6.1-alt2
- Drop python2 support.

* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 1.6.1-alt1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Mon Nov 27 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 1.6.1-alt1
- Updated to upstream version 1.6.1.

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 1.6.0-alt1.git20141212.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 1.6.0-alt1.git20141212.1
- NMU: Use buildreq for BR.

* Thu Dec 25 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.6.0-alt1.git20141212
- Version 1.6.0

* Thu Nov 06 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.5.0-alt1.git20141105
- Version 1.5.0

* Tue Nov 04 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.3.1-alt1.git20140505
- Initial build for Sisyphus

