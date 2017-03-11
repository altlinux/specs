%define modulename  acme

%def_with python3

Name: python-module-acme
Version: 0.12.0
Release: alt1

Summary: Python library for the ACME protocol

License: ASL 2.0
Group: Development/Python
Url: https://pypi.python.org/pypi/acme

Packager: Vitaly Lipatov <lav@altlinux.ru>

## Source-url: https://pypi.python.org/packages/source/a/%modulename/%modulename-%version.tar.gz
# Source-url: https://pypi.python.org/packages/3a/3e/63df00eeb3d06e2e08fd5c6308ff2d6d6e4730e4d5721ca978f079cdcd79/acme-0.12.0.tar.gz
Source: %modulename-%version.tar

BuildRequires: python-devel
#BuildRequires: python-sphinx
#BuildRequires: python-sphinxcontrib-programoutput
#BuildRequires: python-sphinx_rtd_theme
#BuildRequires: python-cryptography
BuildRequires: python-module-OpenSSL >= 0.13
#BuildRequires: python-requests
#BuildRequires: python-pyrfc3339
#BuildRequires: python-werkzeug

Requires: python-module-cryptography >= 0.8

%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools python3-module-setuptools-tests
#BuildRequires: python3-sphinx
#BuildRequires: python3-sphinxcontrib-programoutput
#BuildRequires: python3-cryptography
BuildRequires: python3-module-OpenSSL >= 0.13
#BuildRequires: python3-requests
#BuildRequires: python3-pyrfc3339
#BuildRequires: python3-werkzeug
%endif

# Required for testing
#BuildRequires: python-ndg_httpsclient
#BuildRequires: python-nose
#BuildRequires: python-tox
#BuildRequires: python-mock
#BuildRequires: pytz

#%if_with python3
#BuildRequires: python3-ndg_httpsclient
#BuildRequires: python3-nose
#BuildRequires: python3-tox
#BuildRequires: python3-mock
#BuildRequires: python3-pytz
#%endif

BuildArch: noarch

%description
Python libraries implementing the Automatic Certificate Management Environment
(ACME) protocol. It is used by the Certbot Project.

#%package -n python-module-acme
#Group: Development/Python
#Summary: %summary
#Requires: python-cryptography
#Requires: python-ndg_httpsclient
#Requires: python-pyasn1
#Requires: pyOpenSSL >= 0.13
#Requires: python-pyrfc3339
#Requires: pytz
#Requires: python-requests
#Requires: python-six
#Requires: python-werkzeug
#%if_with python3
# Recommends not supported by rpm on EL7
#Recommends: python-acme-doc
#%endif

#%description -n python-module-acme
#Python 2 library for use of the Automatic Certificate Management Environment
#protocol as defined by the IETF. It's used by the Let's Encrypt project.

%if_with python3
%package -n python3-module-acme
Group: Development/Python
Summary: %summary
Requires: python3-module-cryptography >= 0.8
#Requires: python3-ndg_httpsclient
#Requires: python3-pyasn1
#Requires: python3-pyOpenSSL
#Requires: python3-pyrfc3339
#Requires: python3-pytz
#Requires: python3-requests
#Requires: python3-six
#Requires: python3-werkzeug
#Recommends: python-acme-doc

%description -n python3-module-acme
Python 3 library for use of the Automatic Certificate Management Environment
protocol as defined by the IETF. It's used by the Certbot Project.
%endif

%package doc
Group: Development/Python
#Provides: bundled(jquery)
#Provides: bundled(underscore)
#Provides: bundled(inconsolata-fonts)
#Provides: bundled(lato-fonts)
#Provides: bundled(robotoslab-fonts)
#Requires: fontawesome-fonts fontawesome-fonts-web
Summary: Documentation for python-acme libraries

%description doc
Documentation for the ACME python libraries

%prep
%setup -n %modulename-%version

%build
%python_build
%if_with python3
%python3_build
%endif

%install
%if_with python3
# Do python3 first so bin ends up from py2
%python3_install
%endif

%python_install

%check
#__python setup.py test
#if_with python3
#__python3 setup.py test
#endif
# Make sure the script uses the expected python version
grep -q python %buildroot%_bindir/jws

%files
%doc LICENSE.txt
%python_sitelibdir/%modulename/
%python_sitelibdir/%modulename-%{version}*.egg-info
%_bindir/jws

%if_with python3
%files -n python3-module-acme
%doc LICENSE.txt
%python3_sitelibdir/%modulename/
%python3_sitelibdir/%modulename-%{version}*.egg-info
%endif

#%files doc
#%doc LICENSE.txt
#%doc README.rst
#%doc docs/_build/html

%changelog
* Fri Mar 10 2017 Terechkov Evgenii <evg@altlinux.org> 0.12.0-alt1
- 0.12.0

* Sun Dec 04 2016 Vitaly Lipatov <lav@altlinux.ru> 0.9.3-alt1
- new version 0.9.3 (with rpmrb script)

* Fri Oct 07 2016 Vitaly Lipatov <lav@altlinux.ru> 0.9.1-alt1
- new version (0.9.1) with rpmgs script

* Thu Aug 18 2016 Vitaly Lipatov <lav@altlinux.ru> 0.8.1-alt1
- new version 0.8.1

* Thu Apr 21 2016 Vitaly Lipatov <lav@altlinux.ru> 0.5.0-alt1
- new version 0.5.0 (with rpmrb script)

* Fri Mar 18 2016 Vitaly Lipatov <lav@altlinux.ru> 0.4.2-alt1
- new version 0.4.2 (with rpmrb script)

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.4.0-alt1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Tue Feb 16 2016 Vitaly Lipatov <lav@altlinux.ru> 0.4.0-alt1
- initial build for ALT Linux Sisyphus

* Thu Feb 11 2016 Nick Bebout <nb@fedoraproject.org> - 0.4.0-1
- Upgrade to 0.4.0
* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild
* Thu Jan 28 2016 Nick Bebout <nb@fedoraproject.org> - 0.3.0-1
- Upgrade to 0.3.0
* Thu Jan 21 2016 Nick Bebout <nb@fedoraproject.org> - 0.2.0-1
- Upgrade to 0.2.0
* Wed Dec 16 2015 Nick Bebout <nb@fedoraproject.org> - 0.1.1-1
- Upgrade to 0.1.1
* Fri Dec 04 2015 James Hogarth <james.hogarth@gmail.com> - 0.1.0-3
- Restore missing dependencies causing a FTBFS with py3 tests
- Add the man pages
* Thu Dec 03 2015 Robert Buchholz <rbu@goodpoint.de> - 0.1.0-4
- Specify more of the EPEL dependencies
* Thu Dec 03 2015 Robert Buchholz <rbu@goodpoint.de> - 0.1.0-3
- epel7: Only build python2 package
* Thu Dec 03 2015 James Hogarth <james.hogarth@gmail.com> - 0.1.0-2
- Fix up the removal of the dev release snapshot
* Thu Dec 03 2015 James Hogarth <james.hogarth@gmail.com> - 0.1.0-1
- Update to new upstream release for the open beta
* Mon Nov 30 2015 James Hogarth <james.hogarth@gmail.com> - 0.0.0-3-dev20151123
- Update spec with comments from review
* Sat Nov 28 2015 James Hogarth <james.hogarth@gmail.com> - 0.0.0-2.dev20151123
- Update spec with comments from review
- Add python3 library
* Fri Nov 27 2015 James Hogarth <james.hogarth@gmail.com> - 0.0.0-1.dev20151123
- initial packaging
