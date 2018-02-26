%define oname pycmd
Name: python-module-%oname
Version: 1.0.0
Release: alt1.hg20101129.1
Summary: Command line tools for helping with Python development
License: MIT
Group: Development/Python
Url: http://pylib.org/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>
BuildArch: noarch

# hg clone https://bitbucket.org/hpk42/pycmd
Source: %name-%version.tar.gz

BuildRequires(pre): rpm-build-python
BuildPreReq: python-devel python-module-setuptools

Conflicts: py

%description
Collection of command line tools for dealing with python files
(locating, counting LOCs, cleaning up pyc files ...)

%prep
%setup

%build
%python_build

%install
%python_install

%files
%doc AUTHORS CHANGELOG LICENSE *.txt
%_bindir/*
%python_sitelibdir/*

%changelog
* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 1.0.0-alt1.hg20101129.1
- Rebuild with Python-2.7

* Tue May 10 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0.0-alt1.hg20101129
- New snapshot

* Mon Nov 22 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0.0-alt1.hg20101108.1
- Added explicit conflict with py

* Sun Nov 21 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0.0-alt1.hg20101108
- Initial build for Sisyphus

