%define basic_name verlib
%define thislibdir %{python3_sitelibdir_noarch}/%{basic_name}
%define thisdocdir %{_defaultdocdir}/%{name}
%define ax_ver 0.21

Name: python3-module-%{basic_name}
Version: 0.21.0
Release: alt1

Summary: Lib that helps to work with software versions
License: GPLv3
Group: Development/Python3

Packager: Alexey Appolonov <alexey@altlinux.org>

# http://git.altlinux.org/people/alexey/packages/python3-module-verlib.git
Source: %{basic_name}.tar

BuildArch: noarch

BuildRequires: python3-devel
BuildRequires: python3-module-ax >= %{ax_ver}
Requires: python3
Requires: python3-module-ax >= %{ax_ver}

%description
Python library that helps to work with software versions.

%prep
%setup -n %{basic_name}

%build
make testing

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
* Thu Oct 31 2024 Alexey Appolonov <alexey@altlinux.org> 0.21.0-alt1
- Initial release of a new incarnation of the "ver" module of the "ax" library
  as a separate project.

