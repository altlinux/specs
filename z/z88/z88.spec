%define _unpackaged_files_terminate_build 1
%define _stripped_files_terminate_build 1

Name: z88
Version: 15
Release: alt1

Summary: Fast, powerful and free open source finite element method software
License: GPL-2.0
Group: Engineering
Url: https://github.com/LSCAD/Z88OS

Source: %name-%version.tar

# sync with version 15+dfsg-2 from Debian unstable + local fixes
Patch: %name-%version-%release.patch

BuildRequires: pkgconfig(gtk+-2.0)
BuildRequires: pkgconfig(libglvnd)
BuildRequires: pkgconfig(glu)

Requires: z88-data

%description
Z88 features 20 finite element types covering plane stress, plate bending,
axial symmetric structures and spacial structures up to 20-node Serendipity
hexahedrons. Z88 comes with a user-friendly interface, a powerful mesh
generator, a DXF-converter, two plot programs and, of course, two powerful
solvers. Import of COSMOS files from Pro/ENGINEER and Pro/MECHANICA is
supported.

%package data
Summary: Data files for %name
Group: Engineering
BuildArch: noarch

%description data
Z88 features 20 finite element types covering plane stress, plate bending,
axial symmetric structures and spacial structures up to 20-node Serendipity
hexahedrons. Z88 comes with a user-friendly interface, a powerful mesh
generator, a DXF-converter, two plot programs and, of course, two powerful
solvers. Import of COSMOS files from Pro/ENGINEER and Pro/MECHANICA is
supported.

This package provides data files of %name.

%prep
%setup
%patch -p1

rm -rfv bin/mac bin/win32 bin/win64
rm -fv bin/unix64/z88{com,g,h,n,o,r,x}

%build
export CFLAGS="%optflags -std=gnu11 -Wno-incompatible-pointer-types"
make -f make/make_unix_64/z88com.mk.gcc64 DIRECA=$(pwd)
make -f make/make_unix_64/z88g.mk.gcc64 DIRECA=$(pwd)
make -f  make/make_unix_64/z88h.mk.gcc64 DIRECA=$(pwd)
make -f  make/make_unix_64/z88n.mk.gcc64 DIRECA=$(pwd)
make -f  make/make_unix_64/z88o.mk.gcc64 DIRECA=$(pwd)
make -f  make/make_unix_64/z88x.mk.gcc64 DIRECA=$(pwd)
make -f  make/make_unix_64/z88r.mk.gcc64 DIRECA=$(pwd)

%install
# follow z88.install
install -Dpm755 bin/unix64/z88com %buildroot%_bindir/z88com
install -Dpm755 bin/unix64/z88g   %buildroot%_bindir/z88g
install -Dpm755 bin/unix64/z88h   %buildroot%_bindir/z88h
install -Dpm755 bin/unix64/z88n   %buildroot%_bindir/z88n
install -Dpm755 bin/unix64/z88o   %buildroot%_bindir/z88o
install -Dpm755 bin/unix64/z88x   %buildroot%_bindir/z88x
install -Dpm755 z88               %buildroot%_bindir/z88

## add z88r
install -Dpm755 bin/unix64/z88r   %buildroot%_bindir/z88r

mkdir -pv %buildroot%_datadir/z88
cp -pv bin/unix64/z88.fcd         %buildroot%_datadir/z88/
cp -pv bin/unix64/z88.dyn         %buildroot%_datadir/z88/

# follow z88-data.install
cp -pv bin/unix64/*.txt %buildroot%_datadir/z88/
cp -pv bin/unix64/z88x.dxf %buildroot%_datadir/z88/

# follow z88-doc.docs
mkdir -pv %buildroot%_datadir/doc/z88/
cp -arvp examples %buildroot%_datadir/doc/z88/
cp -pv docu/z88man?.pdf %buildroot%_datadir/doc/z88/

# prepare desktop file
mkdir -p %buildroot%_desktopdir
cat <<EOF > %buildroot%_desktopdir/z88.desktop
[Desktop Entry]
Version=1.0
Name=Z88
GenericName=Z88
Comment=Finite Element Analysis Program
Exec=z88
Type=Application
Terminal=true
Categories=Science;
EOF

%files
%doc LICENSE readme.md readme.pdf liesmich.pdf
%_bindir/z88
%_bindir/z88com
%_bindir/z88g
%_bindir/z88h
%_bindir/z88n
%_bindir/z88o
%_bindir/z88r
%_bindir/z88x
%_desktopdir/z88.desktop
%_datadir/z88/z88.dyn
%_datadir/z88/z88.fcd

%files data
%_datadir/z88/*.txt
%_datadir/z88/z88x.dxf
%dir %_datadir/doc/z88
%_datadir/doc/z88/*

%changelog
* Mon Jul 20 2026 Nikolay Strelkov <snk@altlinux.org> 15-alt1
- Initial build for Sisyphus
