%define oname cubicweb-mailinglist
Name: python-module-%oname
Version: 1.7.2
Release: alt1
Summary: Mailing-list component for the CubicWeb framework
License: LGPL
Group: Development/Python
Url: https://pypi.python.org/pypi/cubicweb-mailinglist/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-module-setuptools-tests cubicweb
BuildPreReq: python-module-cubicweb-sioc python-module-markdown

Requires: cubicweb python-module-cubicweb-sioc

%description
This cube models mailing list (MailingList entity type) and allows to
archive threaded e-mail discussions. Together with the email cube, it
can be used to archive mailing lists.

This is not a mailing list manager!

%prep
%setup

%build
%python_build_debug

%install
%python_install

%check
python setup.py test

%files
%doc README
%python_sitelibdir/*
%_datadir/cubicweb/*

%changelog
* Thu Jan 15 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.7.2-alt1
- Initial build for Sisyphus

