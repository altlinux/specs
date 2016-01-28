%define pkgname requests
%def_with python3

Name:           python-module-requests
Version:        2.7.0
Release:        alt1.git20150719.1
Summary:        HTTP library, written in Python, for human beings
Group:          Development/Python

License:        ASL 2.0
URL:            http://pypi.python.org/pypi/requests
# https://github.com/kennethreitz/requests.git
Source0:        %{name}-%{version}.tar
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
# Automatically added by buildreq on Thu Jan 28 2016 (-bi)
# optimized out: python-base python-devel python-module-cffi python-module-cryptography python-module-enum34 python-module-pyasn1 python-module-setuptools python-modules python-modules-compiler python-modules-ctypes python-modules-email python-modules-encodings python-modules-unittest python3 python3-base python3-module-cffi python3-module-cryptography python3-module-enum34 python3-module-ndg-httpsclient python3-module-ntlm python3-module-pycparser python3-module-setuptools
BuildRequires: python-module-chardet python-module-ndg-httpsclient python-module-ntlm python3-module-chardet python3-module-urllib3 rpm-build-python3

#BuildRequires:  python-devel python-modules-json
#BuildRequires:  python-module-chardet
#BuildRequires:  python-module-urllib3 >= 1.8.2

Requires:       ca-certificates
Requires:       python-module-chardet
Requires:       python-module-urllib3 >= 1.8.2
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
#BuildRequires:  python3-devel python3-base
#BuildRequires:  python3-module-chardet
#BuildRequires:  python3-module-urllib3 >= 1.8.2
Requires:       ca-certificates
Requires:       python3-module-chardet
Requires:       python3-module-urllib3 >= 1.8.2

%description -n python3-module-%pkgname
Most existing Python modules for sending HTTP requests are extremely verbose and
cumbersome. Python's built-in urllib2 module provides most of the HTTP
capabilities you should need, but the API is thoroughly broken. This library is
designed to make HTTP requests easy for developers.
%endif

%prep
%setup

#patch0 -p1
#patch1 -p1
#patch2 -p1

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
%python_sitelibdir/%pkgname
%python_sitelibdir/*.egg-info

%if_with python3
%files -n python3-module-%pkgname
%doc NOTICE LICENSE README.rst HISTORY.rst
%python3_sitelibdir/%pkgname
%python3_sitelibdir/*.egg-info
%endif

%changelog
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
