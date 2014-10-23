%define oname Products.PrintingMailHost
Name: python-module-%oname
Version: 0.8
Release: alt1.dev0.git20141014
Summary: A monkey patch to send MailHost messages to standard out
License: GPL
Group: Development/Python
Url: https://pypi.python.org/pypi/Products.PrintingMailHost/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/collective/Products.PrintingMailHost.git
Source: %name-%version.tar

BuildPreReq: python-module-setuptools-tests python-module-Zope2-tests

%py_provides %oname
Requires: python-module-Zope2

%description
This product, when installed, will check if Zope is running in debug
mode, and if so, monkey patch (that is, grab the internals of, squeeze
tight, then rip hard, just like monkeys do) Zope's MailHost class,
meaning that any and all uses of a MailHost will be "fixed" so that
instead of sending mail, it prints messages to the standard output.

This is useful if you don't have a local mailhost for testing, or if you
prefer not to spam the crap out of yourself whilst finding out if your
bulk mail script is working.

%prep
%setup

%build
%python_build_debug

%install
%python_install

%ifarch x86_64
mv %buildroot%_libexecdir %buildroot%_libdir
%endif

%check
python setup.py test

%files
%doc *.rst docs/*
%python_sitelibdir/Products/*
%python_sitelibdir/*.egg-info

%changelog
* Thu Oct 23 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.8-alt1.dev0.git20141014
- Initial build for Sisyphus

