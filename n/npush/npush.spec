# BEGIN SourceDeps(oneline):
BuildRequires: /usr/bin/desktop-file-install gcc-c++
# END SourceDeps(oneline)
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
Name:		npush
Version:	0.7
Release:	alt2_19
Summary:	A logic game similar to Sokoban

Group:		Games/Other
License:	GPLv2+
URL:		http://npush.sourceforge.net/
Source0:	http://downloads.sourceforge.net/%{name}/%{name}-%{version}.tgz
# patch npush.cpp to fix an issue with level path
Patch0:		npush-0.7-level.patch

BuildRequires:	libncurses++-devel libncurses-devel libncursesw-devel libtic-devel libtinfo-devel desktop-file-utils
Source44: import.info

%description
nPush is a logic game similar to Sokoban and Boulder Dash. 
You need to collect all the gold on the level and reach the exit. 
To make it hard there are some rocks that stand in your way,
and you also have some dynamite to blast them away. 
Main difference from Sokoban, KSokoban and similar games is that you 
can have multiple player-controlled characters you can move on the screen.

nPush is a terminal based application and uses nCurses library for 
user interface.


%prep
%setup -q
%patch0 -p0

# as-needed
sed -i -e 's,-lncurses -o $(PROGRAM) $(OBJECTS),-o $(PROGRAM) $(OBJECTS) -lncurses,' Makefile

%build

%make_build CFLAGS="${RPM_OPT_FLAGS}"


%install

mkdir -p  %{buildroot}%{_bindir}
install -p -m 755 npush %{buildroot}%{_bindir}/npush

mkdir -p %{buildroot}%{_datadir}/npush
cp -ra levels*  %{buildroot}%{_datadir}/npush

# desktop file stuff
desktop-file-install \
	--add-category="LogicGame" \
	--delete-original \
	--dir=$RPM_BUILD_ROOT%{_datadir}/applications \
	%{name}.desktop

# icon
mkdir -p $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/32x32/apps

install -p -m 0644 %{name}.png				\
	$RPM_BUILD_ROOT%{_datadir}/icons/hicolor/32x32/apps/%{name}.png


%files
%doc CHANGES COPYING CREDITS readme.txt
%{_bindir}/%{name}
%{_datadir}/%{name}
%{_datadir}/applications/*%{name}.desktop
%{_datadir}/icons/hicolor/*/apps/%{name}.png

%changelog
* Sat Feb 03 2018 Igor Vlasenko <viy@altlinux.ru> 0.7-alt2_19
- update to new release by fcimport

* Wed Sep 27 2017 Igor Vlasenko <viy@altlinux.ru> 0.7-alt2_18
- update to new release by fcimport

* Thu Mar 16 2017 Igor Vlasenko <viy@altlinux.ru> 0.7-alt2_16
- update to new release by fcimport

* Tue Feb 16 2016 Igor Vlasenko <viy@altlinux.ru> 0.7-alt2_15
- update to new release by fcimport

* Sun Sep 20 2015 Igor Vlasenko <viy@altlinux.ru> 0.7-alt2_14
- update to new release by fcimport

* Wed Aug 27 2014 Igor Vlasenko <viy@altlinux.ru> 0.7-alt2_12
- update to new release by fcimport

* Tue Jul 01 2014 Igor Vlasenko <viy@altlinux.ru> 0.7-alt2_11
- update to new release by fcimport

* Mon Aug 12 2013 Igor Vlasenko <viy@altlinux.ru> 0.7-alt2_10
- update to new release by fcimport

* Tue May 07 2013 Igor Vlasenko <viy@altlinux.ru> 0.7-alt2_9
- update to new release by fcimport

* Fri Feb 22 2013 Igor Vlasenko <viy@altlinux.ru> 0.7-alt2_8
- update to new release by fcimport

* Fri Jul 27 2012 Igor Vlasenko <viy@altlinux.ru> 0.7-alt2_7
- update to new release by fcimport

* Fri Mar 02 2012 Igor Vlasenko <viy@altlinux.ru> 0.7-alt2_6
- rebuild with fixed sourcedep analyser (#27020)

* Sat Jan 21 2012 Igor Vlasenko <viy@altlinux.ru> 0.7-alt1_6
- update to new release by fcimport

* Sat Jul 02 2011 Igor Vlasenko <viy@altlinux.ru> 0.7-alt1_5
- initial release by fcimport

