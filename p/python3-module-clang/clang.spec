%define _unpackaged_files_terminate_build 1
%define oname clang

%def_without check

Name:       python3-module-%oname
Version:    6.0.0.2
Release:    alt1.1

Summary:    libclang python bindings
License:    MIT
Group:      Development/Python3
Url:        https://pypi.python.org/pypi/clang/

BuildArch:  noarch

Source0:    %name-%version.tar

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-nose python-tools-2to3

Requires: clang


%description
This is the python bindings subdir of llvm clang repository.
https://github.com/llvm-mirror/clang/tree/master/bindings/python

This is a fork. Mainly for Pypi packaging purposes.

%package tests
Summary: Tests for %oname
Group: Development/Python3
Requires: python3-module-%oname = %EVR

%add_python3_self_prov_path %buildroot%python3_sitelibdir/%oname/tests/

%description tests
This is the python bindings subdir of llvm clang repository.
https://github.com/llvm-mirror/clang/tree/master/bindings/python

This is a fork. Mainly for Pypi packaging purposes.

This package contains tests for %oname.

%prep
%setup

find -type f -name '*.py' -exec 2to3 -w -n '{}' +

%build
%python3_build_debug

%install
%python3_install

mv tests/ %buildroot%python3_sitelibdir/%oname/

%check
%__python3 setup.py test

%files
%doc LICENSE README.txt examples/
%python3_sitelibdir/*
%exclude %python3_sitelibdir/%oname/tests/

%files tests
%python3_sitelibdir/%oname/tests/


%changelog
* Sat Nov 12 2022 Daniel Zagaynov <kotopesutility@altlinux.org> 6.0.0.2-alt1.1
- NMU: used %%add_python3_self_prov_path macro to skip self-provides from dependencies.

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

