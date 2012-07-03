%define oname beaker

%def_with python3

Name: python-module-%oname
Version: 1.6.3
Release: alt1
Summary: WSGI middleware layer to provide sessions

Group:  Development/Python
License: BSD
URL: http://beaker.groovie.org/
Source0: http://pypi.python.org/packages/source/B/Beaker/%{name}-%{version}.tar.gz
BuildPreReq: python-devel python-module-setuptools rpm-build-python
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel python3-module-distribute
%endif

BuildArch: noarch

%add_python_req_skip jarray javax

%description
Beaker is a caching library that includes Session and Cache objects built on
Myghty's Container API used in MyghtyUtils. WSGI middleware is also included to
manage Session objects and signed cookies.

%if_with python3
%package -n python3-module-%oname
Summary: WSGI middleware layer to provide sessions (Python 3)
Group: Development/Python3
%add_python3_req_skip jarray javax builtins

%description -n python3-module-%oname
Beaker is a caching library that includes Session and Cache objects built on
Myghty's Container API used in MyghtyUtils. WSGI middleware is also included to
manage Session objects and signed cookies.
%endif

%prep
%setup
%if_with python3
rm -rf ../python3
cp -a . ../python3
%endif


%build
%python_build
%if_with python3
pushd ../python3
sed -i 's|%_bindir/python|%_bindir/python3|' beaker/crypto/pbkdf2.py
sed -i '2d' beaker/crypto/pbkdf2.py
%python3_build
popd
%endif


%install
%python_install
%if_with python3
pushd ../python3
%python3_install
popd
%endif

%files
%doc LICENSE CHANGELOG
%python_sitelibdir/beaker/
%python_sitelibdir/Beaker*


%if_with python3
%files -n python3-module-%oname
%doc LICENSE CHANGELOG
%python3_sitelibdir/beaker/
%python3_sitelibdir/Beaker*
%endif

%changelog
* Thu May 10 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.6.3-alt1
- Version 1.6.3
- Added module for Python 3

* Mon Oct 24 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 1.3.1-alt1.1.1
- Rebuild with Python-2.7

* Thu Nov 19 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.3.1-alt1.1
- Rebuilt with python 2.6

* Fri Aug 04 2009 Paul Wolneykien <manowar@altlinux.ru> 1.3.1-alt1
- Initial build for ALTLinux

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Tue Jul 21 2009 Kyle VanderBeek <kylev@kylev.com> - 1.3.1-5
- Add patch based on upstream hg 403ef7c82d32 for config overwriting that
  breaks Pylons unit tests

* Sat Jun 27 2009 Luke Macken <lmacken@redhat.com> - 1.3.1-4
- Add a patch to remove the use of __future__.absolute_import in the google
  backend

* Sat Jun 20 2009 Toshio Kuratomi <toshio@fedoraproject.org> - 1.3.1-3
- Different hmac patch suitable for upstream inclusion.

* Tue Jun 02 2009 Luke Macken <lmacken@redhat.com> - 1.3.1-2
- Add a patch to remove Beaker's use of hashlib on Python2.4,
  due to incompatiblities with Python's hmac module (#503772)

* Sun May 31 2009 Luke Macken <lmacken@redhat.com> - 1.3.1-1
- Update to 1.3.1

* Tue Apr 07 2009 Felix Schwarz <felix.schwarz@oss.schwarz.eu> - 1.3-1
- Update to 1.3
 
* Sun Apr 05 2009 Felix Schwarz <felix.schwarz@oss.schwarz.eu> - 1.2.3-1
- Update to 1.2.3
 
* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Tue Jan 06 2009 Luke Macken <lmacken@redhat.com> - 1.1.3-1
- Update to 1.1.3

* Sat Dec 20 2008 Felix Schwarz <felix.schwarz@oss.schwarz.eu> - 1.1.2-1
- Update to 1.1.2
 
* Sat Nov 29 2008 Ignacio Vazquez-Abrams <ivazqueznet+rpm@gmail.com> - 1.0.3-2
- Rebuild for Python 2.6

* Tue Jun 24 2008 Felix Schwarz <felix.schwarz@oss.schwarz.eu> - 1.0.3-1
- Update to 1.0.3.

* Tue Jun 24 2008 Kyle VanderBeek <kylev@kylev.com> - 0.9.5-1
- Update to 0.9.5.
- Remove license patch which is now corrected upstream.

* Mon May 12 2008 Kyle VanderBeek <kylev@kylev.com> - 0.9.4-4
- Fix files to not use wildcard, fixing dir ownership

* Mon May 12 2008 Kyle VanderBeek <kylev@kylev.com> - 0.9.4-3
- Corrected license

* Mon May 12 2008 Kyle VanderBeek <kylev@kylev.com> - 0.9.4-2
- More restrictive file includes for safety

* Sun May 11 2008 Kyle VanderBeek <kylev@kylev.com> - 0.9.4-1
- Update to 0.9.4 (security fix)
- Fix rpmlint complaints, add CHANGELOG and LICENSE

* Wed Apr  9 2008 Kyle VanderBeek <kylev@kylev.com> - 0.9.3-1
- Initial version.
