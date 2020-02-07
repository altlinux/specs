%define mname gocept
%define oname %mname.munin

Name: python3-module-%oname
Version: 0.1
Release: alt2

Summary: Utilities for writing munin plugins
License: ZPLv2.1
Group: Development/Python3
Url: https://pypi.python.org/pypi/gocept.munin/

Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3
BuildRequires: python-tools-2to3

%py3_provides %oname
Requires: python3-module-%mname = %EVR


%description
This package provides base classes for defining Munin graphs and a
main function to handle munin-typical symlinked scripts.

%package -n python3-module-%mname
Summary: Core files of %mname
Group: Development/Python3
%py3_provides %mname

%description -n python3-module-%mname
Core files of %mname.

%prep
%setup

find -type f -name '*.py' -exec 2to3 -w -n '{}' +

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
* Fri Feb 07 2020 Andrey Bychkov <mrdrew@altlinux.org> 0.1-alt2
- Porting to python3.

* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 0.1-alt1.1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Tue May 24 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.1-alt1.1
- (AUTO) subst_x86_64.

* Mon Dec 15 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1-alt1
- Initial build for Sisyphus

