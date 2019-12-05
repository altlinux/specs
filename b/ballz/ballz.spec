Group: Games/Other
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-fedora-compat
BuildRequires: /usr/bin/desktop-file-validate
# END SourceDeps(oneline)
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
Name:           ballz
Version:        1.0.4
Release:        alt1_2
Summary:        B.A.L.L.Z. - platform/puzzle game where you control a rolling ball
License:        BSD
URL:            https://gitlab.com/groups/ballz
Source0:        %{name}-%{version}.tar.gz
BuildRequires:  gcc-c++
BuildRequires:  gcc
BuildRequires:  liballegro-devel dumb-devel libguichan-devel intltool
# https://docs.fedoraproject.org/en-US/packaging-guidelines/#_desktop_files
BuildRequires:  desktop-file-utils
# https://docs.fedoraproject.org/en-US/packaging-guidelines/AppData/
BuildRequires:  libappstream-glib
Source44: import.info

%description
The game is a platformer with some puzzle elements. You take control
of a ball which is genetically modified by the British secret
service. Your mission is to rescue captured British soldiers from a
prison in Iran.

The game was written in 72 hours for the TINS competition, a
competition similar to Speedhack. The name TINS is an recursive
acronym for 'TINS is not Speedhack'.


%prep
%setup -q


%build
export LDFLAGS="$LDFLAGS -Wl,--no-as-needed"
%add_optflags -DALLEGRO_NO_FIX_ALIASES
%configure
%make_build


%install
%makeinstall_std
%find_lang %{name}
desktop-file-validate %{buildroot}/%{_datadir}/applications/%{name}.desktop
appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/*.appdata.xml

%files -f %{name}.lang
%doc AUTHORS README BSD-license ChangeLog
%{_bindir}/%{name}
%{_datadir}/%{name}
%{_datadir}/metainfo/*.appdata.xml
%{_datadir}/applications/*
%{_datadir}/icons/hicolor/256x256/apps/*
%{_mandir}/man6/*


%changelog
* Thu Dec 05 2019 Igor Vlasenko <viy@altlinux.ru> 1.0.4-alt1_2
- fixed build

* Fri Mar 15 2019 Igor Vlasenko <viy@altlinux.ru> 1.0.4-alt1_1
- update to new release by fcimport

* Wed Sep 27 2017 Igor Vlasenko <viy@altlinux.ru> 1.0.3-alt1_5
- update to new release by fcimport

* Thu Mar 16 2017 Igor Vlasenko <viy@altlinux.ru> 1.0.3-alt1_3
- update to new release by fcimport

* Mon Feb 15 2016 Igor Vlasenko <viy@altlinux.ru> 1.0.3-alt1_2
- update to new release by fcimport

* Sun Sep 20 2015 Igor Vlasenko <viy@altlinux.ru> 1.0.3-alt1_1
- update to new release by fcimport

* Wed Jun 10 2015 Gleb F-Malinovskiy <glebfm@altlinux.org> 1.0.2-alt2_13.1
- Rebuilt for gcc5 C++11 ABI.

* Tue Apr 07 2015 Igor Vlasenko <viy@altlinux.ru> 1.0.2-alt2_13
- update to new release by fcimport

* Wed Aug 27 2014 Igor Vlasenko <viy@altlinux.ru> 1.0.2-alt2_12
- update to new release by fcimport

* Tue Jul 01 2014 Igor Vlasenko <viy@altlinux.ru> 1.0.2-alt2_11
- update to new release by fcimport

* Mon Aug 12 2013 Igor Vlasenko <viy@altlinux.ru> 1.0.2-alt2_10
- update to new release by fcimport

* Mon May 13 2013 Igor Vlasenko <viy@altlinux.ru> 1.0.2-alt2_9
- update to new release by fcimport

* Fri Feb 22 2013 Igor Vlasenko <viy@altlinux.ru> 1.0.2-alt2_7
- update to new release by fcimport

* Fri Jul 27 2012 Igor Vlasenko <viy@altlinux.ru> 1.0.2-alt2_6
- update to new release by fcimport

* Wed May 09 2012 Igor Vlasenko <viy@altlinux.ru> 1.0.2-alt2_5
- update to new release by fcimport

* Fri Mar 02 2012 Igor Vlasenko <viy@altlinux.ru> 1.0.2-alt2_3
- rebuild with fixed sourcedep analyser (#27020)

* Sat Jan 21 2012 Igor Vlasenko <viy@altlinux.ru> 1.0.2-alt1_3
- update to new release by fcimport

* Thu Jul 28 2011 Igor Vlasenko <viy@altlinux.ru> 1.0.2-alt1_2
- update to new release by fcimport

* Fri Jul 01 2011 Igor Vlasenko <viy@altlinux.ru> 1.0.1-alt1_5
- initial release by fcimport

