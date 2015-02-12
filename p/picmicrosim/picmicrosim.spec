Name:		picmicrosim
Version:	1.0
Release:	alt1
Summary:	PIC Microprocessor Simulator on Linux

License:	GPLv2+
Group:		Engineering
URL:		http://sourceforge.net/projects/picmicrosim/

Packager:	Andrey Cherepanov <cas@altlinux.org>

Source:		microsim_v1.0.tar.gz

Patch1:		picmicrosim-fix-permissive.patch
Patch2:		picmicrosim-fix-missing-includes.patch
Patch3:		picmicrosim-use-stuff-from-app-dir.patch

BuildRequires:  gcc-c++ libqt3-devel

%description
Microprocessor simulator for the PIC16F84A on Linux using a GUI to allow
for easier programming and debugging of PIC applications. Features a
memory viewer, source browser, register editor and mapping PIC pins to
parallel port for real world interfacing.

%prep
%setup -q -n version-1.0
%patch1 -p2
%patch2 -p2
%patch3 -p2

qmake-qt3 "QMAKE_CXXFLAGS+=%optflags `pkg-config --cflags qt-mt`" "DEFINES+=APPSDIR=\\\"%_datadir/apps/microsim/\\\"" microsim.pro

%build
%make_build

%install
mkdir -p %buildroot%_bindir
cp -a microsim %buildroot%_bindir
mkdir -p %buildroot%_datadir/apps/microsim
cp -a documentation images %buildroot%_datadir/apps/microsim

%files
%doc README
%_bindir/microsim
%_datadir/apps/microsim

%changelog
* Tue Feb 10 2015 Andrey Cherepanov <cas@altlinux.org> 1.0-alt1
- Initial build in Sisyphus

