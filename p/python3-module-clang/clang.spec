%define _unpackaged_files_terminate_build 1
%define oname clang
%define llvm_ver 18.1

%def_without check

Name:       python3-module-%oname
Version:    18.1.1
Release:    alt1

Summary:    Libclang python bindings
License:    Apache-2.0
Group:      Development/Python3
Url:        https://pypi.org/project/libclang/
VCS:        https://github.com/sighingnow/libclang

Source0:    %name-%version.tar

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-setuptools
BuildRequires: python3-module-wheel
BuildRequires: clang%{llvm_ver}-devel
BuildRequires: llvm%{llvm_ver}-devel

%description
The aim of this project is to make the clang.cindex
(aka., Clang Python Bindings) available for more Python users, without setting
up the LLVM environment.

%prep
%setup

%build
%pyproject_build

%install
%pyproject_install

%if "%python3_sitelibdir_noarch" != "%python3_sitelibdir"
install -d %buildroot%python3_sitelibdir
mv %buildroot%python3_sitelibdir_noarch/* \
	%buildroot%python3_sitelibdir/
%endif

# Using system libclang.so
export ALTWRAP_LLVM_VERSION=%llvm_ver
libdir=$(llvm-config --libdir)
ln -s $libdir/libclang.so %buildroot%python3_sitelibdir/%oname/native/libclang.so

%files
%doc LICENSE.TXT README.md
%python3_sitelibdir/%oname
%python3_sitelibdir/lib%oname-%version.dist-info

%changelog
* Tue Apr 23 2024 L.A. Kostis <lakostis@altlinux.ru> 18.1.1-alt1
- NMU: update to llvm-18.

* Thu Nov 23 2023 Anton Vyatkin <toni@altlinux.org> 16.0.6-alt2
- Using system lib.

* Fri Jul 28 2023 Anton Vyatkin <toni@altlinux.org> 16.0.6-alt1
- New version 16.0.6.

* Fri Mar 17 2023 Anton Vyatkin <toni@altlinux.org> 15.0.6.1-alt1
- New version 15.0.6.1

* Sat Nov 12 2022 Daniel Zagaynov <kotopesutility@altlinux.org> 6.0.0.2-alt1.1
- NMU: used %%add_python3_self_prov_path macro to skip self-provides from
  dependencies.

* Thu Feb 06 2020 Andrey Bychkov <mrdrew@altlinux.org> 6.0.0.2-alt1
- Version updated to 6.0.0.2
- build for python2 disabled.

* Fri Mar 16 2018 Oleg Solovyov <mcpain@altlinux.org> 5.0-alt1
- version 5.0

* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 3.8-alt1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Wed Jan 11 2017 Igor Vlasenko <viy@altlinux.ru> 3.8-alt1
- automated PyPI update

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 3.5-alt1.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 3.5-alt1.1
- NMU: Use buildreq for BR.

* Fri Jan 23 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.5-alt1
- Initial build for Sisyphus

