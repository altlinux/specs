%define oname sphinx-argparse

Name: python3-module-%oname
Version: 0.4.0
Release: alt1

Summary: Sphinx extension that automatically document argparse commands and options

License: MIT
Group: Development/Python3
URL: https://pypi.org/project/sphinx-argparse
VCS: https://github.com/sphinx-doc/sphinx-argparse

BuildArch: noarch

Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-sphinx
BuildRequires: python3-module-poetry
BuildRequires: python3-module-pkg_resources
BuildRequires: python3-module-sphinx_rtd_theme
BuildRequires: python3-module-pytest python3-module-commonmark

Requires: python3-module-commonmark

%py3_provides sphinxarg


%description
Sphinx extension that automatically document argparse commands and
options.

%package pickles
Summary: Pickles for %oname
Group: Development/Python3

%description pickles
Sphinx extension that automatically document argparse commands and
options.

This package contains pickles for %oname.

%package docs
Summary: Documentation for %oname
Group: Development/Documentation
BuildArch: noarch

%description docs
Sphinx extension that automatically document argparse commands and
options.

This package contains documentation for %oname.

%prep
%setup

sed -i 's|sphinx-build|sphinx-build-3|' docs/Makefile

%build
%pyproject_build

%install
%pyproject_install

export PYTHONPATH=%buildroot%python3_sitelibdir
%make -C docs pickle
%make -C docs html

install -d %buildroot%python3_sitelibdir/%oname
cp -fR docs/_build/pickle %buildroot%python3_sitelibdir/%oname/

%check
%pyproject_run_pytest

%files
%doc *.md
%python3_sitelibdir/sphinxarg
%python3_sitelibdir/sphinx_argparse-%version.dist-info
%exclude %python3_sitelibdir/*/pickle

%files pickles
%python3_sitelibdir/*/pickle

%files docs
%doc docs/_build/html/*

%changelog
* Thu May 30 2024 Grigory Ustinov <grenka@altlinux.org> 0.4.0-alt1
- Build new version.

* Sat Apr 03 2021 Grigory Ustinov <grenka@altlinux.org> 0.2.5-alt2
- Fixed BuildRequires.

* Fri Jan 17 2020 Andrey Bychkov <mrdrew@altlinux.org> 0.2.5-alt1
- Version updated to 0.2.5
- porting on python3.

* Mon Jun 10 2019 Stanislav Levin <slev@altlinux.org> 0.1.13-alt1.git20140818.1.1
- Added missing dep on Pytest.

* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 0.1.13-alt1.git20140818.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Thu Oct 30 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1.13-alt1.git20140818
- Initial build for Sisyphus

