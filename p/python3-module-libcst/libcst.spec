%define _unpackaged_files_terminate_build 1
%define oname libcst

%def_with check

Name: python3-module-%oname
Version: 0.3.18
Release: alt1

Summary: A Concrete Syntax Tree (CST) parser and serializer library for Python
License: MIT and Python-2.0 and Apache-2.0
Group: Development/Python3
# Source-git: https://github.com/Instagram/LibCST.git
Url: https://pypi.org/project/libcst/

Source: %name-%version.tar
Patch0: %name-%version-alt.patch

BuildRequires(pre): rpm-build-python3

%if_with check
BuildRequires: python3(black)
BuildRequires: python3(hypothesis)
BuildRequires: python3(isort)
BuildRequires: python3(tox)
BuildRequires: python3(tox_no_deps)
BuildRequires: python3(typing_extensions)
BuildRequires: python3(typing_inspect)
BuildRequires: python3(yaml)
%endif

BuildArch: noarch

%description
LibCST parses Python source code as a CST tree that keeps all formatting
details (comments, whitespaces, parentheses, etc). It's useful for building
automated refactoring (codemod) applications and linters.

LibCST creates a compromise between an Abstract Syntax Tree (AST) and a
traditional Concrete Syntax Tree (CST). By carefully reorganizing and naming
node types and fields, we've created a lossless CST that looks and feels like
an AST.

%prep
%setup
%autopatch -p1

%build
%python3_build

%install
%python3_install

# don't package tests
find %buildroot%python3_sitelibdir_noarch -type d -name tests | \
    xargs -I {} rm -rf "{}"

# don't remove libcst/codemod/_testing.py and libcst/testing/
# contains CodemodTest class which provides testing facility for Codemods

%check
export PIP_NO_BUILD_ISOLATION=no
export PIP_NO_INDEX=YES
export TOXENV=py3
tox.py3 --sitepackages --no-deps -vvr

%files
%doc README.rst
%python3_sitelibdir/libcst/
%python3_sitelibdir/libcst-%version-py%_python3_version.egg-info/

%changelog
* Fri Apr 16 2021 Stanislav Levin <slev@altlinux.org> 0.3.18-alt1
- Initial build for Sisyphus.
