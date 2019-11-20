Group: Other
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
Name:       light
Version:    1.2.1
Release:    alt1_1
Summary:    Control backlight controllers

License:    GPLv3
URL:        http://haikarainen.github.io/light/
Source0:    https://github.com/haikarainen/%{name}/archive/v%{version}/%{name}-%{version}.tar.gz

BuildRequires:  gcc
BuildRequires: help2man
BuildRequires: automake
Source44: import.info


%description
Light is a program to control backlight controllers under GNU/Linux,
it is the successor of lightscript, which was a bash script
with the same purpose, and tries to maintain the same functionality.

Features

- Works excellent where other software have been proven unusable
  or problematic, thanks to how it operates internally
  and the fact that it does not rely on X.
- Can automatically figure out the best controller to use,
  making full use of underlying hardware.
- Possibility to set a minimum brightness value, as some controllers
  set the screen to be pitch black at a value of 0 (or higher).


%prep
%setup -q


%build
./autogen.sh
%configure
%make_build


%install
%makeinstall_std


%files
%doc COPYING
%doc ChangeLog.md
%doc README.md
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1*


%changelog
* Wed Nov 20 2019 Igor Vlasenko <viy@altlinux.ru> 1.2.1-alt1_1
- update to new release by fcimport

* Mon Sep 30 2019 Igor Vlasenko <viy@altlinux.ru> 1.1.2-alt1_4
- new version

