%define pkgver 123-0-1
Name: simutrans
Version: 123.0.1
Release: alt1
Summary: Transport and Economic Simulation Game
License: Artistic-1.0
Group: Games/Strategy
Url: http://sourceforge.net/projects/simutrans/
Packager: Artyom Bystrov <arbars@altlinux.org>

Source: http://downloads.sourceforge.net/simutrans/simutrans-src-%pkgver.zip
Source1: config.default
Source2: http://www.simutrans.com/images/resources/simutrans-square.svg
# PATCH-FIX-UPSTREAM http://forum.simutrans.com/index.php?topic=11173.0
Patch0: simutrans-fhs-home-directory.patch
BuildRequires: gcc
BuildRequires: gcc-c++
BuildRequires: unzip
BuildRequires: pkgconfig(bzip2)
BuildRequires: pkgconfig(libpng)
BuildRequires: pkgconfig(sdl2)
BuildRequires: pkgconfig(zlib)
BuildRequires: freetype2-devel
BuildRequires: dos2unix
BuildRequires: hicolor-icon-theme

BuildRequires: libzstd-devel

%description
Simutrans is a transport and economic simulation with some ecological
aspects. The goal of the game is to build an infrastructure which
allows you to transport goods between the various industries and towns,
and to support the towns with water and energy. A second goal is to
become as rich as possible, but you will have to reinvest a good part
of your earned money to expand your infrastructure network.

%package makeobj
Summary: Tool for compiling simutrans data packages
Group: Development/Tools
# Package was called simutrans previously
Obsoletes: makeobj < %version-%release

%description makeobj
Makeobj is a easy to use software used to compile .dat files and .png pictures
to simutrans .pak files.

%prep
%setup -c -n simutrans
cp %SOURCE1 .
# files with the wrong line-endings, which give a rpmlint warning:
dos2unix simutrans/*.txt

%build
export CFLAGS="%optflags"
export CCFLAGS="$CFLAGS"
%make_build all makeobj
# The next 3 lines did not function correctly; so now we use the available theme pak files:
# cd themes.src
# sed -i 's|../makeobj|../../build/default/makeobj/makeobj|g' build_themes.sh
# ./build_themes.sh

%install
# Create starter-wrapper script (not a source so we can use directory macros):
mkdir -vp %buildroot%_bindir
cat > %buildroot%_bindir/%name << EOF
#!/bin/sh
cd %_datadir/%name
exec %_libexecdir/%name/sim -use_workdir \$@
EOF
chmod 755 %buildroot%_bindir/%name
# Install the executable "sim":
install -vDm755 build/default/sim %buildroot%_libexecdir/%name/sim
# Install makeobj, avoid conflict with makeobj from kdesdk-scripts
install -vm755 build/default/makeobj/makeobj %buildroot%_libexecdir/%name/makeobj
ln -s %_libexecdir/%name/makeobj %buildroot%_bindir/makeobj-simutrans
# Install data
mkdir -vp %buildroot%_datadir/%name
cp -va simutrans/* %buildroot%_datadir/%name
# Create dummy directories addons
mkdir -vp %buildroot%_datadir/%name/addons
# Move docs to the correct place
mkdir -vp %buildroot%_docdir/%name
mv -v %buildroot%_datadir/%name/*.txt %buildroot%_docdir/%name
# Install icon and .desktop file
install -vDm644 %SOURCE2 %buildroot%_iconsdir/hicolor/scalable/apps/%name.svg

mkdir -p %buildroot%_desktopdir
cat > %buildroot%_desktopdir/%name.desktop << EOF
[Desktop Entry]
Name=Simutrans
Comment=Transport and Economic Simulation Game
Exec=%name
Icon=%name
Terminal=false
Type=Application
Categories=Game;ArcadeGame;
EOF

%files
%doc %_docdir/%name
%_bindir/%name
%_datadir/%name
%dir %_libexecdir/%name
%_libexecdir/%name/sim
%_iconsdir/hicolor/scalable/apps/%name.svg
%_desktopdir/%name.desktop

%files makeobj
%_bindir/makeobj-simutrans
%dir %_libexecdir/%name
%_libexecdir/%name/makeobj

%changelog
* Mon Mar 13 2023 Artyom Bystrov <arbars@altlinux.org> 123.0.1-alt1
- initial build for ALT Sisyphus

* Thu Jul 06 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 0.120.2.2-alt1
- New version
- Drop old patches, it looks like upstream applied similar fixes
- Improve debug info

* Sat Nov 24 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.111.2.1-alt1.1
- Fixed build with zlib 1.2.7

* Thu Mar 22 2012 Aleksey Avdeev <solo@altlinux.ru> 0.111.2.1-alt1
- new version

* Sat Jun 25 2011 Aleksey Avdeev <solo@altlinux.ru> 0.110.0.1-alt2
- buffer overflow fix

* Sun Jun 19 2011 Aleksey Avdeev <solo@altlinux.ru> 0.110.0.1-alt1
- new version

* Thu Feb 26 2009 Michael Shigorin <mike@altlinux.org> 0.99.17.1-alt2.r1533
- applied PPC patch by sbolshakov@ (only on non-x86 arches)
- spec cleanup
- buildreq
- NB: this package would benefit from proper maintainer. :)

* Tue Jan 08 2008 Michael Shigorin <mike@altlinux.org> 0.99.17.1-alt1.r1533
- rebuilt for Sisyphus

* Sat Jan  5 2008 Alexey Morozov <morozov@altlinux.org> 0.99.17.1-alt1.r1533
- Initial build for ALTLinux (SuSE binary-only spec was taken as
  starting point).
