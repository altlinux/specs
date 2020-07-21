%define modname wheezy.template
%def_disable check

Name: python3-module-%modname
Version: 0.1.178
Release: alt1

Summary: %modname is a lightweight template library
Group: Development/Python3
License: MIT
Url: https://pypi.org/project/%modname

#VCS: https://github.com/akornatskyy/wheezy.template.git
Source: https://pypi.io/packages/source/w/%modname/%modname-%version.tar.gz

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel python3-module-Cython

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
%python3_build

%install
%python3_install

%check
tox.py3

%files
%_bindir/*
%python3_sitelibdir/*
%doc README*

%changelog
* Tue Jul 21 2020 Yuri N. Sedunov <aris@altlinux.org> 0.1.178-alt1
- first build for Sisyphus




