%define oname threadframe

Name: python3-module-%oname
Version: 0.2
Release: alt2
Summary: Advanced thread debugging extension
License: Python
Group: Development/Python3
Url: http://pypi.python.org/pypi/threadframe/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3
#BuildPreReq: python3-devel python3-module-setuptools

# Automatically added by buildreq on Thu Jan 28 2016 (-bi)
# optimized out: elfutils python-base python3 python3-base
BuildRequires: python3-devel rpm-build-python3

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
* Fri Jan 29 2016 Mikhail Efremov <sem@altlinux.org> 0.2-alt2
- NMU: Use buildreq for BR.

* Sun Jul 27 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.2-alt1
- Initial build for Sisyphus

