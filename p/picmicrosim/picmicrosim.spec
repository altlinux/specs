Name: picmicrosim
Version: 1.0
Release: alt5

Summary: PIC Microprocessor Simulator on Linux
License: GPLv2+
Group: Engineering

Url: http://sourceforge.net/projects/picmicrosim/
Source: microsim_v1.0.tar.gz
Packager: Andrey Cherepanov <cas@altlinux.org>

Patch1: picmicrosim-fix-permissive.patch
Patch2: picmicrosim-fix-missing-includes.patch
Patch3: picmicrosim-use-stuff-from-app-dir.patch
Patch4: %name-%version-alt-gcc6.patch
Patch5: %name-g++8.patch

BuildRequires: gcc-c++ libqt3-devel
ExclusiveArch:  i586 x86_64

%description
Microprocessor simulator for the PIC16F84A on Linux using a GUI to allow
for easier programming and debugging of PIC applications. Features a
memory viewer, source browser, register editor and mapping PIC pins to
parallel port for real world interfacing.

%prep
%setup -n version-1.0
%patch1 -p2
%patch2 -p2
%patch3 -p2
%patch4 -p2
%patch5 -p2

qmake-qt3 "QMAKE_CXXFLAGS+=%optflags `pkg-config --cflags qt-mt`" "DEFINES+=APPSDIR=\\\"%_datadir/apps/microsim/\\\"" microsim.pro

%build
%make_build

%install
mkdir -p %buildroot{%_bindir,%_datadir/apps/microsim}
cp -a microsim %buildroot%_bindir
cp -a documentation images %buildroot%_datadir/apps/microsim

%files
%doc README
%_bindir/microsim
%_datadir/apps/microsim

%changelog
* Wed Nov 06 2019 Michael Shigorin <mike@altlinux.org> 1.0-alt5
- minor spec cleanup (and yes, it's x86 specific: sys/io.h)

* Tue Feb 12 2019 Andrey Bychkov <mrdrew@altlinux.org> 1.0-alt4
- no return statement in the non-void function fixed (according g++8)

* Mon Jul 03 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 1.0-alt3
- Updated to build with gcc-6

* Mon Oct 05 2015 Andrey Cherepanov <cas@altlinux.org> 1.0-alt2
- rebuilt against gcc5-built qt3

* Tue Feb 10 2015 Andrey Cherepanov <cas@altlinux.org> 1.0-alt1
- Initial build in Sisyphus

