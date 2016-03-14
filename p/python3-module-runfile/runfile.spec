%define oname runfile
Name: python3-module-%oname
Version: 0.46.1
Release: alt1.git20141130.1
Summary: Run tasks from files
License: MIT
Group: Development/Python3
Url: https://pypi.python.org/pypi/runfile/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/run-hub/run.git
Source: %name-%version.tar
BuildArch: noarch

BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools-tests
BuildPreReq: python3-module-sugarbowl python3-module-clyde
BuildPreReq: python3-module-nose python3-module-coverage
BuildPreReq: python3-module-sphinx python3-module-sphinx-settings
BuildPreReq: python3-module-sphinx_rtd_theme

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

export PYTHONPATH=$PWD
pushd docs
py3_sphinx-build -b html -d _build/doctrees . _build/html
popd

%check
python3 setup.py test

%files
%doc *.rst demo docs/_build/html
%_bindir/*
%python3_sitelibdir/*

%changelog
* Mon Mar 14 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.46.1-alt1.git20141130.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Mon Jan 26 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.46.1-alt1.git20141130
- Initial build for Sisyphus

