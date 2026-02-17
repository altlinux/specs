Name: hp2xx
Version: 3.4.4
Release: alt1

Summary: Converts HP-GL Plotter Language into a Variety of Formats
License: GPLv2+
Group: Office

Url: http://www.gnu.org/software/hp2xx/hp2xx.html
Source: hp2xx-%version.tar

Patch0: hp2xx-3.4.4-fix.patch
Patch3: hp2xx-texinfo-5.0.patch
BuildRequires: libjpeg-devel
BuildRequires: libpng-devel
BuildRequires: zlib-devel
BuildRequires: libtiff-devel
BuildRequires: libX11-devel
BuildRequires: makeinfo

%description
The hp2xx program is a versatile tool for converting vector graphics
data given in Hewlett-Packard's HP-GL plotter language into a variety
of popular graphics formats, both vector and raster.

%prep
%setup
%patch0 -p1
%patch3 -p1

%build
make CC="gcc" OPTFLAGS="%optflags -fcommon" #LFLAGS="-L/usr/X11R6/%_lib"

%install
mkdir -p %buildroot{%_bindir,%_infodir,%_man1dir}
make bindir=%buildroot%_bindir \
     infodir=%buildroot%_infodir \
     mandir=%buildroot%_mandir install STRIP=true

%files
%_bindir/hp2xx
%_man1dir/hp2xx.*
%_infodir/hp2xx.*
%doc AUTHORS CHANGES README TODO copying doc/readme doc/changes doc/hp_cmds.lst

%changelog
* Tue Feb 17 2026 Grigory Ustinov <grenka@altlinux.org> 3.4.4-alt1
- Build new version.

* Fri Apr 16 2021 Grigory Ustinov <grenka@altlinux.org> 3.4.2-alt2
- Fixed FTBFS with -fcommon.

* Wed Apr 01 2015 Michael Shigorin <mike@altlinux.org> 3.4.2-alt1
- built for ALT Linux (based on opensuse's 3.4.2-593.1 package)

