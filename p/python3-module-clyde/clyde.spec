%define oname clyde
Name: python3-module-%oname
Version: 0.8.0
Release: alt1.git20141130
Summary: Command line interface designer
License: MIT
Group: Development/Python3
Url: https://pypi.python.org/pypi/clyde/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/clyde-hub/clyde.git
Source: %name-%version.tar
BuildArch: noarch

BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools-tests
BuildPreReq: python3-module-sugarbowl python3-module-jinja2
BuildPreReq: python3-module-nose python3-module-coverage
BuildPreReq: python-module-sphinx-devel python3-module-sphinx
BuildPreReq: python3-module-sphinx-settings
BuildPreReq: python3-module-sphinx_rtd_theme

%py3_provides %oname
%py3_requires sugarbowl jinja2

%description
Clyde is a command line interface designer.

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
%python3_sitelibdir/*

%changelog
* Mon Jan 26 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.8.0-alt1.git20141130
- Initial build for Sisyphus

