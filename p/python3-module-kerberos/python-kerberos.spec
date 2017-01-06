Name: python3-module-kerberos
Version: 1.1.13
Release: alt1
Summary: A high-level wrapper for Kerberos (GSSAPI) operations
Group: Development/Python3
License: ASL 2.0
URL: http://trac.calendarserver.org/projects/calendarserver/browser/PyKerberos
# get from http://packages.ubuntu.com/ru/utopic/python3-kerberos
Source0: https://pypi.python.org/packages/5c/05/55936bc02aead261bc8d2edd57ffbdfb3f814549c85d011ee14d4763ace5/pykerberos-%{version}.tar.gz

BuildRequires(pre): rpm-build-python3
BuildPreReq:  python3-devel
BuildPreReq:  libkrb5-devel
BuildPreReq:  python3-module-setuptools

%description
This Python package is a high-level wrapper for Kerberos (GSSAPI) operations.
The goal is to avoid having to build a module that wraps the entire
Kerberos.framework, and instead offer a limited set of functions that do what
is needed for client/serverKerberos authentication based on
<http://www.ietf.org/rfc/rfc4559.txt>.

Much of the C-code here is adapted from Apache's mod_auth_kerb-5.0rc7.

%prep
%setup -q -n pykerberos-%{version}

%build
%python3_build_debug

%install
%python3_install

%files
%doc README.txt LICENSE
%python3_sitelibdir/*

%changelog
* Fri Jan 06 2017 Igor Vlasenko <viy@altlinux.ru> 1.1.13-alt1
- automated PyPI update

* Thu Mar 17 2016 Ivan Zakharyaschev <imz@altlinux.org> 1.1.5-alt1.1
- (NMU) rebuild with python3-3.5 & rpm-build-python3-0.1.10
  (for ABI dependence and new python3(*) reqs)

* Mon Aug 25 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.1.5-alt1
- Initial build for Sisyphus

