%define _unpackaged_files_terminate_build 1
%define pypi_name boolean.py

%def_with check

Name: python3-module-%pypi_name
Version: 4.0
Release: alt1

Summary: Define boolean algebras, create and parse boolean expressions and create custom boolean DSL
License: BSD-2-Clause
Group: Development/Python3
VCS: https://github.com/bastikr/boolean.py.git
Url: https://pypi.org/project/boolean.py

Source: %name-%version.tar
Patch: %name-%version-alt.patch

BuildRequires(pre): rpm-build-python3

# build backend and its deps
BuildRequires: python3(setuptools)
BuildRequires: python3(wheel)

%if_with check
BuildRequires: python3(pytest)
%endif

BuildArch: noarch

%py3_provides %pypi_name

%description
This library helps you deal with boolean expressions and algebra with variables
and the boolean functions AND, OR, NOT.

You can parse expressions from strings and simplify and compare expressions. You
can also easily create your custom algreba and mini DSL and create custom
tokenizers to handle custom expressions.

%prep
%setup
%autopatch -p1

%build
%pyproject_build

%install
%pyproject_install

# don't ship tests
rm %buildroot%python3_sitelibdir/boolean/test_boolean.py

%check
# override default `setup.py test`
%tox_create_default_config
%tox_check_pyproject -- -vvs boolean

%files
%doc README.rst
%python3_sitelibdir/boolean/
%python3_sitelibdir/%pypi_name-%version.dist-info/

%changelog
* Wed Oct 05 2022 Stanislav Levin <slev@altlinux.org> 4.0-alt1
- Initial build for Sisyphus.
