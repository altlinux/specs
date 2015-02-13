%define oname kotti_bootswatch
Name: python-module-%oname
Version: 0.1.3
Release: alt1.dev0.git20141231
Summary: Kotti bootswatch theme / theme generator
License: BSD
Group: Development/Python
Url: https://pypi.python.org/pypi/kotti_bootswatch/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/mete0r/kotti_bootswatch.git
Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-module-setuptools-tests python-module-kotti-tests
BuildPreReq: python-module-fanstatic python-module-pyramid
BuildPreReq: python-module-js.bootstrap

%py_provides %oname
%py_requires kotti fanstatic pyramid js.bootstrap

%description
Bootswatch theme and theme generator for Kotti.

This theme and the generated themes supersede css files of the
js.bootstrap and Kotti via fanstatic's supersedes and rollup mechanism.

%prep
%setup

%build
%python_build_debug

%install
%python_install

%check
python setup.py test

%files
%doc *.rst
%python_sitelibdir/*

%changelog
* Fri Feb 13 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1.3-alt1.dev0.git20141231
- Initial build for Sisyphus

