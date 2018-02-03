%define oname ldap3

%def_with python3
%def_disable check

Summary: A strictly RFC 4511 conforming LDAP V3 pure Python 3 client - Python 2 compatible
Name: python-module-%oname
Version: 2.3
Release: alt1%ubt.1
License: LGPLv3
Group: Development/Python
BuildArch: noarch
Url: https://pypi.python.org/pypi/ldap3/

# https://github.com/cannatag/ldap3.git
Source: %name-%version.tar

BuildRequires(pre): rpm-build-ubt
BuildRequires(pre): rpm-macros-sphinx
BuildRequires: python-devel python-module-setuptools
BuildRequires: python-module-pyasn1
BuildRequires: python-module-alabaster python-module-docutils python-module-html5lib python-module-objects.inv python-module-sphinx_rtd_theme python2.7(gssapi)
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel python3-module-setuptools
BuildRequires: python3-module-pyasn1
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
# it is stated in comment that this file is used for python2 only, remove it for python3
rm -f ../python3/ldap3/utils/ordDict.py
%endif

%prepare_sphinx docs/manual
ln -s ../objects.inv docs/manual/source/

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
%make -C docs/manual html

mv docs/manual/build/html manual

%check
python setup.py test
%if_with python3
pushd ../python3
python3 setup.py test
popd
%endif

%files
%doc *.txt *.rst
%python_sitelibdir/*

%files docs
%doc docs/rfc manual

%if_with python3
%files -n python3-module-%oname
%doc *.txt *.rst
%python3_sitelibdir/*
%endif

%changelog
* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 2.3-alt1%ubt.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Thu Nov 02 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 2.3-alt1%ubt
- Updated to upstream version 2.3.
- Disabled tests since it requires running ldap server.

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.9.7.4-alt1.git20150203.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 0.9.7.4-alt1.git20150203.1
- NMU: Use buildreq for BR.

* Tue Feb 03 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.9.7.4-alt1.git20150203
- Version 0.9.7.4

* Fri Jan 16 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.9.7.2-alt1.git20150116
- Version 0.9.7.2

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

