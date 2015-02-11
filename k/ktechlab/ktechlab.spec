Name:             ktechlab
Version:          0.3.7
Release:          alt2.20090304
# revision checkout 238

Summary:          Development and simulation of micro-controllers and electronic circuits

License:          GPLv2
Group:            Engineering

URL:              http://sourceforge.net/projects/ktechlab/
Source:           %{name}-0.3.7.tar.gz
Source1:	  %name.desktop

Patch0:           ktechlab-0.3.6-multilib.patch
Patch1:           ktechlab-detect_gpsim.patch
Patch2:           ktechlab-gcc-4.5.patch
Patch3:           ktechlab-autotools.patch
Patch4:           ktechlab-gpsim-0.27.patch
Patch5:		  ktechlab-fpnode.patch
Patch6:		  ktechlab-fix-link.patch

BuildRequires(pre): kdelibs-devel gcc-c++
BuildRequires:    libgpsim-devel readline-devel
BuildRequires:    desktop-file-utils autoconf automake

# Ktechlab requires gputils for PIC simulation.
Requires:         gputils sdcc kdebase-common

%description
KTechlab is a development and simulation environment for
micro-controllers and electronic circuits. KTechlab consists of several
well-integrated components: A circuit simulator, capable of simulating
logic, linear devices and some nonlinear devices. Integration with
gpsim, allowing PICs to be simulated in circuit. A schematic editor,
which provides a rich real-time feedback of the simulation. A flowchart
editor, allowing PIC programs to be constructed visually. MicroBASIC; a
BASIC-like compiler for PICs, written as a companion program to
KTechlab. An embedded Kate part, which provides a powerful editor for
PIC programs. Integrated assembler and disassembler via gpasm and
gpdasm.

%prep
%setup -q

chmod +x ./admin/detect-autoconf.pl
rm -rf autom4te.cache

%patch0 -p0 -b .multilib

# Upstream already applied this patch
%patch1 -p0 -b .gpsim

# GCC 4.5 and newer automake compatibility TODO: send upstream
%patch2 -p0 -b .orig
%patch3 -p0 -b .orig
%patch4 -p1 -b .gpsim027
%patch5 -p1
%patch6 -p2

# /usr/bin/install: will not overwrite just-created
subst "s|while.png for.png||" icons/pics/Makefile.am

%build
%add_optflags -I%_includedir/tqtinterface
make -f Makefile.cvs
%K3configure \
        --disable-new-ldflags
%make_build

%install
%K3install
install -Dm0644 %SOURCE1 %buildroot%_desktopdir/%name.desktop

# Fix absolute symlink
rm -f %{buildroot}%{_docdir}/HTML/en/%{name}/common

# Set application icon available from normal path
for i in 16 22 32 48 64 128; do
	mkdir -p %buildroot%_iconsdir/hicolor/${i}x${i}/apps
	ln -s ../../../../kde/icons/hicolor/${i}x${i}/apps/ktechlab.png \
	      %buildroot%_iconsdir/hicolor/${i}x${i}/apps/ktechlab.png 
done


%find_lang %name

%files -f %name.lang
%doc AUTHORS ChangeLog COPYING TODO
%doc %_K3doc/en/%name
%_K3bindir/%name
%_K3bindir/microbe
%_K3apps/%name
%_K3apps/katepart/syntax/microbe.xml
%_K3cfg/%name.kcfg
%_K3mimelnk/application/*.desktop
%_K3applnk/Development/%name.desktop
%_desktopdir/%name.desktop
%_K3datadir/icons/hicolor/*/*/*.png
%_iconsdir/hicolor/*/*/*.png

%changelog
* Thu Feb 12 2015 Andrey Cherepanov <cas@altlinux.org> 0.3.7-alt2.20090304
- Fix desktop file and its icon

* Wed Feb 11 2015 Andrey Cherepanov <cas@altlinux.org> 0.3.7-alt1.20090304
- Build in Sisyphus from Fedora
