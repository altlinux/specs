%define oname run-io
Name: python3-module-%oname
Version: 0.7.0
Release: alt1.git20141130.1.1
Summary: A plugin for Run
License: MIT
Group: Development/Python3
Url: https://pypi.python.org/pypi/run-io/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/run-hub/run-io.git
Source: %name-%version.tar
BuildArch: noarch

BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools
BuildPreReq: python3-module-runfile python3-module-run-function
BuildPreReq: python3-module-nose python3-module-coverage

%py3_provides run_io
%py3_requires run run_function
%add_python3_req_skip run.plugins.function

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
* Tue Feb 13 2018 Stanislav Levin <slev@altlinux.org> 0.7.0-alt1.git20141130.1.1
- (NMU) Fix Requires and BuildRequires to python setuptools

* Mon Mar 14 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.7.0-alt1.git20141130.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Mon Jan 26 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.7.0-alt1.git20141130
- Initial build for Sisyphus

