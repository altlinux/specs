%define modulename lxml

%def_with python3

Name: python-module-lxml
Version: 3.4.1
Release: alt1.git20141120

Summary: Powerful and Pythonic XML processing library combining libxml2/libxslt with the ElementTree API.

# http://codespeak.net/lxml/%modulename-%version.tar
# git://github.com/lxml/lxml.git
Source: %name-%version.tar

License: BSD/GPLv2/ZPL/PSF
Group: Development/Python
URL: http://codespeak.net/lxml

BuildPreReq: libxslt-devel python-module-distribute zlib-devel
# see doc/build.txt
BuildPreReq: python-module-Cython >= 0.18
BuildPreReq: python-modules-wsgiref python-module-cssselect

%setup_python_module lxml

%if_with python3
BuildRequires(pre): rpm-build-python3
# see doc/build.txt
BuildPreReq: python3-module-Cython >= 0.18
BuildPreReq: python3-devel python3-module-distribute
BuildPreReq: python3-module-cssselect

%add_python3_req_skip etree
%endif

%description
lxml is a Pythonic, mature binding for the libxml2 and libxslt libraries.  It
provides safe and convenient access to these libraries using the ElementTree
API.

It extends the ElementTree API significantly to offer support for XPath,
RelaxNG, XML Schema, XSLT, C14N and much more.

%if_with python3
%package -n python3-module-%modulename
Summary: XML processing library combining libxml2/libxslt with the ElementTree API (Python 3)
Group: Development/Python3

%description -n python3-module-%modulename
lxml is a Pythonic, mature binding for the libxml2 and libxslt libraries.  It
provides safe and convenient access to these libraries using the ElementTree
API.

It extends the ElementTree API significantly to offer support for XPath,
RelaxNG, XML Schema, XSLT, C14N and much more.

This is module for use with Python 3.
%endif

%package doc
Summary: Documentation for lxml
Group: Development/Documentation
BuildArch: noarch

%description doc
lxml is a Pythonic, mature binding for the libxml2 and libxslt libraries.  It
provides safe and convenient access to these libraries using the ElementTree
API.

It extends the ElementTree API significantly to offer support for XPath,
RelaxNG, XML Schema, XSLT, C14N and much more.

This package contains documentation for lxml.

%prep
%setup
%if_with python3
rm -rf ../python3
cp -a . ../python3
%endif

%build
# see Makefile
%python_build_debug --with-cython
%if_with python3
pushd ../python3
sed -i 's|/usr/bin/env python.*|/usr/bin/env python3|' \
	update-error-constants.py test.py
sed -i 's|/usr/bin/python|/usr/bin/python3|' \
	doc/rest2latex.py doc/rest2html.py
%python3_build --with-cython
popd
%endif

%install
%python_install
%if_with python3
pushd ../python3
%python3_install
popd
%endif

%check
export LC_ALL=en_US.UTF-8

# see Makefile
CFLAGS="${CFLAGS:-%optflags}" ; export CFLAGS ;
CXXFLAGS="${CXXFLAGS:-%optflags}" ; export CXXFLAGS ;
FFLAGS="${FFLAGS:-%optflags}" ; export FFLAGS ;
cp -l build/lib.linux-*/lxml/*.so src/lxml/
%__python test.py -p -v
PYTHONPATH=src:$PYTHONPATH %__python selftest.py
PYTHONPATH=src:$PYTHONPATH %__python selftest2.py
%if_with python3
pushd ../python3
cp -l build/lib.linux-*/lxml/*.so src/lxml/
%__python3 test.py -p -v
PYTHONPATH=src:$PYTHONPATH %__python3 selftest.py
PYTHONPATH=src:$PYTHONPATH %__python3 selftest2.py
popd
%endif

%files
%python_sitelibdir/*

%if_with python3
%files -n python3-module-%modulename
%python3_sitelibdir/*
%endif

%files doc
%doc doc samples

%changelog
* Fri Nov 21 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.4.1-alt1.git20141120
- Version 3.4.1

* Fri Aug 22 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.3.5-alt1.git20140418
- Version 3.3.5

* Sat Mar 30 2013 Aleksey Avdeev <solo@altlinux.ru> 3.1.1-alt1.git20130330
- Version 3.1.1 (d7ea8fd4bb60e8e0799b1cb4a3ef0f79da8f3530)

* Thu Mar 28 2013 Aleksey Avdeev <solo@altlinux.ru> 3.1.0-alt1
- Version 3.1.0

* Sun Mar 17 2013 Aleksey Avdeev <solo@altlinux.ru> 2.3.6-alt1
- Version 2.3.6

* Tue Apr 10 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.3.4-alt2
- Added module for Python 3

* Mon Apr 09 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.3.4-alt1
- Version 2.3.4

* Fri Oct 21 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 2.2.8-alt2.1
- Rebuild with Python-2.7

* Sun Mar 27 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.2.8-alt2
- Added zlib-devel into BuildPreReq
- Rebuilt for debuginfo

* Tue Nov 30 2010 Ivan Fedorov <ns@altlinux.org> 2.2.8-alt1
- Version 2.2.8

* Thu Jul 29 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.2.7-alt1
- Version 2.2.7
- Added docs

* Mon Feb 08 2010 Vitaly Lipatov <lav@altlinux.ru> 2.2.4-alt1
- cleanup spec
- new version 2.2.4 (with rpmrb script)

* Sun Dec 13 2009 Repocop Q. A. Robot <repocop@altlinux.org> 2.1.1-alt1.1.qa1
- NMU (by repocop): the following fixes applied:
  * vendor-tag for python-module-lxml
  * postclean-05-filetriggers for spec file

* Wed Nov 11 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.1.1-alt1.1
- Rebuilt with python 2.6

* Wed Jul 30 2008 Ivan Fedorov <ns@altlinux.org> 2.1.1-alt1
- 2.1.1

* Wed May 28 2008 Ivan Fedorov <ns@altlinux.org> 2.0.5-alt1
- 2.0.5

* Wed Apr 09 2008 Ivan Fedorov <ns@altlinux.org> 2.0.3-alt1
- 2.0.3

* Mon Jan 28 2008 Grigory Batalov <bga@altlinux.ru> 1.3.6-alt1.1
- Rebuilt with python-2.5.

* Wed Jan 02 2008 Vitaly Lipatov <lav@altlinux.ru> 1.3.6-alt1
- initial build for ALT Linux Sisyphus
