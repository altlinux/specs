%define oname python-ldap3

Summary: A strictly RFC 4511 conforming LDAP V3 pure Python 3 client - Python 2 compatible
Name: python3-module-ldap3
Version: 0.9.6.2
Release: alt1
Source0: %name-%version.tar
BuildArch: noarch
License: LGPLv3
Group: Development/Python3
Url: https://pypi.python.org/pypi/python3-ldap

BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools
BuildRequires: libsasl2-devel libldap-devel libssl-devel

%description
python-ldap provides an object-oriented API to access LDAP
directory servers from Python programs. Mainly it wraps the
OpenLDAP 2.x libs for that purpose.

Additionally the package contains modules for other LDAP-related
stuff (e.g. processing LDIF, LDAPURLs, LDAPv3 sub-schema, etc.).

%prep
%setup

%build
%python3_build_debug

%install
%python3_install

%files
%doc *.txt
%python3_sitelibdir/*

%changelog
* Thu Nov 20 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.9.6.2-alt1
- Version 0.9.6.2

* Wed Nov 12 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.9.6.1-alt1
- Version 0.9.6.1

* Thu Jul 31 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.9.5-alt1
- Initial build for Sisyphus

