# BEGIN SourceDeps(oneline):
BuildRequires: /usr/bin/desktop-file-install gcc-c++ imake libGL-devel libGLU-devel libSDL-devel libXext-devel libXt-devel libogg-devel perl(Cwd.pm) perl(Digest/MD5.pm) perl(DirHandle.pm) xorg-cf-files
# END SourceDeps(oneline)
%define fedora 27
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
Summary:        Action game in four spatial dimensions
Name:           adanaxisgpl
Version:        1.2.5
Release:        alt4_28
License:        GPLv2
Group:          Games/Other
URL:            http://www.mushware.com/
Source0:        http://www.mushware.com/files/%{name}-1.2.5.tar.gz
Patch0:         adanaxisgpl-1.2.5-const.patch
Patch1:         adanaxisgpl-1.2.5-gcc47.patch
Patch2:         adanaxisgpl-1.2.5-xdg-open.patch
BuildRequires:  desktop-file-utils
BuildRequires:  libfreeglut-devel
BuildRequires:  libexpat-devel
BuildRequires:  libjpeg-devel
BuildRequires:  libtiff-devel libtiffxx-devel
BuildRequires:  libvorbis-devel
BuildRequires:  libpcre-devel libpcrecpp-devel
BuildRequires:  libSDL_mixer-devel
Source44: import.info
Patch33: adanaxisgpl-1.2.5-alt-nomessages.patch

%description
Adanaxis is a fast-moving first person shooter set in deep space, where the
fundamentals of space itself are changed.  By adding another dimension to
space this game provides an environment with movement in four directions
and six planes of rotation.  Initially the game explains the 4D control
system via a graphical sequence, before moving on to 30 levels of gameplay
with numerous enemy, ally, weapon and mission types.  Features include
simulated 4D texturing, mouse and joystick control, and original music.
Screenshots, movies and further information are available at
http://www.mushware.com/.

Hardware-accelerated 3D is recommended, ideally with support for OpenGL
Shading Language.


%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch33 -p0


%build
%configure
%make_build

# Build .desktop files
cat > %{name}.desktop <<EOF
[Desktop Entry]
Name=Adanaxis GPL
Comment=An action game in four spatial dimensions
Exec=%{name} 
Icon=%{name}
Terminal=false
Type=Application
StartupNotify=false
Categories=Game;ActionGame;
EOF


%install
%makeinstall_std INSTALL="install -p" CPPROG="cp -p"

# Install desktop files
mkdir -p %{buildroot}%{_datadir}/applications
desktop-file-install                           \
  --dir %{buildroot}%{_datadir}/applications   \
%if 0%{?fedora} && 0%{?fedora} < 19
 --vendor=mushware                             \
%endif
  %{name}.desktop

# Icons
mkdir -p -m 755 %{buildroot}%{_datadir}/icons/hicolor/16x16/apps
mkdir -p -m 755 %{buildroot}%{_datadir}/icons/hicolor/32x32/apps
mkdir -p -m 755 %{buildroot}%{_datadir}/icons/hicolor/48x48/apps
install -p -m 644 x11/icons/%{name}-16.png %{buildroot}%{_datadir}/icons/hicolor/16x16/apps/%{name}.png
install -p -m 644 x11/icons/%{name}-32.png %{buildroot}%{_datadir}/icons/hicolor/32x32/apps/%{name}.png
install -p -m 644 x11/icons/%{name}-48.png %{buildroot}%{_datadir}/icons/hicolor/48x48/apps/%{name}.png


%files
%doc COPYING README ChangeLog AUTHORS
%{_bindir}/%{name}
%{_datadir}/%{name}
%{_datadir}/applications/*%{name}.desktop
%{_datadir}/icons/hicolor/16x16/apps/%{name}.png
%{_datadir}/icons/hicolor/32x32/apps/%{name}.png
%{_datadir}/icons/hicolor/48x48/apps/%{name}.png
%{_mandir}/man6/%{name}*.6*


%changelog
* Sat Feb 03 2018 Igor Vlasenko <viy@altlinux.ru> 1.2.5-alt4_28
- update to new release by fcimport

* Wed Sep 27 2017 Igor Vlasenko <viy@altlinux.ru> 1.2.5-alt4_26
- update to new release by fcimport

* Thu Aug 03 2017 Igor Vlasenko <viy@altlinux.ru> 1.2.5-alt4_24
- update to new release by fcimport

* Thu Mar 16 2017 Igor Vlasenko <viy@altlinux.ru> 1.2.5-alt4_23
- update to new release by fcimport

* Mon Feb 15 2016 Igor Vlasenko <viy@altlinux.ru> 1.2.5-alt4_22
- update to new release by fcimport

* Sun Sep 20 2015 Igor Vlasenko <viy@altlinux.ru> 1.2.5-alt4_21
- update to new release by fcimport

* Wed Aug 27 2014 Igor Vlasenko <viy@altlinux.ru> 1.2.5-alt4_19
- update to new release by fcimport

* Tue Jul 01 2014 Igor Vlasenko <viy@altlinux.ru> 1.2.5-alt4_18
- update to new release by fcimport

* Mon Aug 12 2013 Igor Vlasenko <viy@altlinux.ru> 1.2.5-alt4_17
- update to new release by fcimport

* Mon May 13 2013 Igor Vlasenko <viy@altlinux.ru> 1.2.5-alt4_16
- update to new release by fcimport

* Sat May 04 2013 Igor Vlasenko <viy@altlinux.ru> 1.2.5-alt4_15
- update to new release by fcimport

* Fri Feb 22 2013 Igor Vlasenko <viy@altlinux.ru> 1.2.5-alt4_14
- update to new release by fcimport

* Wed Jan 23 2013 Igor Vlasenko <viy@altlinux.ru> 1.2.5-alt4_13
- update to new release by fcimport

* Wed Dec 26 2012 Igor Vlasenko <viy@altlinux.ru> 1.2.5-alt4_12
- update to new release by fcimport

* Thu Oct 04 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.2.5-alt4_11.1
- Rebuilt with libtiff5

* Fri Jul 27 2012 Igor Vlasenko <viy@altlinux.ru> 1.2.5-alt4_11
- update to new release by fcimport

* Fri Mar 02 2012 Igor Vlasenko <viy@altlinux.ru> 1.2.5-alt4_10
- rebuild with fixed sourcedep analyser (#27020)

* Tue Feb 21 2012 Igor Vlasenko <viy@altlinux.ru> 1.2.5-alt3_10
- update to new release by fcimport

* Mon Jan 16 2012 Igor Vlasenko <viy@altlinux.ru> 1.2.5-alt3_8
- update to new release by fcimport

* Mon Oct 31 2011 Igor Vlasenko <viy@altlinux.ru> 1.2.5-alt3_6
- bugfix release

* Mon Feb 28 2011 Igor Vlasenko <viy@altlinux.ru> 1.2.5-alt2_6
- spec sleanup

* Wed Feb 16 2011 Igor Vlasenko <viy@altlinux.ru> 1.2.5-alt1_6
- converted from Fedora by srpmconvert script

