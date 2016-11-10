%def_enable cupstifffilter
%def_enable sane_backend
%def_enable python_code
%def_enable autostart
%def_enable PPDs
%def_disable qt3
%def_enable qt4
%def_disable qt5
%def_enable policykit
# udev >= 145
# note: flag dropped upstream
%def_enable udevacl
%def_disable halacl
%def_without python3
%if_with backport
%define cups_filters foomatic-filters
%else
%define cups_filters cups-filters >= 1.0.46-alt1
%endif
%if_with python3
%define pysuffix 3
%else
%define pysuffix %nil
%endif

Summary: Solution for printing, scanning, and faxing with Hewlett-Packard inkjet and laser printers.
Name: hplip
Epoch: 1
Version: 3.16.7
Release: alt2
License: GPL/MIT/BSD
Group: Publishing
URL: http://hplip.sourceforge.net
Packager: Igor Vlasenko <viy@altlinux.org>

%define hpijsname hpijs

Conflicts: ghostscript <= 7.05-alt15
Obsoletes: hpoj <= 0.91
Provides: cups-backend-ptal
Obsoletes: cups-backend-ptal
Conflicts: cups < 1.1.18-alt7

PreReq:	cups
Requires: %name-common = %{?epoch:%epoch:}%version-%release

# TODO: split hplip and hplip-utils
# and remove this Req:
Requires: %name-hpcups = %{?epoch:%epoch:}%version-%release

# Main package requires wget to avoid
# misleading errors about network connectivity (fc bug #705843).
Requires: wget

# for hplip/base/validation.py (fc bug #1118724).
Requires: gnupg

%if_enabled python_code
###Requires: python
%if_with python3
%add_python3_lib_path %_datadir/%name
%else
%add_python_lib_path %_datadir/%name
%endif
# Andy Kuleshov report
Requires: python%{pysuffix}-module-dbus python%{pysuffix}-modules-ctypes
%endif

Requires: service => 0.5.9-alt1

BuildPreReq: libsane-devel
# Automatically added by buildreq on Thu Sep 22 2005
BuildRequires: gcc-c++ libcups-devel libjpeg-devel libnet-snmp-devel libssl-devel libstdc++-devel libusb-devel libusb-compat-devel libdbus-devel

%if_enabled python_code
#BuildRequires: python-module-qt-devel
BuildRequires: python%{pysuffix}-module-PyQt4-devel
#RemovedBuildRequires: python-base python-dev python-modules-compiler python-modules-encodings
BuildRequires: python%{pysuffix}-devel
%endif

%if_enabled PPDs
#cups-common and foomatic-filters is for cupstestppd
BuildPreReq: perl cups-common %{cups_filters}
%endif

Source: http://dl.sourceforge.net/hplip/%name-%version.tar
Source2: %name.init
Source4: 80-hpmud.perms
Source5: %name.png
Source6: %name-icons.tar
Source7: %name-fixppd.sh
Source8: %name.watch
Source9: upstream-signing-key.asc

#TODO: see what fdi is better:
# https://bugzilla.redhat.com/show_bug.cgi?id=478495
# https://bugzilla.redhat.com/show_bug.cgi?id=479648
# fedora fdi acl policy
Source100: hplip.fdi
# cvs update: hplip.fdi is no longer in the repository (due to udev-acl)
Source102: copy-deviceids.py
Source101: hpcups-update-ppds.sh

# OpenSuSE based sources
# deprecated; 2.7.7 shows 'can't connect to device'
Source201: hp-toolbox.wrapper
Source202: hpijs.1

Patch1: hplip-3.12.9-alt-urlhandler.patch
# dead patch 2
Patch2: hplip-3.9.12-alt-fix-udev-rules-ppdev.patch
Patch4: hplip-3.9.12-alt-hplip-desktop.patch
Patch5: hplip-3.15.9-alt-link-libhpipp.patch
Patch6: hplip-3.15.9-alt-systemd.patch
Patch7: hplip-3.16.7-alt-link-python2.patch
Patch8: hplip-3.16.7-alt-link-python3.patch

Patch10: http://www.linuxprinting.org/download/printing/hpijs/hpijs-1.4.1-rss.1.patch
# it is patch 10 rediffed
Patch11: hpijs-1.4.1-rss-alt-for-2.7.7.patch

# fedora patches
Patch101: fedora-3.16.7-1-hplip-pstotiff-is-rubbish.patch
Patch102: fedora-3.16.7-1-hplip-strstr-const.patch
Patch103: fedora-3.16.7-1-hplip-ui-optional.patch
Patch104: fedora-3.16.7-1-hplip-no-asm.patch
Patch105: fedora-3.16.7-1-hplip-deviceIDs-drv.patch
Patch106: fedora-3.16.7-1-hplip-udev-rules.patch
Patch107: fedora-3.16.7-1-hplip-retry-open.patch
Patch108: fedora-3.16.7-1-hplip-snmp-quirks.patch
Patch109: fedora-3.16.7-1-hplip-hpijs-marker-supply.patch
Patch110: fedora-3.16.7-1-hplip-clear-old-state-reasons.patch
Patch111: fedora-3.16.7-1-hplip-hpcups-sigpipe.patch
Patch112: fedora-3.16.7-1-hplip-logdir.patch
Patch113: fedora-3.16.7-1-hplip-bad-low-ink-warning.patch
Patch114: fedora-3.16.7-1-hplip-deviceIDs-ppd.patch
Patch115: fedora-3.16.7-1-hplip-ppd-ImageableArea.patch
Patch116: fedora-3.16.7-1-hplip-scan-tmp.patch
Patch117: fedora-3.16.7-1-hplip-log-stderr.patch
Patch118: fedora-3.16.7-1-hplip-avahi-parsing.patch
Patch120: fedora-3.16.7-1-hplip-dj990c-margin.patch
Patch121: fedora-3.16.7-1-hplip-strncpy.patch
Patch122: fedora-3.16.7-1-hplip-no-write-bytecode.patch
Patch123: fedora-3.16.7-1-hplip-silence-ioerror.patch
Patch124: fedora-3.16.7-1-hplip-3165-sourceoption.patch
Patch125: fedora-3.16.7-1-hplip-include-ppdh.patch


%description
This is the HP driver package to supply Linux support for most
Hewlett-Packard DeskJet, LaserJet, PSC, OfficeJet, and PhotoSmart
printers and all-in-one peripherals (also known as Multi-Function
Peripherals or MFPs), which can print, scan, copy, fax, and/or access
flash memory cards.

This package contains various tools for memory card access,
ink/toner/battery/consumable level checking, and inkjet printer
maintenance, along with python cups backends.

%package hpcups
Summary: Hpcups printer driver for Hewlett-Packard Co. Inkjet Printers and MFPs
License: BSD
Group: Publishing
Requires: %name-common = %{?epoch:%epoch:}%version-%release
Conflicts: %name-common < 3.13

%description hpcups
Hpcups driver is a raster driver that produces printer-ready-bits.
The hpcups driver only works CUPS. Hpcups does not use the APDK, but
is based on re-purposed APDK code.

%if_enabled python_code
%package gui
Summary: HPLIP graphical tools for Hewlett-Packard Co. Inkjet Printers and MFPs
License: GPL
Group: Publishing
Obsoletes: xojpanel <= 0.91
Obsoletes: hpoj-xojpanel <= 0.91
Obsoletes: hplip-tools < 2.0
Provides: hplip-tools = 2.0
BuildArch: noarch

%if_enabled qt3
Requires: python%{pysuffix}-module-qt >= 3.16
%endif
%if_enabled qt4
Requires: python%{pysuffix}-module-PyQt4
%else
Requires: python%{pysuffix}-module-PyQt5
%endif

# some utils do require dbus user session
Requires: dbus-tools-gui
# for hp-scan -n
Requires: python%{pysuffix}-module-imaging
# from fedora 3.10.9-9 patch 33 (= 133)
# Enable D-Bus threading (and require pygobject2) (bug #600932).
# patch33 -p1 -b .dbus-threads
Requires: python%{pysuffix}-module-pygobject

Requires: %name = %{?epoch:%epoch:}%version-%release
%if_enabled PPDs
Requires: %name-PPDs >= %{?epoch:%epoch:}%version-%release
%endif

%description gui
HPLIP is an HP developed solution for printing, scanning, and faxing
with HP inkjet and laser based printers in Linux.

The HPLIP project provides printing support for nearly 1000 printer
models, including Deskjet, Officejet, Photosmart, PSC (Print Scan Copy),
Business Inkjet, LaserJet, and LaserJet MFP.

This package contains the gui toolbox application for HPLIP,
with which several tasks such as memory card access,
ink/toner/battery/consumable level checking, and inkjet printer
maintenance can be done.

%if_enabled autostart
%package gui-autostart
Summary: GNOME/KDE/other XDGE autostart file for HPLIP graphical tools
License: GPL
Group: Publishing
Requires: %name-gui = %{?epoch:%epoch:}%version-%release
BuildArch: noarch

%description gui-autostart
HPLIP is an HP developed solution for printing, scanning, and faxing
with HP inkjet and laser based printers in Linux.

The HPLIP project provides printing support for nearly 1000 printer
models, including Deskjet, Officejet, Photosmart, PSC (Print Scan Copy),
Business Inkjet, LaserJet, and LaserJet MFP.

This package contains the HPLIP gui toolbox application autostart file
for GNOME, KDE and other freedesktop compatible desktop environments.
%endif
%endif

%package recommends
Summary: recommended packages for hplip
License: GPL
Group: Publishing
Requires: cups-ddk
Requires: foomatic-db >= 3.0.2-alt7
Requires: %{cups_filters}
Requires: %name = %{?epoch:%epoch:}%version-%release
BuildArch: noarch

%description recommends
HPLIP is an HP developed solution for printing, scanning, and faxing
with HP inkjet and laser based printers in Linux.

The HPLIP project provides printing support for nearly 1000 printer
models, including Deskjet, Officejet, Photosmart, PSC (Print Scan Copy),

This package is a virtual package that installs packages
recommended for use with hplip.

%package common
Summary: Hewlett-Packard Co. Inkjet Driver Project
License: GPL
Group: Publishing
Conflicts: udev-extras < 0.20090516-alt4

%description common
HPLIP is an HP developed solution for printing, scanning, and faxing
with HP inkjet and laser based printers in Linux.

The HPLIP project provides printing support for nearly 1000 printer
models, including Deskjet, Officejet, Photosmart, PSC (Print Scan Copy),

This package contains common libraries for
The Hewlett-Packard  Inkjet  Driver  Project.

%description
This is the HP driver package to supply Linux support for most
Hewlett-Packard DeskJet, LaserJet, PSC, OfficeJet, and PhotoSmart
printers and all-in-one peripherals (also known as Multi-Function
Peripherals or MFPs), which can print, scan, copy, fax, and/or access
flash memory cards.

%if_enabled PPDs
%package PPDs
Summary: PPDs for Hewlett-Packard Co. Inkjet Printers and MFPs
License: MIT
Group: Publishing
Requires: %name-ps-PPDs = %{?epoch:%epoch:}%version-%release
Requires: %name-hpcups-PPDs = %{?epoch:%epoch:}%version-%release
Requires: %name-hpijs-PPDs = %{?epoch:%epoch:}%version-%release
# due to foomatic-rip
Requires:	%{cups_filters}
BuildArch: noarch

%description PPDs
HPLIP is an HP developed solution for printing, scanning, and faxing
with HP inkjet and laser based printers in Linux.

The HPLIP project provides printing support for nearly 1000 printer
models, including Deskjet, Officejet, Photosmart, PSC (Print Scan Copy),


%package ps-PPDs
Summary: PPDs for Hewlett-Packard Co. Inkjet Printers and MFPs for postscript HP printers
License: MIT
Group: Publishing
# due to foomatic-rip
Requires:	%{cups_filters}
Conflicts: %name-PPDs < %version
BuildArch: noarch

%description ps-PPDs
HPLIP is an HP developed solution for printing, scanning, and faxing
with HP inkjet and laser based printers in Linux.

The HPLIP project provides printing support for nearly 1000 printer
models, including Deskjet, Officejet, Photosmart, PSC (Print Scan Copy),

This package contains postscript printer definition files (PPDs) for postscript HP printers.

%package hpcups-PPDs
Summary: PPDs for Hewlett-Packard Co. Inkjet Printers and MFPs for hpcups cups driver
License: MIT
Group: Publishing
# due to foomatic-rip
Requires:	%{cups_filters}
Requires: %name-hpcups = %{?epoch:%epoch:}%version-%release
Conflicts: %name-PPDs < %version
BuildArch: noarch

%description hpcups-PPDs
HPLIP is an HP developed solution for printing, scanning, and faxing
with HP inkjet and laser based printers in Linux.

The HPLIP project provides printing support for nearly 1000 printer
models, including Deskjet, Officejet, Photosmart, PSC (Print Scan Copy),

This package contains postscript printer definition files (PPDs) for hpcups cups driver.

%package hpijs-PPDs
Summary: PPDs for Hewlett-Packard Co. Inkjet Printers and MFPs for hpijs cups driver
License: MIT
Group: Publishing
# due to foomatic-rip
Requires:	%{cups_filters}
Requires: %name-hpijs = %{?epoch:%epoch:}%version-%release
Conflicts: %name-PPDs < %version
BuildArch: noarch

%description hpijs-PPDs
HPLIP is an HP developed solution for printing, scanning, and faxing
with HP inkjet and laser based printers in Linux.

The HPLIP project provides printing support for nearly 1000 printer
models, including Deskjet, Officejet, Photosmart, PSC (Print Scan Copy),

This package contains postscript printer definition files (PPDs) for hpijs cups driver.
%endif

%package hpijs
Summary: Hewlett-Packard Co. Inkjet Driver Project
License: BSD
Group: Publishing
Obsoletes: hpijs < 2.7
Provides: %hpijsname = %version
Requires: %name-common = %{?epoch:%epoch:}%version-%release
Requires: ghostscript

%description hpijs
hpijs is a collection of optimized drivers for HP printers.
hpijs supports the DeskJet 350C, 600C, 600C Photo, 630C, Apollo 2000,
Apollo 2100, Apollo 2560, DeskJet 800C, DeskJet 825, DeskJet 900,
PhotoSmart, DeskJet 990C, and PhotoSmart 100 series.

The  Hewlett-Packard  Inkjet  Driver  Project  is  a add-on to the GNU
Ghostscript  application. This driver is open source software based on
the  Hewlett  Packard  Appliance  Printing Development Kit APDK for
deskjet printers.

%if_enabled sane_backend
%package sane
Summary: SANE driver for scanners in HP's multi-function devices (from HPLIP)
License: GPL
Group: Publishing
Requires: libsane
Requires: %name-common = %{?epoch:%epoch:}%version-%release
Obsoletes: libsane-hpoj <= 0.91

%description sane
SANE driver for scanners in HP's multi-function devices (from HPLIP)
%endif # sane_backend

%prep
%setup -q
%patch1 -p2
# let keep it as is.
#patch2 -p2

# # Fix desktop file.
%patch4 -p1 -b .desktop
%patch5 -p1
%patch6 -p1
%if_with python3
#patch8 -p2
%else
#patch7 -p2
%endif


# The pstotiff filter is rubbish so replace it (launchpad #528394).
%patch101 -p1 -b .pstotiff-is-rubbish

# Fix compilation.
%patch102 -p1 -b .strstr-const

# Make utils.checkPyQtImport() look for the gui sub-package (bug #243273).
%patch103 -p1 -b .ui-optional

# Make sure to avoid handwritten asm.
%patch104 -p1 -b .no-asm

# Corrected several IEEE 1284 Device IDs using foomatic data.
# Color LaserJet 2500 series (bug #659040)
# LaserJet 4100 Series/2100 Series (bug #659039)
%patch105 -p1 -b .deviceIDs-drv
chmod +x %{SOURCE102}
mv prnt/drv/hpijs.drv.in{,.deviceIDs-drv-hpijs}
%{SOURCE102} prnt/drv/hpcups.drv.in \
       prnt/drv/hpijs.drv.in.deviceIDs-drv-hpijs \
       > prnt/drv/hpijs.drv.in

# Move udev rules from /etc/ to /usr/lib/ (bug #748208).
%patch106 -p1 -b .udev-rules

# Retry when connecting to device fails (bug #532112).
%patch107 -p1 -b .retry-open

# Mark SNMP quirks in PPD for HP OfficeJet Pro 8500 (bug #581825).
%patch108 -p1 -b .snmp-quirks

# Fixed bogus low ink warnings from hpijs driver (bug #643643).
%patch109 -p1 -b .hpijs-marker-supply

# Clear old printer-state-reasons we used to manage (bug #510926).
%patch110 -p1 -b .clear-old-state-reasons

# Avoid busy loop in hpcups when backend has exited (bug #525944).
%patch111 -p1 -b .hpcups-sigpipe

# CUPS filters should use TMPDIR when available (bug #865603).
%patch112 -p1 -b .logdir

# Fixed Device ID parsing code in hpijs's dj9xxvip.c (bug #510926).
%patch113 -p1 -b .bad-low-ink-warning

# Add Device ID for
# HP LaserJet Color M451dn (bug #1159380)
%patch114 -p1 -b .deviceIDs-ppd

# Fix ImageableArea for Laserjet 8150/9000 (bug #596298).
%patch115 -p1 -b .ImageableArea

# Scan to /var/tmp instead of /tmp (bug #1076954).
%patch116 -p1 -b .scan-tmp

# Treat logging before importing of logger module (bug #984699).
%patch117 -p1 -b .log-stderr

# Fix parsing of avahi-daemon output (bug #1096939).
%patch118 -p1 -b .parsing

# Fixed left/right margins for HP DeskJet 990C (LP #1405212).
%patch120 -p1 -b .dj990c-margin

# Fixed uses of strncpy throughout.
%patch121 -p1 -b .strncpy

# Don't try to write bytecode cache for hpfax backend (bug #1192761)
# or hp-config_usb_printer (bug #1266903)
# or hpps filter (bug #1241548).
%patch122 -p1 -b .no-write-bytecode

# Ignore IOError when logging output (bug #712537).
%patch123 -p1 -b .silence-ioerror
 
# [abrt] hplip: hp-scan:663:<module>:NameError: name 'source_option' is not defined (bug #1341304)
%patch124 -p1 -b .sourceoption

%patch125 -p1 -b .include-ppdh

# from fedora 3.9.12-3/3.10.9-9
sed -i.duplex-constraints \
    -e 's,\(UIConstraints.* \*Duplex\),//\1,' \
    prnt/drv/hpcups.drv.in


tar -xf %SOURCE6

#pushd prnt/hpijs
#%patch10 -p1
#popd
# it is patch 10 rediffed
%patch11 -p1

fgrep -lZr '#!/usr/bin/env python' . | xargs -r0 sed -i 's,#!/usr/bin/env python,#!/usr/bin/python%{pysuffix},'

%build

for i in ppd/hpijs/*.ppd ppd/hpcups/*.ppd ; do
    sed -i s,foomatic-rip-hplip,foomatic-rip,g $i
done
# we use source that is not pristine; in upstream they gzipped it :(
gzip_n_mov_ppd() {
#	mkdir tmp1; cp -a $1/*.ppd tmp1
	gzip -9 $1/*.ppd
#	mv tmp1/*.ppd $1/; rmdir tmp1
}

gzip -9 fax/ppd/HP-Fax*-hpcups.ppd fax/ppd/HP-Fax*-hpijs.ppd
#gzip -9 prnt/ps/*.ppd
#gzip -9 ppd/*.ppd
gzip_n_mov_ppd prnt/ps
gzip_n_mov_ppd ppd/hpijs
gzip_n_mov_ppd ppd/hpcups

# Work-around Makefile.am imperfections.
sed -i 's|^AM_INIT_AUTOMAKE|AM_INIT_AUTOMAKE([foreign subdir-objects])|g' configure.in
# Upstream uses old libtool, which causes problems (due to libhpmud requiring
# libhpdiscovery) when we try to remove rpath from it.
# Regenerating all autotools files works-around these rpath issues.
autoreconf -fisv

cat > /dev/null <<EOF
  --disable-option-checking  ignore unrecognized --enable/--with options
  --enable-static[=PKGS]  build static libraries [default=no]
  --disable-dependency-tracking  speeds up one-time build
  --enable-dependency-tracking   do not reject slow dependency extractors
  --enable-shared[=PKGS]  build shared libraries [default=yes]
  --enable-doc-build     enable documentation build (default=yes)
  --enable-hpijs-only-build     enable hpijs only build (default=yes)
  --enable-lite-build     enable lite build, print & scan only (default=no)
  --enable-hpcups-only-build     enable hpcups only build, print only (default=no)
  --enable-hpijs-install     enable hpijs install (default=no)
  --enable-hpcups-install     enable hpcups install (default=yes)
  --enable-new-hpcups     enable new hpcups install (default=no)
  --enable-network-build    enable network build (default=yes)
  --enable-pp-build    enable parallel port build (default=no)
  --enable-scan-build    enable scanner build (default=yes)
  --enable-gui-build    enable gui build (default=yes)
  --enable-fax-build    enable fax build (default=yes)
  --enable-dbus-build    enable dbus build (default=yes)
  --enable-cups11-build    enable cups 1.1.x build (default=no)
  --enable-udev-acl-rules    enable udev acl rules (default=no)
  --enable-shadow-build    enable shadow build (default=no)
  --enable-foomatic-ppd-install    enable foomatic static ppd install (default=no), uses hpppddir
  --enable-foomatic-drv-install    enable foomatic dynamic ppd install (default=no), uses drvdir and hpppddir
  --enable-cups-drv-install    enable cups dynamic ppd install (default=yes), uses drvdir and hpppddir
  --enable-cups-ppd-install    enable cups static ppd install (default=no), uses hpppddir
  --enable-foomatic-rip-hplip-install    enable foomatic-rip-hplip install (default=no), uses cupsfilterdir
  --enable-qt4    enable qt4 (default=yes)
  --enable-qt3    enable qt3 (default=no)
  --enable-policykit    enable PolicyKit (default=no)
EOF

#we install foomatic data in separate package
# TODO
%configure \
    --with-mimedir=%{_datadir}/cups/mime \
    --disable-foomatic-rip-hplip-install \
    --enable-pp-build \
%if_enabled PPDs
    --enable-foomatic-ppd-install \
    --enable-foomatic-drv-install \
    --enable-cups-ppd-install \
%else
    --disable-foomatic-ppd-install \
    --disable-cups-ppd-install \
%endif
    --enable-hpijs-install \
%if_enabled python_code
    --enable-gui-build \
    --enable-fax-build \
    --enable-network-build=yes \
    %{subst_enable policykit} \
    %{subst_enable qt3} \
    %{subst_enable qt4} \
    %{subst_enable qt5} \
%if_enabled sane_backend
    --enable-scan-build \
%else
    --disable-scan-build \
%endif
%if_with python3
	 PYTHON=%{__python3}
%endif
%else
    --enable-hpijs-only-build 
%endif

%make

%install

install -d $RPM_BUILD_ROOT/%_datadir/cups/model/
%if_disabled PPDs
# in alt, ppds are stored with cups (not good?)
#mv $RPM_BUILD_ROOT/usr/share/ppd/HP/fax/HP-Fax-hplip.ppd.gz $RPM_BUILD_ROOT/%_datadir/cups/model/
install -m644 fax/ppd/HP-Fax-hplip.ppd $RPM_BUILD_ROOT/%_datadir/cups/model/
%endif

%make DESTDIR=$RPM_BUILD_ROOT install \
%if_with python3
	 PYTHON=%{__python3}
%endif


%if_enabled python_code

%if_disabled udevacl
###
mkdir -p $RPM_BUILD_ROOT%_sysconfdir/security/console.perms.d/
install -m 600 %{SOURCE4} $RPM_BUILD_ROOT%_sysconfdir/security/console.perms.d/80-hpmud.perms
%endif

#mkdir -p $RPM_BUILD_ROOT%_initdir/
#install -m 755 %{SOURCE2} $RPM_BUILD_ROOT%_initdir/%name

mkdir -p $RPM_BUILD_ROOT%_sysconfdir/hp

# Create /var/run/hplip
mkdir -p %buildroot%_runtimedir/hplip
## Create /run/hplip
#mkdir -p %{buildroot}/run/hplip
# Create /var/lib/hp
mkdir -p %{buildroot}%{_sharedstatedir}/hp

# install /usr/lib/tmpfiles.d/hplip.conf (bug #1015831)
mkdir -p %{buildroot}%{_tmpfilesdir}
cat > %{buildroot}%{_tmpfilesdir}/hplip.conf <<EOF
# See tmpfiles.d(5) for details

d /run/hplip 0775 root lp -
EOF


### add to doc install
cp COPYING $RPM_BUILD_ROOT%_docdir/%name-%version/

# # Comment out all "setSizePolicy" calls, this function is incompatible with
# # PyQT/SIP <3.16
# # the code below is correct: it does'nt comments semilines ..., as previous
# # which cause syntax error in 1.6.6a, but is deprecated with PyQT = 3.16
# perl -p -i -e 'if (/^(.*setSizePolicy.*)$/) {$_="#".$_; if (/,\s*$/) {$endcomma=1}} elsif ($endcomma) {$_="#".$_; $endcomma=0}' `grep -l setSizePolicy $RPM_BUILD_ROOT%_datadir/%name/ui/*.py`

# Menu Icons
install -pD -m644 %name.16.png $RPM_BUILD_ROOT%_miconsdir/hplip.png
install -pD -m644 %name.32.png $RPM_BUILD_ROOT%_niconsdir/hplip.png
install -pD -m644 %name.48.png $RPM_BUILD_ROOT%_liconsdir/hplip.png

# Remove the installed /etc/sane.d/dll.conf
# because this is provided by the sane package:
rm -f $RPM_BUILD_ROOT%_sysconfdir/sane.d/dll.conf
# Remove other unneeded files
rm -f $RPM_BUILD_ROOT%_datadir/%name/%name
rm -f $RPM_BUILD_ROOT%_datadir/%name/hplip_readme.html
rm -f $RPM_BUILD_ROOT%_datadir/%name/hplip_overview.png
rm -f $RPM_BUILD_ROOT%_datadir/%name/COPYING

# fedora
rm -f %{buildroot}%{_datadir}/hplip/hplip-install
rm -rf %{buildroot}%{_datadir}/hplip/install.*
rm -f %{buildroot}%{_datadir}/hplip/uninstall.*
rm -f %{buildroot}%{_bindir}/hp-uninstall
rm -f %{buildroot}%{_datadir}/hplip/upgrade.*
rm -f %{buildroot}%{_bindir}/hp-upgrade
#rm -f %{buildroot}%{_bindir}/hp-config_usb_printer
#rm -f %{buildroot}%{_datadir}/hplip/config_usb_printer.*
#rm -f %{buildroot}%{_unitdir}/hplip-printer@.service
%endif # python_code

# Install other files for HPIJS
mkdir -p $RPM_BUILD_ROOT%_docdir/%hpijsname-%version
install -pD -m644 prnt/hpijs/README_LIBJPG  $RPM_BUILD_ROOT%_docdir/%hpijsname-%version/
install -d %{buildroot}%{_man1dir}/
install -p -m644 %{SOURCE202} %{buildroot}%{_man1dir}/

%if_enabled PPDs
#### Remove the installed /usr/bin/foomatic-rip
#### because this is provided by the cups-filters package:
###rm %{buildroot}%{_bindir}/foomatic-rip

### a piece of ancient wisdom of SuSE
# Make some general tests and adjustments for all PPDs (see manufacturer-PPDs.spec):
pushd %{buildroot}%{_datadir}/ppd/HP
#pushd foomatic-db/db/source/PPD/HP
for ppd in *.ppd{,.gz,.bz2}; 
do
       [ -e $ppd ] && sh %{SOURCE7} $ppd
done
popd
# End of the general tests and adjustments for all PPDs.
%endif # PPDs

%if_enabled halacl
# fedora fdi policy
mkdir -p %{buildroot}%{_datadir}/hal/fdi/policy/10osvendor
install -p -m644 %{SOURCE100} %{buildroot}%{_datadir}/hal/fdi/policy/10osvendor/22-hplip.fdi
%endif

# hack to properly compile .py files
python%{pysuffix} -m compileall $RPM_BUILD_ROOT%_datadir/%name


# removing unpackaged files
pushd $RPM_BUILD_ROOT
#rm  usr/share/hplip/hplip-install usr/share/hplip/install.*
popd

# Regenerate hpcups PPDs on upgrade if necessary (bug #579355).
install -p -m755 %{SOURCE101} %{buildroot}%{_bindir}/hpcups-update-ppds

mkdir -p %{buildroot}%{_sysconfdir}/sane.d/dll.d
echo hpaio > %{buildroot}%{_sysconfdir}/sane.d/dll.d/hpaio

# Create an empty plugins directory to make sure it gets the right
# SELinux file context (bug #564551).
mkdir -p %{buildroot}%{_datadir}/hplip/prnt/plugins

# traditional place for udev rules
mkdir -p %{buildroot}/lib
mv %{buildroot}/usr/lib/udev %{buildroot}/lib/

%pre
# TODO: drop it somewhere after p7 release
# no more services
if [ -f %_initrddir/%name ]; then
    /sbin/service hplip condstop ||:
    /sbin/chkconfig --del hplip ||:
fi

%post
/sbin/service cups condrestart ||:

%preun
if [ "$RPM_INSTALL_ARG1" -eq 0 ]; then
    /sbin/service cups condrestart ||:
fi

#fedora use it in post...
#%post hpijs
#%{_bindir}/hpcups-update-ppds &>/dev/null ||:

%if_enabled sane_backend
%preun sane
# no more /etc/sane.d/dll.conf - using /etc/sane.d/dll.d
# Remove HPLIP driver from /etc/sane.d/dll.conf
if [ "$1" = 0 ]; then
        %__subst 's|^\([[:space:]]*hpaio[[:space:]]*\)$|#\1|' %_sysconfdir/sane.d/dll.conf
fi
%endif #sane_backend

%files
%if_enabled python_code
%doc %_docdir/%name-%version
%dir %{_sysconfdir}/hp
%config %{_sysconfdir}/hp/hplip.conf
#deprecated
#%_initdir/%name
# C libraries for Python
%_libdir/python*/site-packages/*.so*
%if_disabled udevacl
# logged-in user gave direct access to the printers
%_sysconfdir/security/console.perms.d/80-hpmud.perms
%endif
%exclude %_libdir/python*/site-packages/*.la
# CUPS backend
%_prefix/lib/cups/backend/hp
%_prefix/lib/cups/backend/hpfax
# python
%{_bindir}/hp-align
%{_bindir}/hp-check
%{_bindir}/hp-clean
%{_bindir}/hp-colorcal
%{_bindir}/hp-config_usb_printer
%{_bindir}/hp-devicesettings
%{_bindir}/hp-diagnose_plugin
%{_bindir}/hp-diagnose_queues
%{_bindir}/hp-fab
%{_bindir}/hp-faxsetup
%{_bindir}/hp-firmware
%{_bindir}/hp-info
%{_bindir}/hp-levels
%{_bindir}/hp-linefeedcal
%{_bindir}/hp-logcapture
%{_bindir}/hp-makecopies
%{_bindir}/hp-makeuri
%if_enabled policykit
%{_bindir}/hp-pkservice
%endif
%{_bindir}/hp-plugin
%{_bindir}/hp-pqdiag
%{_bindir}/hp-printsettings
%{_bindir}/hp-probe
%{_bindir}/hp-query
%{_bindir}/hp-scan
%{_bindir}/hp-sendfax
%{_bindir}/hp-setup
%{_bindir}/hp-testpage
%{_bindir}/hp-timedate
%{_bindir}/hp-unload
%{_bindir}/hp-wificonfig
# Files
%dir %{_datadir}/hplip
%{_datadir}/hplip/align.py*
%{_datadir}/hplip/check.py*
%{_datadir}/hplip/check-plugin.py*
%{_datadir}/hplip/clean.py*
%{_datadir}/hplip/colorcal.py*
%{_datadir}/hplip/config_usb_printer.py*
%{_datadir}/hplip/devicesettings.py*
%{_datadir}/hplip/diagnose_plugin.py*
%{_datadir}/hplip/diagnose_queues.py*
%{_datadir}/hplip/fab.py*
%{_datadir}/hplip/fax
#exclude %{_datadir}/hplip/fax/pstotiff*
%{_datadir}/hplip/faxsetup.py*
%{_datadir}/hplip/firmware.py*
%{_datadir}/hplip/hpdio.py*
%{_datadir}/hplip/hplip_clean.sh
%{_datadir}/hplip/hpssd*
%{_datadir}/hplip/info.py*
%{_datadir}/hplip/__init__.py*
%{_datadir}/hplip/levels.py*
%{_datadir}/hplip/linefeedcal.py*
%{_datadir}/hplip/logcapture.py*
%{_datadir}/hplip/makecopies.py*
%{_datadir}/hplip/makeuri.py*
%{_datadir}/hplip/plugin.py*
%{_datadir}/hplip/pqdiag.py*
%{_datadir}/hplip/printsettings.py*
%{_datadir}/hplip/probe.py*
%{_datadir}/hplip/query.py*
%{_datadir}/hplip/scan.py*
%{_datadir}/hplip/sendfax.py*
%{_datadir}/hplip/setup.py*
%{_datadir}/hplip/testpage.py*
%{_datadir}/hplip/timedate.py*
%{_datadir}/hplip/unload.py*
%{_datadir}/hplip/wificonfig.py*
%if_enabled policykit
%{_datadir}/hplip/pkservice.py*
%{_datadir}/PolicyKit/policy/com.hp.hplip.policy
%{_unitdir}/hplip-printer@.service
%endif
# global dbus service
%{_datadir}/dbus-1/system-services/com.hp.hplip.service
/etc/dbus-1/system.d/com.hp.hplip.conf

# Directories
%{_datadir}/hplip/base
%{_datadir}/hplip/copier
%dir %{_datadir}/hplip/data
#%{_datadir}/hplip/data/firmware
%{_datadir}/hplip/data/ldl
%{_datadir}/hplip/data/localization
%{_datadir}/hplip/data/models
%{_datadir}/hplip/data/pcl
%{_datadir}/hplip/data/ps
%{_datadir}/hplip/installer
%{_datadir}/hplip/pcard
%{_datadir}/hplip/prnt
%{_datadir}/hplip/scan
%dir %_sharedstatedir/hp
#%_sharedstatedir/hp/hplip.state
#%dir %attr(0775,root,lp) %{_var}/log/hp
#%dir %attr(1775,root,lp) %{_var}/log/hp/tmp
%dir %attr(0775,root,lp) %_runtimedir/hplip
#%{_sysconfdir}/cron.daily/hplip_cron
%endif

%files hpcups
# CUPS drv
%dir %{_datadir}/cups/drv/hp
%{_datadir}/cups/drv/hp/hpcups.drv
# CUPS filter
%_prefix/lib/cups/filter/hpcups
%_prefix/lib/cups/filter/hpcupsfax
%{_bindir}/hpcups-update-ppds
# moved from common
%_prefix/lib/cups/filter/hpps
%if_enabled cupstifffilter
/usr/lib/cups/filter/pstotiff
%{_datadir}/cups/mime/pstotiff.convs
%{_datadir}/cups/mime/pstotiff.types
%endif


%if_enabled python_code
%files gui
# xdg autostart instead of init.d (do we need them???)
# The systray applet doesn't work properly (displays icon as a
# window), so don't ship the launcher yet.
#/etc/xdg/autostart/hplip-systray.desktop
#_bindir/hp-*
%{_bindir}/hp-doctor
%{_bindir}/hp-print
%{_bindir}/hp-systray
#%{_bindir}/hp-toolbox.wrapper
%{_bindir}/hp-toolbox
# Files
%{_datadir}/hplip/doctor.py*
%{_datadir}/hplip/print.py*
%{_datadir}/hplip/toolbox.py*
%{_datadir}/hplip/systray.py*
# Directories
%{_datadir}/hplip/data/images
# qt3 interface
%if_enabled qt3
%{_datadir}/hplip/plugins
%{_datadir}/hplip/ui
%endif
# qt4 interface
%if_enabled qt4
%{_datadir}/hplip/ui4
%endif
# qt5 interface
%if_enabled qt5
%{_datadir}/hplip/ui5
%endif

# HPLIP menu files
%_datadir/applications/%name.desktop
%_niconsdir/hplip.png
%_liconsdir/hplip.png
%_miconsdir/hplip.png

%if_enabled autostart
%files gui-autostart
/etc/xdg/autostart/hplip-systray.desktop
%endif
%endif

%if_enabled PPDs
%files PPDs
### moved to foomatic
###%_datadir/cups/model/foomatic-ppds
%files hpijs-PPDs
%_datadir/ppd/HP/*-hpijs*.ppd*
%files hpcups-PPDs
%_datadir/ppd/HP/*
%exclude %_datadir/ppd/HP/*-hpijs*.ppd*
%exclude %_datadir/ppd/HP/*-ps.ppd*
%files ps-PPDs
%_datadir/ppd/HP/*-ps.ppd*
%else
%_datadir/cups/model/HP-Fax-hplip.ppd*
%endif

%files recommends

%files common
# HPIP
%_libdir/libhpip*so.*
%_libdir/libhpdiscovery.so.*
%exclude %_libdir/libhpip*so
%exclude %_libdir/libhpdiscovery.so
# The so symlink is required here (see RH bug #489059).
%_libdir/libhpmud*so*
%{_udevrulesdir}/56-hpmud.rules
%{_tmpfilesdir}/hplip.conf

%files hpijs
#doc prnt/hpijs/COPYING
%doc %_docdir/%hpijsname-%version
%_bindir/%hpijsname
%{_man1dir}/%hpijsname.1*
%dir %{_datadir}/cups/drv/hp
%{_datadir}/cups/drv/hp/hpijs.drv

%if_enabled sane_backend
# SANE
%files sane
%config(noreplace) %{_sysconfdir}/sane.d/dll.d/hpaio
%{_datadir}/hal/fdi/preprobe/10osvendor/20-hplip-devices.fdi
%if_enabled halacl
# fedora's hal-based acl
%{_datadir}/hal/fdi/policy/10osvendor/22-hplip.fdi
%endif
%_libdir/sane/libsane-hpaio*.so*
%exclude %_libdir/sane/libsane-hpaio*.la
# is it needed?
#%{_datadir}/hplip/hpaio.desc
%endif

#TODO
#*** SANE Backend ***
#SANE - need test with real devices and SANE software
#SANE - merge SuSE trigger on installing sane

%changelog
* Thu Nov 10 2016 Igor Vlasenko <viy@altlinux.ru> 1:3.16.7-alt2
- reverted back to 3.16.7 due to problems in 3.16.10

* Wed Nov 09 2016 Igor Vlasenko <viy@altlinux.ru> 3.16.10-alt1
- new version

* Wed Jul 27 2016 Igor Vlasenko <viy@altlinux.ru> 3.16.7-alt1
- new version (closes: #31946)

* Fri Oct 23 2015 Igor Vlasenko <viy@altlinux.ru> 3.15.9-alt1
- new version

* Thu Nov 20 2014 Igor Vlasenko <viy@altlinux.ru> 3.14.10-alt1
- new version

* Mon Jul 21 2014 Igor Vlasenko <viy@altlinux.ru> 3.14.6-alt1
- new version (closes: #30203)

* Mon Jun 09 2014 Igor Vlasenko <viy@altlinux.ru> 3.14.3-alt2
- added watch file
- added upstream-signing-key.asc

* Mon Apr 14 2014 Igor Vlasenko <viy@altlinux.ru> 3.14.3-alt1
- new version

* Wed Feb 26 2014 Anton Farygin <rider@altlinux.ru> 3.13.9-alt2
- NMU: fixed requires - foomatic-filters now is 
  integraded to cups-filters package.

* Wed Sep 25 2013 Igor Vlasenko <viy@altlinux.ru> 3.13.9-alt1
- new version

* Wed Jan 30 2013 Igor Vlasenko <viy@altlinux.ru> 3.12.11-alt1
- new version

* Thu Nov 22 2012 Igor Vlasenko <viy@altlinux.ru> 3.12.10a-alt0.M60P.1
- backport

* Tue Nov 20 2012 Igor Vlasenko <viy@altlinux.ru> 3.12.10a-alt1
- new version 3.12.10a

* Sat Sep 29 2012 Igor Vlasenko <viy@altlinux.ru> 3.12.9-alt2
- build with cups 1.6

* Thu Sep 20 2012 Igor Vlasenko <viy@altlinux.ru> 3.12.9-alt1
- new version

* Wed Aug 08 2012 Igor Vlasenko <viy@altlinux.ru> 3.12.6-alt1
- new version

* Tue Dec 20 2011 Igor Vlasenko <viy@altlinux.ru> 3.11.10-alt1.M60P.1
- backport

* Mon Dec 19 2011 Igor Vlasenko <viy@altlinux.ru> 3.11.10-alt2
- updated fedora patches

* Sat Oct 22 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 3.11.10-alt1.1
- Rebuild with Python-2.7

* Thu Oct 20 2011 Igor Vlasenko <viy@altlinux.ru> 3.11.10-alt0.M60P.1
- M60P backport

* Thu Oct 20 2011 Igor Vlasenko <viy@altlinux.ru> 3.11.10-alt1
- new version 3.11.10

* Sun Oct 02 2011 Igor Vlasenko <viy@altlinux.ru> 3.11.7-alt2.M60P.1
- backport

* Sun Oct 02 2011 Igor Vlasenko <viy@altlinux.ru> 3.11.7-alt3
- updated fedora patches
- use /etc/sane.d/dll.d

* Tue Sep 13 2011 Igor Vlasenko <viy@altlinux.ru> 3.11.7-alt2
- CVE-2011-2722

* Fri Jul 29 2011 Igor Vlasenko <viy@altlinux.ru> 3.11.7-alt1
- new version

* Wed May 25 2011 Igor Vlasenko <viy@altlinux.ru> 3.11.5-alt0.M51.1
- M51 backport

* Wed May 25 2011 Igor Vlasenko <viy@altlinux.ru> 3.11.5-alt1
- new version

* Wed Mar 30 2011 Igor Vlasenko <viy@altlinux.ru> 3.11.3-alt1
- new version

* Sat Feb 19 2011 Igor Vlasenko <viy@altlinux.ru> 3.11.1-alt4
- marked noarch packages

* Fri Feb 18 2011 Igor Vlasenko <viy@altlinux.ru> 3.11.1-alt3
- added conflicts (closes: #23348)
- synced fedora patches

* Fri Jan 28 2011 Igor Vlasenko <viy@altlinux.ru> 3.11.1-alt2
- restored .desktop patch

* Thu Jan 27 2011 Igor Vlasenko <viy@altlinux.ru> 3.11.1-alt1
- new version

* Mon Jan 03 2011 Igor Vlasenko <viy@altlinux.ru> 3.10.9-alt4
- added fedora patches as of 3.10.9-9
- added gui-autostart

* Wed Nov 24 2010 Igor Vlasenko <viy@altlinux.ru> 3.10.9-alt3
- added hpcups driver and PPDs subpackages (closes: 24624)

* Mon Nov 22 2010 Igor Vlasenko <viy@altlinux.ru> 3.10.9-alt0.M50P.1
- p5 backport

* Sat Nov 20 2010 Igor Vlasenko <viy@altlinux.ru> 3.10.9-alt0.M51.1
- backport

* Sat Nov 20 2010 Igor Vlasenko <viy@altlinux.ru> 3.10.9-alt2
- added fedora patches as of 3.10.9-6

* Wed Oct 27 2010 Igor Vlasenko <viy@altlinux.ru> 3.10.9-alt1
- new version

* Tue Aug 03 2010 Igor Vlasenko <viy@altlinux.ru> 3.10.6-alt0.M51.1
- backport

* Tue Aug 03 2010 Igor Vlasenko <viy@altlinux.ru> 3.10.6-alt1
- new version

* Tue May 11 2010 Igor Vlasenko <viy@altlinux.ru> 3.10.2-alt1
- new version

* Tue Jan 26 2010 Igor Vlasenko <viy@altlinux.ru> 3.9.12-alt0.M51.1
- backport

* Mon Jan 25 2010 Igor Vlasenko <viy@altlinux.ru> 3.9.12-alt1
- new version

* Sat Oct 10 2009 Igor Vlasenko <viy@altlinux.ru> 3.9.8-alt4
- enabled udev acl (via console kit)

* Tue Oct 06 2009 Igor Vlasenko <viy@altlinux.ru> 3.9.8-alt3
- moved hpijs.drv

* Mon Oct 05 2009 Igor Vlasenko <viy@altlinux.ru> 3.9.8-alt2
- PPDs split into hpcups PPDs and hpijs PPDs.
- fixed hplip dependencies (closes #21827)

* Wed Sep 09 2009 Igor Vlasenko <viy@altlinux.ru> 3.9.8-alt1
- new version

* Thu Jul 23 2009 Igor Vlasenko <viy@altlinux.ru> 3.9.4b-alt3
- rebuild,
- does not require qt3, close #20615

* Fri May 15 2009 Igor Vlasenko <viy@altlinux.ru> 3.9.4b-alt2
- fixed requires

* Wed May 13 2009 Igor Vlasenko <viy@altlinux.ru> 3.9.4b-alt1
- new version

* Wed Apr 08 2009 Igor Vlasenko <viy@altlinux.ru> 3.9.2-alt0.2
- experimental build 2

* Mon Apr 06 2009 Igor Vlasenko <viy@altlinux.ru> 3.9.2-alt0.1
- new version
- experimental build

* Sun Dec 07 2008 Igor Vlasenko <viy@altlinux.ru> 2.8.10-alt3
- lenient hplip-fixppd - warns only (todo: report upstream)

* Thu Dec 04 2008 Igor Vlasenko <viy@altlinux.ru> 2.8.10-alt2
- fixed and loosed dependencies
- added recommends subpackage

* Wed Dec 03 2008 Igor Vlasenko <viy@altlinux.ru> 2.8.10-alt1
- new version
- spec cleanup: foomatic stuff is now in foomatic-db

* Sun Sep 21 2008 Igor Vlasenko <viy@altlinux.ru> 2.8.9-alt1
- new version

* Thu Jul 31 2008 Igor Vlasenko <viy@altlinux.ru> 2.8.7-alt1
- new version

* Sat Jul 26 2008 Igor Vlasenko <viy@altlinux.ru> 2.8.6b-alt1
- version 2.6.8b 

* Fri Jul 04 2008 Igor Vlasenko <viy@altlinux.ru> 2.8.6-alt1
- new version
- Update hplip.fdi for new kernels: info.bus -> info.subsystem.

* Fri May 30 2008 Igor Vlasenko <viy@altlinux.ru> 2.8.5-alt1
- new version

* Tue Jan 08 2008 Igor Vlasenko <viy@altlinux.ru> 2.7.12-alt1
- new version

* Thu Nov 22 2007 Igor Vlasenko <viy@altlinux.ru> 2.7.10-alt3
- thanks to mithraen@:
  + added provides hplip-tools
  + added Requires: python-module-imaging for hp-scan -n mode

* Wed Nov 07 2007 Igor Vlasenko <viy@altlinux.ru> 2.7.10-alt2
- removed dependency on printer-drivers-utils

* Mon Oct 22 2007 Igor Vlasenko <viy@altlinux.ru> 2.7.10-alt1
- new version

* Sat Sep 29 2007 Igor Vlasenko <viy@altlinux.ru> 2.7.9-alt1
- added security patch (thanks to ldv@)
- new version

* Thu Sep 13 2007 Igor Vlasenko <viy@altlinux.ru> 2.7.7-alt2
- resolved conflict with foomatic-db

* Wed Aug 22 2007 Igor Vlasenko <viy@altlinux.ru> 2.7.7-alt1
- new version
  * Replaced hpiod with the new HP Multi-Point Transport Driver (hpmud).
  * Hpmud is a shared library instead of a daemon.
  * Hpssd is started automatically when needed by HPLIP.
- removed foomatic-db-hpijs snapshots (included upstream)
- removed hp-toolbox.wrapper (hp-toolbox is already fixed)
- removed init script for hpssd 
  (it is is started automatically when needed by HPLIP)
- hplip-tools renamed and rearranged to hplip-gui
- added pam_console support.

* Wed May 16 2007 Igor Vlasenko <viy@altlinux.ru> 1.7.4a-alt1
- new version
- foomatic-db-hpijs snapshot 20070516

* Mon Apr 02 2007 Igor Vlasenko <viy@altlinux.ru> 1.7.3-alt1
- new version
- new foomatic snapshot 20070327 

* Thu Mar 01 2007 Igor Vlasenko <viy@altlinux.ru> 1.7.2-alt1
- new version

* Wed Feb 28 2007 Igor Vlasenko <viy@altlinux.ru> 1.7.1-alt2
- foomatic-db-hpijs snapshot 20070227

* Thu Jan 25 2007 Igor Vlasenko <viy@altlinux.ru> 1.7.1-alt1
- new version

* Thu Jan 18 2007 Igor Vlasenko <viy@altlinux.ru> 1.6.12-alt5
- foomatic_snapshot updated to 20070117
- fixes for x86_64 (thanks to Dmitriy Khanzhin - dimajin-sandy.ru)

* Tue Jan 02 2007 Igor Vlasenko <viy@altlinux.ru> 1.6.12-alt4
- PPDs are moved to separate package
- removed .desktop (menu is used again due to Configuration/Printing)

* Tue Jan 02 2007 Igor Vlasenko <viy@altlinux.ru> 1.6.12-alt3
- spec cleanup -- removed manual links as they are already created

* Mon Jan 01 2007 Igor Vlasenko <viy@altlinux.ru> 1.6.12-alt0.M30.1
- backport for M30

* Mon Jan 01 2007 Igor Vlasenko <viy@altlinux.ru> 1.6.12-alt2
- enabled PPDs by default (some hplip tools do require them)
- hplip initscript merge

* Sat Dec 23 2006 Igor Vlasenko <viy@altlinux.ru> 1.6.12-alt1
- new version
- spec cleanup
- removed menu (now .desktop is used)

* Sat Nov 11 2006 Igor Vlasenko <viy@altlinux.ru> 1.6.10-alt1
- new version
- new foomatic snapshot 20061109

* Sat Sep 23 2006 Igor Vlasenko <viy@altlinux.ru> 1.6.9-alt1
- new version
- new foomatic snapshot 20060922 

* Fri Sep 08 2006 Igor Vlasenko <viy@altlinux.ru> 1.6.7-alt2
- new foomatic snapshot 20060906 

* Tue Sep 05 2006 Igor Vlasenko <viy@altlinux.ru> 1.6.7-alt1
- new version

* Fri Aug 25 2006 Igor Vlasenko <viy@altlinux.ru> 1.6.6a-alt0.M30.4.1
- backport for M30

* Mon Aug 07 2006 Igor Vlasenko <viy@altlinux.ru> 1.6.6a-alt4
- set default url viewer to url_handler.sh
  (hplip-1.6.6a-alt-urlhandler.patch)

* Thu Aug 03 2006 Igor Vlasenko <viy@altlinux.ru> 1.6.6a-alt3
- all python code moved to package hplip-tools
- BuildRequires python-devel according to python policy
- added hpfax cups backend
- added build of ppds (disabled)
- OpenSuSE experience partially integrated
- fedora experience partially integrated

* Sun Jul 30 2006 Igor Vlasenko <viy@altlinux.ru> 1.6.6a-alt2
- libhpip moved to package common --- this eliminates 
  printing system dependency on python.

* Thu Jul 27 2006 Igor Vlasenko <viy@altlinux.ru> 1.6.6a-alt1
- new fresh versions of hplip, hpijs, foomatic-db-hpijs
- build for Sisyphus

* Fri Jul 21 2006 Igor Vlasenko <viy@altlinux.ru> 1.6.6a-alt0
- build for Daedalus 

* Wed Jul 12 2006 Igor Vlasenko <viy@altlinux.ru> 1.6.6a-alt0.M30.1
- new fresh versions of hplip, hpijs, foomatic-db-hpijs
- backport for M30

* Fri Dec 02 2005 ALT QA Team Robot <qa-robot@altlinux.org> 0.9.4-alt3.1
- rebuild with libnetsnmp.so.9 .

* Mon Sep 19 2005 Serge A. Volkov <vserge at altlinux.ru> 0.9.4-alt3
- update initscript (add --displayname)
- Add Requires to package service-0.5.9-alt1
- Fix absolute symlinks (#7984)
- Update Buildreq

* Fri Sep 09 2005 Serge A. Volkov <vserge at altlinux.ru> 0.9.4-alt2.2
- Correct SANE backend scripts and etc

* Sun Sep 04 2005 Serge A. Volkov <vserge at altlinux.ru> 0.9.4-alt2.1
- Update foomatic version to new snapshot at 20050903
- Add Provides: foomatic-db-hpijs = %%fooversion-%%foomatic_snapshot
- Add PreReq: cups

* Sun Sep 04 2005 Serge A. Volkov <vserge at altlinux.ru> 0.9.4-alt2
- FIX (thanks Dmitry Vukolov)
  + mistake in "Provides hplip-hpijs-%%hpijsversion"
  + Provides/Obsoletes in hplip-foomatic
  + PreReq in hplip-foomatic
  + remove automatic requirements to gcc-g77
  + correct descriptions
  + correct mistake in hplip.desktop
  + correct hplip.menu (change title, section and add icons)

* Mon Aug 22 2005 Serge A. Volkov <vserge at altlinux.ru> 0.9.4-alt1
- Initscript fix hack
- Replace #!/usr/bin/env python  by the #!/usr/bin/python

* Thu Aug 18 2005 Serge A. Volkov <vserge at altlinux.ru> 0.9.4-alt0.2
- Init script cleanup
- Local hack in initscript for work hpssd.py from it (start, stop, status) 

* Mon Aug 08 2005 Serge A. Volkov <vserge at altlinux.ru> 0.9.4-alt0.1
- Update to new version 0.9.4
- Create link %_bindir/hp-* to %_datadir/%name/*

* Tue May 31 2005 Serge A. Volkov <vserge at altlinux.ru> 0.9.3-alt0.2
- FIX rpm conflicts with hpijs <= 2.0

* Sun May 29 2005 Serge A. Volkov <vserge at altlinux.ru> 0.9.3-alt0.1
- Update to new version 0.9.3
- Add variable %%hplip_minor

* Thu May 19 2005 Serge A. Volkov <vserge at altlinux.ru> 0.9.2-alt4
- Correct python builds
- Update BuildRequires and spec cleanup
- Add menu files
- Add correct QTDIR

* Sat May 14 2005 Serge A. Volkov <vserge at altlinux.ru> 0.9.2-alt3
- SPEC cleanup
- Add Requires to python-module-PyQt

* Fri May 13 2005 Serge A. Volkov <vserge at altlinux.ru> 0.9.2-alt2
- Add initial hplip.init for ALT Linux Sisyphus

* Mon May 09 2005 Serge A. Volkov <vserge at altlinux.ru> 0.9.2-alt1
- Update 
  - to new version HPLIP 0.9.2
  - version of hpijs componets to 2.1.2
  - Build Requires
  - spec according spec from Mandrake (Mandriva) linux
- Add conflicts with hpijs < 2.0
- Spec clean up
- Remove all patches
- Correct license
- Devide four packages hplip, hplip-hpijs, hplip-sane, hplip-foomatic

* Mon May 09 2005 Serge A. Volkov <vserge at altlinux.ru> 0.9.1-alt2
- Update to new foomatic-db-hpijs snapshot 20050508 (v.1.5)

* Mon Apr 18 2005 Serge A. Volkov <vserge at altlinux.ru> 0.9.1-alt1
- Update to new version 0.9.1
- Disable
  - patch1
  - buils with SANE
- Add patch from MDK package: hplip-0.9.1-HP-DeskJet_450-Battery.patch

* Sun Jan 09 2005 Serge A. Volkov <vserge at altlinux.ru> 0.8.4-alt1
- Add patch from Debian
- Initial release
