%define oname robotframework-lint
Name: python-module-%oname
Version: 0.1
Release: alt1.git20141130
Summary: Static analysis tool for robotframework plain text files
License: ASLv2.0
Group: Development/Python
Url: https://pypi.python.org/pypi/robotframework-lint
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/boakley/robotframework-lint.git
Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-devel python-module-setuptools-tests
BuildPreReq: python-module-robotframework

%py_provides rflint

%description
Linter for robot framework plain text files.

This is a static analysis tool for robot framework plain text files.

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
* Mon Dec 01 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1-alt1.git20141130
- New snapshot

* Wed Nov 26 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1-alt1.git20141125
- Initial build for Sisyphus

