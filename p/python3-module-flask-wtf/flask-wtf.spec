%define oname flask-wtf

%def_with check

Name: python3-module-%oname
Version: 1.1.1
Release: alt1

Summary: Simple integration of Flask and WTForms

License: BSD-3-Clause
Group: Development/Python3
Url: https://pypi.python.org/pypi/Flask-WTF/

# https://github.com/lepture/flask-wtf.git
Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-flask
BuildRequires: python3-module-flask-babel
BuildRequires: python3-module-pallets-sphinx-themes
BuildRequires: python3-module-setuptools
BuildRequires: python3-module-sphinx
BuildRequires: python3-module-sphinx-issues
BuildRequires: python3-module-sphinxcontrib-log-cabinet
BuildRequires: python3-module-werkzeug
BuildRequires: python3-module-wheel
BuildRequires: python3-module-wtforms

%py3_provides flask_wtf

BuildArch: noarch

%description
Simple integration of Flask and WTForms, including CSRF, file upload and
Recaptcha integration.

%package pickles
Summary: Pickles for %oname
Group: Development/Python3

%description pickles
Simple integration of Flask and WTForms, including CSRF, file upload and
Recaptcha integration.

This package contains pickles for %oname.

%package docs
Summary: Documentation for %oname
Group: Development/Documentation
BuildArch: noarch

%description docs
Simple integration of Flask and WTForms, including CSRF, file upload and
Recaptcha integration.

This package contains documentation for %oname.

%prep
%setup

sed -i 's|sphinx-build|sphinx-build-3|' docs/Makefile

%build
%pyproject_build
PYTHONPATH=$(pwd)/src %make -C docs pickle html

%install
%pyproject_install
install -d %buildroot%python3_sitelibdir/%oname
cp -fR docs/_build/pickle %buildroot%python3_sitelibdir/%oname/

%check
%tox_check_pyproject

%files
%doc README.rst
%python3_sitelibdir/flask_wtf
%python3_sitelibdir/Flask_WTF-%version.dist-info
%exclude %python3_sitelibdir/*/pickle

%files pickles
%python3_sitelibdir/*/pickle

%files docs
%doc docs/_build/html examples

%changelog
* Wed Jan 18 2023 Grigory Ustinov <grenka@altlinux.org> 1.1.1-alt1
- Automatically updated to 1.1.1.
- Build with check.

* Mon Jan 16 2023 Andrey Cherepanov <cas@altlinux.org> 1.1.0-alt1
- New version.

* Mon Oct 03 2022 Grigory Ustinov <grenka@altlinux.org> 1.0.1-alt2
- Fixed build requires.

* Sat May 28 2022 Grigory Ustinov <grenka@altlinux.org> 1.0.1-alt1
- Automatically updated to 1.0.1.

* Tue Jun 01 2021 Grigory Ustinov <grenka@altlinux.org> 0.15.1-alt1
- Automatically updated to 0.15.1.

* Mon Feb 10 2020 Andrey Bychkov <mrdrew@altlinux.org> 0.14.2-alt2
- Build for python2 disabled.

* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 0.14.2-alt1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Wed Aug 23 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 0.14.2-alt1
- Updated to upstream version 0.14.2.

* Tue Oct 21 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.10.2-alt1.git20141005
- Initial build for Sisyphus

