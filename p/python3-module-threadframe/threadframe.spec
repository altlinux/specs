%define oname threadframe

Name: python3-module-%oname
Version: 0.2
Release: alt1
Summary: Advanced thread debugging extension
License: Python
Group: Development/Python3
Url: http://pypi.python.org/pypi/threadframe/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools

%description
Obtaining tracebacks on other threads than the current thread.

%prep
%setup

%build
%python3_build

%install
%python3_install

%files
%doc README
%python3_sitelibdir/*

%changelog
* Sun Jul 27 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.2-alt1
- Initial build for Sisyphus

