%define _unpackaged_files_terminate_build 1
%define oname cubicweb-localperms
Name: python-module-%oname
Version: 0.3.2
Release: alt1.1
Summary: Allow definition of local permissions
License: LGPL
Group: Development/Python
Url: https://pypi.python.org/pypi/cubicweb-localperms/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source0: https://pypi.python.org/packages/e7/21/3223f3755b695ea68ea3247219f450561c9b0544488487e06da539a939ce/%{oname}-%{version}.tar.gz
BuildArch: noarch

BuildPreReq: python-module-setuptools cubicweb

Requires: cubicweb

%description
This cube allows definition of local permissions using a generic
CWPermission entity type which you should use in your schema definition.

A CWPermission entity type:

* has a name and a label
* means groups linked to it through the 'require_group' relation have
  the <name> permission on entities linked through the
  'require_permission' object relation.

%prep
%setup -q -n %{oname}-%{version}

%build
%python_build_debug

%install
%python_install

%check
python setup.py test

%files
%doc README PKG-INFO
%python_sitelibdir/*
%_datadir/cubicweb/*

%changelog
* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 0.3.2-alt1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Tue Jan 17 2017 Igor Vlasenko <viy@altlinux.ru> 0.3.2-alt1
- automated PyPI update

* Thu Nov 27 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.3.0-alt1
- Initial build for Sisyphus

