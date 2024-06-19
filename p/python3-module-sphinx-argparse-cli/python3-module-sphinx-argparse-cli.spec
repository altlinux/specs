%def_disable snapshot
%define modname sphinx-argparse-cli
%define pypi_name sphinx_argparse_cli
%def_enable check

Name: python3-module-%modname
Version: 1.16.0
Release: alt1

Summary: CLI arguments renderer for Sphinx
Group: Development/Python3
License: MIT
Url: https://pypi.org/project/%modname

%if_disabled snapshot
Source: https://pypi.io/packages/source/s/%pypi_name/%pypi_name-%version.tar.gz
# tar -cf sphinx_argparse_cli-1.15.0-roots.tar roots/
Source1: %pypi_name-%version-roots.tar
%else
Vcs: https://github.com/tox-dev/sphinx-argparse-cli.git
Source: %pypi_name-%version.tar
%endif

BuildArch: noarch
Provides: python3-module-%pypi_name = %EVR

%define sphinx_ver 6.1.3

BuildRequires(pre): rpm-build-python3 >= 0.1.19
BuildRequires: python3-module-hatchling python3-module-hatch-vcs python3-module-wheel
%{?_enable_check:BuildRequires: python3-module-sphinx-tests >= %sphinx_ver python3-module-pytest-cov
BuildRequires: python3-module-covdefaults}

%description
Render CLI arguments (sub-commands friendly) defined by the argparse module.

%prep
%setup -n %pypi_name-%version -a1

%build
%pyproject_build

%install
%pyproject_install

%check
export PYTHONPATH=%buildroot%python3_sitelibdir_noarch
py.test3

%files
%python3_sitelibdir_noarch/%pypi_name
%python3_sitelibdir_noarch/%{pyproject_distinfo %pypi_name}
%doc README*


%changelog
* Wed Jun 19 2024 Yuri N. Sedunov <aris@altlinux.org> 1.16.0-alt1
- 1.16.0

* Thu Apr 18 2024 Yuri N. Sedunov <aris@altlinux.org> 1.15.0-alt1
- 1.15.0

* Sat Apr 06 2024 Yuri N. Sedunov <aris@altlinux.org> 1.14.0-alt1
- 1.14.0

* Thu Feb 22 2024 Yuri N. Sedunov <aris@altlinux.org> 1.13.1-alt1
- 1.13.1

* Tue Feb 13 2024 Yuri N. Sedunov <aris@altlinux.org> 1.12.0-alt1
- 1.12.0

* Fri Jun 16 2023 Yuri N. Sedunov <aris@altlinux.org> 1.11.1-alt1
- 1.11.1

* Thu Apr 20 2023 Yuri N. Sedunov <aris@altlinux.org> 1.11.0-alt1
- 1.11.0

* Wed Aug 10 2022 Yuri N. Sedunov <aris@altlinux.org> 1.10.0-alt1
- 1.10.0

* Fri Jun 24 2022 Yuri N. Sedunov <aris@altlinux.org> 1.9.0-alt1
- 1.9.0
- spec ported to %%pyproject/%%tox macros

* Wed Dec 29 2021 Yuri N. Sedunov <aris@altlinux.org> 1.8.3-alt1
- 1.8.3

* Wed Nov 24 2021 Yuri N. Sedunov <aris@altlinux.org> 1.8.2-alt1
- 1.8.2

* Mon Oct 18 2021 Yuri N. Sedunov <aris@altlinux.org> 1.8.0-alt1
- 1.8.0

* Thu Sep 30 2021 Yuri N. Sedunov <aris@altlinux.org> 1.7.0-alt1
- first build for Sisyphus





