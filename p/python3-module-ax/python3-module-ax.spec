%define pyname ax
%define thislibdir %{python3_sitelibdir_noarch}/%{pyname}
%define thisdocdir %{_defaultdocdir}/%{name}

Name: python3-module-%{pyname}
Version: 0.5.0
Release: alt1

Summary: Generic function library initially developed for cve-manager
License: GPLv3
Group: Development/Python3

Packager: Alexey Appolonov <alexey@altlinux.org>

# http://git.altlinux.org/people/alexey/packages/?p=python3-module-ax.git
Source: %{name}-%{version}.tar

BuildArch: noarch

BuildRequires: python3-devel
Requires: python3

%description
Python module with various helpfull features initially developed for
cve-manager project but potentially reusable elsewhere.

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
* Fri Jan 03 2020 Alexey Appolonov <alexey@altlinux.org> 0.5.0-alt1
- Functions for working with ranges of versions.

* Fri Dec 20 2019 Alexey Appolonov <alexey@altlinux.org> 0.4.0-alt1
- Optimized 'printer' module;
- Modified procedure of version comparisment.

* Fri Nov 29 2019 Alexey Appolonov <alexey@altlinux.org> 0.3.0-alt1
- New submodule named 'alt' that helps to work with ALT Linux repos;
- Enhancement of 'Printer' class;
- Couple of new functions - one checks existence/access of a file and other
  prettifies string representation of a number.

* Wed Nov 20 2019 Alexey Appolonov <alexey@altlinux.org> 0.2.0-alt1
- Couple of new functions - one for searching files and one for removing
  duplicates from a given list.

* Sat Nov 16 2019 Alexey Appolonov <alexey@altlinux.org> 0.1.0-alt1
- Initial release.
