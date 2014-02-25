# BEGIN SourceDeps(oneline):
BuildRequires: /usr/bin/update-desktop-database
# END SourceDeps(oneline)
Name:           garden
Version:        1.0.8
Release:        alt2_10
Summary:        An innovative old-school 2D vertical shoot-em-up

Group:          Games/Other
License:        GPLv3+
URL:            http://garden.sourceforge.net/
Source0:        http://downloads.sourceforge.net/%{name}/%{name}-%{version}.tar.gz
Patch0:         garden-dso.patch
Patch1:         garden-printf-format.patch

BuildRequires:  liballegro-devel
BuildRequires:  desktop-file-utils
BuildRequires:  automake
BuildRequires:  autoconf
BuildRequires:  libtool
Requires:       liballegro4.4
Source44: import.info

%description
Garden of colored lights is an old school 2D vertical shoot-em-up with some
innovative elements. Innovative graphics, soundtrack and game concept. The
game itself is very challenging and as you progress, you will understand that
you are dealing with a true piece of art...

%prep
%setup -q

# patch for DSO-linking
# https://sourceforge.net/tracker/?func=detail&aid=2982590&group_id=242667&atid=1121672
%patch0 -p1 -b .dso
%patch1 -p0 -b .format

%build
autoreconf -if
%configure 
make %{?_smp_mflags}


%install
make install DESTDIR=$RPM_BUILD_ROOT

desktop-file-validate \
%{buildroot}%{_datadir}/applications/%{name}.desktop

%files
%doc README NEWS AUTHORS ChangeLog COPYING
%{_bindir}/%{name}
%{_datadir}/%{name}/
%{_datadir}/icons/hicolor/scalable/apps/%{name}.svg
%{_datadir}/applications/%{name}.desktop

%changelog
* Tue Feb 25 2014 Igor Vlasenko <viy@altlinux.ru> 1.0.8-alt2_10
- update to new release by fcimport

* Mon Aug 12 2013 Igor Vlasenko <viy@altlinux.ru> 1.0.8-alt2_8
- update to new release by fcimport

* Fri Feb 22 2013 Igor Vlasenko <viy@altlinux.ru> 1.0.8-alt2_7
- update to new release by fcimport

* Fri Jul 27 2012 Igor Vlasenko <viy@altlinux.ru> 1.0.8-alt2_6
- update to new release by fcimport

* Fri Mar 02 2012 Igor Vlasenko <viy@altlinux.ru> 1.0.8-alt2_5
- rebuild with fixed sourcedep analyser (#27020)

* Wed Feb 01 2012 Igor Vlasenko <viy@altlinux.ru> 1.0.8-alt1_5
- update to new release by fcimport

* Mon Oct 17 2011 Igor Vlasenko <viy@altlinux.ru> 1.0.8-alt1_4
- update to new release by fcimport

* Fri Jul 01 2011 Igor Vlasenko <viy@altlinux.ru> 1.0.8-alt1_3
- initial release by fcimport

