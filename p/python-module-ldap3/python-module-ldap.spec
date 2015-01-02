%define oname ldap3

%def_with python3

Summary: A strictly RFC 4511 conforming LDAP V3 pure Python 3 client - Python 2 compatible
Name: python-module-%oname
Version: 0.9.7.1
Release: alt1.git20150102
# https://github.com/cannatag/ldap3.git
Source0: %name-%version.tar
BuildArch: noarch
License: LGPLv3
Group: Development/Python
Url: https://pypi.python.org/pypi/ldap3/

BuildRequires(pre): rpm-build-python
BuildRequires: libsasl2-devel libldap-devel libssl-devel
BuildPreReq: python-devel python-module-setuptools-tests
BuildPreReq: python-module-pyasn1
BuildPreReq: python-module-sphinx-devel
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools-tests
BuildPreReq: python3-module-pyasn1
%endif

%py_provides %oname

%description
python-ldap provides an object-oriented API to access LDAP
directory servers from Python programs. Mainly it wraps the
OpenLDAP 2.x libs for that purpose.

Additionally the package contains modules for other LDAP-related
stuff (e.g. processing LDIF, LDAPURLs, LDAPv3 sub-schema, etc.).

%package -n python3-module-%oname
Summary: A strictly RFC 4511 conforming LDAP V3 pure Python 3 client - Python 2 compatible
Group: Development/Python3
%py3_provides %oname

%description -n python3-module-%oname
python-ldap provides an object-oriented API to access LDAP
directory servers from Python programs. Mainly it wraps the
OpenLDAP 2.x libs for that purpose.

Additionally the package contains modules for other LDAP-related
stuff (e.g. processing LDIF, LDAPURLs, LDAPv3 sub-schema, etc.).

%package docs
Summary: Documentation for %oname
Group: Development/Documentation
BuildArch: noarch

%description docs
python-ldap provides an object-oriented API to access LDAP
directory servers from Python programs. Mainly it wraps the
OpenLDAP 2.x libs for that purpose.

Additionally the package contains modules for other LDAP-related
stuff (e.g. processing LDIF, LDAPURLs, LDAPv3 sub-schema, etc.).

This package contains documentation for %oname.

%prep
%setup

%if_with python3
cp -fR . ../python3
%endif

%prepare_sphinx %oname/docs/manual
ln -s ../objects.inv %oname/docs/manual/source/

%build
%python_build_debug

%if_with python3
pushd ../python3
%python3_build_debug
popd
%endif

%install
%python_install

%if_with python3
pushd ../python3
%python3_install
popd
%endif

export PYTHONPATH=%buildroot%python_sitelibdir
%make -C %oname/docs/manual html

mv %oname/docs/manual/build/html manual

%check
python setup.py test
%if_with python3
pushd ../python3
python3 setup.py test
popd
%endif

%files
%doc *.txt *.md
%python_sitelibdir/*

%files docs
%doc %oname/docs/rfc manual

%if_with python3
%files -n python3-module-%oname
%doc *.txt *.md
%python3_sitelibdir/*
%endif

%changelog
* Fri Jan 02 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.9.7.1-alt1.git20150102
- New snapshot

* Mon Dec 29 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.9.7.1-alt1.git20141229
- Version 0.9.7.1

* Wed Nov 26 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.9.6.2-alt2
- Tuned requirements

* Thu Nov 20 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.9.6.2-alt1
- Version 0.9.6.2

* Wed Nov 12 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.9.6.1-alt1
- Version 0.9.6.1

* Thu Jul 31 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.9.5-alt1
- Initial build for Sisyphus

