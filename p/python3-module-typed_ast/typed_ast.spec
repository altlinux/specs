%define _unpackaged_files_terminate_build 1
%define oname typed_ast

%def_with check

Name: python3-module-%oname
Version: 1.4.0
Release: alt1

Summary: A fork of the ast module with type annotations
License: ASL 2.0
Group: Development/Python3
# Source-git: https://github.com/python/typed_ast.git
Url: https://pypi.org/project/typed-ast/

Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3

%if_with check
BuildRequires: python3(pytest)
%endif

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
# don't package tests
rm -rf %buildroot%python3_sitelibdir/typed_ast/tests

%check
export PYTHONPATH=%buildroot%python3_sitelibdir
%_bindir/py.test3 -v

%files
%dir %python3_sitelibdir/typed_ast
%python3_sitelibdir/typed_ast/_ast27.cpython-*.so
%python3_sitelibdir/typed_ast/_ast3.cpython-*.so
%python3_sitelibdir/typed_ast/*.py
%python3_sitelibdir/typed_ast/__pycache__/
%python3_sitelibdir/typed_ast-*.egg-info/

%changelog
* Wed Oct 16 2019 Stanislav Levin <slev@altlinux.org> 1.4.0-alt1
- 1.3.1 -> 1.4.0.

* Mon Feb 11 2019 Stanislav Levin <slev@altlinux.org> 1.3.1-alt1
- 1.2.0 -> 1.3.1.

* Tue Jan 15 2019 Stanislav Levin <slev@altlinux.org> 1.2.0-alt1
- 1.1.0 -> 1.2.0.

* Mon Sep 03 2018 Stanislav Levin <slev@altlinux.org> 1.1.0-alt1
- Initial build.
