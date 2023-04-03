%define _unpackaged_files_terminate_build 1
%define oname ctypesgen

%def_with check

Name: python3-module-%oname
Version: 1.1.1
Release: alt1

Summary: Python wrapper generator for ctypes
License: BSD-2-Clause
Group: Development/Python3
Url: https://pypi.org/project/ctypesgen/
Vcs: https://github.com/ctypesgen/ctypesgen

Source: %name-%version.tar

BuildArch: noarch

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-setuptools
BuildRequires: python3-module-setuptools_scm
BuildRequires: python3-module-wheel

%description
ctypesgen is a pure-python ctypes wrapper generator. It parses C header files
and creates a wrapper for libraries based on what it finds.
Preprocessor macros are handled in a manner consistent with typical C code.
Preprocessor macro functions are translated into Python functions that are
then made available to the user of the newly-generated Python wrapper library.
It can also output JSON, which can be used with Mork, which generates bindings
for Lua, using the alien module (which binds libffi to Lua).

%prep
%setup

if [ ! -d .git ]; then
    git init
    git config user.email author@example.com
    git config user.name author
    git add .
    git commit -m 'release'
    git tag '%version'
fi

%build
%pyproject_build

%install
%pyproject_install

%check
%tox_check_pyproject

%files
%doc LICENSE *.md
%_bindir/*
%python3_sitelibdir/%oname
%python3_sitelibdir/%{pyproject_distinfo %oname}


%changelog
* Mon Apr 03 2023 Anton Vyatkin <toni@altlinux.org> 1.1.1-alt1
- New version 1.1.1

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

