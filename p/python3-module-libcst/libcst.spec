%define _unpackaged_files_terminate_build 1
%define oname libcst

%def_with check

Name: python3-module-%oname
Version: 0.4.1
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
BuildRequires: python3(setuptools_scm)

# rust
BuildRequires: /proc
BuildRequires: rust
BuildRequires: rust-cargo
BuildRequires: python3(setuptools_rust)

%if_with check
# install_requires=
BuildRequires: python3(typing_extensions)
BuildRequires: python3(typing_inspect)
BuildRequires: python3(yaml)

BuildRequires: /usr/bin/ufmt
BuildRequires: python3(hypothesis)
BuildRequires: python3(tox)
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

%build
# https://github.com/pypa/setuptools_scm/#environment-variables
export SETUPTOOLS_SCM_PRETEND_VERSION=%version
%python3_build

%install
export SETUPTOOLS_SCM_PRETEND_VERSION=%version
%python3_install

# don't package tests
find %buildroot%python3_sitelibdir -type d -name tests | \
    xargs -I {} rm -rf "{}"

# don't remove libcst/codemod/_testing.py and libcst/testing/
# contains CodemodTest class which provides testing facility for Codemods

%check
cat > tox.ini <<'EOF'
[testenv]
setenv   =
    native: LIBCST_PARSER_TYPE = native
    pure: LIBCST_PARSER_TYPE = pure
    NO_PYRE = yes
usedevelop=True
commands =
    python -m unittest -v
EOF
export SETUPTOOLS_SCM_PRETEND_VERSION=%version
export PIP_NO_BUILD_ISOLATION=no
export PIP_NO_INDEX=YES
export TOXENV=py3-pure,py3-native
tox.py3 --sitepackages -vvr

%files
%doc README.rst
%python3_sitelibdir/libcst/
%python3_sitelibdir/libcst-%version-py%_python3_version.egg-info/

%changelog
* Fri Feb 11 2022 Stanislav Levin <slev@altlinux.org> 0.4.1-alt1
- 0.3.18 -> 0.4.1.

* Fri Apr 16 2021 Stanislav Levin <slev@altlinux.org> 0.3.18-alt1
- Initial build for Sisyphus.
