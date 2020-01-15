%define oname gccjit

Name: python3-module-%oname
Version: 0.4.0.5.g541d3a6
Release: alt2

Summary: Python bindings for libgccjit
License: GPLv3
Group: Development/Python3

Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-Cython libgccjit-devel


%description
Python bindings for libgccjit.so (using Cython).

%prep
%setup -n %name-%version

%build
%python3_build

%install
%python3_install

%files
%python3_sitelibdir/gccjit
%python3_sitelibdir/gccjit-*-py?.?.egg-info


%changelog
* Wed Jan 15 2020 Andrey Bychkov <mrdrew@altlinux.org> 0.4.0.5.g541d3a6-alt2
- porting on python3

* Thu Dec 24 2015 Gleb F-Malinovskiy <glebfm@altlinux.org> 0.4.0.5.g541d3a6-alt1
- Initial build (v0.4-5-g541d3a6).
