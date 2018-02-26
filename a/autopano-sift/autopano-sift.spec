Name: autopano-sift
Version: 2.4
Release: alt8

Group: Graphics
Summary: autopano - automatic creation of control points for panoramas
License: GPL
Url: http://user.cs.tu-berlin.de/~nowozin/autopano-sift/
Source0: http://user.cs.tu-berlin.de/~nowozin/autopano-sift/autopano-sift-%version.tar.gz
Patch0: autopano-sift-Makefile.patch
Packager: Sergei Epiphanov <serpiph@altlinux.ru>

BuildRequires: gcc-c++ libstdc++-devel pkgconfig
BuildRequires: mono >= 1.0.2 mono-mcs >= 1.0.2
BuildRequires: mono(atk-sharp) mono(gdk-sharp) mono(glade-sharp) mono(glib-sharp) mono(gtk-sharp)
BuildRequires: mono(System) mono(System.Drawing) mono(System.Windows.Forms) mono(System.Data)
BuildRequires: pkgconfig(gapi-2.0) pkgconfig(mono) pkgconfig(gtk-sharp-2.0) mono-devel
BuildRequires: /proc
Requires: mono >= 1.0.2 mono(System) mono(System.Drawing) mono(System.Windows.Forms) mono(System.Data)
Requires: mono(atk-sharp) mono(gdk-sharp) mono(glade-sharp) mono(glib-sharp) mono(gtk-sharp)
Requires: libgtk-sharp2-gapi
Conflicts: autopano-sift-C
ExclusiveArch: %ix86

%description
Panorama images are wide-angle images that amaze people:
you often feel being inside the scene when watching a good
panorama image. Creating such images is easy and everybody
with a digital camera and a bit of patience can do it.
Autopano-SIFT is there to make the creation of panorama images more fun.

%prep
%setup -q
%patch0 -p1

%build
%make -C src
pushd bin

%install

/bin/install -D -m0755 src/libsift.dll %buildroot/usr/lib/libsift.dll
/bin/install -D -m0755 src/util/autopanog/autopanog.exe %buildroot%_bindir/autopanog.exe
/bin/install -D -m0755 src/util/autopano.exe %buildroot%_bindir/autopano.exe
/bin/install -D -m0755 src/util/showone.exe %buildroot%_bindir/showone.exe
/bin/install -D -m0755 src/util/showtwo.exe %buildroot%_bindir/showtwo.exe
/bin/install -D -m0755 src/util/generatekeys.exe %buildroot%_bindir/generatekeys.exe
/bin/install -D -m0755 src/util/generatekeys-sd.exe %buildroot%_bindir/generatekeys-sd.exe
/bin/install -D -m0755 src/bin/autopano-complete.sh %buildroot%_bindir/autopano-complete.sh
/bin/install -D -m0755 src/util/monoopt.sh %buildroot%_bindir/monoopt.sh

/bin/mkdir -p %buildroot%_man1dir
/bin/mkdir -p %buildroot%_man7dir
pushd doc
for i in *.1; do
bzip2 $i
done
for i in *.7; do
bzip2 $i
done
%__install -p -m644 -D *.1.bz2 %buildroot%_man1dir
%__install -p -m644 -D *.7.bz2 %buildroot%_man7dir
popd

cat >%buildroot%_bindir/autopano <<EOF_AUTOPANO
#!/bin/sh
mono /usr/bin/autopano.exe \$@
EOF_AUTOPANO
chmod 755 %buildroot%_bindir/autopano

cat >%buildroot%_bindir/autopanog <<EOF_AUTOPANOG
#!/bin/sh
mono /usr/bin/autopanog.exe \$@
EOF_AUTOPANOG
chmod 755 %buildroot%_bindir/autopanog

%files
%doc README doc/*.pdf doc/*.txt
%_bindir/*
/usr/lib/*
%_man1dir/*
%_man7dir/*

%changelog
* Wed Feb 15 2012 Sergei Epiphanov <serpiph@altlinux.ru> 2.4-alt8
- Rebuild with mono

* Mon Mar 02 2009 Sergei Epiphanov <serpiph@altlinux.ru> 2.4-alt6.M50.1
- Build for Master5.0

* Wed Feb 25 2009 Sergei Epiphanov <serpiph@altlinux.ru> 2.4-alt7
- Set conflicts to autopano-sift-C

* Thu Jul 24 2008 Sergei Epiphanov <serpiph@altlinux.ru> 2.4-alt6
- Fix program dependencies

* Sun Feb 17 2008 Sergei Epiphanov <serpiph@altlinux.ru> 2.4-alt5
- Fix mono dependencies

* Wed Nov 28 2007 Sergei Epiphanov <serpiph@altlinux.ru> 2.4-alt4
- Fix mono dependencies

* Mon Feb 05 2007 Sergei Epiphanov <serpiph@altlinux.ru> 2.4-alt3
- Clean build (replace package names with module names)
- Fix build with gtk-sharp2
- Add scripts to start autopano and autopanog via mono

* Tue Nov 14 2006 Sergei Epiphanov <serpiph@altlinux.ru> 2.4-alt2
- Fix build with mono (add BuildRequires: mono-mcs)

* Tue Dec 27 2005 Sergei Epiphanov <serpiph@altlinux.ru> 2.4-alt1
- New version
- Add compilation from sources

* Mon Sep 05 2005 Sergei Epiphanov <serpiph@altlinux.ru> 2.3-alt3
- Fixing for ALT Linux

* Thu Aug 11 2005 Sergei Epiphanov <serpiph@nikiet.ru> 2.3-alt2
-corrections for build and install

* Tue Jul 26 2005 Sergei Epiphanov <serpiph@nikiet.ru> 2.3-alt1
-initial build
