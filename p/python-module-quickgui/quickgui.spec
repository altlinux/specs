%define oname quickgui
Name: python-module-%oname
Version: 1.5.1
Release: alt1
Summary: Rapidly create gui without any knowledge of wxpython
License: MIT
Group: Development/Python
Url: https://pypi.python.org/pypi/quickgui/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-module-setuptools-tests python-module-wx3.0

%py_provides %oname
Requires: python-module-wx > 2.9

%description
Rapidly create GUI without any knowledge of wxpython.

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
* Wed Feb 04 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.5.1-alt1
- Initial build for Sisyphus

