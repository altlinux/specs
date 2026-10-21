%define pypi_name pyduktape2

%def_with check

Name:    python3-module-%pypi_name
Version: 0.5.0
Release: alt1

Summary: Embed the Duktape JS interpreter in Python
License: GPL-2.0-or-later
Group:   Development/Python3
URL:     https://github.com/phith0n/pyduktape2
VCS:     https://github.com/phith0n/pyduktape2

BuildRequires(pre): rpm-macros-python3
BuildREquires: rpm-build-python3
BuildRequires: python3-module-setuptools
BuildRequires: python3-module-wheel
BuildRequires: python3-module-Cython

Source: %name-%version.tar

%description
Pyduktape is a python wrapper around Duktape, an embeddable Javascript
interpreter.

On top of the interpreter wrapper, pyduktape offers easy integration between the
Python and the Javascript environments. You can pass Python objects to
Javascript, call methods on them and access their attributes. Similarly, you can
pass Javascript objects to Python.

Objects are never copied or serialized. Instead, they are passed between the two
environments using proxy objects. Proxy objects delegate the execution to the
original object environment.

%prep
%setup

%build
%pyproject_build

%install
%pyproject_install

%check
%pyproject_run_pytest -v

%files
%doc LICENSE.txt README.rst
%python3_sitelibdir/%{pypi_name}*.so
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}

%changelog
* Tue Oct 06 2026 Evgeniy Serov <scala@altlinux.org> 0.5.0-alt1
- Initial build for Sisyphus.
