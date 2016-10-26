%define oname pyldap

%def_with python3
%def_without docs

Summary: Python modules for implementing LDAP clients
Name: python-module-%oname
Version: 2.4.25.1
Release: alt2
Source: %name-%version.tar
Patch: python-pyldap-dirs.patch
License: Python-style license
Group: Development/Python
Url:  https://github.com/pyldap/pyldap/

BuildPreReq: python-devel
BuildPreReq: rpm-build-python
BuildRequires: libldap-devel libssl-devel libsasl2-devel
BuildPreReq: python-module-sphinx
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel
%endif

Provides: python-module-ldap = %version-%release
Conflicts: python-module-ldap < %version-%release

%description
pyldap is a fork of python-ldap, and provides an object-oriented API
to access LDAP directory servers from Python programs.
Mainly it wraps the OpenLDAP 2.x libs for that purpose.

Additionally the package contains modules for other LDAP-related
stuff (e.g. processing LDIF, LDAPURLs, LDAPv3 sub-schema, etc.).

%package -n python3-module-%oname
Summary: LDAP client API for Python
Group: Development/Python3

Provides: python3-module-ldap = %version-%release
Conflicts: python3-module-ldap < %version-%release

%description -n python3-module-%oname
pyldap is a fork of python-ldap, and provides an object-oriented API
to access LDAP directory servers from Python programs.
Mainly it wraps the OpenLDAP 2.x libs for that purpose.

Additionally the package contains modules for other LDAP-related
stuff (e.g. processing LDIF, LDAPURLs, LDAPv3 sub-schema, etc.).

%package demos
Summary: Demos for python-%oname
Group: Development/Documentation
BuildArch: noarch
Requires: %name = %version-%release
Conflicts: python-module-ldap-demos

%description demos
pyldap is a fork of python-ldap, and provides an object-oriented API
to access LDAP directory servers from Python programs.
Mainly it wraps the OpenLDAP 2.x libs for that purpose.

python-ldap provides an object-oriented API to access LDAP
directory servers from Python programs. Mainly it wraps the
OpenLDAP 2.x libs for that purpose.

Additionally the package contains modules for other LDAP-related
stuff (e.g. processing LDIF, LDAPURLs, LDAPv3 sub-schema, etc.).

This package contains demos for python-ldap.

%package tests
Summary: Tests for python-ldap
Group: Development/Python
BuildArch: noarch
Requires: %name = %version-%release
Conflicts: python-module-ldap-tests

%description tests
pyldap is a fork of python-ldap, and provides an object-oriented API
to access LDAP directory servers from Python programs.
Mainly it wraps the OpenLDAP 2.x libs for that purpose.

Additionally the package contains modules for other LDAP-related
stuff (e.g. processing LDIF, LDAPURLs, LDAPv3 sub-schema, etc.).

This package contains tests for python-ldap.

%package doc
Summary: Documentation for python-ldap
Group: Development/Documentation
BuildArch: noarch
Conflicts: python-module-ldap-doc

%description doc
pyldap is a fork of python-ldap, and provides an object-oriented API
to access LDAP directory servers from Python programs.
Mainly it wraps the OpenLDAP 2.x libs for that purpose.

Additionally the package contains modules for other LDAP-related
stuff (e.g. processing LDIF, LDAPURLs, LDAPv3 sub-schema, etc.).

This package contains documentation for python-ldap.

%package pickles
Summary: Pickles for python-ldap
Group: Development/Python
Conflicts: python-module-ldap-pickles

%description pickles
pyldap is a fork of python-ldap, and provides an object-oriented API
to access LDAP directory servers from Python programs.
Mainly it wraps the OpenLDAP 2.x libs for that purpose.

Additionally the package contains modules for other LDAP-related
stuff (e.g. processing LDIF, LDAPURLs, LDAPv3 sub-schema, etc.).

This package contains pickles for python-ldap.

%prep
%setup -q
%patch -p1

rm -rf Lib/*.egg-info

%if_with python3
cp -fR . ../python3
%endif

%build
%add_optflags -I%_includedir/sasl
export LC_ALL=en_US.UTF-8

%python_build_debug

%if_with python3
pushd ../python3
%python3_build_debug
popd
%endif

%if_with docs
%make -C Doc html
%endif

%install
export LC_ALL=en_US.UTF-8

%python_install

%if_with python3
pushd ../python3
%python3_install
popd
%endif

%if_with docs
cp -fR Doc/.build/pickle %buildroot%python_sitelibdir/ldap/
%endif

%files
%doc CHANGES README TODO
%python_sitelibdir/*
%if_with docs
%exclude %python_sitelibdir/ldap/pickle
%endif

%files demos
%doc Demo

%files tests
%doc Tests

%if_with docs
%files doc
%doc Doc/.build/html Doc/.build/latex/*.pdf

%files pickles
%python_sitelibdir/ldap/pickle
%endif

%if_with python3
%files -n python3-module-%oname
%doc CHANGES README TODO
%python3_sitelibdir/*
%endif

%changelog
* Wed Oct 26 2016 Alexey Shabalin <shaba@altlinux.ru> 2.4.25.1-alt2
- add conflicts with python-module-ldap

* Mon Oct 17 2016 Alexey Shabalin <shaba@altlinux.ru> 2.4.25.1-alt1
- Initial build
