%define basic_name cmp-branches
%define mod_dir_name cmp_branches
%define thislibdir %{python3_sitelibdir_noarch}/%{mod_dir_name}
%define thisdocdir %{_defaultdocdir}/%{name}

Name: python3-module-%{basic_name}
Version: 0.1.0
Release: alt1

Summary: Utility for comparing ALT Linux package repositories
License: GPLv3
Group: Development/Tools

Packager: Alexey Appolonov <alexey@altlinux.org>

# http://git.altlinux.org/people/alexey/packages/python3-module-cmp-branches.git
Source: %{name}-%{version}.tar

BuildArch: noarch

BuildRequires: python3-devel
Requires: python3

%description
%{name} is a utility for comparing ALT Linux package repositories.

%prep
%setup

%build

%install
mkdir -p %{buildroot}%{_bindir}
mkdir -p %{buildroot}%{thislibdir}
mkdir -p %{buildroot}%{thisdocdir}
# Executable
cp %{basic_name} %{buildroot}%{_bindir}
# Modules
cp `ls "$PWD/"%{mod_dir_name}/*.py | grep -vE "debug"` %{buildroot}%{thislibdir}
# Documentation
cp COPYING %{buildroot}%{thisdocdir}

%files
%{_bindir}/%{basic_name}
%{thislibdir}
%{thisdocdir}

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

%changelog
* Wed Sep 25 2024 Alexey Appolonov <alexey@altlinux.org> 0.1.0-alt1
- Initial release.
