# REMOVE ME (I was set for NMU) and uncomment real Release tags:
Release: alt1.dev0.git20141107.1.1
%define mname cs.zestreleaser
%define oname %mname.upload
Name: python-module-%oname
Version: 1.1
#Release: alt1.dev0.git20141107
Summary: zest.releaser plugin to enter from the command-line the destination of the upload
License: GPLv2+
Group: Development/Python
Url: https://pypi.python.org/pypi/cs.zestreleaser.upload/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/codesyntax/cs.zestreleaser.upload.git
Source: %name-%version.tar

BuildPreReq: python-devel python-module-setuptools
BuildPreReq: python-module-zest.releaser

%py_provides %oname
Requires: python-module-%mname = %EVR
%py_requires zest.releaser

%description
This package provides a plugin for zest.releaser that offers to upload
the released egg via SCP, SFTP or HTTP(S) PUT (WebDAV) to a custom
location (instead of or in addition to PyPI).

%package -n python-module-%mname
Summary: Core files of %mname
Group: Development/Python
%py_provides %mname
%py_requires cs

%description -n python-module-%mname
Core files of %mname.

%prep
%setup

%build
%python_build_debug

%install
%python_install

%if "%_libexecdir" != "%_libdir"
mv %buildroot%_libexecdir %buildroot%_libdir
%endif

install -p -m644 cs/zestreleaser/__init__.py \
	%buildroot%python_sitelibdir/cs/zestreleaser/

%check
python setup.py test

%files
%doc *.rst docs/*
%python_sitelibdir/cs/zestreleaser/*
%python_sitelibdir/*.egg-info
%exclude %python_sitelibdir/cs/zestreleaser/__init__.py*

%files -n python-module-%mname
%dir %python_sitelibdir/cs/zestreleaser
%python_sitelibdir/cs/zestreleaser/__init__.py*

%changelog
* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 1.1-alt1.dev0.git20141107.1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Tue May 24 2016 Ivan Zakharyaschev <imz@altlinux.org> 1.1-alt1.dev0.git20141107.1
- (AUTO) subst_x86_64.

* Tue Dec 30 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.1-alt1.dev0.git20141107
- Initial build for Sisyphus

