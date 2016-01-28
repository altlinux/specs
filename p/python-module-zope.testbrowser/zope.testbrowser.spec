%define oname zope.testbrowser

%def_with python3
%def_disable check

Name: python-module-%oname
Version: 5.0.0
Release: alt2.dev0.git20150220.1
Summary: Programmable browser for functional black-box tests
License: ZPLv2.1
Group: Development/Python
Url: http://pypi.python.org/pypi/zope.testbrowser/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/zopefoundation/zope.testbrowser.git
Source: %name-%version.tar

#BuildPreReq: python-devel python-module-setuptools-tests
#BuildPreReq: python-module-zope.testing python-module-zope.interface
#BuildPreReq: python-module-zope.schema python-module-pytz
#BuildPreReq: python-module-zope.cachedescriptors
#BuildPreReq: python-module-pytz python-module-webtest
#BuildPreReq: python-module-WSGIProxy2 python-module-six
#BuildPreReq: python-module-nose
%if_with python3
BuildRequires(pre): rpm-build-python3
#BuildPreReq: python3-devel python3-module-setuptools-tests
#BuildPreReq: python-tools-2to3 python3-module-zope.interface
#BuildPreReq: python3-module-zope.testing
#BuildPreReq: python3-module-zope.schema
#BuildPreReq: python3-module-zope.cachedescriptors
#BuildPreReq: python3-module-pytz python3-module-webtest
#BuildPreReq: python3-module-WSGIProxy2 python-module-six
#BuildPreReq: python3-module-nose
%endif

%py_provides %oname
Requires: python-module-WSGIProxy2
%py_requires zope.interface zope.schema zope.cachedescriptors
# for tests:
%py_requires zope.testing

# Automatically added by buildreq on Thu Jan 28 2016 (-bi)
# optimized out: python-base python-devel python-module-cffi python-module-chardet python-module-cryptography python-module-cssselect python-module-dns python-module-enum34 python-module-genshi python-module-greenlet python-module-html5lib python-module-ndg-httpsclient python-module-ntlm python-module-psycopg2 python-module-pyasn1 python-module-restkit python-module-setuptools python-module-waitress python-module-zope.event python-module-zope.exceptions python-module-zope.interface python-modules python-modules-compiler python-modules-ctypes python-modules-email python-modules-encodings python-modules-logging python-modules-unittest python-modules-wsgiref python-tools-2to3 python3 python3-base python3-module-cffi python3-module-chardet python3-module-cryptography python3-module-cssselect python3-module-dns python3-module-enum34 python3-module-genshi python3-module-greenlet python3-module-html5lib python3-module-ndg-httpsclient python3-module-ntlm python3-module-psycopg2 python3-module-pycparser python3-module-restkit python3-module-setuptools python3-module-urllib3 python3-module-waitress python3-module-yieldfrom.http.client python3-module-yieldfrom.requests python3-module-yieldfrom.urllib3 python3-module-zope python3-module-zope.event python3-module-zope.exceptions python3-module-zope.interface
BuildRequires: python-module-WSGIProxy2 python-module-nose python-module-pytest python-module-pytz python-module-webtest python-module-zope.cachedescriptors python-module-zope.schema python-module-zope.testing python3-module-WSGIProxy2 python3-module-nose python3-module-pytest python3-module-pytz python3-module-webtest python3-module-zope.cachedescriptors python3-module-zope.schema python3-module-zope.testing rpm-build-python3 time

%description
zope.testbrowser provides an easy-to-use programmable web browser with
special focus on testing. It is used in Zope, but it's not Zope specific
at all. For instance, it can be used to test or otherwise interact with
any web site.

%package -n python3-module-%oname
Summary: Programmable browser for functional black-box tests
Group: Development/Python3

%description -n python3-module-%oname
zope.testbrowser provides an easy-to-use programmable web browser with
special focus on testing. It is used in Zope, but it's not Zope specific
at all. For instance, it can be used to test or otherwise interact with
any web site.

%prep
%setup

ln -s README.rst README.txt

%if_with python3
cp -fR . ../python3
%endif

%build
%python_build

%if_with python3
pushd ../python3
find -type f -name '*.py' -exec 2to3 -w -n '{}' + 
%python3_build
popd
%endif

%install
%python_install
%ifarch x86_64
install -d %buildroot%python_sitelibdir
mv %buildroot%python_sitelibdir_noarch/* \
	%buildroot%python_sitelibdir/
%endif

%if_with python3
pushd ../python3
%python3_install
popd
%ifarch x86_64
install -d %buildroot%python3_sitelibdir
mv %buildroot%python3_sitelibdir_noarch/* \
	%buildroot%python3_sitelibdir/
%endif
%endif

%check
python setup.py test
%if_with python3
pushd ../python3
python3 setup.py test
popd
%endif

%files
%doc *.rst
%python_sitelibdir/*
%exclude %python_sitelibdir/*.pth

%if_with python3
%files -n python3-module-%oname
%doc *.rst
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*.pth
%endif

%changelog
* Fri Jan 29 2016 Mikhail Efremov <sem@altlinux.org> 5.0.0-alt2.dev0.git20150220.1
- NMU: Use buildreq for BR.

* Sat Aug 29 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 5.0.0-alt2.dev0.git20150220
- New snapshot

* Wed Feb 18 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 5.0.0-alt2.dev0.git20140125
- Restored zope.testbrowser.connection

* Wed Oct 22 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 5.0.0-alt1.dev0.git20140125
- Version 5.0.0.dev0

* Thu Jul 17 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.0.4-alt2
- Added module for Python 3

* Mon Dec 02 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.0.4-alt1
- Version 4.0.4

* Tue Sep 24 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.0.3-alt1
- Version 4.0.3

* Wed Dec 28 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.0.2-alt1
- Version 4.0.2

* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 4.0.1-alt1.1
- Rebuild with Python-2.7

* Sat May 21 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.0.1-alt1
- Initial build for Sisyphus

