%define thislibdir %{python3_sitelibdir_noarch}/%{name}
%define thisdocdir %{_defaultdocdir}/%{name}
%define ax_ver 0.5

Name: anti-cppcheck
Version: 0.1.0
Release: alt1

Summary: Utility that helps to handle reports produced by cppcheck
License: GPLv3
Group: Other

Packager: Alexey Appolonov <alexey@altlinux.org>

# http://git.altlinux.org/people/alexey/packages/?p=%{name}.git
Source: %{name}-%{version}.tar

BuildArch: noarch

BuildRequires: python3-devel
Requires: python3
Requires: python3-module-ax >= %{ax_ver}

%description
%{name} helps to handle reports produced by cppcheck - it converts error
and warning messages to more generic format and presents them as united list,
so a user can give generic commentaries to multiple messages at once, and then
this tool can join those commentaries with an initial report.

%prep
%setup

%build

%install
mkdir -p %{buildroot}%{_bindir}
mkdir -p %{buildroot}%{thislibdir}
mkdir -p %{buildroot}%{thisdocdir}
# Executable
cp %{name} %{buildroot}%{_bindir}
# Modules
cp *.py %{buildroot}%{thislibdir}
# Documentation
cp COPYING %{buildroot}%{thisdocdir}

%files
%{_bindir}/%{name}
%{thislibdir}
%{thisdocdir}

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

%changelog
* Fri Feb 28 2020 Alexey Appolonov <alexey@altlinux.org> 0.1.0-alt1
- Initial release.
