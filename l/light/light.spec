Group: Other
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
Name:       light
Version:    1.2.2
Release:    alt1_10
Summary:    Control backlight controllers

License:    GPL-3.0-only
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
%add_optflags -fcommon
%global build_cflags %{optflags} -fcommon
./autogen.sh
%configure
%make_build


%install
%makeinstall_std


%post
if [ -e "%{_sysconfdir}/%{name}" ]; then
    chown -R :root %{_sysconfdir}/%{name}
fi


%files
%doc COPYING
%doc ChangeLog.md
%doc README.md
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1*


%changelog
* Tue Oct 10 2023 Igor Vlasenko <viy@altlinux.org> 1.2.2-alt1_10
- update to new release by fcimport

* Fri Dec 11 2020 Igor Vlasenko <viy@altlinux.ru> 1.2.2-alt1_3
- fixed build

* Thu Apr 02 2020 Igor Vlasenko <viy@altlinux.ru> 1.2.2-alt1_2
- update to new release by fcimport

* Tue Mar 24 2020 Igor Vlasenko <viy@altlinux.ru> 1.2.2-alt1_1
- update to new release by fcimport

* Tue Feb 25 2020 Igor Vlasenko <viy@altlinux.ru> 1.2.1-alt1_3
- update to new release by fcimport

* Wed Nov 20 2019 Igor Vlasenko <viy@altlinux.ru> 1.2.1-alt1_1
- update to new release by fcimport

* Mon Sep 30 2019 Igor Vlasenko <viy@altlinux.ru> 1.1.2-alt1_4
- new version

