# BEGIN SourceDeps(oneline):
BuildRequires: /usr/bin/desktop-file-install gcc-c++
# END SourceDeps(oneline)
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
Name: agistudio
Version: 1.3.0
Release: alt1_15
Summary: AGI integrated development environment
License: GPLv2+
Group: Games/Other
Source0: http://downloads.sourceforge.net/%{name}/%{name}-%{version}.tar.gz
Source1: %{name}.desktop
Patch0: agistudio-1.3.0-format.patch
URL: http://agistudio.sourceforge.net/

BuildRequires: libqt4-declarative libqt4-devel libqt5-declarative qt4-designer qt5-designer qt5-tools qt5-xmlpatterns-devel desktop-file-utils
#Requiring nagi, needed at runtime, not picked up by rpm.
Requires: icon-theme-hicolor, nagi libgail libgtk+2
Source44: import.info

%description
AGI (Adventure Game Interpreter) is the adventure game engine used by
Sierra On-Line to create some of their early games. QT AGI Studio
is a program which allows you to view, create and edit AGI games.

%prep

%setup -q

%patch0 -p0

%build
CXXFLAGS="$RPM_OPT_FLAGS $CXXFLAGS -std=gnu++98 -fPIC"
export CXXFLAGS
cd src
%{qmake_qt4}
make RPM_OPT_FLAGS="$RPM_OPT_FLAGS"

%install
mkdir -p %{buildroot}%{_bindir}
mkdir -p %{buildroot}%{_datadir}/agistudio
install -m 755 src/agistudio %{buildroot}%{_bindir}
mkdir -p %{buildroot}%{_datadir}/agistudio/template
mkdir -p %{buildroot}%{_datadir}/agistudio/help
install -p -m 0644 help/* %{buildroot}%{_datadir}/agistudio/help
cp -pr template/* %{buildroot}%{_datadir}/%{name}/template 

# icon
install -d %{buildroot}%{_datadir}/icons/hicolor/32x32/apps
install -p -m 0644  src/app_icon.xpm %{buildroot}%{_datadir}/icons/hicolor/32x32/apps/%{name}.xpm

# desktop file
desktop-file-install  \
        --dir $RPM_BUILD_ROOT%{_datadir}/applications \
        %{SOURCE1}

%files
%doc COPYING README relnotes help/*
%{_bindir}/agistudio
%{_datadir}/agistudio/
%{_datadir}/applications/agistudio.desktop
%{_datadir}/icons/hicolor/32x32/apps/agistudio.xpm

%changelog
* Sat Feb 03 2018 Igor Vlasenko <viy@altlinux.ru> 1.3.0-alt1_15
- update to new release by fcimport

* Wed Sep 27 2017 Igor Vlasenko <viy@altlinux.ru> 1.3.0-alt1_14
- update to new release by fcimport

* Thu Mar 16 2017 Igor Vlasenko <viy@altlinux.ru> 1.3.0-alt1_11
- update to new release by fcimport

* Tue Mar 29 2016 Igor Vlasenko <viy@altlinux.ru> 1.3.0-alt1_10
- update to new release by fcimport

* Sun Sep 20 2015 Igor Vlasenko <viy@altlinux.ru> 1.3.0-alt1_6
- update to new release by fcimport

* Wed Aug 27 2014 Igor Vlasenko <viy@altlinux.ru> 1.3.0-alt1_4
- update to new release by fcimport

* Tue Jul 01 2014 Igor Vlasenko <viy@altlinux.ru> 1.3.0-alt1_3
- update to new release by fcimport

* Mon Aug 12 2013 Igor Vlasenko <viy@altlinux.ru> 1.3.0-alt1_2
- update to new release by fcimport

* Tue Apr 09 2013 Igor Vlasenko <viy@altlinux.ru> 1.3.0-alt1_1
- update to new release by fcimport

* Mon Feb 11 2013 Igor Vlasenko <viy@altlinux.ru> 1.2.4-alt2_8
- update to new release by fcimport

* Fri Jul 27 2012 Igor Vlasenko <viy@altlinux.ru> 1.2.4-alt2_7
- update to new release by fcimport

* Fri Mar 02 2012 Igor Vlasenko <viy@altlinux.ru> 1.2.4-alt2_6
- rebuild with fixed sourcedep analyser (#27020)

* Fri Jan 20 2012 Igor Vlasenko <viy@altlinux.ru> 1.2.4-alt1_6
- update to new release by fcimport

* Thu Jul 07 2011 Igor Vlasenko <viy@altlinux.ru> 1.2.4-alt1_5
- update to new release by fcimport

* Mon May 23 2011 Igor Vlasenko <viy@altlinux.ru> 1.2.4-alt1_4
- converted from Fedora by srpmconvert script

