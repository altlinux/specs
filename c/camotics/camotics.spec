# Unpackaged files in buildroot should terminate build
%define _unpackaged_files_terminate_build 1

Name: camotics
Version: 1.2.1
Release: alt3.20191008

Summary: Open-Source Simulation and Computer Aided Machining - A 3-axis CNC GCode simulator

License: GPLv2+ and LGPL2.1
Group: Engineering
Url: https://github.com/CauldronDevelopmentLLC/CAMotics

Packager: Anton Midyukov <antohami@altlinux.org>

Source: %name-%version.tar
Source2: camotics.xml
Source3: CAMotics.appdata.xml
Patch: 0001-Revert-Updates-to-use-newer-v8.patch
Patch1: 0002-do-not-check-conf.TryCompile-for-dxflib.patch
Patch2: camotics-1.2.1-fix-build-with-gcc13.patch

# libv8-3.14-devel cannot be compiled for aarch64, ppc64le
ExclusiveArch: %ix86 x86_64

BuildRequires: gcc-c++
BuildRequires: python3-devel
BuildRequires: scons
BuildRequires: libcairo-devel
BuildRequires: qt5-base-devel
BuildRequires: qt5-websockets-devel
BuildRequires: qt5-tools
BuildRequires: bzlib-devel
BuildRequires: libsqlite3-devel
BuildRequires: libexpat-devel
BuildRequires: libevent-devel
BuildRequires: libv8-3.14-devel
BuildRequires: python3-module-six
BuildRequires: libssl-devel
BuildRequires: libre2-devel
BuildRequires: zlib-devel
BuildRequires: libyaml-devel
BuildRequires: libleveldb-devel
BuildRequires: libsnappy-devel
BuildRequires: libdxflib-devel
BuildRequires: ImageMagick-tools desktop-file-utils
BuildRequires: chrpath
BuildRequires: libappstream-glib

Requires: %name-data = %EVR

%description
CAMotics is an Open-Source software which can simulate 3-axis NC machining. It
is a fast, flexible and user friendly simulation software for the DIY and
Open-Source community. CAMotics works on Linux, OS-X and Windows.

At home manufacturing is one of the next big technology revolutions. Much like
the PC was 30 years ago. There have been major advances in desktop 3D printing
yet uptake of desktop CNCs has lagged depsite the availability of cheap CNC
machines. One of the major reasons for this is a lack of Open-Source simulation
and CAM software. CAM and NC machine simulation present some very difficult
programming problems, as is evidenced by 30 years of academic papers on these
topics. Whereas, 3D printing simulation and tool path generation are much
easier. Such software is essential to using a CNC.

Being able to simulate is a critical part of creating CNC tool paths.
Programming a CNC with out a simulator is cutting with out measuring; it s both
dangerous and expensive. With CAMotics you can preview the results of your
cutting operation before you fire up your machine. This will save you time and
money and open up a world of creative possibilities by allowing you to rapidly
visualize and improve upon designs with out wasting material or breaking tools.

%package data
Summary: Data files for %name
Group: Engineering
Buildarch: noarch

%description data
Data files for %name

%prep
%setup
pushd cbang
%patch -p1
popd
%patch1 -p1
%patch2 -p1

for file in $(grep -Rl --include=SConscript -- '-Werror' src/ 2>/dev/null); do
  sed -i "s/\.replace('-Werror', '')/\nflags = re.sub(r'-Werro([^\\\s]+|r)', '', flags)/" $file
  sed -i '1iimport re' $file
done

%build
# re2 from system uses c++11 features (GH cbang #22)
%global _scopts cxxstd=c++11 debug=1 strict=0 disable_local="bzip2 expat re2 sqlite3 zlib" %_smp_mflags
export QT5DIR=%_includedir/qt5
scons -C cbang %_scopts
scons %_scopts

%install
scons install install_prefix=%buildroot%prefix %_scopts

# https://github.com/CauldronDevelopmentLLC/CAMotics/issues/211
install -d -m 0755 %buildroot%_datadir/mime/packages
install -p -m 0644 %SOURCE2 %buildroot/%_datadir/mime/packages

#Install missing data files
mkdir -p %buildroot%_datadir/%name
cp -r tpl_lib %buildroot%_datadir/%name

#Install examples
mkdir -p %buildroot%_docdir/%name
cp -r examples %buildroot%_docdir/%name

#Install and fixing desktop files
install -pD -m644 CAMotics.desktop %buildroot%_desktopdir/CAMotics.desktop
desktop-file-install --dir %buildroot%_desktopdir \
        --remove-key=Encoding \
        --set-icon=camotics \
        --remove-category=Science \
        --add-category=Development \
        --add-category=Engineering \
%buildroot%_desktopdir/CAMotics.desktop

install -d -m 0755 %buildroot%_iconsdir/hicolor/128x128/apps
install -p -m 0644 images/camotics.png %buildroot%_iconsdir/hicolor/128x128/apps/
#Convert and install images files
for x in 16 32 48; do
    mkdir -p %buildroot%_iconsdir/hicolor/$x'x'$x/apps/
	convert images/camotics.png -resize $x'x'$x %buildroot/%_iconsdir/hicolor/$x'x'$x/apps/camotics.png
done

# https://github.com/CauldronDevelopmentLLC/CAMotics/pull/236
install -d -m 0755 %buildroot%_datadir/metainfo
install -p -m 0644 %SOURCE3 %buildroot/%_datadir/metainfo

# Convert files with DOS line endings to Unix
find "%buildroot%_datadir" -not -type d -exec file {} \; \
     | grep CRLF | cut -f1 -d: | while read -r dosfile; do
       sed -i $'s/\r$//' $dosfile; done

# Remove executable bit from executable files in datadir
find "%buildroot%_datadir" -executable -type f -exec chmod -x {} \;

# fix RPATH
chrpath -d %buildroot%_bindir/*

%check
appstream-util validate-relax --nonet %buildroot/%_datadir/metainfo/*.appdata.xml

%files
%_bindir/*
%_iconsdir/hicolor/*/apps/*
%_desktopdir/CAMotics.desktop
%_datadir/metainfo/*
%_datadir/mime/packages/*

%files data
%_docdir/%name
%_datadir/%name

%changelog
* Fri Jun 23 2023 Anton Midyukov <antohami@altlinux.org> 1.2.1-alt3.20191008
- fix build with gcc13

* Mon Oct 21 2019 Anton Midyukov <antohami@altlinux.org> 1.2.1-alt2.20191008
- fix directory: 's|_datadir/appdata|_datadir/metainfo|g'

* Sun Oct 20 2019 Anton Midyukov <antohami@altlinux.org> 1.2.1-alt1.20191008
- new snapshot
- fix build with scons switched to python3
- ExclusiveArch: ix86 x86_64
- add appdata
- add mime
- update BuildRequires

* Wed Jun 12 2019 Stanislav Levin <slev@altlinux.org> 1.2.0-alt2
- Added missing dep on `six`.

* Mon Apr 15 2019 Anton Midyukov <antohami@altlinux.org> 1.2.0-alt1
- New version 1.2.0
- build with qt5

* Thu Jan 03 2019 Anton Midyukov <antohami@altlinux.org> 1.1.1-alt1.4
- rebuild with libv8-3.14

* Sat Sep 15 2018 Anton Midyukov <antohami@altlinux.org> 1.1.1-alt1.3
- rebuilt with openssl-1.1
- exclusive arch %ix86 x86_64

* Thu May 31 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 1.1.1-alt1.2
- NMU: rebuilt with boost-1.67.0

* Fri Apr 27 2018 Anton Midyukov <antohami@altlinux.org> 1.1.1-alt1.1
- Rebuilt with boost 1.66

* Sun Jul 30 2017 Anton Midyukov <antohami@altlinux.org> 1.1.1-alt1
- New version 1.1.1
- Fix desktop categories.

* Wed Feb 08 2017 Anton Midyukov <antohami@altlinux.org> 1.1.0-alt1
- New version 1.1.0

* Sun Jan 29 2017 Anton Midyukov <antohami@altlinux.org> 1.0.6-alt1.20170106.1
- Initial build for ALT Linux Sisyphus (Closes: 33041).
