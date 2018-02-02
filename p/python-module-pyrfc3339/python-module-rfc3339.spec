%global srcname pyRFC3339

%def_with python3

Name: python-module-pyrfc3339
Version: 1.0
Release: alt1.1.1
Summary: Generate and parse RFC 3339 timestamps

License: MIT
Group: Development/Python
Url: https://pypi.python.org/pypi/pyRFC3339
Packager: Vitaly Lipatov <lav@altlinux.ru>

# Source-url: https://pypi.python.org/packages/source/p/pyRFC3339/pyRFC3339-%version.tar.gz
Source: %srcname-%version.tar

BuildArch: noarch
BuildRequires: python-devel python-module-distribute
# --- unit tests ---
#BuildRequires: python-nose
#BuildRequires: pytz


%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools python3-module-setuptools
# --- unit tests ---
#BuildRequires: python3-nose
#BuildRequires: python3-pytz
%endif

%description
This package contains a python library to parse and generate
RFC 3339-compliant timestamps using Python datetime.datetime objects.

%if_with python3
%package -n python3-module-rfc3339
Group: Development/Python
Summary: Generate and parse RFC 3339 timestamps

%description -n python3-module-rfc3339
This package contains a Python 3 library to parse and generate
RFC 3339-compliant timestamps using Python datetime.datetime objects.
%endif

%prep
%setup -n %srcname-%version

%build
%python_build
%if_with python3
%python3_build
%endif

%install
%python_install
%if_with python3
%python3_install
%endif

%check
#__python setup.py test
#if_with python3
#__python3 setup.py test
#endif

%files
%doc README.rst
%doc LICENSE.txt
%python_sitelibdir/pyrfc3339/
%python_sitelibdir/%srcname-%version-*.egg-info

%if_with python3
%files -n python3-module-rfc3339
%doc README.rst
%doc LICENSE.txt
%python3_sitelibdir/pyrfc3339/
%python3_sitelibdir/%srcname-%version-*.egg-info
%endif

%changelog
* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 1.0-alt1.1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 1.0-alt1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Tue Feb 16 2016 Vitaly Lipatov <lav@altlinux.ru> 1.0-alt1
- initial build for ALT Linux Sisyphus

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Dec 03 2015 Robert Buchholz <rbu@goodpoint.de> - 1.0-2
- epel7: Only build python2 package

* Tue Nov 10 2015 James Hogarth <james.hogarth@gmail.com>    - 1.0-1
- Add installed tests back as per review
- Update to new 1.0 PyPi release
- Add external license file
* Sun Nov 08 2015 James Hogarth <james.hogarth@gmail.com>    - 0.2-2
- Update to follow the python guidelines
* Wed Oct 28 2015 Felix Schwarz <fschwarz@fedoraproject.org> - 0.2-1
- initial packaging
