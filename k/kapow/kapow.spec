%define _localstatedir %{_var}
Name:		kapow
Version:	1.6.1
Release:	alt1
Summary:	Punch clock
Group:		Office
License:	GPLv3+
URL:		https://gottcode.org/%{name}/
Source:		https://gottcode.org/%{name}/%{name}-%{version}.tar.bz2
Packager: Ilya Mashkin <oddity@altlinux.ru>
Source44: import.info
BuildRequires(pre): rpm-macros-cmake
BuildRequires: gcc-c++ cmake rpm-macros-qt6 qt6-base-devel qt6-tools-devel qt6-multimedia-devel qt6-declarative-devel qt6-5compat-devel libicu-devel


%description
A punch clock program designed to easily keep track of your hours,
whether you're working on one project or many. Simply clock in and
out with the Start/Stop button. If you make a mistake in your hours,
you can go back and edit any of the entries by double-clicking on
the session in question. Kapow also allows you to easily keep track
of the hours since you lasted billed a client, by providing a
helpful "Billed" check box--the totals will reflect your work
after the last billed session.

%prep
%setup -q

%build

%cmake 
%cmake_build

%install
%cmakeinstall_std

%files
%{_bindir}/%{name}
%{_datadir}/%{name}/
%{_datadir}/metainfo/%{name}.appdata.xml
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/*/apps/%{name}.png
%{_datadir}/icons/hicolor/scalable/apps/%{name}.svg
#{_datadir}/pixmaps/%{name}.xpm
%{_mandir}/man1/%{name}.1*


%changelog
* Thu Jan 12 2023 Ilya Mashkin <oddity@altlinux.ru> 1.6.1-alt1
- 1.6.1

* Wed Jul 13 2022 Ilya Mashkin <oddity@altlinux.ru> 1.6.0-alt1
- 1.6.0
- Build with qt6/cmake

* Tue Apr 12 2022 Cronbuild Service <cronbuild@altlinux.org> 1.5.10-alt1_3
- update by mgaimport

* Fri Dec 25 2020 Igor Vlasenko <viy@altlinux.ru> 1.5.10-alt1_2
- update by mgaimport

* Fri Jun 12 2020 Igor Vlasenko <viy@altlinux.ru> 1.5.10-alt1_1
- update by mgaimport

* Tue Mar 10 2020 Igor Vlasenko <viy@altlinux.ru> 1.5.9-alt1_2
- update by mgaimport

* Wed Sep 18 2019 Igor Vlasenko <viy@altlinux.ru> 1.5.9-alt1_1
- update by mgaimport

* Wed Apr 10 2019 Igor Vlasenko <viy@altlinux.ru> 1.5.8-alt1_3
- update by mgaimport

* Thu Oct 04 2018 Igor Vlasenko <viy@altlinux.ru> 1.5.8-alt1_2
- update by mgaimport

* Wed Aug 01 2018 Igor Vlasenko <viy@altlinux.ru> 1.5.8-alt1_1
- update by mgaimport

* Sat Jul 14 2018 Igor Vlasenko <viy@altlinux.ru> 1.5.7-alt1_1
- update by mgaimport

* Thu Jun 07 2018 Igor Vlasenko <viy@altlinux.ru> 1.5.6-alt1_1
- update by mgaimport

* Fri May 04 2018 Igor Vlasenko <viy@altlinux.ru> 1.5.5-alt1_1
- update by mgaimport

* Sun Mar 18 2018 Igor Vlasenko <viy@altlinux.ru> 1.5.4-alt1_1
- new version

