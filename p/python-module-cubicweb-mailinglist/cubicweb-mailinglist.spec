%define _unpackaged_files_terminate_build 1
%define oname cubicweb-mailinglist
Name: python-module-%oname
Version: 1.7.3
Release: alt1.1
Summary: Mailing-list component for the CubicWeb framework
License: LGPL
Group: Development/Python
Url: https://pypi.python.org/pypi/cubicweb-mailinglist/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source0: https://pypi.python.org/packages/6f/08/b49e521ec387f5c8d563aa88e141c0095317d262847704d7a6dbf180f019/%{oname}-%{version}.tar.gz
BuildArch: noarch

BuildPreReq: python-module-setuptools cubicweb
BuildPreReq: python-module-cubicweb-sioc python-module-markdown

Requires: cubicweb python-module-cubicweb-sioc

%description
This cube models mailing list (MailingList entity type) and allows to
archive threaded e-mail discussions. Together with the email cube, it
can be used to archive mailing lists.

This is not a mailing list manager!

%prep
%setup -q -n %{oname}-%{version}

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
* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 1.7.3-alt1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Wed Jan 11 2017 Igor Vlasenko <viy@altlinux.ru> 1.7.3-alt1
- automated PyPI update

* Thu Jan 15 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.7.2-alt1
- Initial build for Sisyphus

