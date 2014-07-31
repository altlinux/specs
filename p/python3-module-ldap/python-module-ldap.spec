%define oname python-ldap

Summary: LDAP client API for Python
Name: python3-module-ldap
Version: 2.3.13
Release: alt1
Source0: %oname-%version.tar
License: Python-style license
Group: Development/Python3
Url: http://python-ldap.sourceforge.net/

BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel libsasl2-devel
BuildRequires: libldap-devel libssl-devel
BuildPreReq: python-tools-2to3

%description
python-ldap provides an object-oriented API to access LDAP
directory servers from Python programs. Mainly it wraps the
OpenLDAP 2.x libs for that purpose.

Additionally the package contains modules for other LDAP-related
stuff (e.g. processing LDIF, LDAPURLs, LDAPv3 sub-schema, etc.).

%prep
%setup -n %oname-%version
find -type f -name '*.py' -exec 2to3 -w -n '{}' +

%build
%add_optflags -I%_includedir/sasl
export LC_ALL=en_US.UTF-8

%python3_build_debug

%install
export LC_ALL=en_US.UTF-8

%python3_install

%files
%doc LICENCE CHANGES README TODO
%python3_sitelibdir/*

%changelog
* Thu Jul 31 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.3.13-alt1
- Initial build for Sisyphus

