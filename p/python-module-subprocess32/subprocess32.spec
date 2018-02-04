%define _unpackaged_files_terminate_build 1
%define oname subprocess32
Name: python-module-%oname
Version: 3.2.7
Release: alt1.1
Summary: Backport of the subprocess module from Python 3.2/3.3 for use on 2.x
License: PSFL
Group: Development/Python
Url: https://pypi.python.org/pypi/subprocess32/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source0: https://pypi.python.org/packages/b8/2f/49e53b0d0e94611a2dc624a1ad24d41b6d94d0f1b0a078443407ea2214c2/%{oname}-%{version}.tar.gz

BuildPreReq: python-devel python-module-setuptools

%py_provides %oname

%description
This is a backport of the subprocess standard library module from Python
3.2 & 3.3 for use on Python 2.4, 2.5, 2.6 and 2.7. It includes bugfixes
and new features. On POSIX systems it is guaranteed to be reliable when
used in threaded applications. Bonus: It includes timeout support from
Python 3.3.

%prep
%setup -q -n %{oname}-%{version}

%build
%python_build_debug

%install
%python_install

%files
%doc ChangeLog PKG-INFO README.md
%python_sitelibdir/*

%changelog
* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 3.2.7-alt1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Tue Jan 17 2017 Igor Vlasenko <viy@altlinux.ru> 3.2.7-alt1
- automated PyPI update

* Tue Jan 20 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.2.6-alt1
- Initial build for Sisyphus

