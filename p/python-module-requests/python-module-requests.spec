%define _unpackaged_files_terminate_build 1
%define pkgname requests
%def_with python3

Name:           python-module-requests
Version:        2.12.4
Release:        alt3
Summary:        HTTP library, written in Python, for human beings
Group:          Development/Python

License:        ASL 2.0
URL:            http://pypi.python.org/pypi/requests
# https://github.com/kennethreitz/requests.git
Source0:        https://pypi.python.org/packages/5b/0b/34be574b1ec997247796e5d516f3a6b6509c4e064f2885a96ed885ce7579/requests-%{version}.tar.gz
# Explicitly use the system certificates in ca-certificates.
# https://bugzilla.redhat.com/show_bug.cgi?id=904614
Patch0:         python-requests-system-cert-bundle.patch
# Unbundle python-charade (a fork of python-chardet).
# https://bugzilla.redhat.com/show_bug.cgi?id=904623
Patch1:         python-requests-system-chardet-not-charade.patch
# Unbundle python-urllib3 (a fork of python-urllib3).
# https://bugzilla.redhat.com/show_bug.cgi?id=904623
Patch2:         python-requests-system-urllib3.patch

BuildArch:      noarch

BuildRequires:  python-devel python-modules-json
BuildRequires:  python-module-chardet
BuildRequires:  python-module-urllib3 >= 1.13.1
BuildRequires:  python-module-idna
BuildRequires:  python-module-httpbin
BuildRequires:  python-module-setuptools-tests

Requires:       ca-certificates
Requires:       python-module-chardet
Requires:       python-module-urllib3 >= 1.13.1
%py_requires json

%description
Most existing Python modules for sending HTTP requests are extremely verbose and
cumbersome. Python's built-in urllib2 module provides most of the HTTP
capabilities you should need, but the API is thoroughly broken. This library is
designed to make HTTP requests easy for developers.

%if_with python3
%package -n python3-module-%pkgname
Summary: HTTP library, written in Python, for human beings
Group:   Development/Python3
BuildRequires(pre): rpm-build-python3
BuildRequires:  python3-devel
BuildRequires:  python3-module-chardet
BuildRequires:  python3-module-urllib3 >= 1.13.1
BuildRequires:  python3-module-idna
BuildRequires:  python3-module-httpbin
BuildRequires:  python3-module-setuptools-tests
Requires:       ca-certificates
Requires:       python3-module-chardet
Requires:       python3-module-urllib3 >= 1.13.1
%py3_requires json

%description -n python3-module-%pkgname
Most existing Python modules for sending HTTP requests are extremely verbose and
cumbersome. Python's built-in urllib2 module provides most of the HTTP
capabilities you should need, but the API is thoroughly broken. This library is
designed to make HTTP requests easy for developers.
%endif

%prep
%setup -q -n requests-%{version}

%patch0 -p1
%patch1 -p1
%patch2 -p1

# Unbundle the certificate bundle from mozilla.
rm -rf requests/cacert.pem

%if_with python3
rm -rf ../python3
cp -a . ../python3
%endif

%build
%python_build

# Unbundle chardet.  Patch1 switches usage to system chardet.
# Unbundle urllib3.  Patch2 switches usage to system urllib3.
rm -rf build/lib/requests/packages

%if_with python3
pushd ../python3
%python3_build

# Unbundle chardet.  Patch1 switches usage to system chardet.
# Unbundle urllib3.  Patch2 switches usage to system urllib3.
rm -rf build/lib/requests/packages

popd
%endif

%install
%python_install

%if_with python3
pushd ../python3
%python3_install
popd
%endif


## The tests succeed if run locally, but fail in koji.
## They require an active network connection to query httpbin.org
#%%check
#%%{__python} test_requests.py
#%%if 0%%{?_with_python3}
#pushd %%{py3dir}
#%%{__python3} test_requests.py
#popd
#%%endif

%files
%doc NOTICE LICENSE README.rst HISTORY.rst
%python_sitelibdir/*

%if_with python3
%files -n python3-module-%pkgname
%doc NOTICE LICENSE README.rst HISTORY.rst
%python3_sitelibdir/*
%endif

%changelog
* Mon Jan 16 2017 Igor Vlasenko <viy@altlinux.ru> 2.12.4-alt3
- removed bundled idna

* Mon Jan 16 2017 Igor Vlasenko <viy@altlinux.ru> 2.12.4-alt2
- updated urllib3 patches

* Wed Jan 11 2017 Igor Vlasenko <viy@altlinux.ru> 2.12.4-alt1
- automated PyPI update

* Fri May 6 2016 Vladimir Didenko <cow@altlinux.ru> 2.10.0-alt1
- 2.10.0

* Wed Apr 20 2016 Alexey Shabalin <shaba@altlinux.ru> 2.9.1-alt1
- 2.9.1

* Mon Apr 11 2016 Ivan Zakharyaschev <imz@altlinux.org> 2.7.0-alt1.git20150719.1.1.1
- (NMU) rebuild with rpm-build-python3-0.1.10 (for new-style python3(*) reqs)
  and with python3-3.5 (for byte-compilation).

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 2.7.0-alt1.git20150719.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 2.7.0-alt1.git20150719.1
- NMU: Use buildreq for BR.

* Fri Jul 31 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.7.0-alt1.git20150719
- Version 2.7.0

* Thu Mar 19 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.6.0-alt1.git20150316
- Version 2.6.0

* Fri Feb 06 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.5.1-alt1.git20150204
- New snapshot

* Mon Jan 19 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.5.1-alt1.git20150109
- New snapshot

* Wed Dec 24 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.5.1-alt1.git20141223
- Version 2.5.1

* Tue Dec 23 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.5.0-alt1.git20141216
- Version 2.5.0

* Tue Nov 11 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.4.3-alt2.git20141107
- New snapshot

* Fri Nov 07 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.4.3-alt2.git20141101
- I took it

* Fri Nov 07 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.4.3-alt1.git20141101
- Version 2.4.3 (ALT #30439)

* Tue Jul 22 2014 Lenar Shakirov <snejok@altlinux.ru> 2.3.0-alt1
- New version (based on Fedora - 2.3.0-2.fc21.src)
- Unbundle urllib3 and chardet packages (use system modules)

* Fri Mar 22 2013 Aleksey Avdeev <solo@altlinux.ru> 0.12.1-alt1.1
- Rebuild with Python-3.3

* Fri May 18 2012 Vitaly Kuznetsov <vitty@altlinux.ru> 0.12.1-alt1
- initial
