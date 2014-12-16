%define oname Products.MaildropHost
Name: python-module-%oname
Version: 2.4
Release: alt1.dev.svn20091124
Summary: Asynchronous transaction-aware MailHost replacement for Zope 2
License: ZPLv2.1
Group: Development/Python
Url: https://pypi.python.org/pypi/Products.MaildropHost/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://www.dataflake.org/svn/Products.MaildropHost/trunk/
Source: %name-%version.tar

BuildPreReq: python-module-setuptools-tests python-module-Zope2-tests
BuildPreReq: python-module-Products.MailHost

%py_provides %oname
Requires: python-module-Zope2
%py_requires Products.MailHost zope.interface

%description
The MaildropHost product provides support for sending email from within
the Zope environment using MaildropHost objects. Unlike the built-in
MailHost object, the sending is done asynchronously from a separate
process. Furthermore, MaildropHost can optionally integrate with the
Zope transaction machinery to ensure that retried transactions do not
lead to multiple emails being created.

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR

%description tests
The MaildropHost product provides support for sending email from within
the Zope environment using MaildropHost objects. Unlike the built-in
MailHost object, the sending is done asynchronously from a separate
process. Furthermore, MaildropHost can optionally integrate with the
Zope transaction machinery to ensure that retried transactions do not
lead to multiple emails being created.

This package contains tests for %oname.

%prep
%setup

%build
%python_build_debug

%install
%python_install

%ifarch x86_64
mv %buildroot%_libexecdir %buildroot%_libdir
%endif

pushd Products/MaildropHost
rm -f maildrop/bin/maildrop-suse
cp -fR *.txt config dtml help seleniumtests www \
	%buildroot%python_sitelibdir/Products/MaildropHost/
cp -fR maildrop/bin maildrop/testing \
	%buildroot%python_sitelibdir/Products/MaildropHost/maildrop/
cp -fR tests/badconfig tests/dummyconfig \
	%buildroot%python_sitelibdir/Products/MaildropHost/tests/
popd

%check
python setup.py test

%files
%doc *.txt
%python_sitelibdir/Products/*
%python_sitelibdir/*.egg-info
%exclude %python_sitelibdir/Products/*/maildrop/testing
%exclude %python_sitelibdir/Products/*/seleniumtests
%exclude %python_sitelibdir/Products/*/tests

%files tests
%python_sitelibdir/Products/*/maildrop/testing
%python_sitelibdir/Products/*/seleniumtests
%python_sitelibdir/Products/*/tests

%changelog
* Tue Dec 16 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.4-alt1.dev.svn20091124
- Initial build for Sisyphus

