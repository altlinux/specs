# REMOVE ME (I was set for NMU) and uncomment real Release tags:
Release: alt1.1.1
%define ocore backports
%define oname %ocore.ssl_match_hostname

%def_with python3

Name: python-module-%oname
Version: 3.5.0.1
#Release: alt1
Summary: The ssl.match_hostname() function from Python 3.5
License: Python
Group: Development/Python
Url: https://pypi.python.org/pypi/backports.ssl_match_hostname/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar

#BuildPreReq: python-devel python-module-setuptools

%py_provides %oname
%py_requires %ocore

# Automatically added by buildreq on Wed Jan 27 2016 (-bi)
# optimized out: python-base python-devel python-module-pytest python-module-setuptools python-modules python-modules-compiler python-modules-ctypes python-modules-email python-modules-encodings python-modules-unittest python3 python3-base python3-module-setuptools
BuildRequires: python-module-setuptools python3-module-pytest rpm-build-python3

%description
The Secure Sockets layer is only actually secure if you check the
hostname in the certificate returned by the server to which you are
connecting, and verify that it matches to hostname that you are trying
to reach.

But the matching logic, defined in RFC2818, can be a bit tricky to
implement on your own. So the ssl package in the Standard Library of
Python 3.2 and greater now includes a match_hostname() function for
performing this check instead of requiring every application to
implement the check separately.

%package -n python-module-%ocore
Summary: Core package of %ocore
Group: Development/Python
%py_provides %ocore

%description -n python-module-%ocore
Core package of %ocore.

%prep
%setup

%build
%python_build_debug

%install
%python_install

%if "%_libexecdir" != "%_libdir"
mv %buildroot%_libexecdir %buildroot%_libdir
%endif

%files
%doc PKG-INFO
%python_sitelibdir/%ocore/*
%python_sitelibdir/*.egg-info
%exclude %python_sitelibdir/%ocore/__init__.py*

%files -n python-module-%ocore
%dir %python_sitelibdir/%ocore
%python_sitelibdir/%ocore/__init__.py*

%changelog
* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 3.5.0.1-alt1.1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Tue May 24 2016 Ivan Zakharyaschev <imz@altlinux.org> 3.5.0.1-alt1.1
- (AUTO) subst_x86_64.

* Fri May 6 2016 Vladimir Didenko <cow@altlinux.org> 3.5.0.1-alt1
- New version
- Don't pack Python 3 version anymore

* Mon Apr 11 2016 Ivan Zakharyaschev <imz@altlinux.org> 3.4.0.2-alt2.1.1.1
- (NMU) rebuild with rpm-build-python3-0.1.10 (for new-style python3(*) reqs)
  and with python3-3.5 (for byte-compilation).

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 3.4.0.2-alt2.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 3.4.0.2-alt2.1
- NMU: Use buildreq for BR.

* Mon Oct 20 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.4.0.2-alt2
- Added module for Python 3

* Fri Jul 11 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.4.0.2-alt1
- Initial build for Sisyphus
