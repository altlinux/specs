%define oname sphinx-argparse

Name: python3-module-%oname
Version: 0.2.5
Release: alt1

Summary: Sphinx extension that automatically document argparse commands and options
License: MIT
Group: Development/Python3
Url: https://pypi.python.org/pypi/sphinx-argparse/
BuildArch: noarch

# https://github.com/ribozz/sphinx-argparse.git
Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-sphinx python3-module-pytest
BuildRequires: python3-module-sphinx_rtd_theme
BuildRequires: python3-module-pytest python3-module-commonmark0.7

Requires: python3-module-commonmark0.7

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
%python3_build_debug

%install
%python3_install

export PYTHONPATH=$PWD
%make -C docs pickle
%make -C docs html

install -d %buildroot%python3_sitelibdir/%oname
cp -fR docs/_build/pickle %buildroot%python3_sitelibdir/%oname/

%check
%__python3 setup.py test

%files
%doc *.md
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*/pickle

%files pickles
%python3_sitelibdir/*/pickle

%files docs
%doc docs/_build/html/*


%changelog
* Fri Jan 17 2020 Andrey Bychkov <mrdrew@altlinux.org> 0.2.5-alt1
- Version updated to 0.2.5
- porting on python3.

* Mon Jun 10 2019 Stanislav Levin <slev@altlinux.org> 0.1.13-alt1.git20140818.1.1
- Added missing dep on Pytest.

* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 0.1.13-alt1.git20140818.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Thu Oct 30 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1.13-alt1.git20140818
- Initial build for Sisyphus

