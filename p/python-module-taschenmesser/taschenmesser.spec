%define oname taschenmesser
Name: python-module-%oname
Version: 0.1.5
Release: alt1.git20140825
Summary: Taschenmesser, a toolbelt with plugins for SCons
License: ASLv2.0
Group: Development/Python
Url: https://pypi.python.org/pypi/taschenmesser/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/oberstet/taschenmesser.git
Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-module-setuptools-tests python-module-boto
BuildPreReq: python-module-scour scons

%py_provides %oname

%description
Taschenmesser is a toolbelt containing builders for SCons. It helps you
getting stuff done.

%prep
%setup

%build
%python_build_debug

%install
%python_install

%check
python setup.py test

%files
%doc *.md
%python_sitelibdir/*

%changelog
* Sun Nov 09 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1.5-alt1.git20140825
- Initial build for Sisyphus

