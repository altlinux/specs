%define oname subprocess32
Name: python-module-%oname
Version: 3.2.6
Release: alt1
Summary: Backport of the subprocess module from Python 3.2/3.3 for use on 2.x
License: PSFL
Group: Development/Python
Url: https://pypi.python.org/pypi/subprocess32/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar

BuildPreReq: python-devel python-module-setuptools-tests

%py_provides %oname

%description
This is a backport of the subprocess standard library module from Python
3.2 & 3.3 for use on Python 2.4, 2.5, 2.6 and 2.7. It includes bugfixes
and new features. On POSIX systems it is guaranteed to be reliable when
used in threaded applications. Bonus: It includes timeout support from
Python 3.3.

%prep
%setup

%build
%python_build_debug

%install
%python_install

%files
%doc ChangeLog *.txt
%python_sitelibdir/*

%changelog
* Tue Jan 20 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.2.6-alt1
- Initial build for Sisyphus

