
%def_with python3

Name: python-module-z3c
Summary: Pure namespace package 'z3c' for Python 2
Version: 3.0.0
Release: alt3
License: ZPL
Group: Development/Python

Source: __init__.py
BuildRequires(pre): rpm-build-python
%if_with python3
BuildRequires(pre): rpm-build-python3
%endif

%description
%summary

%if_with python3
%package -n python3-module-z3c
Summary: Pure namespace package 'z3c' for Python 3
Group: Development/Python3

%description -n python3-module-z3c
%summary
%endif

%install

install -Dm644 %SOURCE0 %buildroot%python_sitelibdir/z3c/__init__.py

%if_with python3
install -Dm644 %SOURCE0 %buildroot%python3_sitelibdir/z3c/__init__.py
%endif

%files
%python_sitelibdir/z3c

%if_with python3
%files -n python3-module-z3c
%python3_sitelibdir/z3c
%endif

%changelog
* Sat Feb 02 2019 Ivan A. Melnikov <iv@altlinux.org> 3.0.0-alt3
- Build as a separate package
