%define pyname ax
%define thislibdir %{python3_sitelibdir_noarch}/%{pyname}
%define thisdocdir %{_defaultdocdir}/%{name}

Name: python3-module-%{pyname}
Version: 0.1.0
Release: alt1

Summary: Python module with various useful features
License: GPLv3
Group: Development/Python3

Packager: Alexey Appolonov <alexey@altlinux.org>

# http://git.altlinux.org/people/alexey/packages/?p=python3-module-ax.git
Source: %{name}-%{version}.tar

BuildArch: noarch

BuildRequires: python3-devel
Requires: python3

%description
%{summary}.

%prep
%setup

%build
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
* Sat Nov 16 2019 Alexey Appolonov <alexey@altlinux.org> 0.1.0-alt1
- Initial release.
