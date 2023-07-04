%define modname anytree
%def_disable check
# broken script
%def_disable tools

Name: python-module-%modname
Version: 3.0.0
Release: alt1

Summary: Python Tree Data Structure Library
Group: Development/Python
License: Apache-2.0
Url: https://pypi.org/project/%modname
# https://github.com/c0fec0de/anytree

Source: https://pypi.io/packages/source/a/%modname/%modname-%version.tar.gz

BuildArch: noarch

BuildRequires: python3-devel rpm-build-python3 python3-module-wheel
BuildRequires: python3-module-distribute python3-module-poetry

%description
Python module to manipulate tree data structures

%package -n python3-module-%modname
Summary: Python Tree Data Structure Library
Group: Development/Python3

%description -n python3-module-%modname
Python3 module to manipulate tree data structures

%if_enabled tools
%package -n %modname-tools
Summary: Tools for %name
Group: Development/Tools

%description -n %modname-tools
Tools for %name.
%endif

%prep
%setup -n %modname-%version

%build
%pyproject_build

%install
%pyproject_install

%if_disabled tools
rm -rf %buildroot%_bindir/ebt
%endif

%if_enabled check
%check
%pyproject_run_pytest
%endif

%files -n python3-module-%modname
%doc README.rst LICENSE
%python3_sitelibdir_noarch/%{modname}*/

%if_enabled tools
%files -n %modname-tools
%_bindir/ebt
%endif

%changelog
* Tue Jul 04 2023 Leontiy Volodin <lvol@altlinux.org> 3.0.0-alt1
- 3.0.0.
- Disabled python2 build again (by upstream) (ALT #44959).

* Thu Jul 28 2022 Leontiy Volodin <lvol@altlinux.org> 2.8.0-alt2
- Returned python2 build for mlnx-tools (ALT #41412, #43337).

* Tue Nov 23 2021 Leontiy Volodin <lvol@altlinux.org> 2.8.0-alt1.1
- Returned into Sisyphus as require for mlnx-tools.

* Wed Jan 15 2020 Yuri N. Sedunov <aris@altlinux.org> 2.8.0-alt1
- 2.8.0

* Wed Dec 11 2019 Yuri N. Sedunov <aris@altlinux.org> 2.7.3-alt1
- 2.7.3
- disabled python2 build

* Mon Feb 11 2019 Yuri N. Sedunov <aris@altlinux.org> 2.6.0-alt1
- 2.6.0

* Sat Feb 02 2019 Yuri N. Sedunov <aris@altlinux.org> 2.5.0-alt1
- 2.5.0

* Sat Mar 24 2018 Yuri N. Sedunov <aris@altlinux.org> 2.4.3-alt1
- first build for Sisyphus



