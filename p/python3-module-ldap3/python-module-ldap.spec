%define _unpackaged_files_terminate_build 1
%define oname ldap3

Summary: A strictly RFC 4511 conforming LDAP V3 pure Python 3 client - Python 2 compatible
Name: python3-module-%oname
Version: 2.7
Release: alt1
License: LGPLv3
Group: Development/Python3
BuildArch: noarch
Url: https://pypi.org/project/ldap3/

# https://github.com/cannatag/ldap3.git
Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3

%py3_provides %oname

%description
python-ldap provides an object-oriented API to access LDAP
directory servers from Python programs. Mainly it wraps the
OpenLDAP 2.x libs for that purpose.

Additionally the package contains modules for other LDAP-related
stuff (e.g. processing LDIF, LDAPURLs, LDAPv3 sub-schema, etc.).

%prep
%setup

# it is stated in comment that this file is used for python2 only, remove it for python3
rm -f ldap3/utils/ordDict.py

%build
%python3_build_debug

%install
%python3_install

%files
%doc *.txt *.rst
%python3_sitelibdir/*

%changelog
* Wed Jul 08 2020 Stanislav Levin <slev@altlinux.org> 2.7-alt1
- 2.5.2 -> 2.7.

* Fri Feb 01 2019 Ivan A. Melnikov <iv@altlinux.org> 2.5.2-alt1
- Version 2.5.2.
- Get rid of ubt.

* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 2.3-alt1.S1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Thu Nov 02 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 2.3-alt1.S1
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

