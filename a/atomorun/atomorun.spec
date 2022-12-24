Group: Games/Other
# BEGIN SourceDeps(oneline):
BuildRequires: /usr/bin/desktop-file-install libGLU-devel libSDL-devel libglvnd-devel
# END SourceDeps(oneline)
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
%define prever pre2

Name:           atomorun
Version:        1.1
Release:        alt5_0.38.%{prever}
Summary:        Jump & Run game where you have to flee an exploding nuclear bomb
License:        GPL+
URL:            http://atomorun.whosme.de/index.php
# the file seems to be gone from upstreams server so no URL
Source0:        %{name}-%{version}_%{prever}.tar.gz
Source1:        %{name}.desktop
Source2:        %{name}.png
Source3:        %{name}.appdata.xml
Patch0:         atomorun-1.1-missing-protos.patch
Patch1:         atomorun-1.1-fcommon-fix.patch
Patch2:         atomorun-1.1-warnings-fix.patch
Patch3:         atomorun-1.1-configure-c99.patch
BuildRequires:  gcc
BuildRequires:  libSDL_mixer-devel libSDL_image-devel libtiff-devel libtiffxx-devel libvorbis-devel
BuildRequires:  libalsa-devel desktop-file-utils libappstream-glib libappstream-glib-gir
Requires:       icon-theme-hicolor
Source44: import.info

%description
Atomorun is a OpenGL Jump&Run game where you have to flee an exploding
nuclear bomb.


%prep
%setup -q -n %{name}-%{version}_%{prever}
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1



%build
export CFLAGS="$RPM_OPT_FLAGS -Wno-pointer-sign"
%configure
%make_build


%install
%makeinstall_std
rm $RPM_BUILD_ROOT%{_datadir}/%{name}/pixmaps/atomorun_winicon.ico
rm -rf $RPM_BUILD_ROOT%{_prefix}/doc/%{name}

mkdir -p $RPM_BUILD_ROOT%{_datadir}/applications
desktop-file-install --dir $RPM_BUILD_ROOT%{_datadir}/applications %{SOURCE1}
mkdir -p $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/48x48/apps
install -p -m 644 pixmaps/%{name}_icon.png \
  $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/48x48/apps/%{name}.png
mkdir -p $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/128x128/apps
install -p -m 644 %{SOURCE2} \
  $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/128x128/apps
mkdir -p $RPM_BUILD_ROOT%{_datadir}/appdata
install -p -m 644 %{SOURCE3} $RPM_BUILD_ROOT%{_datadir}/appdata
appstream-util validate-relax --nonet \
  $RPM_BUILD_ROOT%{_datadir}/appdata/%{name}.appdata.xml


%files
%doc AUTHORS ChangeLog COPYING README TODO
%{_bindir}/%{name}
%{_datadir}/%{name}
%{_datadir}/appdata/%{name}.appdata.xml
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/*/apps/%{name}.png


%changelog
* Sat Dec 24 2022 Igor Vlasenko <viy@altlinux.org> 1.1-alt5_0.38.pre2
- update to new release by fcimport

* Tue Mar 24 2020 Igor Vlasenko <viy@altlinux.ru> 1.1-alt5_0.32.pre2
- update to new release by fcimport

* Tue Feb 25 2020 Igor Vlasenko <viy@altlinux.ru> 1.1-alt5_0.31.pre2
- update to new release by fcimport

* Sat Feb 03 2018 Igor Vlasenko <viy@altlinux.ru> 1.1-alt5_0.25.pre2
- update to new release by fcimport

* Wed Sep 27 2017 Igor Vlasenko <viy@altlinux.ru> 1.1-alt5_0.24.pre2
- update to new release by fcimport

* Thu Mar 16 2017 Igor Vlasenko <viy@altlinux.ru> 1.1-alt5_0.22.pre2
- update to new release by fcimport

* Mon Feb 15 2016 Igor Vlasenko <viy@altlinux.ru> 1.1-alt5_0.21.pre2
- update to new release by fcimport

* Sun Sep 20 2015 Igor Vlasenko <viy@altlinux.ru> 1.1-alt5_0.20.pre2
- update to new release by fcimport

* Wed Aug 27 2014 Igor Vlasenko <viy@altlinux.ru> 1.1-alt5_0.19.pre2
- update to new release by fcimport

* Tue Jul 01 2014 Igor Vlasenko <viy@altlinux.ru> 1.1-alt5_0.18.pre2
- update to new release by fcimport

* Mon Aug 12 2013 Igor Vlasenko <viy@altlinux.ru> 1.1-alt5_0.17.pre2
- update to new release by fcimport

* Mon May 13 2013 Igor Vlasenko <viy@altlinux.ru> 1.1-alt5_0.16.pre2
- update to new release by fcimport

* Sat May 04 2013 Igor Vlasenko <viy@altlinux.ru> 1.1-alt5_0.15.pre2
- update to new release by fcimport

* Fri Feb 15 2013 Igor Vlasenko <viy@altlinux.ru> 1.1-alt5_0.14.pre2
- update to new release by fcimport

* Fri Jul 27 2012 Igor Vlasenko <viy@altlinux.ru> 1.1-alt5_0.13.pre2
- update to new release by fcimport

* Fri Mar 02 2012 Igor Vlasenko <viy@altlinux.ru> 1.1-alt5_0.12.pre2
- rebuild with fixed sourcedep analyser (#27020)

* Fri Jan 20 2012 Igor Vlasenko <viy@altlinux.ru> 1.1-alt4_0.12.pre2
- update to new release by fcimport

* Sat May 21 2011 Igor Vlasenko <viy@altlinux.ru> 1.1-alt4_0.11.pre2
- rebuild to fix .desktop permissions

* Thu May 19 2011 Igor Vlasenko <viy@altlinux.ru> 1.1-alt3_0.11.pre2
- rebuild with new rpm desktop cleaner

* Mon Feb 28 2011 Igor Vlasenko <viy@altlinux.ru> 1.1-alt2_0.11.pre2
- spec sleanup

* Wed Feb 16 2011 Igor Vlasenko <viy@altlinux.ru> 1.1-alt1_0.11.pre2
- converted from Fedora by srpmconvert script

