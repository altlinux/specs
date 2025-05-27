%define _unpackaged_files_terminate_build 1

Name:           magnifier
Version:        3.6
Release:        alt1
Summary:        Virtual Magnifying Glass
Group:          Accessibility
License:        GPL Version 2
URL:            http://magnifier.sourceforge.net
VCS: https://sourceforge.net/projects/magnifier/

Source:        %name-%version.tar

BuildRequires(pre): rpm-build-fpc
BuildRequires: lazarus
BuildRequires: lazarus-gtk
BuildRequires: libgtk2-engine-adwaita
BuildRequires: fpc-units-base
BuildRequires: fpc-units-fcl
BuildRequires: fpc-units-fv
BuildRequires: fpc-units-gfx
BuildRequires: fpc-units-gtk2
BuildRequires: fpc-units-rtl

%description
Virtual Magnifying Glass is a free, open source, multiplatform, screen magnification tool. It is simple, customizable, and easy-to-use.

%prep
%setup

%build
ARCH_OS=%_arch-linux

case "%_arch" in
  "i686"|"i586"|"i486") ARCH_OS="i386-linux";;
  "x86_64") ARCH_OS="x86_64-linux";;
esac


DEPENDENCY_PATHS="\
-Fu%_libdir/fpc/units/$ARCH_OS \
-Fu%_libdir/fpc/units/$ARCH_OS/gtk2 \
-Fu%_libdir/fpc/units/$ARCH_OS/rtl \
-Fu%_libdir/lazarus/units/$ARCH_OS \
-Fu%_libdir/lazarus/lcl/units/$ARCH_OS \
-Fu%_libdir/lazarus/lcl/units/$ARCH_OS/gtk2 \
-Fu%_libdir/lazarus/packager/units/$ARCH_OS \
-Fu%_libdir/lazarus/components/lazutils \
-Fu%_libdir/lazarus/packager/units/$ARCH_OS"

fpc -S2cgi -O1 -gl -vewnhi -l $DEPENDENCY_PATHS -Fu. -o./magnifier -dLCL -dLCLgtk2 magnifier.dpr

%install
./install.sh DESTDIR=%buildroot

%files
%_datadir/magnifier/
%_bindir/vmg

%changelog
* Wed May 21 2025 Timofei Fedotov <sovtouch@altlinux.org> 3.6-alt1
- Initial build for sisyphus (THX: Artem Semenov) (Closes: #52615)

* Wed Dec 14 2011 Felipe Monteiro de Carvalho <felipemonteiro.carvalho at gmail.com> - 3.6-mdk.i386.rpm
- New update for version 3.6.

* Mon Jun 29 2010 Felipe Monteiro de Carvalho <felipemonteiro.carvalho at gmail.com> - 3.5-mdk.i386.rpm
- New update for version 3.5.

* Mon May 24 2010 Felipe Monteiro de Carvalho <felipemonteiro.carvalho at gmail.com> - 3.4-mdk.i386.rpm
- New update for version 3.4.

* Wed Dec 10 2008 Felipe Monteiro de Carvalho <felipemonteiro.carvalho at gmail.com> - 3.3.2-mdk.i386.rpm
- New update for version 3.3.2.

* Wed Jul 2 2007 Felipe Monteiro de Carvalho <felipemonteiro.carvalho at gmail.com> - 3.3-mdk.i386.rpm
- Updated the package.

* Wed Feb 15 2006 Felipe Monteiro de Carvalho <felipemonteiro.carvalho at gmail.com> - 3.2-mdk.i386.rpm
- The Linux RPM package is created.
