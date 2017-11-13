Name: dangerdeep
Version: 0.4.0_pre3327
Release: alt2

Summary: Danger from the Deep - WW2 german submarine simulation
License: GPL v2
Group: Games/Other

Url: http://dangerdeep.sourceforge.net
Source: http://dl.sourceforge.net/dangerdeep/%name-%version.tar.gz
Patch: dangerdeep-0.4.0_pre3327-alt-libGL-x86_64.patch
Patch1: dangerdeep-0.4.0_pre3327-alt-glibc-2.16.patch
Patch2: dangerdeep-0.4.0_pre3327-alt-gcc-6.patch

Requires: dangerdeep-data = %version

# Automatically added by buildreq on Mon Jul 26 2010
BuildRequires: ImageMagick-tools bzlib-devel cvs flex gcc-c++ ghostscript-utils libGL-devel libSDL_image-devel libSDL_mixer-devel libSDL_net-devel libX11-devel libavutil-devel libfftw3-devel libfreeglut-devel python-modules-email rcs scons texlive-latex-base
BuildRequires: desktop-file-utils

%description
Danger from the deep (aka dangerdeep) is a Free / Open Source World
War II german submarine simulation. It is currently available for
Linux/i386 and Windows, but since it uses SDL/OpenGL it should be
portable to other operating systems or platforms. This game is planned
as tactical simulation and will be as realistic as our time and
knowledge of physics allows. It's current state is ALPHA, but it is
playable.

%prep
%setup -q
%patch -p2
%patch1 -p2
%patch2 -p2

sed -i 's@-g -O2@%optflags@' SConstruct
sed -i 's@/usr/local/bin@%_bindir@' SConstruct
sed -i 's@/usr/local/share/dangerdeep@%_datadir/%name@' SConstruct
sed -i 's@ffmpeg/libavutil@libavutil@' SConstruct

%build
scons
for i in 16 32 48; do
    convert -size ${i}x$i logo.xpm -resize ${i}x$i %name-${i}x$i.png
done

%install
install -pD -m644 logo.xpm %buildroot%_pixmapsdir/%name.xpm
install -pD -m644 %name-16x16.png %buildroot/%_miconsdir/%name.png
install -pD -m644 %name-32x32.png %buildroot/%_iconsdir/%name.png
install -pD -m644 %name-48x48.png %buildroot/%_liconsdir/%name.png

mkdir -p %buildroot%_bindir
install build/linux/%name %buildroot%_bindir/

mkdir -p %buildroot%_desktopdir
cat > %buildroot%_desktopdir/alt-%name.desktop << EOF
[Desktop Entry]
Name=Danger from the deep
Comment=WW2 german submarine simulation
Exec=%name
Icon=%name
Terminal=false
Type=Application
StartupNotify=false
Categories=Game;
EOF
desktop-file-install --dir %buildroot%_desktopdir \
	--add-category=StrategyGame \
	%buildroot%_desktopdir/alt-dangerdeep.desktop

%files
%doc CREDITS ChangeLog README
%_bindir/%name
%_desktopdir/*.desktop
%_pixmapsdir/%name.xpm
%_iconsdir/%name.png
%_iconsdir/hicolor/*/*/*.png

%changelog
* Mon Nov 13 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 0.4.0_pre3327-alt2
- Fixed build with gcc-6.

* Mon Dec 03 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.4.0_pre3327-alt1.qa3
- Fixed build with glibc 2.16

* Mon Jul 23 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.4.0_pre3327-alt1.qa2
- Fixed build

* Mon May 23 2011 Repocop Q. A. Robot <repocop@altlinux.org> 0.4.0_pre3327-alt1.qa1
- NMU (by repocop). See http://www.altlinux.org/Tools/Repocop
- applied repocop fixes:
  * freedesktop-desktop-file-proposed-patch for dangerdeep

* Mon Jul 26 2010 Slava Dubrovskiy <dubrsl@altlinux.org> 0.4.0_pre3327-alt1
- New version
- Update spec

* Sun Apr 22 2007 Michael Shigorin <mike@altlinux.org> 0.2.0-alt2
- fixed #10702 (thanks raorn@ again; it would be especially pity
  if dangerdeep-data-0.2-alt2 -- which also fixed this even if in
  less logical manner -- didn't hit Sisyphus with its 70M due to
  me being careless...)

* Mon Jan 01 2007 Michael Shigorin <mike@altlinux.org> 0.2.0-alt1
- initial build for ALT Linux Sisyphus (spec based on PLD and
  Mandriva 2007 contrib)
- data moved to separate package (different source, in theory
  could be updated asynchronously upstream)
- massive spec cleanup
- buildreq
- added SConstruct patch to cope with missing /proc/cpuinfo
- adjusted package Group:
