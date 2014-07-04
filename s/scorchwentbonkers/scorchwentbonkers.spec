# BEGIN SourceDeps(oneline):
BuildRequires: gcc-c++
# END SourceDeps(oneline)
%define fedora 21
Name:           scorchwentbonkers
Version:        1.1
Release:        alt2_16
Summary:        Realtime remake of Scorched Earth
Group:          Games/Other
License:        zlib
URL:            http://www.allegro.cc/depot/ScorchWentBonkers
# should be
# http://www.allegro.cc/files/depot/537/%{name}-src-%{version}.tar.gz
# but that is powered by a script which breaks every other day.
Source0:        %{name}-src-%{version}.tar.gz
Source1:        %{name}.desktop
Source2:        %{name}.png
Patch0:         %{name}-no-fmod.patch
Patch1:         %{name}-support-16bpp.patch
Patch2:         %{name}-unixify.patch
Patch3:         %{name}-fullscreen.patch
Patch4:         %{name}-divbyzero.patch
Patch5:         %{name}-1.1-al-4.4.patch
BuildRequires:  liballegro-devel liballegro-devel dumb-devel AllegroOGG-devel
BuildRequires:  libGLU-devel desktop-file-utils
Requires:       icon-theme-hicolor
Source44: import.info

%description
As the name suggests, Scorch Went Bonkers is a remake of the old PC classic.
However, many things were changed and the type of fun delivered by the game is
different. Where Scorched Earth puts emphasis on tactics and careful
calculations, SWB requires quick thinking, perfect timing and only one finger
for controlling your tank. The game is real-time instead of turn based.


%prep
%setup -q -c
%patch0 -p1 -z .no-fmod
%patch1 -p1 -z .16bpp
%patch2 -p1 -z .unix
%patch3 -p1 -z .fs
%patch4 -p1 -z .dbz
%patch5 -p1
sed -i 's/\r//' doc/readme.htm


%build
make %{?_smp_mflags} -f Makefile.linux PREFIX=%{_prefix} \
  OPTFLAGS="$RPM_OPT_FLAGS -fsigned-char -Wno-non-virtual-dtor"


%install
make -f Makefile.linux install PREFIX=$RPM_BUILD_ROOT%{_prefix}

# below is the desktop file and icon stuff.
mkdir -p $RPM_BUILD_ROOT%{_datadir}/applications
desktop-file-install \
%if 0%{?fedora} && 0%{?fedora} < 19
              \
%endif
  --dir $RPM_BUILD_ROOT%{_datadir}/applications \
  %{SOURCE1}
mkdir -p $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/32x32/apps
install -p -m 644 %{SOURCE2} \
  $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/32x32/apps


%files
%doc README doc/readme.htm
%{_bindir}/swb
%{_datadir}/swb
%if 0%{?fedora} && 0%{?fedora} < 19
%{_datadir}/applications/%{name}.desktop
%else
%{_datadir}/applications/%{name}.desktop
%endif
%{_datadir}/icons/hicolor/32x32/apps/%{name}.png


%changelog
* Tue Jul 01 2014 Igor Vlasenko <viy@altlinux.ru> 1.1-alt2_16
- update to new release by fcimport

* Mon Aug 12 2013 Igor Vlasenko <viy@altlinux.ru> 1.1-alt2_15
- update to new release by fcimport

* Tue Feb 26 2013 Igor Vlasenko <viy@altlinux.ru> 1.1-alt2_14
- update to new release by fcimport

* Fri Feb 22 2013 Igor Vlasenko <viy@altlinux.ru> 1.1-alt2_13
- update to new release by fcimport

* Fri Jul 27 2012 Igor Vlasenko <viy@altlinux.ru> 1.1-alt2_12
- update to new release by fcimport

* Fri Mar 02 2012 Igor Vlasenko <viy@altlinux.ru> 1.1-alt2_11
- rebuild with fixed sourcedep analyser (#27020)

* Sat Jan 21 2012 Igor Vlasenko <viy@altlinux.ru> 1.1-alt1_11
- update to new release by fcimport

* Wed Jul 20 2011 Igor Vlasenko <viy@altlinux.ru> 1.1-alt1_10
- initial release by fcimport

