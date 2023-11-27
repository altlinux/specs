%define base       alt-tasks
%define thislibdir %{python3_sitelibdir_noarch}/alt_tasks_explorer
%define thisdocdir %{_defaultdocdir}/%{name}

Name: %{base}-explorer
Version: 0.1.0
Release: alt3

Summary: A set of utils used on top of the "alt-task" utility
License: GPLv3
Group: Other

Packager: Alexey Appolonov <alexey@altlinux.org>

# http://git.altlinux.org/people/alexey/packages/%{name}.git
Source: %{name}-%{version}.tar

BuildArch: noarch

BuildRequires: python3-devel
Requires: python3
Requires: %{base} >= 0.9

%description
%{name} is a set of utilities that can be used to perform various operations
over ALT Linux tasks found via the "%{base}" utility.

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

%prep
%setup

%build

%install
mkdir -p %{buildroot}%{_bindir}
mkdir -p %{buildroot}%{thislibdir}
mkdir -p %{buildroot}%{thisdocdir}
# Executables
cp %{base}-* %{buildroot}%{_bindir}
# Modules
cp alt_tasks_explorer/*.py %{buildroot}%{thislibdir}
# Documentation
cp COPYING readme.txt %{buildroot}%{thisdocdir}

%files
%{_bindir}/%{base}-*
%{thislibdir}
%{thisdocdir}

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

%changelog
* Mon Nov 27 2023 Alexey Appolonov <alexey@altlinux.org> 0.1.0-alt3
- Edited manual.

* Mon Nov 20 2023 Alexey Appolonov <alexey@altlinux.org> 0.1.0-alt2
- Added manual.

* Thu Nov 16 2023 Alexey Appolonov <alexey@altlinux.org> 0.1.0-alt1
- Initial release.
