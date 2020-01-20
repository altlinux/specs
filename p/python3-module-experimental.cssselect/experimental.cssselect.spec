%define mname experimental
%define oname %mname.cssselect

Name: python3-module-%oname
Version: 0.3
Release: alt2

Summary: Experimental version of lxml.cssselect
License: BSD
Group: Development/Python3
Url: https://pypi.python.org/pypi/experimental.cssselect/

# https://github.com/lrowe/experimental.cssselect.git
Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-lxml

%py3_provides %oname
Requires: python3-module-%mname = %EVR


%description
This package contains an experimental fork of the lxml.cssselect module.

%package -n python3-module-%mname
Summary: Core files of %mname
Group: Development/Python3
%py3_provides %mname

%description -n python3-module-%mname
Core files of %mname.

%prep
%setup

%build
%python3_build_debug

%install
%python3_install

%if "%_libexecdir" != "%_libdir"
mv %buildroot%_libexecdir %buildroot%_libdir
%endif

install -p -m644 src/%mname/__init__.py \
    %buildroot%python3_sitelibdir/%mname/

%check
%__python3 setup.py test

%files
%doc *.txt
%python3_sitelibdir/%mname/*
%python3_sitelibdir/*.egg-info
%exclude %python3_sitelibdir/%mname/__init__.py*

%files -n python3-module-%mname
%dir %python3_sitelibdir/%mname
%python3_sitelibdir/%mname/__init__.py*


%changelog
* Mon Jan 20 2020 Andrey Bychkov <mrdrew@altlinux.org> 0.3-alt2
- Porting on Python3.

* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 0.3-alt1.git20120405.1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Tue May 24 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.3-alt1.git20120405.1
- (AUTO) subst_x86_64.

* Tue Oct 14 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.3-alt1.git20120405
- Initial build for Sisyphus

