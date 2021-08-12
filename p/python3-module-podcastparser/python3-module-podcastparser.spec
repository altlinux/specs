%define modname podcastparser
%def_enable check

Name: python3-module-%modname
Version: 0.6.7
Release: alt1

Summary: Simple, fast and efficient podcast parser written in Python.
Group: Development/Python3
License: ISC
Url: http://gpodder.org/%modname

BuildArch: noarch

#VCS: https://github.com/gpodder/podcastparser.git
Source: https://github.com/gpodder/%modname/archive/%version/%modname-%version.tar.gz

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel rpm-build-python3 python3-module-setuptools
%{?_enable_check:BuildRequires: python3-module-pytest python3-module-pytest-cov python3-module-coverage}

%description
The podcast parser project is a library from the gPodder project to provide an
easy and reliable way of parsing RSS- and Atom-based podcast feeds in Python.

%prep
%setup -n %modname-%version

%build
%python3_build

%install
%python3_install

%check
py.test3

%files
%python3_sitelibdir_noarch/%{modname}*
%python3_sitelibdir_noarch/__pycache__/%{modname}*
%doc README.md


%changelog
* Thu Aug 12 2021 Yuri N. Sedunov <aris@altlinux.org> 0.6.7-alt1
- 0.6.7

* Tue Nov 10 2020 Yuri N. Sedunov <aris@altlinux.org> 0.6.6-alt1
- 0.6.6

* Thu Apr 09 2020 Yuri N. Sedunov <aris@altlinux.org> 0.6.5-alt1
- 0.6.5 (python3 only)
- fixed License tag

* Fri Aug 31 2018 Yuri N. Sedunov <aris@altlinux.org> 0.6.4-alt1
- 0.6.4

* Wed Jan 31 2018 Yuri N. Sedunov <aris@altlinux.org> 0.6.3-alt1
- 0.6.3

* Fri Nov 03 2017 Yuri N. Sedunov <aris@altlinux.org> 0.6.2-alt1
- 0.6.2

* Sun Jan 08 2017 Yuri N. Sedunov <aris@altlinux.org> 0.6.1-alt1
- first build for Sisyphus


