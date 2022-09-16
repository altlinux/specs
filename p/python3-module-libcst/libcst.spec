%define _unpackaged_files_terminate_build 1
%define pypi_name libcst

%def_with check

Name: python3-module-%pypi_name
Version: 0.4.7
Release: alt1

Summary: A Concrete Syntax Tree (CST) parser and serializer library for Python
License: MIT and Python-2.0 and Apache-2.0
Group: Development/Python3
# Source-git: https://github.com/Instagram/LibCST.git
Url: https://pypi.org/project/libcst/

Source0: %name-%version.tar
Source1: vendor.tar
Patch0: %name-%version-alt.patch

BuildRequires(pre): rpm-build-python3

# build backend and its deps
BuildRequires: python3(setuptools)
BuildRequires: python3(wheel)
BuildRequires: python3(setuptools_rust)

BuildRequires: python3(setuptools_scm)

# rust
BuildRequires: /proc
BuildRequires: rust
BuildRequires: rust-cargo

%if_with check
# install_requires=
BuildRequires: python3(typing_extensions)
BuildRequires: python3(typing_inspect)
BuildRequires: python3(yaml)

BuildRequires: /usr/bin/ufmt
BuildRequires: python3(hypothesis)
%endif

%description
LibCST parses Python source code as a CST tree that keeps all formatting
details (comments, whitespaces, parentheses, etc). It's useful for building
automated refactoring (codemod) applications and linters.

LibCST creates a compromise between an Abstract Syntax Tree (AST) and a
traditional Concrete Syntax Tree (CST). By carefully reorganizing and naming
node types and fields, we've created a lossless CST that looks and feels like
an AST.

%prep
%setup -a1
%autopatch -p1

# setuptools_scm implements a file_finders entry point which returns all files
# tracked by SCM.
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

# don't package tests
find %buildroot%python3_sitelibdir -type d -name tests | \
    xargs -I {} rm -rf "{}"

# don't remove libcst/codemod/_testing.py and libcst/testing/
# contains CodemodTest class which provides testing facility for Codemods

%check
# upstream run its test suite with deprecated `setup.py test` and supports
# only in-tree tests. We run those tests within Python virtualenv and thereby,
# libcst must be removed, otherwise unittest imports libcst from source
# directory instead of installed one.
rm -rf libcst

# ufmt ignores files ignored by VCS and codegen tests fail
sed -i 's/^\.tox\/$/# &/' .gitignore

cat > tox.ini <<'EOF'
[testenv]
allowlist_externals =
    /bin/bash
setenv =
    native: LIBCST_PARSER_TYPE = native
    pure: LIBCST_PARSER_TYPE = pure
    NO_PYRE = yes
commands_pre =
    # enforce installation of libcst being tested instead of system-wide one,
    # pip rejects installation of a package if there is installed one having the
    # same version
    /bin/bash -c 'pip install --force-reinstall --no-deps "dist/$(cat dist/.wheeltracker)"'
commands =
    python -m unittest discover -v libcst
EOF
export TOXENV=py3-pure,py3-native
%tox_check_pyproject

%files
%doc README.rst
%python3_sitelibdir/libcst/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}/

%changelog
* Thu Sep 15 2022 Stanislav Levin <slev@altlinux.org> 0.4.7-alt1
- 0.4.1 -> 0.4.7.

* Fri Feb 11 2022 Stanislav Levin <slev@altlinux.org> 0.4.1-alt1
- 0.3.18 -> 0.4.1.

* Fri Apr 16 2021 Stanislav Levin <slev@altlinux.org> 0.3.18-alt1
- Initial build for Sisyphus.
