%define _unpackaged_files_terminate_build 1
%define oname asttokens

%def_with check

Name: python3-module-%oname
Version: 2.0.5
Release: alt1
Summary: annotates Python abstract syntax trees (ASTs) with the positions of tokens and text in the source code
Group: Development/Python3
License: Apache-2.0
Url: https://pypi.org/project/asttokens
BuildArch: noarch

# https://github.com/gristlabs/asttokens/archive/refs/tags/v%version.tar.gz
Source: %oname-%version.tar.gz
Source44: %oname.watch

BuildRequires(pre): rpm-build-python3
# Automatically added by buildreq on Thu Oct 21 2021
# optimized out: python3 python3-base python3-dev python3-module-pkg_resources python3-module-setuptools sh4
BuildRequires: python3-module-packaging python3-module-setuptools_scm python3-module-toml

%if_with check
BuildRequires: python3(pytest)
BuildRequires: python3(astroid)
%endif

%description
The ``asttokens`` module annotates Python abstract syntax trees (ASTs) with the
positions of tokens and text in the source code that generated them.

It makes it possible for tools that work with logical AST nodes to find the
particular text that resulted in those nodes, for example for automated
refactoring or highlighting.

%prep
%setup -n %oname-%version
%autopatch -p2

%build
%python3_build

%install
%python3_install

%check
#TODO

%files
%doc README* LICENSE*
%python3_sitelibdir/%oname
%python3_sitelibdir/%oname-%version-py3*.egg-info

%changelog
* Thu Oct 21 2021 Ildar Mulyukov <ildar@altlinux.ru> 2.0.5-alt1
- 1st build for Sisyphus
