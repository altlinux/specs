%define ocore backports
%define oname %ocore.ssl_match_hostname

Name: python3-module-%oname
Version: 3.7.0.1
Release: alt1

Summary: The ssl.match_hostname() function from Python 3.5
License: Python
Group: Development/Python3
Url: https://pypi.python.org/pypi/backports.ssl_match_hostname/

Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-pytest

%py3_requires %ocore
%py3_provides %oname


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

%package -n python3-module-%ocore
Summary: Core package of %ocore
Group: Development/Python3
%py3_provides %ocore

%description -n python3-module-%ocore
Core package of %ocore.

%prep
%setup

%build
%python3_build_debug

%install
%python3_install

%if "%_libexecdir" != "%_libdir"
mv %buildroot%_libexecdir %buildroot%_libdir
%endif

%files
%doc PKG-INFO
%python3_sitelibdir/%ocore/*
%python3_sitelibdir/*.egg-info
%exclude %python3_sitelibdir/%ocore/__init__.py*

%files -n python3-module-%ocore
%dir %python3_sitelibdir/%ocore
%python3_sitelibdir/%ocore/__init__.py*


%changelog
* Wed Jan 22 2020 Andrey Bychkov <mrdrew@altlinux.org> 3.7.0.1-alt1
- Version updated to 3.7.0.1
- porting on python3.

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
