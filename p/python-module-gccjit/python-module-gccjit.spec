Name: python-module-gccjit
Version: 0.4.0.5.g541d3a6
Release: alt1
Summary: Python bindings for libgccjit
Group: Development/Python

License: GPLv3
Source: %name-%version.tar

BuildRequires: python-devel python-module-Cython libgccjit-devel

%description
Python bindings for libgccjit.so (using Cython).

%prep
%setup -n %name-%version

%build
%python_build

%install
%python_install

%files
%python_sitelibdir/gccjit
%python_sitelibdir/gccjit-*-py?.?.egg-info

%changelog
* Thu Dec 24 2015 Gleb F-Malinovskiy <glebfm@altlinux.org> 0.4.0.5.g541d3a6-alt1
- Initial build (v0.4-5-g541d3a6).
