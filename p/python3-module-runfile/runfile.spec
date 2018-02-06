%define oname runfile

%def_without docs

Name: python3-module-%oname
Version: 0.46.1
Release: alt1.git20141130.2.1
Summary: Run tasks from files
License: MIT
Group: Development/Python3
BuildArch: noarch
Url: https://pypi.python.org/pypi/runfile/

# https://github.com/run-hub/run.git
Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel python3-module-setuptools
BuildRequires: python3-module-sugarbowl python3-module-clyde
BuildRequires: python3-module-nose python3-module-coverage
%if_with docs
BuildRequires: python3-module-sphinx python3-module-sphinx-settings
BuildRequires: python3-module-sphinx_rtd_theme
%endif

%py3_provides run
%py3_requires sugarbowl clyde

%description
Run is a program to run tasks from files.

%prep
%setup

%build
%python3_build_debug

%install
%python3_install

%if_with docs
export PYTHONPATH=$PWD
pushd docs
py3_sphinx-build -b html -d _build/doctrees . _build/html
popd
%endif

%check
python3 setup.py test

%files
%doc *.rst demo
%if_with docs
%doc docs/_build/html
%endif
%_bindir/*
%python3_sitelibdir/*

%changelog
* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 0.46.1-alt1.git20141130.2.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Wed Nov 01 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 0.46.1-alt1.git20141130.2
- Rebuilt without docs since doc generation config is incompatible with python-module-sphinx-1.6.5.

* Mon Mar 14 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.46.1-alt1.git20141130.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Mon Jan 26 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.46.1-alt1.git20141130
- Initial build for Sisyphus

