%define oname wtforms

%def_with check

Name: python3-module-%oname
Version: 3.0.1
Release: alt2

Summary: A flexible forms validation and rendering library for python web development

License: BSD-3-Clause
Group: Development/Python3
Url: https://pypi.python.org/pypi/WTForms/

BuildArch: noarch

# https://github.com/wtforms/wtforms.git
Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-setuptools
BuildRequires: python3-module-wheel

BuildRequires: python3-module-sphinx
BuildRequires: python3-module-pallets-sphinx-themes
BuildRequires: python3-module-sphinx-issues
BuildRequires: python3-module-sphinxcontrib-log-cabinet

%if_with check
BuildRequires: python3-module-email_validator
%endif

%description
WTForms is a flexible forms validation and rendering library for python
web development.

To get started using WTForms, we recommend reading the crash course on
the website: http://wtforms.simplecodes.com/.

%package pickles
Summary: Pickles for %oname
Group: Development/Python3

%description pickles
WTForms is a flexible forms validation and rendering library for python
web development.

This package contains pickles for %oname.

%package docs
Summary: Documentation for %oname
Group: Development/Documentation

%description docs
WTForms is a flexible forms validation and rendering library for python
web development.

This package contains documentation for %oname.

%prep
%setup

sed -i 's|sphinx-build|&-3|' docs/Makefile

%build
%pyproject_build

%install
%pyproject_install

export PYTHONPATH=%buildroot%python3_sitelibdir
%make -C docs pickle html
cp -fR docs/_build/pickle %buildroot%python3_sitelibdir/%oname/

%check
%tox_check_pyproject

%files
%doc README.rst
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*/pickle

%files pickles
%python3_sitelibdir/*/pickle

%files docs
%doc docs/_build/html/*

%changelog
* Wed Jan 18 2023 Grigory Ustinov <grenka@altlinux.org> 3.0.1-alt2
- Built with pyproject macros.
- Built with check.

* Sat May 28 2022 Grigory Ustinov <grenka@altlinux.org> 3.0.1-alt1
- Automatically updated to 3.0.1.

* Fri Jul 31 2020 Andrey Cherepanov <cas@altlinux.org> 2.3.3-alt1
- New version.

* Sun Apr 26 2020 Andrey Cherepanov <cas@altlinux.org> 2.3.1-alt1
- New version.

* Wed Apr 22 2020 Andrey Cherepanov <cas@altlinux.org> 2.3.0-alt1
- New version.

* Tue Apr 14 2020 Andrey Bychkov <mrdrew@altlinux.org> 2.2.1-alt2
- Build for python2 disabled.

* Tue Mar 24 2020 Andrey Cherepanov <cas@altlinux.org> 2.2.1-alt1
- New version.
- Fix License tag according to SPDX.

* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 2.1-alt1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Wed Aug 23 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 2.1-alt1
- Updated to upstream version 2.1.

* Tue Dec 23 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.0.2-alt1.dev.git20141210
- New snapshot

* Thu Oct 16 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.0.2-alt1.dev.git20140718
- Initial build for Sisyphus

