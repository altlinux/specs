%define _unpackaged_files_terminate_build 1
%define soname 9

Name: gutenprint
Version: 5.3.5
Release: alt2
Epoch: 1
Summary: Gutenprint Printer Drivers
License: GPL-2.0-or-later
Group: Publishing
Requires: libgutenprint%soname = %EVR
Requires: ghostscript
Url: http://gimp-print.sourceforge.net/
VCS: https://git.code.sf.net/p/gimp-print/source.git

Source: %name-%version.tar
Source1: gutenprint.watch
Source2: ru.po

Patch0: gutenprint-5.3.1-alt-fixes.patch
Patch1: gutenprint-5.2.9-alt-makefile.patch
Patch2: gutenprint-alt-LFS.patch
Patch3: gutenprint-alt-link-plugins-with-libraries.patch
Patch4: gutenprint-alt-add-oki-mb472.patch
Patch5: gutenprint-5.3.5-alt-pantum-p3300dn-backside.patch

BuildRequires: chrpath
BuildRequires: flex
BuildRequires: foomatic-db-engine
BuildRequires: libcups-devel
BuildRequires: libreadline-devel
BuildRequires: libusb-devel
BuildRequires: zlib-devel

%description
Gutenprint is a package of high quality printer drivers for Linux and
other UNIX-alike operating systems.
Gutenprint was formerly called Gimp-Print.

%package -n libgutenprint%soname
Summary: Shared libraries for high-quality image printing
Group: Publishing
Obsoletes: libgutenprint < 5.3.5

%description -n libgutenprint%soname
Gutenprint is a package of high quality printer drivers for Linux and
other UNIX-alike operating systems.

This package contains gutenprint shared libraries.

%package -n libgutenprint-devel
Summary: Library development files for gutenprint
Group: Development/C
Requires: libgutenprint%soname = %EVR

%description -n libgutenprint-devel
Gutenprint is a package of high quality printer drivers for Linux and
other UNIX-alike operating systems.

This package contains header files and libraries required to build
gutenprint-based software.

%package -n gimp-plugin-gutenprint
Summary: GIMP plug-in for gutenprint
Group: Publishing
Requires: gutenprint = %EVR gimp

%description -n gimp-plugin-gutenprint
Gutenprint is a package of high quality printer drivers for Linux and
other UNIX-alike operating systems.

This package contains the gutenprint GIMP plug-in.

%package cups
Summary: CUPS drivers for Canon, Epson, HP and compatible printers
Group: System/Configuration/Hardware
Provides: gutenprint-CUPS = %EVR
Obsoletes: gutenprint-CUPS < %EVR
Requires: gutenprint = %EVR

%description cups
Gutenprint is a package of high quality printer drivers for Linux and
other UNIX-alike operating systems.

This package contains native CUPS support for a wide range of Canon,
Epson, HP and compatible printers.

%package cups-ppds
Summary: PPDs for CUPS drivers for Canon, Epson, HP and compatible printers
Group: System/Configuration/Hardware
Requires: gutenprint-cups = %EVR
Requires: gutenprint-cups-bjc-ppds = %EVR
Requires: gutenprint-cups-brother-ppds = %EVR
Requires: gutenprint-cups-canon-ppds = %EVR
Requires: gutenprint-cups-ciaat-ppds = %EVR
Requires: gutenprint-cups-citizen-ppds = %EVR
Requires: gutenprint-cups-compaq-ppds = %EVR
Requires: gutenprint-cups-datamax-ppds = %EVR
Requires: gutenprint-cups-dec-ppds = %EVR
Requires: gutenprint-cups-dell-ppds = %EVR
Requires: gutenprint-cups-dnp-ppds = %EVR
Requires: gutenprint-cups-epson-ppds = %EVR
Requires: gutenprint-cups-escp2-ppds = %EVR
Requires: gutenprint-cups-fujifilm-ppds = %EVR
Requires: gutenprint-cups-fujitsu-ppds = %EVR
Requires: gutenprint-cups-gestetner-ppds = %EVR
Requires: gutenprint-cups-hiti-ppds = %EVR
Requires: gutenprint-cups-honeywell-ppds = %EVR
Requires: gutenprint-cups-hp-ppds = %EVR
Requires: gutenprint-cups-ibm-ppds = %EVR
Requires: gutenprint-cups-infotec-ppds = %EVR
Requires: gutenprint-cups-joyspace-ppds = %EVR
Requires: gutenprint-cups-kodak-ppds = %EVR
Requires: gutenprint-cups-kyocera-ppds = %EVR
Requires: gutenprint-cups-lanier-ppds = %EVR
Requires: gutenprint-cups-lexmark-ppds = %EVR
Requires: gutenprint-cups-magicard-ppds = %EVR
Requires: gutenprint-cups-minolta-ppds = %EVR
Requires: gutenprint-cups-mitsubishi-ppds = %EVR
Requires: gutenprint-cups-nec-ppds = %EVR
Requires: gutenprint-cups-nidalcopac-ppds = %EVR
Requires: gutenprint-cups-nrg-ppds = %EVR
Requires: gutenprint-cups-oki-ppds = %EVR
Requires: gutenprint-cups-okidata-ppds = %EVR
Requires: gutenprint-cups-olivetti-ppds = %EVR
Requires: gutenprint-cups-olmec-ppds = %EVR
Requires: gutenprint-cups-olympus-ppds = %EVR
Requires: gutenprint-cups-panasonic-ppds = %EVR
Requires: gutenprint-cups-pantum-ppds = %EVR
Requires: gutenprint-cups-pcl-ppds = %EVR
Requires: gutenprint-cups-pcpi-ppds = %EVR
Requires: gutenprint-cups-raven-ppds = %EVR
Requires: gutenprint-cups-ricoh-ppds = %EVR
Requires: gutenprint-cups-samsung-ppds = %EVR
Requires: gutenprint-cups-savin-ppds = %EVR
Requires: gutenprint-cups-seiko-ppds = %EVR
Requires: gutenprint-cups-sharp-ppds = %EVR
Requires: gutenprint-cups-shinko-ppds = %EVR
Requires: gutenprint-cups-sinfonia-ppds = %EVR
Requires: gutenprint-cups-sony-ppds = %EVR
Requires: gutenprint-cups-star-ppds = %EVR
Requires: gutenprint-cups-stryker-ppds = %EVR
Requires: gutenprint-cups-tally-ppds = %EVR
Requires: gutenprint-cups-tektronix-ppds = %EVR
Requires: gutenprint-cups-toshiba-ppds = %EVR
BuildArch: noarch

%description cups-ppds
Gutenprint is a package of high quality printer drivers for Linux and
other UNIX-alike operating systems.

Meta-package for install PPDs for all families supported by gutenprint.

%package cups-bjc-ppds
Summary: PPDs for CUPS drivers for bjc and compatible printers
Group: System/Configuration/Hardware
Requires: gutenprint-cups = %EVR
BuildArch: noarch

%description cups-bjc-ppds
Gutenprint is a package of high quality printer drivers for Linux and
other UNIX-alike operating systems.

This package contains bjc PPDs for gutenprint-cups.

%package cups-brother-ppds
Summary: PPDs for CUPS drivers for brother and compatible printers
Group: System/Configuration/Hardware
Requires: gutenprint-cups = %EVR
BuildArch: noarch

%description cups-brother-ppds
Gutenprint is a package of high quality printer drivers for Linux and
other UNIX-alike operating systems.

This package contains brother PPDs for gutenprint-cups.

%package cups-canon-ppds
Summary: PPDs for CUPS drivers for canon and compatible printers
Group: System/Configuration/Hardware
Requires: gutenprint-cups = %EVR
BuildArch: noarch

%description cups-canon-ppds
Gutenprint is a package of high quality printer drivers for Linux and
other UNIX-alike operating systems.

This package contains canon PPDs for gutenprint-cups.

%package cups-ciaat-ppds
Summary: PPDs for CUPS drivers for ciaat and compatible printers
Group: System/Configuration/Hardware
Requires: gutenprint-cups = %EVR
BuildArch: noarch

%description cups-ciaat-ppds
Gutenprint is a package of high quality printer drivers for Linux and
other UNIX-alike operating systems.

This package contains ciaat PPDs for gutenprint-cups.

%package cups-citizen-ppds
Summary: PPDs for CUPS drivers for citizen and compatible printers
Group: System/Configuration/Hardware
Requires: gutenprint-cups = %EVR
BuildArch: noarch

%description cups-citizen-ppds
Gutenprint is a package of high quality printer drivers for Linux and
other UNIX-alike operating systems.

This package contains citizen PPDs for gutenprint-cups.

%package cups-compaq-ppds
Summary: PPDs for CUPS drivers for compaq and compatible printers
Group: System/Configuration/Hardware
Requires: gutenprint-cups = %EVR
BuildArch: noarch

%description cups-compaq-ppds
Gutenprint is a package of high quality printer drivers for Linux and
other UNIX-alike operating systems.

This package contains compaq PPDs for gutenprint-cups.

%package cups-datamax-ppds
Summary: PPDs for CUPS drivers for datamax and compatible printers
Group: System/Configuration/Hardware
Requires: gutenprint-cups = %EVR
BuildArch: noarch

%description cups-datamax-ppds
Gutenprint is a package of high quality printer drivers for Linux and
other UNIX-alike operating systems.

This package contains datamax PPDs for gutenprint-cups.

%package cups-dec-ppds
Summary: PPDs for CUPS drivers for dec and compatible printers
Group: System/Configuration/Hardware
Requires: gutenprint-cups = %EVR
BuildArch: noarch

%description cups-dec-ppds
Gutenprint is a package of high quality printer drivers for Linux and
other UNIX-alike operating systems.

This package contains dec PPDs for gutenprint-cups.

%package cups-dell-ppds
Summary: PPDs for CUPS drivers for dell and compatible printers
Group: System/Configuration/Hardware
Requires: gutenprint-cups = %EVR
BuildArch: noarch

%description cups-dell-ppds
Gutenprint is a package of high quality printer drivers for Linux and
other UNIX-alike operating systems.

This package contains dell PPDs for gutenprint-cups.

%package cups-dnp-ppds
Summary: PPDs for CUPS drivers for dnp and compatible printers
Group: System/Configuration/Hardware
Requires: gutenprint-cups = %EVR
BuildArch: noarch

%description cups-dnp-ppds
Gutenprint is a package of high quality printer drivers for Linux and
other UNIX-alike operating systems.

This package contains dnp PPDs for gutenprint-cups.

%package cups-epson-ppds
Summary: PPDs for CUPS drivers for epson and compatible printers
Group: System/Configuration/Hardware
Requires: gutenprint-cups = %EVR
BuildArch: noarch

%description cups-epson-ppds
Gutenprint is a package of high quality printer drivers for Linux and
other UNIX-alike operating systems.

This package contains epson PPDs for gutenprint-cups.

%package cups-escp2-ppds
Summary: PPDs for CUPS drivers for escp2 and compatible printers
Group: System/Configuration/Hardware
Requires: gutenprint-cups = %EVR
BuildArch: noarch

%description cups-escp2-ppds
Gutenprint is a package of high quality printer drivers for Linux and
other UNIX-alike operating systems.

This package contains escp2 PPDs for gutenprint-cups.

%package cups-fujifilm-ppds
Summary: PPDs for CUPS drivers for fujifilm and compatible printers
Group: System/Configuration/Hardware
Requires: gutenprint-cups = %EVR
BuildArch: noarch

%description cups-fujifilm-ppds
Gutenprint is a package of high quality printer drivers for Linux and
other UNIX-alike operating systems.

This package contains fujifilm PPDs for gutenprint-cups.

%package cups-fujitsu-ppds
Summary: PPDs for CUPS drivers for fujitsu and compatible printers
Group: System/Configuration/Hardware
Requires: gutenprint-cups = %EVR
BuildArch: noarch

%description cups-fujitsu-ppds
Gutenprint is a package of high quality printer drivers for Linux and
other UNIX-alike operating systems.

This package contains fujitsu PPDs for gutenprint-cups.

%package cups-gestetner-ppds
Summary: PPDs for CUPS drivers for gestetner and compatible printers
Group: System/Configuration/Hardware
Requires: gutenprint-cups = %EVR
BuildArch: noarch

%description cups-gestetner-ppds
Gutenprint is a package of high quality printer drivers for Linux and
other UNIX-alike operating systems.

This package contains gestetner PPDs for gutenprint-cups.

%package cups-hiti-ppds
Summary: PPDs for CUPS drivers for hiti and compatible printers
Group: System/Configuration/Hardware
Requires: gutenprint-cups = %EVR
BuildArch: noarch

%description cups-hiti-ppds
Gutenprint is a package of high quality printer drivers for Linux and
other UNIX-alike operating systems.

This package contains hiti PPDs for gutenprint-cups.

%package cups-honeywell-ppds
Summary: PPDs for CUPS drivers for honeywell and compatible printers
Group: System/Configuration/Hardware
Requires: gutenprint-cups = %EVR
BuildArch: noarch

%description cups-honeywell-ppds
Gutenprint is a package of high quality printer drivers for Linux and
other UNIX-alike operating systems.

This package contains honeywell PPDs for gutenprint-cups.

%package cups-hp-ppds
Summary: PPDs for CUPS drivers for hp and compatible printers
Group: System/Configuration/Hardware
Requires: gutenprint-cups = %EVR
BuildArch: noarch

%description cups-hp-ppds
Gutenprint is a package of high quality printer drivers for Linux and
other UNIX-alike operating systems.

This package contains hp PPDs for gutenprint-cups.

%package cups-ibm-ppds
Summary: PPDs for CUPS drivers for ibm and compatible printers
Group: System/Configuration/Hardware
Requires: gutenprint-cups = %EVR
BuildArch: noarch

%description cups-ibm-ppds
Gutenprint is a package of high quality printer drivers for Linux and
other UNIX-alike operating systems.

This package contains ibm PPDs for gutenprint-cups.

%package cups-infotec-ppds
Summary: PPDs for CUPS drivers for infotec and compatible printers
Group: System/Configuration/Hardware
Requires: gutenprint-cups = %EVR
BuildArch: noarch

%description cups-infotec-ppds
Gutenprint is a package of high quality printer drivers for Linux and
other UNIX-alike operating systems.

This package contains infotec PPDs for gutenprint-cups.

%package cups-joyspace-ppds
Summary: PPDs for CUPS drivers for joyspace and compatible printers
Group: System/Configuration/Hardware
Requires: gutenprint-cups = %EVR
BuildArch: noarch

%description cups-joyspace-ppds
Gutenprint is a package of high quality printer drivers for Linux and
other UNIX-alike operating systems.

This package contains joyspace PPDs for gutenprint-cups.

%package cups-kodak-ppds
Summary: PPDs for CUPS drivers for kodak and compatible printers
Group: System/Configuration/Hardware
Requires: gutenprint-cups = %EVR
BuildArch: noarch

%description cups-kodak-ppds
Gutenprint is a package of high quality printer drivers for Linux and
other UNIX-alike operating systems.

This package contains kodak PPDs for gutenprint-cups.

%package cups-kyocera-ppds
Summary: PPDs for CUPS drivers for kyocera and compatible printers
Group: System/Configuration/Hardware
Requires: gutenprint-cups = %EVR
BuildArch: noarch

%description cups-kyocera-ppds
Gutenprint is a package of high quality printer drivers for Linux and
other UNIX-alike operating systems.

This package contains kyocera PPDs for gutenprint-cups.

%package cups-lanier-ppds
Summary: PPDs for CUPS drivers for lanier and compatible printers
Group: System/Configuration/Hardware
Requires: gutenprint-cups = %EVR
BuildArch: noarch

%description cups-lanier-ppds
Gutenprint is a package of high quality printer drivers for Linux and
other UNIX-alike operating systems.

This package contains lanier PPDs for gutenprint-cups.

%package cups-lexmark-ppds
Summary: PPDs for CUPS drivers for lexmark and compatible printers
Group: System/Configuration/Hardware
Requires: gutenprint-cups = %EVR
BuildArch: noarch

%description cups-lexmark-ppds
Gutenprint is a package of high quality printer drivers for Linux and
other UNIX-alike operating systems.

This package contains lexmark PPDs for gutenprint-cups.

%package cups-magicard-ppds
Summary: PPDs for CUPS drivers for magicard and compatible printers
Group: System/Configuration/Hardware
Requires: gutenprint-cups = %EVR
BuildArch: noarch

%description cups-magicard-ppds
Gutenprint is a package of high quality printer drivers for Linux and
other UNIX-alike operating systems.

This package contains magicard PPDs for gutenprint-cups.

%package cups-minolta-ppds
Summary: PPDs for CUPS drivers for minolta and compatible printers
Group: System/Configuration/Hardware
Requires: gutenprint-cups = %EVR
BuildArch: noarch

%description cups-minolta-ppds
Gutenprint is a package of high quality printer drivers for Linux and
other UNIX-alike operating systems.

This package contains minolta PPDs for gutenprint-cups.

%package cups-mitsubishi-ppds
Summary: PPDs for CUPS drivers for mitsubishi and compatible printers
Group: System/Configuration/Hardware
Requires: gutenprint-cups = %EVR
BuildArch: noarch

%description cups-mitsubishi-ppds
Gutenprint is a package of high quality printer drivers for Linux and
other UNIX-alike operating systems.

This package contains mitsubishi PPDs for gutenprint-cups.

%package cups-nec-ppds
Summary: PPDs for CUPS drivers for nec and compatible printers
Group: System/Configuration/Hardware
Requires: gutenprint-cups = %EVR
BuildArch: noarch

%description cups-nec-ppds
Gutenprint is a package of high quality printer drivers for Linux and
other UNIX-alike operating systems.

This package contains nec PPDs for gutenprint-cups.

%package cups-nidalcopac-ppds
Summary: PPDs for CUPS drivers for nidalcopac and compatible printers
Group: System/Configuration/Hardware
Requires: gutenprint-cups = %EVR
BuildArch: noarch

%description cups-nidalcopac-ppds
Gutenprint is a package of high quality printer drivers for Linux and
other UNIX-alike operating systems.

This package contains nidalcopac PPDs for gutenprint-cups.

%package cups-nrg-ppds
Summary: PPDs for CUPS drivers for nrg and compatible printers
Group: System/Configuration/Hardware
Requires: gutenprint-cups = %EVR
BuildArch: noarch

%description cups-nrg-ppds
Gutenprint is a package of high quality printer drivers for Linux and
other UNIX-alike operating systems.

This package contains nrg PPDs for gutenprint-cups.

%package cups-oki-ppds
Summary: PPDs for CUPS drivers for oki and compatible printers
Group: System/Configuration/Hardware
Requires: gutenprint-cups = %EVR
BuildArch: noarch

%description cups-oki-ppds
Gutenprint is a package of high quality printer drivers for Linux and
other UNIX-alike operating systems.

This package contains oki PPDs for gutenprint-cups.

%package cups-okidata-ppds
Summary: PPDs for CUPS drivers for okidata and compatible printers
Group: System/Configuration/Hardware
Requires: gutenprint-cups = %EVR
BuildArch: noarch

%description cups-okidata-ppds
Gutenprint is a package of high quality printer drivers for Linux and
other UNIX-alike operating systems.

This package contains okidata PPDs for gutenprint-cups.

%package cups-olivetti-ppds
Summary: PPDs for CUPS drivers for olivetti and compatible printers
Group: System/Configuration/Hardware
Requires: gutenprint-cups = %EVR
BuildArch: noarch

%description cups-olivetti-ppds
Gutenprint is a package of high quality printer drivers for Linux and
other UNIX-alike operating systems.

This package contains olivetti PPDs for gutenprint-cups.

%package cups-olmec-ppds
Summary: PPDs for CUPS drivers for olmec and compatible printers
Group: System/Configuration/Hardware
Requires: gutenprint-cups = %EVR
BuildArch: noarch

%description cups-olmec-ppds
Gutenprint is a package of high quality printer drivers for Linux and
other UNIX-alike operating systems.

This package contains olmec PPDs for gutenprint-cups.

%package cups-olympus-ppds
Summary: PPDs for CUPS drivers for olympus and compatible printers
Group: System/Configuration/Hardware
Requires: gutenprint-cups = %EVR
BuildArch: noarch

%description cups-olympus-ppds
Gutenprint is a package of high quality printer drivers for Linux and
other UNIX-alike operating systems.

This package contains olympus PPDs for gutenprint-cups.

%package cups-panasonic-ppds
Summary: PPDs for CUPS drivers for panasonic and compatible printers
Group: System/Configuration/Hardware
Requires: gutenprint-cups = %EVR
BuildArch: noarch

%description cups-panasonic-ppds
Gutenprint is a package of high quality printer drivers for Linux and
other UNIX-alike operating systems.

This package contains panasonic PPDs for gutenprint-cups.

%package cups-pantum-ppds
Summary: PPDs for CUPS drivers for pantum and compatible printers
Group: System/Configuration/Hardware
Requires: gutenprint-cups = %EVR
BuildArch: noarch

%description cups-pantum-ppds
Gutenprint is a package of high quality printer drivers for Linux and
other UNIX-alike operating systems.

This package contains pantum PPDs for gutenprint-cups.

%package cups-pcl-ppds
Summary: PPDs for CUPS drivers for pcl and compatible printers
Group: System/Configuration/Hardware
Requires: gutenprint-cups = %EVR
BuildArch: noarch

%description cups-pcl-ppds
Gutenprint is a package of high quality printer drivers for Linux and
other UNIX-alike operating systems.

This package contains pcl PPDs for gutenprint-cups.

%package cups-pcpi-ppds
Summary: PPDs for CUPS drivers for pcpi and compatible printers
Group: System/Configuration/Hardware
Requires: gutenprint-cups = %EVR
BuildArch: noarch

%description cups-pcpi-ppds
Gutenprint is a package of high quality printer drivers for Linux and
other UNIX-alike operating systems.

This package contains pcpi PPDs for gutenprint-cups.

%package cups-raven-ppds
Summary: PPDs for CUPS drivers for raven and compatible printers
Group: System/Configuration/Hardware
Requires: gutenprint-cups = %EVR
BuildArch: noarch

%description cups-raven-ppds
Gutenprint is a package of high quality printer drivers for Linux and
other UNIX-alike operating systems.

This package contains raven PPDs for gutenprint-cups.

%package cups-ricoh-ppds
Summary: PPDs for CUPS drivers for ricoh and compatible printers
Group: System/Configuration/Hardware
Requires: gutenprint-cups = %EVR
BuildArch: noarch

%description cups-ricoh-ppds
Gutenprint is a package of high quality printer drivers for Linux and
other UNIX-alike operating systems.

This package contains ricoh PPDs for gutenprint-cups.

%package cups-samsung-ppds
Summary: PPDs for CUPS drivers for samsung and compatible printers
Group: System/Configuration/Hardware
Requires: gutenprint-cups = %EVR
BuildArch: noarch

%description cups-samsung-ppds
Gutenprint is a package of high quality printer drivers for Linux and
other UNIX-alike operating systems.

This package contains samsung PPDs for gutenprint-cups.

%package cups-savin-ppds
Summary: PPDs for CUPS drivers for savin and compatible printers
Group: System/Configuration/Hardware
Requires: gutenprint-cups = %EVR
BuildArch: noarch

%description cups-savin-ppds
Gutenprint is a package of high quality printer drivers for Linux and
other UNIX-alike operating systems.

This package contains savin PPDs for gutenprint-cups.

%package cups-seiko-ppds
Summary: PPDs for CUPS drivers for seiko and compatible printers
Group: System/Configuration/Hardware
Requires: gutenprint-cups = %EVR
BuildArch: noarch

%description cups-seiko-ppds
Gutenprint is a package of high quality printer drivers for Linux and
other UNIX-alike operating systems.

This package contains seiko PPDs for gutenprint-cups.

%package cups-sharp-ppds
Summary: PPDs for CUPS drivers for sharp and compatible printers
Group: System/Configuration/Hardware
Requires: gutenprint-cups = %EVR
BuildArch: noarch

%description cups-sharp-ppds
Gutenprint is a package of high quality printer drivers for Linux and
other UNIX-alike operating systems.

This package contains sharp PPDs for gutenprint-cups.

%package cups-shinko-ppds
Summary: PPDs for CUPS drivers for shinko and compatible printers
Group: System/Configuration/Hardware
Requires: gutenprint-cups = %EVR
BuildArch: noarch

%description cups-shinko-ppds
Gutenprint is a package of high quality printer drivers for Linux and
other UNIX-alike operating systems.

This package contains shinko PPDs for gutenprint-cups.

%package cups-sinfonia-ppds
Summary: PPDs for CUPS drivers for sinfonia and compatible printers
Group: System/Configuration/Hardware
Requires: gutenprint-cups = %EVR
BuildArch: noarch

%description cups-sinfonia-ppds
Gutenprint is a package of high quality printer drivers for Linux and
other UNIX-alike operating systems.

This package contains sinfonia PPDs for gutenprint-cups.

%package cups-sony-ppds
Summary: PPDs for CUPS drivers for sony and compatible printers
Group: System/Configuration/Hardware
Requires: gutenprint-cups = %EVR
BuildArch: noarch

%description cups-sony-ppds
Gutenprint is a package of high quality printer drivers for Linux and
other UNIX-alike operating systems.

This package contains sony PPDs for gutenprint-cups.

%package cups-star-ppds
Summary: PPDs for CUPS drivers for star and compatible printers
Group: System/Configuration/Hardware
Requires: gutenprint-cups = %EVR
BuildArch: noarch

%description cups-star-ppds
Gutenprint is a package of high quality printer drivers for Linux and
other UNIX-alike operating systems.

This package contains star PPDs for gutenprint-cups.

%package cups-stryker-ppds
Summary: PPDs for CUPS drivers for stryker and compatible printers
Group: System/Configuration/Hardware
Requires: gutenprint-cups = %EVR
BuildArch: noarch

%description cups-stryker-ppds
Gutenprint is a package of high quality printer drivers for Linux and
other UNIX-alike operating systems.

This package contains stryker PPDs for gutenprint-cups.

%package cups-tally-ppds
Summary: PPDs for CUPS drivers for tally and compatible printers
Group: System/Configuration/Hardware
Requires: gutenprint-cups = %EVR
BuildArch: noarch

%description cups-tally-ppds
Gutenprint is a package of high quality printer drivers for Linux and
other UNIX-alike operating systems.

This package contains tally PPDs for gutenprint-cups.

%package cups-tektronix-ppds
Summary: PPDs for CUPS drivers for tektronix and compatible printers
Group: System/Configuration/Hardware
Requires: gutenprint-cups = %EVR
BuildArch: noarch

%description cups-tektronix-ppds
Gutenprint is a package of high quality printer drivers for Linux and
other UNIX-alike operating systems.

This package contains tektronix PPDs for gutenprint-cups.

%package cups-toshiba-ppds
Summary: PPDs for CUPS drivers for toshiba and compatible printers
Group: System/Configuration/Hardware
Requires: gutenprint-cups = %EVR
BuildArch: noarch

%description cups-toshiba-ppds
Gutenprint is a package of high quality printer drivers for Linux and
other UNIX-alike operating systems.

This package contains toshiba PPDs for gutenprint-cups.

%package cups-xerox-ppds
Summary: PPDs for CUPS drivers for xerox and compatible printers
Group: System/Configuration/Hardware
Requires: gutenprint-cups = %EVR
BuildArch: noarch

%description cups-xerox-ppds
Gutenprint is a package of high quality printer drivers for Linux and
other UNIX-alike operating systems.

This package contains xerox PPDs for gutenprint-cups.

%prep
%setup
%patch0 -p2
%patch1 -p1
%patch2 -p2
%patch3 -p2
%patch4 -p1
%patch5 -p1
rm -rf gutenprint/po/*.gmo
install %SOURCE2 po/ru.po

%build
%undefine _configure_gettext
# remove old versions of standard macros
find m4* -type f -name \*.m4 -print0 |
	xargs -r0 grep -lxZ 'dnl Copyright (C) .* Free Software Foundation, Inc\.' -- |
	xargs -r0 rm -v --
#rm m4*/libtool.m4
%ifarch %ix86
%add_optflags -D_FILE_OFFSET_BITS=64
%endif
%autoreconf
%configure \
	--enable-shared \
	--disable-static \
	--disable-rpath \
	--with-modules=dlopen \
	--with-cups \
	--without-gimp2 \
	--disable-libgutenprintui2 \
	--enable-cups-ppds \
	--enable-cups-level3-ppds \
	--enable-cups-ppds-at-top-level

%make_build

%install
%makeinstall_std
%define docdir %_docdir/gutenprint-%version
mkdir -p %buildroot%_docdir
mv %buildroot%_datadir/gutenprint/doc %buildroot%docdir
find %buildroot%_libdir/gutenprint/ -name \*.la -delete
chmod +rx %buildroot%_prefix/lib/cups/backend/gutenprint*+usb

# Remove standard library path from rpath
for file in \
  %buildroot%_bindir/* \
  %buildroot%_sbindir/cups-genppd.5.3 \
  %buildroot%_libdir/*.so.* \
  %buildroot%_libexecdir/cups/driver/* \
  %buildroot%_libexecdir/cups/filter/*
do \
  chrpath --delete ${file}
done

%find_lang gutenprint
%set_verify_elf_method strict

%triggerpostun cups -- gutenprint-cups < %version
cups=%_initdir/cups
if [ -x $cups ] && %_sbindir/cups-genppdupdate | grep -Fqs Restart; then
	$cups condreload
fi

%files -f gutenprint.lang
%_bindir/escputil
%_bindir/testpattern
%_datadir/gutenprint/
%_libdir/gutenprint
%_man1dir/*.1*
%exclude %_datadir/locale/*/gutenprint_*.po
%dir %docdir
%docdir/[AFNR]*
%docdir/gutenprint-users-manual.pdf
%exclude %docdir/gutenprint-users-manual.odt
%exclude %docdir/C*

%files -n libgutenprint%soname
%_libdir/libgutenprint.so.%{soname}*

%files -n libgutenprint-devel
%_includedir/%{name}*
%_libdir/*.so
%_pkgconfigdir/*.pc
%dir %docdir
%docdir/gutenprint.pdf
%docdir/reference-html

#files -n gimp-plugin-gutenprint
#_libdir/gimp/2.0/plug-ins/gutenprint

%files cups
%dir %_datadir/cups/model/Global
%_sysconfdir/cups/*
%_bindir/cups-*
%_sbindir/cups-*
%_prefix/lib/cups/backend/gutenprint*+usb
%_prefix/lib/cups/driver/%{name}*
%_prefix/lib/cups/filter/*
%_datadir/cups/usb/net.sf.gimp-print.usb-quirks
%_datadir/cups/calibrate.ppm
%_man8dir/*.8*

%files cups-ppds

%files cups-bjc-ppds
%_datadir/cups/model/Global/stp-bjc*.5.3.ppd.gz

%files cups-brother-ppds
%_datadir/cups/model/Global/stp-brother*.5.3.ppd.gz

%files cups-canon-ppds
%_datadir/cups/model/Global/stp-canon*.5.3.ppd.gz

%files cups-ciaat-ppds
%_datadir/cups/model/Global/stp-ciaat*.5.3.ppd.gz

%files cups-citizen-ppds
%_datadir/cups/model/Global/stp-citizen*.5.3.ppd.gz

%files cups-compaq-ppds
%_datadir/cups/model/Global/stp-compaq*.5.3.ppd.gz

%files cups-datamax-ppds
%_datadir/cups/model/Global/stp-datamax*.5.3.ppd.gz

%files cups-dec-ppds
%_datadir/cups/model/Global/stp-dec*.5.3.ppd.gz

%files cups-dell-ppds
%_datadir/cups/model/Global/stp-dell*.5.3.ppd.gz

%files cups-dnp-ppds
%_datadir/cups/model/Global/stp-dnp*.5.3.ppd.gz

%files cups-epson-ppds
%_datadir/cups/model/Global/stp-epson*.5.3.ppd.gz

%files cups-escp2-ppds
%_datadir/cups/model/Global/stp-escp2*.5.3.ppd.gz

%files cups-fujifilm-ppds
%_datadir/cups/model/Global/stp-fujifilm*.5.3.ppd.gz

%files cups-fujitsu-ppds
%_datadir/cups/model/Global/stp-fujitsu*.5.3.ppd.gz

%files cups-gestetner-ppds
%_datadir/cups/model/Global/stp-gestetner*.5.3.ppd.gz

%files cups-hiti-ppds
%_datadir/cups/model/Global/stp-hiti*.5.3.ppd.gz

%files cups-honeywell-ppds
%_datadir/cups/model/Global/stp-honeywell*.5.3.ppd.gz

%files cups-hp-ppds
%_datadir/cups/model/Global/stp-hp*.5.3.ppd.gz

%files cups-ibm-ppds
%_datadir/cups/model/Global/stp-ibm*.5.3.ppd.gz

%files cups-infotec-ppds
%_datadir/cups/model/Global/stp-infotec*.5.3.ppd.gz

%files cups-joyspace-ppds
%_datadir/cups/model/Global/stp-joyspace*.5.3.ppd.gz

%files cups-kodak-ppds
%_datadir/cups/model/Global/stp-kodak*.5.3.ppd.gz

%files cups-kyocera-ppds
%_datadir/cups/model/Global/stp-kyocera*.5.3.ppd.gz

%files cups-lanier-ppds
%_datadir/cups/model/Global/stp-lanier*.5.3.ppd.gz

%files cups-lexmark-ppds
%_datadir/cups/model/Global/stp-lexmark*.5.3.ppd.gz

%files cups-magicard-ppds
%_datadir/cups/model/Global/stp-magicard*.5.3.ppd.gz

%files cups-minolta-ppds
%_datadir/cups/model/Global/stp-minolta*.5.3.ppd.gz

%files cups-mitsubishi-ppds
%_datadir/cups/model/Global/stp-mitsubishi*.5.3.ppd.gz

%files cups-nec-ppds
%_datadir/cups/model/Global/stp-nec*.5.3.ppd.gz

%files cups-nidalcopac-ppds
%_datadir/cups/model/Global/stp-nidalcopac*.5.3.ppd.gz

%files cups-nrg-ppds
%_datadir/cups/model/Global/stp-nrg*.5.3.ppd.gz

%files cups-oki-ppds
%_datadir/cups/model/Global/stp-oki-*.5.3.ppd.gz

%files cups-okidata-ppds
%_datadir/cups/model/Global/stp-okidata*.5.3.ppd.gz

%files cups-olivetti-ppds
%_datadir/cups/model/Global/stp-olivetti*.5.3.ppd.gz

%files cups-olmec-ppds
%_datadir/cups/model/Global/stp-olmec*.5.3.ppd.gz

%files cups-olympus-ppds
%_datadir/cups/model/Global/stp-olympus*.5.3.ppd.gz

%files cups-panasonic-ppds
%_datadir/cups/model/Global/stp-panasonic*.5.3.ppd.gz

%files cups-pantum-ppds
%_datadir/cups/model/Global/stp-pantum*.5.3.ppd.gz

%files cups-pcl-ppds
%_datadir/cups/model/Global/stp-pcl*.5.3.ppd.gz

%files cups-pcpi-ppds
%_datadir/cups/model/Global/stp-pcpi*.5.3.ppd.gz

%files cups-raven-ppds
%_datadir/cups/model/Global/stp-raven*.5.3.ppd.gz

%files cups-ricoh-ppds
%_datadir/cups/model/Global/stp-ricoh*.5.3.ppd.gz

%files cups-samsung-ppds
%_datadir/cups/model/Global/stp-samsung*.5.3.ppd.gz

%files cups-savin-ppds
%_datadir/cups/model/Global/stp-savin*.5.3.ppd.gz

%files cups-seiko-ppds
%_datadir/cups/model/Global/stp-seiko*.5.3.ppd.gz

%files cups-sharp-ppds
%_datadir/cups/model/Global/stp-sharp*.5.3.ppd.gz

%files cups-shinko-ppds
%_datadir/cups/model/Global/stp-shinko*.5.3.ppd.gz

%files cups-sinfonia-ppds
%_datadir/cups/model/Global/stp-sinfonia*.5.3.ppd.gz

%files cups-sony-ppds
%_datadir/cups/model/Global/stp-sony*.5.3.ppd.gz

%files cups-star-ppds
%_datadir/cups/model/Global/stp-star*.5.3.ppd.gz

%files cups-stryker-ppds
%_datadir/cups/model/Global/stp-stryker*.5.3.ppd.gz

%files cups-tally-ppds
%_datadir/cups/model/Global/stp-tally*.5.3.ppd.gz

%files cups-tektronix-ppds
%_datadir/cups/model/Global/stp-tektronix*.5.3.ppd.gz

%files cups-toshiba-ppds
%_datadir/cups/model/Global/stp-toshiba*.5.3.ppd.gz

%files cups-xerox-ppds
%_datadir/cups/model/Global/stp-xerox*.5.3.ppd.gz

%changelog
* Wed May 20 2026 Anton Farygin <rider@altlinux.org> 1:5.3.5-alt2
- add Pantum P3300DN PCL XL driver with cupsBackSide: Rotated to fix
  upside-down second page in duplex printing (closes: #59029).
- new subpackage gutenprint-cups-pantum-ppds.

* Tue Apr 15 2025 Constantin Sunzow <protvin@altlinux.org> 1:5.3.5-alt1
- Split PPDs package by printer families.
- Fix bug 53779.
- New version.

* Wed Feb 12 2025 Valery Inozemtsev <shrek@altlinux.ru> 1:5.3.4-alt3
- disabled gimp-plugin

* Mon Oct 30 2023 Mikhail Chernonog <snowmix@altlinux.org> 1:5.3.4-alt2
- Added support for the manually tested Oki MB472 printer.

* Thu Dec 17 2020 Andrey Cherepanov <cas@altlinux.org> 1:5.3.4-alt1
- New version.
- Package watch file.

* Tue Dec 03 2019 Andrey Cherepanov <cas@altlinux.org> 1:5.3.3-alt1
- New version.

* Thu Oct 31 2019 Lenar Shakirov <snejok@altlinux.ru> 1:5.3.1-alt2
- Make gutenprint-cups-ppds noarch

* Mon Dec 17 2018 Andrey Cherepanov <cas@altlinux.org> 1:5.3.1-alt1
- New version.

* Sun Oct 14 2018 Igor Vlasenko <viy@altlinux.ru> 1:5.2.14-alt1.qa1
- NMU: applied repocop patch

* Thu Jun 07 2018 Andrey Cherepanov <cas@altlinux.org> 1:5.2.14-alt1
- New version (ALT #34674).
- Rename gutenprint-CUPS to gutenprint-cups.
- Enable support of CUPS dyesub USB backend.
- Enable localized ppds.
- Removed Foomatic data generator and the Ghostscript IJS driver.
- Put all PPDs to package gutenprint-cups-ppds.

* Wed Mar 20 2013 Fr. Br. George <george@altlinux.ru> 1:5.2.9-alt1
- Version up
- Fix i586 FILE64 build

* Sat Jun 16 2012 Michael Shigorin <mike@altlinux.org> 1:5.2.8-alt1
- 5.2.8
  + updated patch
  + fixed build with current binutils
- buildreq

* Sat Dec 03 2011 Dmitry V. Levin <ldv@altlinux.org> 1:5.2.7-alt2
- Fixed build, updated build dependencies.
- Fixed packaging of documentation.
- Cleaned up descriptions.
- Disabled build of static libraries.
- Built %name-foomatic as noarch.

* Fri May 27 2011 Valery Inozemtsev <shrek@altlinux.ru> 1:5.2.7-alt1
- 5.2.7

* Tue Nov 23 2010 Valery Inozemtsev <shrek@altlinux.ru> 1:5.2.6-alt2
- rebuild

* Sun Aug 22 2010 Valery Inozemtsev <shrek@altlinux.ru> 1:5.2.6-alt1
- 5.2.6

* Mon Feb 15 2010 Valery Inozemtsev <shrek@altlinux.ru> 1:5.2.5-alt1
- 5.2.5

* Thu Sep 17 2009 Valery Inozemtsev <shrek@altlinux.ru> 1:5.2.4-alt2
- added trigger for update PPD (closes: #20952)

* Fri Jul 31 2009 Valery Inozemtsev <shrek@altlinux.ru> 1:5.2.4-alt1
- 5.2.4

* Mon May 25 2009 Valery Inozemtsev <shrek@altlinux.ru> 1:5.2.3-alt2
- fixed headers install

* Tue Dec 23 2008 Valery Inozemtsev <shrek@altlinux.ru> 1:5.2.3-alt1
- 5.2.3

* Thu Nov 20 2008 Valery Inozemtsev <shrek@altlinux.ru> 1:5.2.2-alt1
- 5.2.2

* Tue Oct 28 2008 Valery Inozemtsev <shrek@altlinux.ru> 1:5.2.1-alt1.M41.1
- build for branch 4.1

* Tue Oct 28 2008 Valery Inozemtsev <shrek@altlinux.ru> 1:5.2.1-alt2
- added russian translation (Alexandre Prokoudine)

* Wed Oct 22 2008 Valery Inozemtsev <shrek@altlinux.ru> 1:5.2.1-alt1
- 5.2.1

* Tue Oct 14 2008 Valery Inozemtsev <shrek@altlinux.ru> 1:5.2.0-alt0.M41.1.rc1
- build for branch 4.1

* Mon Oct 06 2008 Valery Inozemtsev <shrek@altlinux.ru> 1:5.2.0-alt1.rc1
- 5.2.0 RC1

* Fri Mar 14 2008 Valery Inozemtsev <shrek@altlinux.ru> 1:5.1.7-alt1
- 5.1.7

* Fri Feb 29 2008 Valery Inozemtsev <shrek@altlinux.ru> 1:5.1.6-alt2
- relocation all filters to gutenprint subpackage (close #14690)

* Sat Jan 05 2008 Valery Inozemtsev <shrek@altlinux.ru> 1:5.1.6-alt1
- 5.1.6

* Sat Dec 29 2007 Valery Inozemtsev <shrek@altlinux.ru> 1:5.1.4-alt1
- 5.1.4

* Thu Nov 01 2007 Valery Inozemtsev <shrek@altlinux.ru> 1:5.0.1-alt3.M40.1
- build for branch 4.0

* Thu Nov 01 2007 Valery Inozemtsev <shrek@altlinux.ru> 1:5.0.1-alt4
- put "A4" at the beginning to get it as default size

* Tue Oct 02 2007 Valery Inozemtsev <shrek@altlinux.ru> 1:5.0.1-alt3
- drop update-printers-db in %%post from %name-CUPS and %name-foomatic

* Sat Sep 29 2007 Valery Inozemtsev <shrek@altlinux.ru> 1:5.0.1-alt2
- not install gutenprintui.pc (close #12969)

* Sat Jun 23 2007 Valery Inozemtsev <shrek@altlinux.ru> 1:5.0.1-alt1
- 5.0.1 stable release

* Fri Jun 22 2007 Valery Inozemtsev <shrek@altlinux.ru> 5.1.3-alt1
- 5.1.3

* Sun Jun 03 2007 Valery Inozemtsev <shrek@altlinux.ru> 5.1.2-alt1
- 5.1.2
- fixed prereq for %name-{foomatic,CUPS}

* Wed May 23 2007 Valery Inozemtsev <shrek@altlinux.ru> 5.1.1-alt3
- fixed provides/obsoletes

* Wed May 23 2007 Valery Inozemtsev <shrek@altlinux.ru> 5.1.1-alt2
- added requires lib%name-%%version-%%release for %name
- spec cleanup

* Mon May 21 2007 Valery Inozemtsev <shrek@altlinux.ru> 5.1.1-alt1
- 5.1.1
- disable static

* Mon Apr 16 2007 ALT QA Team Robot <qa-robot@altlinux.org> 4.2.7-alt4.0
- Automated rebuild.

* Fri May 26 2006 Stanislav Ievlev <inger@altlinux.org> 4.2.7-alt4
- rebuild with cups-1.2

* Fri Mar 24 2006 Stanislav Ievlev <inger@altlinux.org> 4.2.7-alt3
- rebuild with new ijs

* Fri Dec 30 2005 ALT QA Team Robot <qa-robot@altlinux.org> 4.2.7-alt2.1.1
- Rebuilt with libreadline.so.5.

* Wed Jun 29 2005 Anton D. Kachalov <mouse@altlinux.org> 4.2.7-alt2.1
- multilib hack

* Fri Jan 28 2005 Stanislav Ievlev <inger@altlinux.org> 4.2.7-alt2
- added update-printers-db in post script

* Wed Sep 22 2004 Stanislav Ievlev <inger@altlinux.org> 4.2.7-alt1
- 4.2.7

* Fri Sep 17 2004 ALT QA Team Robot <qa-robot@altlinux.org> 4.2.6-alt2.1.1.1
- Rebuilt with libtiff.so.4.

* Tue May 11 2004 ALT QA Team Robot <qa-robot@altlinux.org> 4.2.6-alt2.1.1
- Rebuilt with openssl-0.9.7d.

* Fri May 07 2004 Stanislav Ievlev <inger@altlinux.org> 4.2.6-alt2.1
- rebuild without plugin for old gimp

* Fri Apr 02 2004 Stanislav Ievlev <inger@altlinux.org> 4.2.6-alt2
- added russian translation by Valia V. Vaneeva

* Wed Feb 11 2004 Stanislav Ievlev <inger@altlinux.org> 4.2.6-alt1
- final

* Thu Dec 25 2003 Stanislav Ievlev <inger@altlinux.org> 4.2.6-alt0.2
- gimp-print-foomatic requires latest foomatic (>=3.0.1) (was changes id's in xml files)

* Thu Dec 25 2003 Stanislav Ievlev <inger@altlinux.org> 4.2.6-alt0.1
- 4.2.6-pre2

* Tue Sep 30 2003 Stanislav Ievlev <inger@altlinux.ru> 4.2.5-alt3
- fix building in hasher

* Mon Mar 31 2003 Stanislav Ievlev <inger@altlinux.ru> 4.2.5-alt2
- Apply patch for foomatic database (from MDK)

* Thu Feb 27 2003 Stanislav Ievlev <inger@altlinux.ru> 4.2.5-alt1
- 4.2.5

* Thu Jan 09 2003 Stanislav Ievlev <inger@altlinux.ru> 4.2.4-alt1
- update to latest stable

* Mon Oct 28 2002 Stanislav Ievlev <inger@altlinux.ru> 4.2.3-alt1
- 4.2.3

* Fri Sep 20 2002 Stanislav Ievlev <inger@altlinux.ru> 4.2.2-alt1
- 4.2.2
- port to subst from 'perl -pi'

* Wed Jun 26 2002 Stanislav Ievlev <inger@altlinux.ru> 4.2.1-alt3
- Enable IJS driver

* Tue Jun 18 2002 Stanislav Ievlev <inger@altlinux.ru> 4.2.1-alt2
- resurrected foomatic files

* Tue Apr 02 2002 Stanislav Ievlev <inger@altlinux.ru> 4.2.0-alt7
- Added two patches from MDK (to use drivers for more printers and 
  support for small papers on Epson Stylus Pro printers)

* Wed Feb 20 2002 Stanislav Ievlev <inger@altlinux.ru> 4.2.0-alt6
- Buildreq updated

* Tue Feb 19 2002 Stanislav Ievlev <inger@altlinux.ru> 4.2.0-alt5
- added patch.

* Wed Feb 13 2002 AEN <aen@logic.ru> 4.2.0-alt4
- rebuilt with new gimp

* Mon Dec 17 2001 Stanislav Ievlev <inger@altlinux.ru> 4.2.0-alt3
- added requires to gimp-print-foomatic

* Mon Dec 10 2001 Stanislav Ievlev <inger@altlinux.ru> 4.2.0-alt2
- added buildreqs, fix docs

* Thu Nov 15 2001 Stanislav Ievlev <inger@altlinux.ru> 4.1.99-alt6
- rc1

* Tue Sep 25 2001 Stanislav Ievlev <inger@altlinux.ru> 4.1.99-alt5
- b2

* Thu Sep 06 2001 Stanislav Ievlev <inger@altlinux.ru> 4.1.99-alt4
- new snapshot.

* Mon Aug 13 2001 Stanislav Ievlev <inger@altlinux.ru> 4.1.99-alt3
- Splited again: common files (filters,docs); CUPS only drivers, foomatic only drivers.

* Fri Aug 10 2001 AEN <aen@logic.ru> 4.1.99-alt2
- added plugin package
- a2

* Mon Aug 06 2001 Stanislav Ievlev <inger@altlinux.ru> 4.1.99-alt1
- Initial release for ALT Linux.
- Now we are splitting cups-drivers into separate packages.
