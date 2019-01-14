%define _unpackaged_files_terminate_build 1
%define oname typed_ast

Name: python3-module-%oname
Version: 1.2.0
Release: alt1

Summary: A fork of the ast module with type annotations
License: ASL 2.0
Group: Development/Python3
# Source-git: https://github.com/python/typed_ast.git
Url: https://pypi.org/project/typed-ast/

Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3

%description
This package is based on the ast modules from Python 2 and 3,
and has been extended with support for type comments and type annotations
as supported in Python 3.6.

%prep
%setup

%build
%add_optflags -fno-strict-aliasing
%python3_build

%install
%python3_install

%check

%files
%python3_sitelibdir/_ast27.cpython-*.so
%python3_sitelibdir/_ast3.cpython-*.so
%python3_sitelibdir/typed_ast/
%python3_sitelibdir/typed_ast-*.egg-info/

%changelog
* Tue Jan 15 2019 Stanislav Levin <slev@altlinux.org> 1.2.0-alt1
- 1.1.0 -> 1.2.0.

* Mon Sep 03 2018 Stanislav Levin <slev@altlinux.org> 1.1.0-alt1
- Initial build.
