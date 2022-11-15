%define _unpackaged_files_terminate_build 1
%define oname ctypesgen

Name: python3-module-%oname
Version: 1.0.2
Release: alt1.1

Summary: Python wrapper generator for ctypes
License: BSD
Group: Development/Python3
Url: https://pypi.python.org/pypi/ctypesgen/
BuildArch: noarch

# https://github.com/davidjamesca/ctypesgen.git
Source: %{oname}-%{version}.tar

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-nose

%add_python3_self_prov_path %buildroot%python3_sitelibdir/%oname/test

%description
ctypesgen is a pure-python ctypes wrapper generator. It can also
output JSON, which can be used with Mork, which generates bindings for
Lua, using the alien module (which binds libffi to Lua).

%prep
%setup -q -n %{oname}-%{version}

rm -f ctypesgen/printer_python/preamble/2_*.py

%build
%python3_build_debug

%install
%python3_install

%check
%__python3 setup.py test

%files
%doc CONTRIBUTING LICENSE README.md
%_bindir/*
%python3_sitelibdir/*


%changelog
* Sat Nov 12 2022 Daniel Zagaynov <kotopesutility@altlinux.org> 1.0.2-alt1.1
- NMU: used %%add_python3_self_prov_path macro to skip self-provides from dependencies.

* Wed Feb 05 2020 Andrey Bychkov <mrdrew@altlinux.org> 1.0.2-alt1
- Version updated to 1.0.2
- porting on python3.

* Mon Mar 05 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 0.r125-alt2
- Fixed floating-point numbers definitions processing.

* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 0.r125-alt1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Tue Jan 17 2017 Igor Vlasenko <viy@altlinux.ru> 0.r125-alt1
- automated PyPI update

* Mon Mar 16 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.0.r151-alt1.git20130821
- Initial build for Sisyphus

