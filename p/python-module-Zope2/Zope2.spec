%define oname Zope2

Name: python-module-%oname
Version: 4.0
Release: alt3.a1.dev.git20150211
Summary: Zope2 application server / web framework
License: ZPLv2.1
Group: Development/Python
Url: http://pypi.python.org/pypi/Zope2/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/zopefoundation/Zope.git
Source: %name-%version.tar
# http://cvs.zope.org/*checkout*/Python-2.2.3/Lib/regsub.py?rev=1.1.1.1&cvsroot=Zope.org&sortby=author&content-type=text/plain
Source1: regsub.py

BuildPreReq: python-devel python-module-setuptools-tests
BuildPreReq: python-module-sphinx-devel
BuildPreReq: python-module-AccessControl
BuildPreReq: python-module-Acquisition
BuildPreReq: python-module-DateTime
BuildPreReq: python-module-DocumentTemplate
BuildPreReq: python-module-ExtensionClass
BuildPreReq: python-module-Missing
BuildPreReq: python-module-MultiMapping
BuildPreReq: python-module-Persistence
BuildPreReq: python-module-Products.OFSP
BuildPreReq: python-module-Products.ZCatalog
BuildPreReq: python-module-Products.ZCTextIndex
BuildPreReq: python-module-Record
BuildPreReq: python-module-RestrictedPython
BuildPreReq: python-module-zconfig
BuildPreReq: python-module-ZODB3
BuildPreReq: python-module-ZopeUndo
BuildPreReq: python-module-docutils
BuildPreReq: python-module-initgroups
BuildPreReq: python-module-pytz
BuildPreReq: python-module-tempstorage
BuildPreReq: python-module-transaction
BuildPreReq: python-module-zdaemon
BuildPreReq: python-module-zExceptions
BuildPreReq: python-module-zLOG
BuildPreReq: python-module-zope.browser
BuildPreReq: python-module-zope.browsermenu
BuildPreReq: python-module-zope.browserpage
BuildPreReq: python-module-zope.browserresource
BuildPreReq: python-module-zope.configuration
BuildPreReq: python-module-zope.container
BuildPreReq: python-module-zope.contentprovider
BuildPreReq: python-module-zope.contenttype
BuildPreReq: python-module-zope.deferredimport
BuildPreReq: python-module-zope.event
BuildPreReq: python-module-zope.exceptions
BuildPreReq: python-module-zope.i18n
BuildPreReq: python-module-zope.i18nmessageid
BuildPreReq: python-module-zope.lifecycleevent
BuildPreReq: python-module-zope.location
BuildPreReq: python-module-zope.pagetemplate
BuildPreReq: python-module-zope.processlifetime
BuildPreReq: python-module-zope.proxy
BuildPreReq: python-module-zope.ptresource
BuildPreReq: python-module-zope.publisher
BuildPreReq: python-module-zope.schema
BuildPreReq: python-module-zope.security
BuildPreReq: python-module-zope.sendmail
BuildPreReq: python-module-zope.sequencesort
BuildPreReq: python-module-zope.site
BuildPreReq: python-module-zope.size
BuildPreReq: python-module-zope.structuredtext
BuildPreReq: python-module-zope.tal
BuildPreReq: python-module-zope.tales
BuildPreReq: python-module-zope.testbrowser
BuildPreReq: python-module-zope.testing
BuildPreReq: python-module-zope.traversing
BuildPreReq: python-module-zope.viewlet
BuildPreReq: python-module-zope.filerepresentation
BuildPreReq: python-module-Products.SiteErrorLog-tests
BuildPreReq: python-module-zope.component-tests
BuildPreReq: python-module-zope.security-tests
BuildPreReq: python-module-zope.traversing-tests
BuildPreReq: python-modules-tkinter

%add_python_req_skip ntsecuritycon pywintypes win32api win32con win32event
%py_requires zope.testbrowser zope.testing zope.traversing zope.viewlet
%py_requires zope.size zope.structuredtext zope.tal zope.tales
%py_requires zope.security zope.sendmail zope.sequencesort zope.site
%py_requires zope.proxy zope.ptresource zope.publisher zope.schema
%py_requires zope.location zope.pagetemplate zope.processlifetime
%py_requires zope.i18nmessageid zope.interface zope.lifecycleevent
%py_requires zope.deferredimport zope.event zope.exceptions zope.i18n
%py_requires zope.container zope.contentprovider zope.contenttype
%py_requires ZODB3 Products.OFSP Products.ZCatalog Products.ZCTextIndex
%py_requires docutils pytz zope.browser zope.browsermenu zope.browserpage
%py_requires zope.browserresource zope.component zope.configuration
%py_requires Products.PythonScripts zLOG Products.MIMETools
%py_requires Products.SiteErrorLog

%description
Zope2 is an open-source web application server.

%package tests
Summary: Tests for Zope2
Group: Development/Python
Requires: %name = %version-%release
Requires: python-module-zope.sendmail-tests python-module-zope.viewlet-tests
Requires: python-module-Products.PythonScripts-tests python-module-zLOG-tests
Requires: python-module-Products.MIMETools-tests python-module-zope.size-tests
Requires: python-module-zope.traversing-tests python-module-zope.tales-tests
Requires: python-module-zope.testbrowser python-module-zope.tal-tests
Requires: python-module-zope.site-tests python-module-zope.ptresource-tests
Requires: python-module-zope.processlifetime-tests python-module-ZODB3
Requires: python-module-zope.pagetemplate-tests
Requires: python-module-zope.lifecycleevent-tests
Requires: python-module-zope.contentprovider-tests
Requires: python-module-zope.container-tests python-module-zope.annotation-tests
Requires: python-module-zope.browserresource-tests
Requires: python-module-zope.browserpage-tests
Requires: python-module-zope.browsermenu-tests python-module-mechanize
Requires: python-module-initgroups python-module-Missing-tests
Requires: python-module-zope.filerepresentation-tests
Requires: python-module-zope.dottedname-tests
Requires: python-module-Products.MailHost-tests
Requires: python-module-Products.StandardCacheManagers-tests
Requires: python-module-Products.ZCTextIndex-tests
Requires: python-module-Products.ZCatalog-tests
Requires: python-module-Products.ExternalMethod-tests
Requires: python-module-Products.BTreeFolder2-tests
Requires: python-module-Products.OFSP
Requires: python-module-zope.component-tests
Requires: python-module-zope.security-tests
Requires: python-module-zope.traversing-tests
Requires: python-module-Products.SiteErrorLog-tests
Requires: python-module-Products.PloneTestCase
Requires: python-modules-tkinter

%add_python_req_skip http_date

%description tests
Zope2 is an open-source web application server.

This package contains tests for Zope2.

%package pickles
Summary: Pickles for Zope2
Group: Development/Python

%description pickles
Zope2 is an open-source web application server.

This package contains pickles for Zope2.

%package docs
Summary: Documentation for Zope2
Group: Development/Documentation
BuildArch: noarch

%description docs
Zope2 is an open-source web application server.

This package contains documentation for Zope2.

%prep
%setup

%prepare_sphinx .
ln -s ../objects.inv docs/

%build
%python_build

pushd docs
export PYTHONPATH=$PWD/../build/lib
%make pickle
%make html
popd

%install
%python_install

%ifarch x86_64
mv %buildroot%_libexecdir %buildroot%_libdir
%endif

for i in Shared Products Testing; do
	for j in $(find %buildroot%python_sitelibdir/$i -type d); do
		touch $j/__init__.py
	done
done

install -p -m644 %SOURCE1 %buildroot%python_sitelibdir

cp -fR docs/.build/pickle %buildroot%python_sitelibdir/%oname/

# There is a file in the package named .DS_Store or .DS_Store.gz, 
# the file name used by Mac OS X to store folder attributes.  
# Such files are generally useless in packages and were usually accidentally 
# included by copying complete directories from the source tarball.
find $RPM_BUILD_ROOT \( -name '*.DS_Store' -o -name '*.DS_Store.gz' \) -print -delete

%check
python setup.py test

%files
%doc *.txt
%_bindir/*
%exclude %_bindir/zpasswd
%python_sitelibdir/*
%exclude %python_sitelibdir/*.pth
%exclude %python_sitelibdir/*/tests
%exclude %python_sitelibdir/*/*/*test*
%exclude %python_sitelibdir/*/*/*/test*
%exclude %python_sitelibdir/*/*/*/*/tests
%exclude %python_sitelibdir/*/Test*
%exclude %python_sitelibdir/Test*
%exclude %python_sitelibdir/*/*/examples
%exclude %python_sitelibdir/%oname/pickle

%files tests
%python_sitelibdir/*/tests
%python_sitelibdir/*/*/*test*
%python_sitelibdir/*/*/*/test*
%python_sitelibdir/*/*/*/*/tests
%python_sitelibdir/*/Test*
%python_sitelibdir/Test*
%python_sitelibdir/*/*/examples

%files pickles
%python_sitelibdir/%oname/pickle

%files docs
%doc docs/.build/html/*

%changelog
* Sat Feb 14 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.0-alt3.a1.dev.git20150211
- New snapshot

* Fri Nov 07 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.0-alt3.a1.dev.git20141102
- Added necessary requirements
- Enabled testing

* Fri Nov 07 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.0-alt2.a1.dev.git20141102
- New snapshot (bootstrap)

* Wed Oct 15 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.0-alt2.a1.dev.git20140402
- More requirements
- Enabled testing

* Sat Oct 11 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.0-alt1.a1.dev.git20140402
- Version 4.0a1.dev

* Sat Oct 11 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.13.22-alt5
- Added more testing requirements

* Sat Oct 11 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.13.22-alt4
- Added testing requirements

* Sat Oct 11 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.13.22-alt3
- Excluded .pth file

* Sat Oct 11 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.13.22-alt2
- Set as archdep

* Wed Jul 16 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.13.22-alt1
- Version 2.13.22

* Mon Dec 02 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.13.21-alt1
- Version 2.13.21

* Fri Apr 12 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.13.19-alt2
- Applied repocop patch
- Moved examples into tests subpackage

* Thu Apr 11 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.13.19-alt1
- Version 2.13.19

* Mon Oct 24 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 2.13.7-alt2.1
- Rebuild with Python-2.7

* Fri Jun 10 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.13.7-alt2
- Moved all tests into tests package

* Sat Jun 04 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.13.7-alt1
- Initial build for Sisyphus

