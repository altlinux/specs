# BEGIN SourceDeps(oneline):
BuildRequires: /usr/bin/find /usr/bin/sdl-config gcc-c++ libGL-devel libGLU-devel libICE-devel libSDL-devel libSM-devel libXext-devel libogg-devel
# END SourceDeps(oneline)
Summary:        Action game in four spatial dimensions
Name:           adanaxisgpl
Version:        1.2.5
Release:        alt4_10
License:        GPLv2
Group:          Games/Other
URL:            http://www.mushware.com/
Source0:        http://www.mushware.com/files/%{name}-1.2.5.tar.gz
Patch0:         adanaxisgpl-1.2.5-const.patch
Patch1:         adanaxisgpl-1.2.5-gcc47.patch
BuildRequires:  desktop-file-utils
BuildRequires:  libfreeglut-devel
BuildRequires:  libexpat-devel
BuildRequires:  libjpeg-devel
BuildRequires:  libtiffxx-devel libtiff-devel
BuildRequires:  libvorbis-devel
BuildRequires:  libpcre-devel
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
%patch33 -p0


%build
%configure
make %{?_smp_mflags}

# Build .desktop files
cat > %{name}.desktop <<EOF
[Desktop Entry]
Encoding=UTF-8
Name=Adanaxis GPL
Comment=An action game in four spatial dimensions
Exec=%{_bindir}/%{name} 
Icon=%{name}
Terminal=false
Type=Application
StartupNotify=false
Categories=Game;ActionGame;
EOF

cat > %{name}-recover.desktop <<EOF
[Desktop Entry]
Name=Adanaxis GPL (Recovery Mode)
Comment=An action game in four spatial dimensions (Launch in Recovery Mode)
Exec=%{_bindir}/%{name} --recover
Icon=%{name}
Terminal=false
Type=Application
StartupNotify=false
Categories=Game;ActionGame;
EOF


%install
make DESTDIR=%{buildroot} INSTALL="install -p" CPPROG="cp -p" install

# Install desktop files
mkdir -p %{buildroot}%{_datadir}/applications
desktop-file-install --vendor=mushware         \
  --dir %{buildroot}%{_datadir}/applications   \
  %{name}.desktop
desktop-file-install --vendor=mushware         \
  --dir %{buildroot}%{_datadir}/applications   \
  %{name}-recover.desktop

# Icons
mkdir -p -m 755 %{buildroot}%{_datadir}/icons/hicolor/16x16/apps
mkdir -p -m 755 %{buildroot}%{_datadir}/icons/hicolor/32x32/apps
mkdir -p -m 755 %{buildroot}%{_datadir}/icons/hicolor/48x48/apps
install -p -m 644 x11/icons/%{name}-16.png %{buildroot}%{_datadir}/icons/hicolor/16x16/apps/%{name}.png
install -p -m 644 x11/icons/%{name}-32.png %{buildroot}%{_datadir}/icons/hicolor/32x32/apps/%{name}.png
install -p -m 644 x11/icons/%{name}-48.png %{buildroot}%{_datadir}/icons/hicolor/48x48/apps/%{name}.png


%files
%doc COPYING README ChangeLog AUTHORS
%{_bindir}/*
%{_datadir}/%{name}
%{_datadir}/applications/*
%{_datadir}/icons/hicolor/16x16/apps/%{name}.png
%{_datadir}/icons/hicolor/32x32/apps/%{name}.png
%{_datadir}/icons/hicolor/48x48/apps/%{name}.png
%{_mandir}/man6/%{name}*.6*


%changelog
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

