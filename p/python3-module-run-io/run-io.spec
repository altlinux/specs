%define oname run-io
Name: python3-module-%oname
Version: 0.7.0
Release: alt1.git20141130
Summary: A plugin for Run
License: MIT
Group: Development/Python3
Url: https://pypi.python.org/pypi/run-io/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/run-hub/run-io.git
Source: %name-%version.tar
BuildArch: noarch

BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools-tests
BuildPreReq: python3-module-runfile python3-module-run-function
BuildPreReq: python3-module-nose python3-module-coverage

%py3_provides run_io
%py3_requires run run_function

%description
Run-io is a plugin for Run.

%prep
%setup

%build
%python3_build_debug

%install
%python3_install

%check
python3 setup.py test

%files
%doc *.rst docs/*.rst
%python3_sitelibdir/*

%changelog
* Mon Jan 26 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.7.0-alt1.git20141130
- Initial build for Sisyphus

