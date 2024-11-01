%define basic_name sisyphus
%define thislibdir %{python3_sitelibdir_noarch}/%{basic_name}
%define thisdocdir %{_defaultdocdir}/%{name}
%define ax_ver 0.21
%define verlib_ver 0.21

Name: python3-module-%{basic_name}
Version: 0.21.0
Release: alt1

Summary: Lib that helps to work with the Sisyphus repo and it's branches
License: GPLv3
Group: Development/Python3

Packager: Alexey Appolonov <alexey@altlinux.org>

# http://git.altlinux.org/people/alexey/packages/python3-module-sisyphus.git
Source: %{basic_name}.tar

BuildArch: noarch

BuildRequires: python3-devel
Requires: python3
Requires: python3-module-ax >= %{ax_ver}
Requires: python3-module-verlib >= %{verlib_ver}

%description
Python library that helps to work with the Sisyphus repository and it's
branches.

%prep
%setup -n %{basic_name}

%install
mkdir -p %{buildroot}%{thislibdir}
mkdir -p %{buildroot}%{thisdocdir}
# Executables
cp *.py %{buildroot}%{thislibdir}
# Documentation
cp COPYING %{buildroot}%{thisdocdir}

%files
%{thisdocdir}
%{thislibdir}

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

%changelog
* Thu Sep 26 2024 Alexey Appolonov <alexey@altlinux.org> 0.21.0-alt1
- Initial release of a new incarnation of the "alt" module of the "ax" library
  as a separate project.

