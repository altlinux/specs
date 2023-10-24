%define modname wheezy.template
%define pypi_name %modname
%def_disable check

Name: python3-module-%modname
Version: 3.1.0
Release: alt1
Epoch: 1

Summary: %modname is a lightweight template library
Group: Development/Python3
License: MIT
Url: https://pypi.org/project/%modname

Vcs: https://github.com/akornatskyy/wheezy.template.git
Source: https://pypi.io/packages/source/w/%modname/%modname-%version.tar.gz

BuildRequires(pre): rpm-build-python3
BuildRequires: python3(wheel) python3(setuptools) python3-module-Cython

%description
%modname is a python package written in pure Python code. It is a
lightweight template library. The design goals achived:

* Compact, Expressive, Clean: Minimizes the number of keystrokes required
to build a template. Enables fast and well read coding. You do not need
to explicitly denote statement blocks within HTML (unlike other template
systems), the parser is smart enough to understand your code. This
enables a compact and expressive syntax which is really clean and just
pleasure to type.

* Intuitive, No time to Learn: Basic Python programming skills plus HTML
markup. You are productive just from start. Use full power of Python with
minimal markup required to denote python statements.

* Do Not Repeat Yourself: Master layout templates for inheritance; include
and import directives for maximum reuse. Blazingly Fast: Maximum
rendering performance: ultimate speed and context preprocessor features.

%prep
%setup -n %modname-%version

%build
%pyproject_build

%install
%pyproject_install

%check
%tox_check

%files
%_bindir/*
%python3_sitelibdir/*
%doc README*

%changelog
* Tue Oct 24 2023 Yuri N. Sedunov <aris@altlinux.org> 1:3.1.0-alt1
- downgrade to 3.1.0 to make hotdoc happy

* Sat Jul 29 2023 Yuri N. Sedunov <aris@altlinux.org> 3.2.1-alt1
- 3.2.1

* Fri Jul 28 2023 Yuri N. Sedunov <aris@altlinux.org> 3.2.0-alt1
- 3.2.0

* Tue Apr 20 2021 Yuri N. Sedunov <aris@altlinux.org> 3.1.0-alt1
- 3.1.0

* Wed Mar 10 2021 Yuri N. Sedunov <aris@altlinux.org> 3.0.3-alt1
- 3.0.3

* Tue Jul 21 2020 Yuri N. Sedunov <aris@altlinux.org> 0.1.178-alt1
- first build for Sisyphus




