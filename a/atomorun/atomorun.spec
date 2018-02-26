# BEGIN SourceDeps(oneline):
BuildRequires: libGL-devel libGLU-devel libSDL-devel
# END SourceDeps(oneline)
%define prever pre2

Name:           atomorun
Version:        1.1
Release:        alt5_0.12.pre2
Summary:        Jump&Run game where you have to flee an exploding nuclear bomb
Group:          Games/Other
License:        GPL+
URL:            http://atomorun.whosme.de/index.php
# the file seems to be gone from upstreams server so no URL
Source0:        %{name}-%{version}_%{prever}.tar.gz
Source1:        atomorun.desktop
Patch0:         atomorun-1.1-missing-protos.patch
BuildRequires:  libSDL_mixer-devel libSDL_image-devel libtiffxx-devel libtiff-devel libvorbis-devel
BuildRequires:  libalsa-devel desktop-file-utils
Requires:       icon-theme-hicolor
Source44: import.info

%description
Atomorun is a OpenGL Jump&Run game where you have to flee an exploding
nuclear bomb.


%prep
%setup -q -n %{name}-%{version}_%{prever}
%patch0 -p1


%build
%configure
make %{?_smp_mflags}


%install
make install DESTDIR=$RPM_BUILD_ROOT
rm $RPM_BUILD_ROOT%{_datadir}/%{name}/pixmaps/atomorun_winicon.ico
rm -rf $RPM_BUILD_ROOT%{_prefix}/doc/%{name}

# below is the desktop file and icon stuff.
mkdir -p $RPM_BUILD_ROOT%{_datadir}/applications
desktop-file-install             \
  --dir $RPM_BUILD_ROOT%{_datadir}/applications \
  %{SOURCE1}
mkdir -p $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/48x48/apps
install -p -m 644 pixmaps/%{name}_icon.png \
  $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/48x48/apps/%{name}.png


%files
%doc AUTHORS ChangeLog COPYING README TODO
%{_bindir}/%{name}
%{_datadir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/48x48/apps/%{name}.png


%changelog
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

