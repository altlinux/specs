%define modname sphinx-autodoc-typehints
%define _modname sphinx_autodoc_typehints
%def_disable check

Name: python3-module-%modname
Version: 1.18.1
Release: alt1

Summary: Type hints (PEP 484) support for the Sphinx autodoc extension
Group: Development/Python3
License: MIT
Url: https://pypi.org/project/%modname

Vcs: https://github.com/tox-dev/sphinx-autodoc-typehints.git
#Source: https://github.com/tox-dev/%modname/archive/%version/%modname-%version.tar.gz
Source: https://pypi.io/packages/source/s/%modname/%_modname-%version.tar.gz

BuildArch: noarch

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-setuptools_scm
%{?_enable_check:BuildRequires: python3-module-pytest python3-module-sphobjinv}

%description
This Sphinx extension allows to use Python 3 annotations for
documenting acceptable argument types and return value types of
functions.

%prep
%setup -n %_modname-%version

%build
%python3_build

%install
%python3_install

%check
export PYTHONPATH=%buildroot%python3_sitelibdir_noarch
py.test3

%files
%python3_sitelibdir_noarch/*
%doc README* CHANGELOG*


%changelog
* Fri May 06 2022 Yuri N. Sedunov <aris@altlinux.org> 1.18.1-alt1
- 1.18.1

* Sat Mar 05 2022 Yuri N. Sedunov <aris@altlinux.org> 1.17.0-alt1
- 1.17.0

* Fri Jan 28 2022 Yuri N. Sedunov <aris@altlinux.org> 1.16.0-alt1
- 1.16.0

* Thu Jan 20 2022 Yuri N. Sedunov <aris@altlinux.org> 1.15.3-alt1
- 1.15.3

* Mon Jan 10 2022 Yuri N. Sedunov <aris@altlinux.org> 1.15.1-alt1
- 1.15.1

* Wed Jan 05 2022 Yuri N. Sedunov <aris@altlinux.org> 1.13.1-alt1
- 1.13.1 (supported Python 3.10)

* Thu Apr 15 2021 Yuri N. Sedunov <aris@altlinux.org> 1.12.0-alt1
- 1.12.0

* Sun Mar 07 2021 Yuri N. Sedunov <aris@altlinux.org> 1.11.1-alt1
- first build for Sisyphus




