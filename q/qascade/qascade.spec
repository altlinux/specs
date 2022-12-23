# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}

Name:           qascade
Version:        0.5
Release:        alt1
Summary:        Classic puzzle game

Group:          Games/Arcade
License:        GPLv2+
URL:            https://github.com/viy2/qascade
Source0:        %{name}-%{version}.tar

BuildRequires:  desktop-file-utils gcc-c++
BuildRequires:  qt5-base-devel

%description
Qascade is a port of the simple yet addictive and enjoyable puzzle
game that came with the Psion Revo PDA.

%prep
%setup -q

%build
qmake-qt5 INSTALL_ROOT=$RPM_BUILD_ROOT qascade.pro
%make_build

%install
%makeinstall
desktop-file-install \
  --dir $RPM_BUILD_ROOT%{_datadir}/applications \
  --mode 644 \
  %{name}.desktop
install -D -p -m 644 %{name}.hscr \
  $RPM_BUILD_ROOT%{_localstatedir}/lib/games/%{name}.hscr

install -D -p -m 644 icons/qascade16.png $RPM_BUILD_ROOT%{_miconsdir}/qascade.png
install -D -p -m 644 icons/qascade32.png $RPM_BUILD_ROOT%{_niconsdir}/qascade.png
install -D -p -m 644 icons/qascade48.png $RPM_BUILD_ROOT%{_liconsdir}/qascade.png

%files
%doc *.htm
%attr(2711,root,games) %{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/*/apps/qascade.png
%attr(0664,games,games) %config(noreplace) %{_localstatedir}/lib/games/%{name}*

%changelog
* Tue Dec 20 2022 Igor Vlasenko <viy@altlinux.org> 0.5-alt1
- new version: qt5/qt6 port

* Sat Feb 03 2018 Igor Vlasenko <viy@altlinux.ru> 0.1-alt2_26
- update to new release by fcimport
