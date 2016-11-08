# BEGIN SourceDeps(oneline):
BuildRequires: /usr/bin/desktop-file-install gcc-c++
# END SourceDeps(oneline)
Name:           hercstudio
Version:        1.5.0
Release:        alt2
Summary:        GUI front-end to the Hercules mainframe Emulator

Group:          Emulators
License:        GPLv3+
URL:            http://www.mvsdasd.org/hercstudio/
Source0:        http://www.mvsdasd.org/hercstudio/herculesstudio-%{version}-src.tar.gz
Source1:        %{name}.desktop
# make build verbose
Patch0:         herculesstudio-1.5.0-verbose-build.patch

BuildRequires:  pkgconfig(Qt5Widgets)
BuildRequires:  pkgconfig(Qt5Network)
BuildRequires:  desktop-file-utils
Requires:       hercules >= 3.06
Source44: import.info


%description
GUI front-end to the Hercules mainframe Emulator.


%prep
%setup -q -c
%patch0 -p1 -b .verbose-build


%build
%{qmake_qt5}
make %{?_smp_mflags}


%install
mkdir -p $RPM_BUILD_ROOT%{_bindir}
mkdir -p $RPM_BUILD_ROOT%{_datadir}/applications
mkdir -p $RPM_BUILD_ROOT%{_datadir}/pixmaps

install -p -m 755 HerculesStudio $RPM_BUILD_ROOT%{_bindir}
install -p -m 644 HercStudio/icons/tray.xpm $RPM_BUILD_ROOT%{_datadir}/pixmaps/hercstudio.xpm

desktop-file-install --dir $RPM_BUILD_ROOT%{_datadir}/applications %{SOURCE1}


%files
%doc COPYING
%{_bindir}/HerculesStudio
%{_datadir}/applications/*.desktop
%{_datadir}/pixmaps/*


%changelog
* Tue Nov 08 2016 Denis Medvedev <nbr@altlinux.org> 1.5.0-alt2
- Compile to Sisyphus

* Fri Sep 30 2016 Igor Vlasenko <viy@altlinux.ru> 1.5.0-alt1_7
- update to new release by fcimport

* Wed Mar 02 2016 Igor Vlasenko <viy@altlinux.ru> 1.5.0-alt1_6
- update to new release by fcimport

* Mon Sep 21 2015 Igor Vlasenko <viy@altlinux.ru> 1.5.0-alt1_4
- update to new release by fcimport

* Wed Sep 10 2014 Igor Vlasenko <viy@altlinux.ru> 1.5.0-alt1_2
- update to new release by fcimport

* Mon Jul 07 2014 Igor Vlasenko <viy@altlinux.ru> 1.4.0-alt1_4
- update to new release by fcimport

* Tue Aug 27 2013 Igor Vlasenko <viy@altlinux.ru> 1.4.0-alt1_3
- update to new release by fcimport

* Wed Mar 13 2013 Igor Vlasenko <viy@altlinux.ru> 1.4.0-alt1_2
- update to new release by fcimport

* Mon Jan 21 2013 Igor Vlasenko <viy@altlinux.ru> 1.4.0-alt1_1
- initial fc import

