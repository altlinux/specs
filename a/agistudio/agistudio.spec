# BEGIN SourceDeps(oneline):
BuildRequires: gcc-c++
# END SourceDeps(oneline)
Name: agistudio
Version: 1.2.4
Release: alt2_6
Summary: AGI integrated development environment
License: GPLv2+
Group: Games/Other
Source0: http://downloads.sourceforge.net/%{name}/%{name}-%{version}.tar.gz
Source1: %{name}.desktop
#Patch0: agistudio-1.2.3-logdecode-stdlib.patch
#Patch1: agistudio-1.2.3-main-stdlib.patch
#Patch2: agistudio-1.2.3-picedit-stdlib.patch
#Patch3: agistudio-1.2.3-roomgen-stringh.patch
#Patch4: agistudio-1.2.3-util-stringh.patch
URL: http://agistudio.sourceforge.net/

BuildRequires: libqt3-devel desktop-file-utils
#Requiring nagi, needed at runtime, not picked up by rpm.
Requires: icon-theme-hicolor nagi libgtk+2
Source44: import.info

%description
AGI (Adventure Game Interpreter) is the adventure game engine used by
Sierra On-Line to create some of their early games. QT AGI Studio
is a program which allows you to view, create and edit AGI games.

%prep

%setup -q
#%patch0 -p0
#%patch1 -p0
#%patch2 -p0
#%patch3 -p0
#%patch4 -p0

%build
cd src
qmake-qt3
make RPM_OPT_FLAGS="$RPM_OPT_FLAGS"

%install
mkdir -p %{buildroot}%{_bindir}
mkdir -p %{buildroot}%{_datadir}/agistudio
install -m 755 src/agistudio %{buildroot}%{_bindir}
mkdir -p %{buildroot}%{_datadir}/agistudio/template
mkdir -p %{buildroot}%{_datadir}/agistudio/help
install -p -m 0644 help/* %{buildroot}%{_datadir}/agistudio/help
#install -p -Dm 0644 template/* %{buildroot}%{_datadir}/%{name}/template 
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
* Fri Mar 02 2012 Igor Vlasenko <viy@altlinux.ru> 1.2.4-alt2_6
- rebuild with fixed sourcedep analyser (#27020)

* Fri Jan 20 2012 Igor Vlasenko <viy@altlinux.ru> 1.2.4-alt1_6
- update to new release by fcimport

* Thu Jul 07 2011 Igor Vlasenko <viy@altlinux.ru> 1.2.4-alt1_5
- update to new release by fcimport

* Mon May 23 2011 Igor Vlasenko <viy@altlinux.ru> 1.2.4-alt1_4
- converted from Fedora by srpmconvert script

