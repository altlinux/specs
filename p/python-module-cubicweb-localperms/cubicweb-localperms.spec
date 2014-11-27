%define oname cubicweb-localperms
Name: python-module-%oname
Version: 0.3.0
Release: alt1
Summary: Allow definition of local permissions
License: LGPL
Group: Development/Python
Url: https://pypi.python.org/pypi/cubicweb-localperms/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-module-setuptools-tests cubicweb

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
* Thu Nov 27 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.3.0-alt1
- Initial build for Sisyphus

