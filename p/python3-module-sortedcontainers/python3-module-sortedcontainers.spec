%define modname sortedcontainers

Name: python3-module-%modname
Version: 2.3.0
Release: alt1

Summary: Python SortedContainers module
Group: Development/Python3
License: Apache-2.0
Url: http://pypi.python.org/pypi/%modname
Source: http://pypi.io/packages/source/s/%modname/%modname-%version.tar.gz

BuildArch: noarch

BuildRequires: python3-devel rpm-build-python3
BuildRequires: python3-module-distribute

%description
`SortedContainers`_ is an Apache2 licensed `sorted collections library`
written in pure-Python, and fast as C-extensions.

%prep
%setup -n %modname-%version

%build
%python3_build

%install
%python3_install

%files
%python3_sitelibdir_noarch/%modname/
%python3_sitelibdir_noarch/*.egg-info
%doc README.rst LICENSE


%changelog
* Mon Nov 09 2020 Yuri N. Sedunov <aris@altlinux.org> 2.3.0-alt1
- 2.3.0

* Sun Jun 07 2020 Yuri N. Sedunov <aris@altlinux.org> 2.2.1-alt1
- 2.2.1 (python3 only)

* Mon Nov 26 2018 Yuri N. Sedunov <aris@altlinux.org> 2.1.0-alt1
- 2.1.0

* Mon Sep 10 2018 Yuri N. Sedunov <aris@altlinux.org> 2.0.5-alt1
- 2.0.5

* Thu Jun 07 2018 Yuri N. Sedunov <aris@altlinux.org> 2.0.4-alt1
- 2.0.4

* Fri Jun 01 2018 Yuri N. Sedunov <aris@altlinux.org> 2.0.3-alt1
- 2.0.3

* Tue May 22 2018 Yuri N. Sedunov <aris@altlinux.org> 2.0.2-alt1
- 2.0.2

* Sat May 19 2018 Yuri N. Sedunov <aris@altlinux.org> 2.0.1-alt1
- 2.0.1

* Fri May 11 2018 Yuri N. Sedunov <aris@altlinux.org> 1.5.10-alt1
- 1.5.10

* Tue Jan 16 2018 Yuri N. Sedunov <aris@altlinux.org> 1.5.9-alt1
- 1.5.9

* Thu Jul 06 2017 Yuri N. Sedunov <aris@altlinux.org> 1.5.7-alt1
- first build for Sisyphus


