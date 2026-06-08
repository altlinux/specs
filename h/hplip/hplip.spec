%define _unpackaged_files_terminate_build 1
%def_enable cupstifffilter
%def_enable sane_backend
%def_enable autostart
%def_enable PPDs
%def_enable python_code
%def_with python3
%def_disable foomatic_rip
%def_disable qt3
%def_disable qt4
%def_enable qt5
%def_enable policykit
# udev >= 145
# note: flag dropped upstream
%def_enable udevacl
%def_disable halacl
%def_without ernie
%def_without l10n
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
%def_with new_systemd

Name:    hplip
Version: 3.26.4
Release: alt1
Epoch:   1

Summary: Solution for printing, scanning, and faxing with Hewlett-Packard inkjet and laser printers.

%if_without ernie
License: GPL-2.0+ and MIT and BSD-3-Clause
%else
License: GPL-2.0+ and MIT and BSD-3-Clause and IJG and ALT-Public-Domain and GPL-2.0+ with exceptions and ISCL
%endif
Group: Publishing
#URL: http://hplip.sourceforge.net -- old
#URL: http://hplipopensource.com/ -- old
URL: https://developers.hp.com/hp-linux-imaging-and-printing
Packager: Andrey Cherepanov <cas@altlinux.org>

# Remove self-satisfied requires
%filter_from_requires /^python[0-9.]*(\(base.*\|installer.*\|prnt\|scan\|copier\|hpmudext\|pcard\))/d

%define hpijsname hpijs

Conflicts: ghostscript <= 7.05-alt15
Obsoletes: hpoj <= 0.91
Provides: cups-backend-ptal
Obsoletes: cups-backend-ptal
Conflicts: cups < 1.1.18-alt7

Requires(pre,postun): cups
Requires: %name-common = %{?epoch:%epoch:}%version-%release

# TODO: split hplip and hplip-utils
# and remove this Req:
Requires: %name-hpcups = %{?epoch:%epoch:}%version-%release

# Main package requires curl to avoid
# misleading errors about network connectivity (fc bug #705843).
Requires: curl

# for hplip/base/validation.py (fc bug #1118724).
#Requires: gnupg
# set require directly to /usr/bin/gpg, because gnupg2 and gnupg ships it,
# but gnupg will be deprecated in the future
Requires: %{_bindir}/gpg

%if_enabled python_code

%if_with python3
BuildRequires(pre): rpm-build-python3
%add_python3_compile_include %_datadir/%name
AutoReqProv: nopython
AutoProv: nopython3
%py3_requires distro
# this is self-provide from sixext.py
%filter_from_requires /^python3\(.*base.sixext.moves\)/d
%else
BuildRequires(pre): rpm-build-python
%add_python_compile_include %_datadir/%name
AutoProv: nopython
%py_requires distro
%endif
# Andy Kuleshov report
Requires: python%{pysuffix}-module-dbus
%if_without python3
Requires: python-modules-ctypes
%endif
%endif

Requires: service => 0.5.9-alt1
# For Fax coverpage
%py3_requires reportlab

BuildRequires(pre): libsane-devel

BuildRequires: gcc-c++
BuildRequires: libavahi-devel
BuildRequires: libcups-devel
BuildRequires: libdbus-devel
BuildRequires: libjpeg-devel
BuildRequires: libnet-snmp-devel
BuildRequires: libssl-devel
BuildRequires: libstdc++-devel
BuildRequires: libusb-compat-devel
BuildRequires: libusb-devel
BuildRequires: zlib-devel

%if_enabled python_code
%if_enabled qt3
BuildRequires: python%{pysuffix}-module-qt-devel
%endif
%if_enabled qt4
BuildRequires: python%{pysuffix}-module-PyQt4-devel
%endif
%if_enabled qt5
BuildRequires: python%{pysuffix}-module-PyQt5-devel
%endif
#RemovedBuildRequires: python-base python-dev python-modules-compiler python-modules-encodings
BuildRequires: python%{pysuffix}-devel
%endif

%if_enabled PPDs
#cups-common and foomatic-filters is for cupstestppd
BuildRequires: perl cups-common %{cups_filters}
Provides:  %name-PPDs = %EVR
Obsoletes: %name-PPDs < %EVR
Provides:  %name-ps-PPDs = %EVR
Obsoletes: %name-ps-PPDs < %EVR
Provides:  %name-hpcups-PPDs = %EVR
Obsoletes: %name-hpcups-PPDs < %EVR
Provides:  %name-hpijs-PPDs = %EVR
Obsoletes: %name-hpijs-PPDs < %EVR
%endif

%if_enabled policykit
BuildRequires: polkit libpolkit-devel
%endif

Source: http://dl.sourceforge.net/hplip/%name-%version.tar
Source2: %name.init
Source3: %{name}.appdata.xml
Source4: 80-hpmud.perms
Source5: %name.png
Source6: %name-icons.tar
Source7: %name-fixppd.sh
Source8: %name.watch
Source9: upstream-signing-key.asc
Source10: hp-systray

#TODO: see what fdi is better:
# https://bugzilla.redhat.com/show_bug.cgi?id=478495
# https://bugzilla.redhat.com/show_bug.cgi?id=479648
# fedora fdi acl policy
Source100: hplip.fdi
# cvs update: hplip.fdi is no longer in the repository (due to udev-acl)
Source101: hpcups-update-ppds.sh
Source102: copy-deviceids-py2.py
Source103: copy-deviceids.py

# OpenSuSE based sources
# deprecated; 2.7.7 shows 'can't connect to device'
Source201: hp-toolbox.wrapper
Source202: hpijs.1

Patch1: hplip-3.12.9-alt-urlhandler.patch
# dead patch 2
Patch2: hplip-3.9.12-alt-fix-udev-rules-ppdev.patch
Patch4: hplip-alt-hplip-desktop.patch
Patch5: hplip-3.17.11-alt-link-libhpipp.patch
Patch6: hplip-3.15.9-alt-systemd.patch
Patch7: hplip-3.16.7-alt-link-python2.patch
Patch8: hplip-3.16.7-alt-link-python3.patch
Patch9: hplip-alt-auth.patch

Patch10: http://www.linuxprinting.org/download/printing/hpijs/hpijs-1.4.1-rss.1.patch
# it is patch 10 rediffed
Patch12: hplip-3.16.11-alt-fax-setup.patch
# Localization files made for old qt3 forms
Patch14: hplip-alt-use-l10n.patch
# Use python3 in service file
Patch15: hplip-alt-use-python3-in-service.patch
Patch18: hplip-alt-add-M125ra-model.patch
Patch19: hplip-alt-ftbfs-fix-buit.patch
Patch20: hplip-alt-add-debug-to-hp-plugin.patch
Patch21: hplip-alt-disable-resize-to-scan-area.patch
Patch22: hplip-alt-checksum-for-3.25.8.patch

# fedora patches
Patch101: hplip-pstotiff-is-rubbish.patch
Patch102: hplip-strstr-const.patch
Patch103: hplip-ui-optional.patch
Patch104: hplip-no-asm.patch
Patch105: hplip-deviceIDs-drv.patch
Patch106: hplip-udev-rules.patch
Patch107: hplip-retry-open.patch
Patch108: hplip-snmp-quirks.patch
Patch109: hplip-hpijs-marker-supply.patch
Patch110: hplip-clear-old-state-reasons.patch
Patch111: hplip-hpcups-sigpipe.patch
Patch112: hplip-logdir.patch
Patch113: hplip-bad-low-ink-warning.patch
Patch114: hplip-deviceIDs-ppd.patch
Patch115: hplip-ppd-ImageableArea.patch
Patch116: hplip-scan-tmp.patch
Patch117: hplip-log-stderr.patch
Patch118: hplip-avahi-parsing.patch
Patch119: hplip-dj990c-margin.patch
Patch120: hplip-strncpy.patch
Patch121: hplip-no-write-bytecode.patch
Patch122: hplip-silence-ioerror.patch
Patch123: hplip-sourceoption.patch
%if_without ernie
Patch124: hplip-noernie.patch
%endif
Patch125: hplip-appdata.patch
Patch126: hplip-check-cups.patch
Patch127: hplip-typo.patch
# python3 - recent HP release removed encoding/decoding to utf-8 in fax/pmlfax.py -
# that results in text string going into translate function in base/utils.py, which
# expects binary string because of parameters. Remove this patch if base/utils.py
# code gets fixed.
Patch128: hplip-use-binary-str.patch
# m278-m281 doesn't work correctly again
Patch129: hplip-error-print.patch
Patch130: hplip-hpfax-importerror-print.patch
Patch131: hplip-wifisetup.patch
# QMessagebox call was copy-pasted from Qt4 version, but Qt5 has different arguments,
# This patch solves most of them
Patch133: 0026-Call-QMessageBox-constructors-of-PyQT5-with-the-corr.patch
# HP upstream introduced new binary blob, which is not open-source, so it violates
# FPG by two ways - shipping binary blob and non open source code - so it needs to be removed.
# Patch1 is taken from Debian.
Patch134: 0025-Remove-all-ImageProcessor-functionality-which-is-clo.patch
# In hplip-3.18.10 some parts of UI code was commented out, which leaved hp-toolbox
# unusable (crashed on the start). The patch removes usages of variables, which were
# commented out.
# The patch is taken from Debian.
Patch135: 0027-Fixed-incomplete-removal-of-hp-toolbox-features-whic.patch
# hp-setup crashed when user wanted to define a path to PPD file. It was due
# byte + string variables incompatibility and it is fixed by decoding the 
# bytes-like variable
# part of https://bugzilla.redhat.com/show_bug.cgi?id=1666076
# reported upstream https://bugs.launchpad.net/hplip/+bug/1814272
Patch136: hplip-add-ppd-crash.patch
# external scripts, which are downloaded and run by hp-plugin, try to create links
# in non-existing dirs. These scripts ignore errors, so plugin is installed fine
# but then internal hp-plugin can check for plugin state, where links are checked too.
# It results in corrupted plugin state, which breaks printer installation by GUI hp-setup.
# Temporary workaround is to ignore these bad links and real fix should come from HP,
# because their external scripts try to create links in non-existing dirs.
# Bugzilla: https://bugzilla.redhat.com/show_bug.cgi?id=1671513
# Reported upstream: https://bugs.launchpad.net/hplip/+bug/1814574
Patch137: hplip-missing-links.patch
# change in 3.18.9 in scanext.c caused broken scanning for HP LaserJet 3052. Since I cannot figure
# it out what author wanted by the change (it sets option number 9 to true, but different handles
# have different options, so I'm not sure what author wanted to set).
# Remove the change for now, it works for user and me.
Patch138: hplip-hplj-3052.patch
# hpmud parses mdns txt record badly
# upstream tickets: https://bugs.launchpad.net/hplip/+bug/1797501
#                   https://bugs.launchpad.net/hplip/+bug/1817214
#                   https://bugs.launchpad.net/hplip/+bug/1821932
# with no response from upstream
# Patch1 taken from Debian https://lists.debian.org/debian-printing/2018/11/msg00049.html
Patch139: hplip-hpmud-string-parse.patch
# Part of https://bugzilla.redhat.com/show_bug.cgi?id=1694663
# It was found out that specific device needs plugin for scanning
# Reported upstream as https://bugs.launchpad.net/hplip/+bug/1822762
Patch140: hplip-m278-m281-needs-plugin.patch
# hpcups crashes when a printer needs a plugin and does not have one installed
# it crashes in destructor, because pointer is not initialized
# bugzilla https://bugzilla.redhat.com/show_bug.cgi?id=1695716
# reported upstream 
Patch141: hplip-hpcups-crash.patch
# Fixing the issues found by coverity scan
# reported upstream https://bugs.launchpad.net/hplip/+bug/1808145
Patch142: hplip-covscan.patch
# Segfault during logging to syslog because argument are switched
# bugzilla https://bugzilla.redhat.com/show_bug.cgi?id=1727162
# upstream https://bugs.launchpad.net/hplip/+bug/1837846
Patch143: hplip-logging-segfault.patch
# Traceback in hp-systray when there are no resource
# wanted to report upstream, but launchpad ends with timeout error
# bugzilla https://bugzilla.redhat.com/show_bug.cgi?id=1738321
Patch144: hplip-systray-blockerror.patch
# several printers were removed in 3.19.1, but actually someone still uses them
# reported upstream https://bugs.launchpad.net/hplip/+bug/1843592
# bugzillas 1742949, 1740132, 1739855
Patch145: hplip-missing-drivers.patch
# laserjet 2200 and other devices have different device id than HP expects...
# https://bugzilla.redhat.com/show_bug.cgi?id=1772698
# reported upstream https://bugs.launchpad.net/hplip/+bug/1853002
Patch146: hplip-model-mismatch.patch
# sixext has problems with python3 strings (bz#1573430)
# reported https://bugs.launchpad.net/bugs/1480152
Patch147: hplip-unicodeerror.patch
# error with new gcc, already reported in upstream as
# https://bugs.launchpad.net/hplip/+bug/1836735
Patch148: hplip-fix-Wreturn-type-warning.patch
# upstream check for python clears OS build system
# CFLAGS
# https://bugs.launchpad.net/hplip/+bug/1879445
Patch149: hplip-configure-python.patch
# taken from hplip upstream report - toolbox uses deprecated method
# setMargin(), which generates an exception, resulting in a infinite loop
# of request on cupsd
# https://bugs.launchpad.net/hplip/+bug/1880275
Patch150: hplip-dialog-infinite-loop.patch
# searching algorithm did not expect '-' in model name and thought it is a new PDL
# it resulted in incorrect PPD match, so e.g. hpijs driver was used instead of hpcups
# bug: https://bugzilla.redhat.com/show_bug.cgi?id=1590014
# reported upstream: https://bugs.launchpad.net/hplip/+bug/1881587
Patch151: hplip-find-driver.patch
# hp-clean didn't work for Photosmart C1410 because it was comparing
# string length with buffer size for string object, which is different,
# causing cleaning to fail - the fix is to make the object bytes-like,
# then buffer size is the same as the length.
# Thanks to Stefan Assmann we were able to fix level 1 cleaning
# for the device, but there can be similar issues with other devices
# bug https://bugzilla.redhat.com/show_bug.cgi?id=1833308
# reported upstream https://bugs.launchpad.net/hplip/+bug/1882193
Patch152: hplip-clean-ldl.patch
# 3.20.6 turned off requirement for most devices which needed it
# - it will cause malfunction of printing and scanning for them
# https://bugs.launchpad.net/hplip/+bug/1883898
Patch153: hplip-revert-plugins.patch
# if an user tries to install scanner via hp-setup (printer/fax utility)
# it fails further down - break out earlier with a message
# reported upstream as https://bugs.launchpad.net/hplip/+bug/1916114
Patch154: hplip-hpsetup-noscanjets.patch
# 1963114 - patch for hplip firmware load timeout fix
# reported upstream https://bugs.launchpad.net/hplip/+bug/1922404
Patch155: hplip-hpfirmware-timeout.patch
# 1985251 - Incorrect permission for gpg directory
# reported upstream https://bugs.launchpad.net/hplip/+bug/1938442
Patch156: hplip-gpgdir-perms.patch
# 1987141 - hp-plugin installs malformed udev files
# reported upstream https://bugs.launchpad.net/hplip/+bug/1847477
Patch157: hplip-plugin-udevissues.patch
# 2080235 - Misleading errors about missing shared libraries when scanning
# downstream patch to prevent errors:
# - when loading libhpmud.so - unversioned .so files belong into devel packages,
#   but dlopen() in hplip was set to load the unversioned .so - so to remove rpmlint
#   error (when libhpmud.so is in non-devel package) and prevent runtime dependency on -devel
#   package (if libhpmud.so had been moved to -devel) the dlopen on unversioned .so file was
#   removed
# - /lib64/libm.so is not symlink but ld script, which cannot be used in dlopen()
Patch158: hplip-no-libhpmud-libm-warnings.patch
Patch160: hplip-plugin-script.patch
# C99 compatibility fixes by fweimer - use explicit int
# Submitted upstream: <https://bugs.launchpad.net/hplip/+bug/1997875>
Patch161: hplip-pserror-c99.patch
# C99 compatibility patch by fweimer - several undefined functions in hpaio
# backend are declared in orblite.h
# Submitted upstream: <https://bugs.launchpad.net/hplip/+bug/1997875>
Patch162: hplip-scan-hpaio-include.patch
# C99 compatibility patch by fweimer - undefined _DBG() and dynamic linking funcs in orblite.c
# - _DBG() looks like typo and new header is added for funcs
# Submitted upstream: <https://bugs.launchpad.net/hplip/+bug/1997875>
Patch163: hplip-scan-orblite-c99.patch
# C99 compatibility patch by fweimer:
# PyString_AsStringAndSize is removed in Python3, remove its compilation for now
# in case there is a request for compiling it again, there is a possible solution
# for the function py3 alternative https://opendev.org/openstack/pyeclib/commit/19c8313986
# - disabling removes hp-unload and /usr/share/hplip/pcard as well
# Submitted upstream: <https://bugs.launchpad.net/hplip/+bug/1997875>
Patch164: hplip-pcardext-disable.patch
# undefined strcasestr() in sclpml.c - build with _GNU_SOURCE
# Submitted upstream: <https://bugs.launchpad.net/hplip/+bug/1997875>
Patch165: hplip-sclpml-strcasestr.patch
# 2192131 - parseQueues() doesn't get device uri from 'lpstat -v', because parsing pattern changed
# https://bugs.launchpad.net/hplip/+bug/2027972
Patch167: hplip-fix-parsing-lpstat.patch
# switch to curl by downstream patch from wget to workaround openstack dropping IPv6
# which causes great delays...
# Remove this once internal openstack handles IPv6 better - test by pinging IPv6 in OpenStack,
# it should not hang.
Patch168: hplip-plugin-curl.patch
# fix SyntaxWarning from python3.12
# https://bugs.launchpad.net/hplip/+bug/2029480
Patch169: hplip-use-raw-strings.patch
# FTBFS GCC 14
# https://bugs.launchpad.net/hplip/+bug/2048780
Patch170: hplip-hpaio-gcc14.patch
# function prototype did not specify argument's data types
# https://bugs.launchpad.net/hplip/+bug/2096650
Patch172: hplip-gcc15-stdc23.patch
# status history table shows unformatted QDateTime values
# https://bugs.launchpad.net/hplip/+bug/1956547
Patch173: hplip-format-qdatetime.patch
# Python 3.14 removed urlopener
# https://bugs.launchpad.net/hplip/+bug/2115046
Patch177: hplip-no-urlopener.patch

# ubuntu patches
Patch201: hp-plugin-download-fix.patch
# end ubuntu patches

# debian patches
Patch302: 01_rss.patch
Patch303: 14_charsign_fixes.patch
Patch304: hp_photosmart_pro_b9100_support.patch
Patch305: pjl-duplex-binding.patch
Patch306: simple-scan-as-default.patch
Patch307: try_libhpmud.so.0.patch
Patch308: add-lidil-two-cartridge-modes.patch
Patch310: hp-systray-make-menu-title-visible-in-sni-qt-indicator.patch
Patch311: hp-systray-make-menu-appear-in-sni-qt-indicator-with-kde.patch
Patch312: hpaio-option-duplex.diff
Patch314: pcardext-python3-workaround-upstream.patch
Patch315: hpscan-deskjet-3520-aio-allow-non-jpeg-scanning.patch
Patch318: install-check-plugin.diff
Patch319: HP-LaserJet_4000-PostScript-PPD.patch
Patch320: ui-patch-upstream-like.patch
Patch321: 0021-Add-include-cups-ppd.h-in-various-places-as-CUPS-2.2.patch
Patch322: 0022-Fix-list-wrapping-in-scan.py-to-fix-generated-manpag.patch
#Patch323: 0023-Fix-handling-of-unicode-filenames-in-sixext.py.patch
Patch324: 0024-Make-dat2drv-and-locateppd-build-dependent-of-class-.patch
Patch328: 0028-hp-check-Fix-core.distro-vs.-core.distro_name-mixups.patch
Patch329: 0029-Make-base.g.xint-more-generous-in-what-it-can-take.patch
# end debian patches

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
License: BSD-3-Clause
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
License: GPL-2.0+
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
# for python-notify
# Requires: notification-daemon
# for hp-scan -n
Requires: python%{pysuffix}-module-Pillow
Requires: python%{pysuffix}-module-pygobject3
# hplip-gui uses lsusb
Requires: %_bindir/lsusb

Requires: %name = %{?epoch:%epoch:}%version-%release

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
License: GPL-2.0+
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
License: GPL-2.0+
Group: Publishing
Requires: %name = %{?epoch:%epoch:}%version-%release
Requires: %name-hpcups = %{?epoch:%epoch:}%version-%release
Requires: %name-sane = %{?epoch:%epoch:}%version-%release
Requires: %name-gui = %{?epoch:%epoch:}%version-%release
Requires: notification-daemon
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
License: GPL-2.0+
Group: Publishing
Conflicts: udev-extras < 0.20090516-alt4

%description common
HPLIP is an HP developed solution for printing, scanning, and faxing
with HP inkjet and laser based printers in Linux.

The HPLIP project provides printing support for nearly 1000 printer
models, including Deskjet, Officejet, Photosmart, PSC (Print Scan Copy),

This package contains common libraries for
The Hewlett-Packard  Inkjet  Driver  Project.

%package hpijs
Summary: Hewlett-Packard Co. Inkjet Driver Project (Deprecated)
License: BSD-3-Clause
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

WARNING! HPIJS is deprecated. Feature can be used as is.
Fixes or updates will not be provided.

%if_enabled sane_backend
%package sane
Summary: SANE driver for scanners in HP's multi-function devices (from HPLIP)
License: GPL-2.0+
Group: Publishing
Requires: libsane
Requires: %name-common = %{?epoch:%epoch:}%version-%release
Obsoletes: libsane-hpoj <= 0.91

%description sane
SANE driver for scanners in HP's multi-function devices (from HPLIP)
%endif # sane_backend

%prep
%setup -q
# For some patch we need to gunzip ppds
find . -name *.ppd.gz -exec gunzip '{}' ';'

%patch1 -p2
# let keep it as is.
#patch2 -p2

# # Fix desktop file.
%patch4 -p2 -b .desktop
%patch5 -p1
%if_without new_systemd
%patch6 -p1
%endif
%if_with python3
#patch8 -p2
%else
#patch7 -p2
%endif
%patch9 -p2

chmod +x %{SOURCE102} %{SOURCE103}

%patch101 -p1 -b .pstotiff-is-rubbish
%patch102 -p1 -b .strstr-const
%patch103 -p1 -b .ui-optional
%patch104 -p1 -b .no-asm
%patch105 -p1 -b .deviceIDs-drv
mv prnt/drv/hpijs.drv.in{,.deviceIDs-drv-hpijs}
%if_with python3
%{SOURCE103} \
%else
%{SOURCE102} \
%endif
       prnt/drv/hpcups.drv.in \
       prnt/drv/hpijs.drv.in.deviceIDs-drv-hpijs \
       > prnt/drv/hpijs.drv.in

%patch106 -p1 -b .udev-rules
%patch107 -p1 -b .retry-open
%patch108 -p1 -b .snmp-quirks
%patch109 -p1 -b .hpijs-marker-supply
%patch110 -p1 -b .clear-old-state-reasons
%patch111 -p1 -b .hpcups-sigpipe
%patch112 -p1 -b .logdir
%patch113 -p1 -b .bad-low-ink-warning
#for ppd_file in $(grep '^diff' %{PATCH114} | cut -d " " -f 4);
#do
#  test -e $ppd_file && gunzip ${ppd_file#*/}.gz
#done
%patch114 -p1 -b .deviceIDs-ppd
#for ppd_file in $(grep '^diff' %{PATCH114} | cut -d " " -f 4);
#do
#  test -e $ppd_file && gzip -n ${ppd_file#*/}
#done
#for ppd_file in $(grep '^diff' %{PATCH115} | cut -d " " -f 4);
#do
#  test -e $ppd_file && gunzip ${ppd_file#*/}.gz
#done
%patch115 -p1 -b .ImageableArea
#for ppd_file in $(grep '^diff' %{PATCH115} | cut -d " " -f 4);
#do
#  test -e $ppd_file && gzip -n ${ppd_file#*/}
#done
%patch116 -p1 -b .scan-tmp
%patch117 -p1 -b .log-stderr
%patch118 -p1 -b .parsing
%patch119 -p1 -b .dj990c-margin
%patch120 -p1 -b .strncpy
%patch121 -p1 -b .no-write-bytecode
%patch122 -p1 -b .silence-ioerror
%patch123 -p1 -b .sourceoption
%if_without ernie
%patch124 -p1 -b .no-ernie
rm prnt/hpcups/ErnieFilter.{cpp,h} prnt/hpijs/ernieplatform.h
%endif
#%%patch125 -p1 -b .appdata
%patch126 -p1 -b .check-cups
%patch127 -p1 -b .typo
%patch128 -p1 -b .use-binary-str
%patch129 -p1 -b .error-print-fix
%patch130 -p1 -b .hpfax-import-error-print
%patch131 -p1 -b .wifisetup-bad-call-fix
%patch133 -p1 -b .qmsgbox-typos-fix
%patch134 -p1 -b .libimageprocessor-removal
# Remove proprietary binary blobs
rm -f prnt/hpcups/libImageProcessor-*.so
%patch135 -p1 -b .toolbox-crash
%patch136 -p1 -b .add-ppd-crash
%patch137 -p1 -b .missing-links
%patch138 -p1 -b .hp-laserjet-3052-broken-scanning
%patch139 -p1 -b .hpmud-string-parse
%patch140 -p1 -b .m278-m281-needs-plugin
%patch141 -p1 -b .hpcups-crash
%patch142 -p1 -b .covscan
%patch143 -p1 -b .logging-segfault
%patch144 -p1 -b .systray-blockerror
%patch145 -p1 -b .missing-drivers
%patch146 -p1 -b .model-mismatch
%patch147 -p1 -b .unicodeerror
%patch148 -p1 -b .Wreturn-fix
%patch149 -p1 -b .configure-python
%patch150 -p1 -b .dialog-infinite-loop
%patch151 -p1 -b .find-driver
%patch152 -p1 -b .clean-ldl
%patch153 -p1 -b .revert-plugins
%patch154 -p1 -b .hpsetup-noscanjets
%patch155 -p1 -b .hpfirmware-timeout
%patch156 -p1 -b .gpgdir-perms
%patch157 -p1 -b .hpplugin-udevperms
%patch158 -p1 -b .no-libm-libhpmud-warn
#%%patch160 -p1 -b .plugin-patch
%patch161 -p1 -b .pserror-int
%patch162 -p1 -b .hpaio-orblite-defs
%patch163 -p1 -b .orblite-undefs
%patch164 -p1 -b .pcardext-disable
%patch165 -p1 -b .sclpml-strcasestr
%patch167 -p1 -b .lpstat-parse
%patch168 -p1 -b .curl-switch
%patch169 -p1 -b .raw-strings
%patch170 -p1 -b .hpaio-gcc14
%patch172 -p1 -b .gcc-strc23
%patch173 -p1 -b .format-qdatetime
%patch177 -p1 -b .no-urlopener

# from fedora 3.9.12-3/3.10.9-9
sed -i.duplex-constraints \
    -e 's,\(UIConstraints.* \*Duplex\),//\1,' \
    prnt/drv/hpcups.drv.in

%patch201 -p1 -b .download-plugin

# debian patches
%patch302 -p1
%patch303 -p1
%patch304 -p1
%patch305 -p1
%patch306 -p1
#patch307 -p1
%patch308 -p1
%patch310 -p1
%patch311 -p1
%patch312 -p1
%patch314 -p2
%patch315 -p1
%patch318 -p1
%patch319 -p1
%patch320 -p1
%patch321 -p1
%patch322 -p1
#patch323 -p1
%patch324 -p1
%patch328 -p1
%patch329 -p1

tar -xf %SOURCE6

#pushd prnt/hpijs
#%patch10 -p1
#popd
%patch12 -p1
%if_with l10n
%patch14 -p2
%endif
%patch15 -p2
%patch18 -p2
%patch19 -p2
%patch20 -p2
%patch21 -p2
%patch22 -p2

egrep -lZr '#!/usr/bin/python$' . | xargs -r0 sed -i 's,#!/usr/bin/python$,#!/usr/bin/python%{pysuffix},'
fgrep -lZr '#!/usr/bin/env python' . | xargs -r0 sed -i 's,#!/usr/bin/env python,#!/usr/bin/python%{pysuffix},'

# ELF binary, if found
rm -f hpps hpcups dat2drv

%build
%add_optflags -Wno-implicit-int -Wno-implicit-function-declaration -Wno-incompatible-pointer-types

# we use source that is not pristine; in upstream they gzipped it :(
gzip_n_mov_ppd() {
#	mkdir tmp1; cp -a $1/*.ppd tmp1
	gzip -9 $1/*.ppd
#	mv tmp1/*.ppd $1/; rmdir tmp1
}

gzip_n_mov_ppd fax/ppd
gzip_n_mov_ppd prnt/ps
gzip_n_mov_ppd ppd/classppd/hpcups
gzip_n_mov_ppd ppd/classppd/ps
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
  --enable-fast-install[=PKGS]
                          optimize for fast installation [default=yes]
  --disable-libtool-lock  avoid locking (might break parallel builds)
  --enable-doc-build     enable documentation build (default=yes)
  --enable-hpijs-only-build     enable hpijs only build (default=yes)(Deprecated)
  --enable-lite-build     enable lite build, print & scan only (default=no)
  --enable-hpcups-only-build     enable hpcups only build, print only (default=no)
  --enable-hpijs-install     enable hpijs install (default=no)(Deprecated)
  --enable-hpcups-install     enable hpcups install (default=yes)
  --enable-new-hpcups     enable new hpcups install (default=no)
  --enable-network-build    enable network build (default=yes)
  --enable-pp-build    enable parallel port build (default=no)(Deprecated)
  --enable-scan-build    enable scanner build (default=yes)
  --enable-gui-build    enable gui build (default=yes)
  --enable-fax-build    enable fax build (default=yes)
  --enable-apparmor_build    enable apparmor build (default=no)
  --enable-dbus-build    enable dbus build (default=yes)
  --enable-cups11-build    enable cups 1.1.x build (default=no)
  --enable-udev_sysfs_rules    Use SYSFS attribute instead of ATTR/ATTRS attribute in udev rules(default=no)
  --enable-shadow-build    enable shadow build (default=no)
  --enable-libusb01_build    Use libusb-0.1 instead of libusb-1.0 (default=no. i.e. libusb-1.0)
  --enable-foomatic-ppd-install    enable foomatic static ppd install (default=no)(Deprecated), uses hpppddir
  --enable-foomatic-drv-install    enable foomatic dynamic ppd install (default=no)(Deprecated), uses drvdir and hpppddir
  --enable-cups-drv-install    enable cups dynamic ppd install (default=yes), uses drvdir and hpppddir
  --enable-cups-ppd-install    enable cups static ppd install (default=no), uses hpppddir
  --enable-foomatic-rip-hplip-install    enable foomatic-rip-hplip install (default=no)(Deprecated), uses cupsfilterdir
  --enable-qt5    enable qt5 (default=no)
  --enable-qt4    enable qt4 (default=yes)
  --enable-qt3    enable qt3 (default=no)
  --enable-policykit    enable PolicyKit (default=no)
EOF

#we install foomatic data in separate package
# TODO

# Fix path to Python3 includes for python3 >= 3.8
%if_with python3
%add_optflags `pkg-config --cflags python3`
%endif
%undefine _configure_gettext

%configure \
    --with-mimedir=%{_datadir}/cups/mime \
    --disable-foomatic-rip-hplip-install \
    --enable-pp-build \
    --disable-imageProcessor_build \
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

%make DESTDIR=%buildroot install \
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

# # Comment out all "setSizePolicy" calls, this function is incompatible with
# # PyQT/SIP <3.16
# # the code below is correct: it does'nt comments semilines ..., as previous
# # which cause syntax error in 1.6.6a, but is deprecated with PyQT = 3.16
# perl -p -i -e 'if (/^(.*setSizePolicy.*)$/) {$_="#".$_; if (/,\s*$/) {$endcomma=1}} elsif ($endcomma) {$_="#".$_; $endcomma=0}' `grep -l setSizePolicy $RPM_BUILD_ROOT%_datadir/%name/ui/*.py`

mkdir -p %{buildroot}%{_datadir}/appdata
cp %{SOURCE3} %{buildroot}%{_datadir}/appdata/

# Menu Icons
#install -pD -m644 %name.16.png $RPM_BUILD_ROOT%_miconsdir/hplip.png
#install -pD -m644 %name.32.png $RPM_BUILD_ROOT%_niconsdir/hplip.png
install -pD -m644 %name.48.png $RPM_BUILD_ROOT%_liconsdir/hplip.png

# TODO: switch to hp_logo in desktop?
install -pD -m644 %{buildroot}%{_datadir}/hplip/data/images/16x16/hp_logo.png \
   %{buildroot}%{_datadir}/icons/hicolor/16x16/apps/hplip.png
install -pD -m644 %{buildroot}%{_datadir}/hplip/data/images/32x32/hp_logo.png \
   %{buildroot}%{_datadir}/icons/hicolor/32x32/apps/hplip.png
install -pD -m644 %{buildroot}%{_datadir}/hplip/data/images/64x64/hp_logo.png \
   %{buildroot}%{_datadir}/icons/hicolor/64x64/apps/hplip.png
rm -v -r %buildroot%_datadir/icons/hicolor/48x48

# Remove the installed /etc/sane.d/dll.conf
# because this is provided by the sane package:
rm -f $RPM_BUILD_ROOT%_sysconfdir/sane.d/dll.conf
# Remove other unneeded files
rm -f $RPM_BUILD_ROOT%_datadir/%name/%name
rm -f $RPM_BUILD_ROOT%_datadir/%name/hplip_readme.html
rm -f $RPM_BUILD_ROOT%_datadir/%name/hplip_overview.png

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

# add shebang to make them visible for python3.req.py
find %buildroot%_datadir/%name -name \*.py -exec sed -i '1 i#!%__python3
                                                 \@^#!/usr/bin@d' {} +
find %buildroot%_datadir/%name -name \*.py -exec chmod +x {} +

# removing unpackaged files
pushd $RPM_BUILD_ROOT
#rm  usr/share/hplip/hplip-install usr/share/hplip/install.*
popd

# ELF object out of allowed directory tree
rm -rf \
   %{buildroot}%{_datadir}/hplip/locatedriver* \
   %{buildroot}%{_datadir}/hplip/dat2drv*

# Regenerate hpcups PPDs on upgrade if necessary (bug #579355).
install -p -m755 %{SOURCE101} %{buildroot}%{_bindir}/hpcups-update-ppds

mkdir -p %{buildroot}%{_sysconfdir}/sane.d/dll.d
echo hpaio > %{buildroot}%{_sysconfdir}/sane.d/dll.d/hpaio

# Create an empty plugins directory to make sure it gets the right
# SELinux file context (bug #564551).
mkdir -p %{buildroot}%{_datadir}/hplip/prnt/plugins

# traditional place for udev rules
%if_without new_systemd
mkdir -p %{buildroot}/lib
mv %{buildroot}/usr/lib/udev %{buildroot}/lib/
%endif

# remove hp-uiscan.desktop
rm -f %buildroot%_desktopdir/hp-uiscan.desktop

# Replace symlink by shell wrapper to correct behaviour of right mouse button
rm -f %buildroot%_bindir/hp-systray
install -Dm0755 %{SOURCE10} %buildroot%_bindir/hp-systray

# warning: Print Quality Diagnostic Utility support is deprecated. Feature can be used as is. Fixes or updates will not be provided
rm -f %buildroot%_bindir/hp-pqdiag

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
%doc %_defaultdocdir/%name-%version
%if_enabled python_code
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
%{_bindir}/hp-check-plugin
%{_bindir}/hp-clean
%{_bindir}/hp-colorcal
%{_bindir}/hp-config_usb_printer
%{_bindir}/hp-diagnose_plugin
%{_bindir}/hp-diagnose_queues
%{_bindir}/hp-fab
%{_bindir}/hp-firmware
%{_bindir}/hp-info
%{_bindir}/hp-levels
%{_bindir}/hp-makeuri
%if_enabled policykit
%{_bindir}/hp-pkservice
%endif
%{_bindir}/hp-plugin
%{_bindir}/hp-probe
%{_bindir}/hp-query
%{_bindir}/hp-scan
%{_bindir}/hp-sendfax
%{_bindir}/hp-setup
%{_bindir}/hp-testpage
%{_bindir}/hp-timedate
%{_bindir}/hp-unload
# Files
%dir %{_datadir}/hplip
%{_datadir}/hplip/__pycache__
%{_datadir}/hplip/align.py*
%{_datadir}/hplip/check-plugin.py*
%{_datadir}/hplip/clean.py*
%{_datadir}/hplip/colorcal.py*
%{_datadir}/hplip/config_usb_printer.py*
%{_datadir}/hplip/diagnose_plugin.py*
%{_datadir}/hplip/diagnose_queues.py*
%{_datadir}/hplip/fab.py*
%{_datadir}/hplip/fax
#exclude %{_datadir}/hplip/fax/pstotiff*
%{_datadir}/hplip/firmware.py*
%{_datadir}/hplip/hpdio.py*
%{_datadir}/hplip/hplip_clean.sh
%{_datadir}/hplip/hpssd*
%{_datadir}/hplip/info.py*
%{_datadir}/hplip/__init__.py*
%{_datadir}/hplip/levels.py*
%{_datadir}/hplip/makeuri.py*
%{_datadir}/hplip/plugin.py*
%{_datadir}/hplip/probe.py*
%{_datadir}/hplip/query.py*
%{_datadir}/hplip/scan.py*
%{_datadir}/hplip/sendfax.py*
%{_datadir}/hplip/setup.py*
%{_datadir}/hplip/testpage.py*
%{_datadir}/hplip/timedate.py*
%{_datadir}/hplip/unload.py*
%if_enabled policykit
%{_datadir}/hplip/pkservice.py*
%{_datadir}/polkit-1/actions/com.hp.hplip.policy
%{_unitdir}/hplip-printer@.service
%endif
%if_with python3
#{_datadir}/hplip/__pycache__/check-plugin.*
%dir %{_datadir}/hplip/__pycache__
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

%if_enabled PPDs
%_datadir/ppd/HP/*
%else
%_datadir/cups/model/HP-Fax-hplip.ppd*
%endif

%files hpcups
# CUPS drv
%dir %{_datadir}/cups/drv/hp
%{_datadir}/cups/drv/hp/hpcups.drv
# CUPS filter
%_prefix/lib/cups/filter/hpcups
%_prefix/lib/cups/filter/hpcupsfax
%_prefix/lib/cups/filter/hpcdmfax
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
%{_bindir}/hp-check
%{_bindir}/hp-devicesettings
%{_bindir}/hp-faxsetup
%{_bindir}/hp-linefeedcal
%{_bindir}/hp-makecopies
%{_bindir}/hp-print
%{_bindir}/hp-printsettings
%{_bindir}/hp-systray
#%{_bindir}/hp-toolbox.wrapper
%{_bindir}/hp-toolbox
%{_bindir}/hp-wificonfig
%{_bindir}/hp-uiscan
# Files
%{_datadir}/hplip/check.py*
%{_datadir}/hplip/devicesettings.py*
%{_datadir}/hplip/faxsetup.py*
%{_datadir}/hplip/linefeedcal.py*
%{_datadir}/hplip/makecopies.py*
%{_datadir}/hplip/print.py*
%{_datadir}/hplip/toolbox.py*
%{_datadir}/hplip/systray.py*
%{_datadir}/hplip/printsettings.py*
%{_datadir}/hplip/wificonfig.py*
%{_datadir}/hplip/uiscan.py*
# garbage
%{_bindir}/hp-doctor
%{_bindir}/hp-logcapture
%{_datadir}/hplip/doctor.py*
%{_datadir}/hplip/logcapture.py*
%{_datadir}/hplip/pqdiag.py*
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
# gui data
%{_datadir}/appdata/hplip.appdata.xml
# HPLIP menu files
%_desktopdir/%name.desktop
#_niconsdir/hplip.png
#_liconsdir/hplip.png
#_miconsdir/hplip.png
%_iconsdir/hicolor/*/apps/hplip.png

%if_enabled autostart
%files gui-autostart
/etc/xdg/autostart/hplip-systray.desktop
%endif
%endif

%files recommends

%files common
# HPIP
%{_libdir}/libhpip.so.0
%{_libdir}/libhpip.so.0.0.1
%{_libdir}/libhpipp.so.0
%{_libdir}/libhpipp.so.0.0.1
%{_libdir}/libhpdiscovery.so.0
%{_libdir}/libhpdiscovery.so.0.0.1
%exclude %_libdir/libhpip*so
%exclude %_libdir/libhpdiscovery.so
# The so symlink is required here (see RH bug #489059).
%{_libdir}/libhpmud.so
%{_libdir}/libhpmud.so.0
%{_libdir}/libhpmud.so.0.0.6
%{_udevrulesdir}/56-hpmud.rules
%{_tmpfilesdir}/hplip.conf

%files hpijs
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
* Thu May 21 2026 Andrey Cherepanov <cas@altlinux.org> 1:3.26.4-alt1
- New version (fixes: CVE-2026-8631, CVE-2026-8632).
- Added support for the following new printers:
  + HP LaserJet Pro MFP 3106sdw
  + HP LaserJet Pro MFP 3105sdw
  + HP Envy 6500e series
  + HP Envy 6500 series
  + HP OfficeJet Pro 9730 Series
  + HP OfficeJet Pro 9730e Series
  + HP OfficeJet Pro 9720 Series
  + HP OfficeJet Pro 9720e Series
  + HP OfficeJet Pro 8130e All-in-One series
  + HP OfficeJet Pro 8130 All-in-One series
  + HP OfficeJet 8130e All-in-One series
  + HP OfficeJet 8130 All-in-One series
  + HP OfficeJet Pro 8120e All-in-One series
  + HP OfficeJet Pro 8120 All-in-One series
  + HP OfficeJet 8120e All-in-One series
  + HP OfficeJet 8120 All-in-One series
  + HP DeskJet Ink Advantage ultra 5800 All-in-One Printer series
  + HP DeskJet Ink Advantage ultra 5100 All-in-One Printer series
  + HP DeskJet 4300e All-in-One Printer series
  + HP DeskJet Ink Advantage 4300 All-in-One Printer series
  + HP DeskJet 4300 All-in-One Printer series
  + HP DeskJet 2900e All-in-One Printer series
  + HP DeskJet Ink Advantage 2900 All-in-One Printer series
  + HP DeskJet 2900 All-in-One Printer series

* Wed Dec 17 2025 Anton Midyukov <antohami@altlinux.org> 1:3.25.8-alt3
- NMU: hplip-alt-hplip-desktop.patch: add Name[ru].

* Thu Dec 11 2025 Andrey Cherepanov <cas@altlinux.org> 1:3.25.8-alt2
- Fixed checksum for 3.25.8 (ALT #57084).

* Tue Nov 18 2025 Andrey Cherepanov <cas@altlinux.org> 1:3.25.8-alt1
- New version.
- Added support for the following new printers:
  + HP LaserJet Enterprise 5501, 5501n, 5502, 5502dn
  + HP LaserJet Enterprise 6500, 6500dn, 6500n, 6501, 6501dn
  + HP LaserJet Enterprise Flow MFP 5602zfw
  + HP LaserJet Enterprise Flow MFP 6600zfsw, 6600zfw
  + HP LaserJet Enterprise Flow MFP 8601z
  + HP LaserJet Enterprise Flow MFP X530
  + HP LaserJet Enterprise Flow MFP X62757zs
  + HP LaserJet Enterprise MFP 5601, 5601dn, 5602, 5602dn, 5602f
  + HP LaserJet Enterprise MFP 6600, 6600dn
  + HP LaserJet Enterprise MFP X53052, X53052dn
  + HP LaserJet Enterprise MFP X62757, X62757dn
  + HP LaserJet Enterprise X50452, X50452dn
  + HP LaserJet Enterprise X60257, X60257dn
  + HP LaserJet Enterprise X60357, X60357dn
  + DEX D50452dn
  + DEX MFP D53052dn

* Thu Nov 13 2025 Aleksandr Shamaraev <shad@altlinux.org> 1:3.25.6-alt3.2
- NMU: fix:
  + launch HP Device Manager via *.desktop while hp-systray is running in Gnome (ALT #54987)
  + launch HP Device Manager via *.desktop while hp-systray is running in other DE (ALT #54478)

* Sat Nov 01 2025 Aleksandr Shamaraev <shad@altlinux.org> 1:3.25.6-alt3.1
- NMU: fix: icon not displayed (ALT #56320)

* Wed Sep 10 2025 Andrey Cherepanov <cas@altlinux.org> 1:3.25.6-alt3
- Disabled resize to scan area (ALT #55386).

* Mon Sep 01 2025 Andrey Cherepanov <cas@altlinux.org> 1:3.25.6-alt2
- Updated hplip-keyserver.patch from fedora to use keyserver.ubuntu.com
  instead of unavialable pool.sks-keyservers.net (ALT #53956).

* Sun Aug 24 2025 Andrey Cherepanov <cas@altlinux.org> 1:3.25.6-alt1
- New version.
- Added support for the following new printers:
  + HP LaserJet Enterprise Flow MFP 8601z
  + HP LaserJet Pro MFP M126a plus, M126nw plus, M126snw plus
  + HP Envy Photo 7200 series
  + HP Envy Photo 7900 series
  + HP OfficeJet Pro 9110 Series
  + HP OfficeJet 9120 Series
  + HP OfficeJet Pro 9120 Series
  + HP OfficeJet Pro 9130 Series

* Tue Jul 29 2025 Aleksandr Shamaraev <shad@altlinux.org> 1:3.25.2-alt4
- NMU: disable resize in hp-scan (ALT #55386)

* Wed Jul 02 2025 Aleksandr Shamaraev <shad@altlinux.org> 1:3.25.2-alt3
- NMU:
  + adjusted hp-systray for Plasma X11 (ALT #54478)
  + fix launch hp-toolbox on Gnome Wayland (ALT #54987)

* Sat Jun 28 2025 Aleksandr Shamaraev <shad@altlinux.org> 1:3.25.2-alt2
- NMU: fix launch hp-systray on Plasma X11 (ALT #54478)

* Fri Mar 21 2025 Andrey Cherepanov <cas@altlinux.org> 1:3.25.2-alt1
- New version.
- Added support for the following new printers:
  + HP LaserJet Enterprise Flow MFP 8601, 8601z+, MFP 8601dn
  + HP Color LaserJet Enterprise MFP 8801dn, Flow MFP 8801z, 8801z+
  + HP LaserJet Enterprise 8501dn, 8501x, 8501x+
  + DEX MFP D826
  + DEX MFP D82640
  + DEX MFP D82650
  + DEX MFP D82660
  + DEX D50145
  + DEX MFP D42540
  + DEX MFP D52645
  + DEX Color D55745
  + DEX Color MFP D57945
  + DEX Color MFP D677
  + DEX Color MFP D67755
  + DEX Color MFP D67765
  + DEX Color MFP D877
  + DEX Color MFP D87740
  + DEX Color MFP D87750
  + DEX Color MFP D87760
  + DEX Color MFP D87770
  + DEX Color MFP D786
  + DEX Colour MFP D78625
  + DEX Color MFP D78630
  + DEX Color MFP D78635
  + DEX MFP D731
  + DEX MFP D73130
  + DEX MFP D73135
  + DEX MFP D73140

* Fri Feb 14 2025 Andrew A. Vasilyev <andy@altlinux.org> 1:3.24.4-alt2
- NMU: fix FTBFS with gcc14

* Wed Jun 19 2024 Andrey Cherepanov <cas@altlinux.org> 1:3.24.4-alt1
- New version.
- Added support for the following new printers:
  + HP OfficeJet 8120 All-in-One series
  + HP OfficeJet Pro 8120 All-in-One series
  + HP OfficeJet 8130 All-in-One series
  + HP OfficeJet Pro 8130 All-in-One series
  + HP OfficeJet Pro 9720 Series
  + HP OfficeJet Pro 9730 Series

* Mon Mar 11 2024 Andrey Cherepanov <cas@altlinux.org> 1:3.23.12-alt4
- FTBFS: fixed build.

* Sat Mar 02 2024 Andrey Cherepanov <cas@altlinux.org> 1:3.23.12-alt3
- Requires python3-module-pygobject3 (ALT #49591).

* Wed Feb 21 2024 Andrey Cherepanov <cas@altlinux.org> 1:3.23.12-alt2
- Fixed crash on readfp (ALT #49464).

* Sat Dec 02 2023 Andrey Cherepanov <cas@altlinux.org> 1:3.23.12-alt1
- New version.
- Added support for the following new printers:
  + HP OfficeJet Pro 9130b, 9120b, 9110b series
  + HP Color LaserJet Enterprise Flow MFP X58045z, X58045zs
  + HP Color LaserJet Enterprise MFP X58045, X58045dn
  + HP LaserJet Pro P1106 plus
  + HP LaserJet Pro P1108 plus

* Wed Sep 20 2023 Andrey Cherepanov <cas@altlinux.org> 1:3.23.8-alt1
- New version.
- Added support for the following new printers:
  + HP Color LaserJet Pro MFP 4201, 4202, 4203, 4301, 4302, 4303
  + HP DeskJet 2800 All-in-One Printer series
  + HP DeskJet 2800e All-in-One Printer series
  + HP DeskJet Ink Advantage 2800 All-in-One Printer series
  + HP DeskJet 4200 All-in-One Printer series
  + HP DeskJet 4200e All-in-One Printer series
  + HP DeskJet Ink Advantage 4200 All-in-One Printer series
  + HP DeskJet Ink Advantage Ultra 4900 All-in-One Printer series

* Sat Aug 12 2023 Daniel Zagaynov <kotopesutility@altlinux.org> 1:3.23.5-alt2.1
- NMU:
    + added shebang to python3-modules from %%_datadir/%%name and made them
      executable to make them visible for python3.req.py
    + ignore self-provide *.sixext.moves

* Fri Jul 14 2023 Andrey Cherepanov <cas@altlinux.org> 1:3.23.5-alt2
- Removed deprecated hp-pqdiag.

* Fri Jun 09 2023 Andrey Cherepanov <cas@altlinux.org> 1:3.23.5-alt1
- New version.
- Added support for the following new printers:
  + HP Color LaserJet Enterprise 5700, 5700dn
  + HP Color LaserJet Enterprise 6700, 6700dn
  + HP Color LaserJet Enterprise 6701, 6701dn
  + HP Color LaserJet Enterprise Flow MFP 5800zf
  + HP Color LaserJet Enterprise Flow MFP 6800zf, 6800zfsw, 6800zfw+
  + HP Color LaserJet Enterprise Flow MFP 6801zfw+
  + HP Color LaserJet Enterprise Flow MFP X57945z
  + HP Color LaserJet Enterprise Flow MFP X57945zs
  + HP Color LaserJet Enterprise Flow MFP X67755zs, X67755z+
  + HP Color LaserJet Enterprise Flow MFP X67765zs, X67765z+
  + HP Color LaserJet Enterprise Flow MFP X677z
  + HP Color LaserJet Enterprise Flow MFP X677zs, X677z+
  + HP Color LaserJet Enterprise MFP 5800, 5800dn, 5800f
  + HP Color LaserJet Enterprise MFP 6800, 6800dn
  + HP Color LaserJet Enterprise MFP 6801, 6801zfsw
  + HP Color LaserJet Enterprise MFP X57945
  + HP Color LaserJet Enterprise MFP X57945dn
  + HP Color LaserJet Enterprise MFP X677
  + HP Color LaserJet Enterprise MFP X67755dn
  + HP Color LaserJet Enterprise MFP X67765dn
  + HP Color LaserJet Enterprise MFP X677dn
  + HP Color LaserJet Enterprise MFP X677s
  + HP Color LaserJet Enterprise X55745, X55745dn
  + HP Color LaserJet Enterprise X654, X654dn
  + HP Color LaserJet Enterprise X65455dn
  + HP Color LaserJet Enterprise X65465dn

* Wed Apr 05 2023 Andrey Cherepanov <cas@altlinux.org> 1:3.23.3-alt1
- New version.
- Added support for the following new printers:
  + HP Smart Tank 520_540 series
  + HP Smart Tank 580-590 series
  + HP Smart Tank 5100 series
  + HP Smart Tank 210-220 series

* Sat Nov 05 2022 Andrey Cherepanov <cas@altlinux.org> 1:3.22.10-alt1
- New version.

* Wed Jun 29 2022 Andrey Cherepanov <cas@altlinux.org> 1:3.22.6-alt1
- New version.
- Added support for the following new printers:
  + HP Color LaserJet Managed MFP E785dn
  + HP Color LaserJet Managed MFP E78523dn
  + HP Color LaserJet Managed MFP E78528dn
  + HP Color LaserJet Managed MFP E786dn
  + HP Color LaserJet Managed MFP E786 Core Printer
  + HP Color LaserJet Managed MFP E78625dn
  + HP Color LaserJet Managed Flow MFP E786z
  + HP Color LaserJet Managed Flow MFP E78625z
  + HP Color LaserJet Managed MFP E78630dn
  + HP Color LaserJet Managed Flow MFP E78630z
  + HP Color LaserJet Managed MFP E78635dn
  + HP Color LaserJet Managed Flow MFP E78635z
  + HP LaserJet Managed MFP E731dn
  + HP LaserJet Managed MFP E731 Core Printer
  + HP LaserJet Managed MFP E73130dn
  + HP LaserJet Managed Flow MFP E731z
  + HP LaserJet Managed Flow MFP E73130z
  + HP LaserJet Managed MFP E73135dn
  + HP LaserJet Managed Flow MFP E73135z
  + HP LaserJet Managed MFP E73140dn
  + HP LaserJet Managed Flow MFP E73140z
  + HP Color LaserJet Managed MFP E877dn
  + HP Color LaserJet Managed MFP E877 Core Printer
  + HP Color LaserJet Managed MFP E87740dn
  + HP Color LaserJet Managed Flow MFP E877z
  + HP Color LaserJet Managed Flow MFP E87740z
  + HP Color LaserJet Managed MFP E87750dn
  + HP Color LaserJet Managed Flow MFP E87750z
  + HP Color LaserJet Managed MFP E87760dn
  + HP Color LaserJet Managed Flow MFP E87760z
  + HP Color LaserJet Managed MFP E87770dn
  + HP Color LaserJet Managed Flow MFP E87770z
  + HP LaserJet Managed MFP E826dn
  + HP LaserJet Managed MFP E826 Core Printer
  + HP LaserJet Managed MFP E82650dn
  + HP LaserJet Managed Flow MFP E826z
  + HP LaserJet Managed Flow MFP E82650z
  + HP LaserJet Managed MFP E82660dn
  + HP LaserJet Managed Flow MFP E82660z
  + HP LaserJet Managed MFP E82670dn
  + HP LaserJet Managed Flow MFP E82670z
  + HP LaserJet Managed MFP E730dn
  + HP LaserJet Managed MFP E73025dn
  + HP LaserJet Managed MFP E73030dn
  + HP LaserJet Pro MFP 3101fdwe, 3101fdw, 3101fdne, 3101fdn
  + HP LaserJet Pro MFP 3102fdwe, 3102fdw, 3102fdne, 3102fdn
  + HP LaserJet Pro MFP 3103fdw, 3103fdn
  + HP LaserJet Pro MFP 3104fdw, 3104fdn
  + HP LaserJet Pro 3001dwe, 3001dn, 3001dne, 3001dw
  + HP LaserJet Pro 3002dn, 3002dne, 3002dw, 3002dwe 
  + HP LaserJet Pro 3003dn, 3003dw
  + HP LaserJet Pro 3004dn, 3004dw

* Sat Apr 30 2022 Andrey Cherepanov <cas@altlinux.org> 1:3.22.4-alt1
- New version.
- Added support for the following new printers:
  + HP LaserJet Pro 4001ne, 4001n, 4001dne, 4001dn, 4001dwe, 4001dw, 4001d, 4001de
  + HP LaserJet Pro 4002ne, 4002n, 4002dne, 4002dn, 4002dwe, 4002dw, 4002d, 4002de
  + HP LaserJet Pro 4003dn, 4003dw, 4003n, 4003d
  + HP LaserJet Pro 4004d, 4004dn, 4004dw
  + HP LaserJet Pro MFP 4101dwe, 4101dw, 4101fdn, 4101fdne, 4101fdw, 4101fdwe
  + HP LaserJet Pro MFP 4102dwe, 4102dw, 4102fdn, 4102fdw, 4102fdwe, 4102fdne, 4102fnw, 4102fnwe
  + HP LaserJet Pro MFP 4103dw, 4103dn, 4103fdn, 4103fdw
  + HP LaserJet Pro MFP 4104dw, 4104fdw, 4104fdn
  + HP ScanJet Pro 3600 f1
  + HP ScanJet Pro N4600 fnw1
  + HP ScanJet Pro 2600 f1
  + HP ScanJet Enterprise Flow N6600 fnw1

* Thu Mar 03 2022 Andrey Cherepanov <cas@altlinux.org> 1:3.22.2-alt1
- New version.
- Added support for the following new printers:
  + HP LaserJet Tank MFP 1602a, 1602w
  + HP LaserJet Tank MFP 1604w
  + HP LaserJet Tank MFP 2602dn, 2602sdn, 2602sdw, 2602dw
  + HP LaserJet Tank MFP 2604dw, 2604sdw
  + HP LaserJet Tank MFP 2603dw, 2603sdw
  + HP LaserJet Tank MFP 2605sdw
  + HP LaserJet Tank MFP 2606dn, 2606sdn, 2606sdw, 2606dw, 2606dc
  + HP LaserJet Tank MFP 1005, 1005w, 1005nw
  + HP LaserJet Tank 1502a, 1502w
  + HP LaserJet Tank 1504w
  + HP LaserJet Tank 2502dw, 2502dn
  + HP LaserJet Tank 2504dw
  + HP LaserJet Tank 2503dw
  + HP LaserJet Tank 2506dw, 2506d, 2506dn
  + HP LaserJet Tank 1020, 1020w, 1020nw

* Sun Jan 02 2022 Andrey Cherepanov <cas@altlinux.org> 1:3.21.12-alt1
- New version.

* Tue Nov 09 2021 Andrey Cherepanov <cas@altlinux.org> 1:3.21.10-alt2
- Move all PPD files to main package hplip.

* Fri Nov 05 2021 Andrey Cherepanov <cas@altlinux.org> 1:3.21.10-alt1
- New version.
- Added support for the following new printers:
  + HP ENVY Inspire 7200e series
  + HP ENVY Inspire 7900e series
  + HP LaserJet MFP M139a, M139w, M139we
  + HP LaserJet MFP M140a, M140w, M140we
  + HP LaserJet MFP M141a, M141w, M141we
  + HP LaserJet MFP M142a, M142w, M142we
  + HP LaserJet M109a, M109w, M109we
  + HP LaserJet M110a, M110w, M110we
  + HP LaserJet M111a, M111w, M111we
  + HP LaserJet M112a, M112w, M112we
  + HP DesignJet Z6 Pro 64in
  + HP DesignJet Z9 Pro 64in
  + HP PageWide XL Pro 5200 PS MFP series
  + HP PageWide XL Pro 8200 PS MFP series
  + HP PageWide XL 3920 MFP
  + HP PageWide XL 4200 Printer, Multifunction Printer
  + HP PageWide XL 4700 Printer, Multifunction Printer
  + HP PageWide XL 5200 Printer, Multifunction Printer
  + HP PageWide XL 8200 Printer

* Thu Sep 09 2021 Andrey Cherepanov <cas@altlinux.org> 1:3.21.8-alt1
- New version.
- Added support for the following new printers:
  + HP Smart Tank 500 series
  + HP Smart Tank 530 series
  + HP Smart Tank Plus 570 series
  + HP Smart Tank 7600
  + HP Smart Tank 750
  + HP Smart Tank 790
  + HP Smart Tank Plus 710-720
  + HP Smart Tank Plus 7000
  + HP Smart Tank Plus 660-670
  + HP Smart Tank Plus 6000
  + HP DeskJet Ink Advantage Ultra 4800 All-in-One Printer series

* Sat Jul 10 2021 Andrey Cherepanov <cas@altlinux.org> 1:3.21.6-alt1
- New version.
- Added support for the following new printers:
  + HP Envy 6400 series

* Tue Jun 22 2021 Andrey Cherepanov <cas@altlinux.org> 1:3.21.4-alt2
- Correctly detect ALT distribution, drop strange auth type change from Fedora.

* Thu May 13 2021 Andrey Cherepanov <cas@altlinux.org> 1:3.21.4-alt1
- New version.
- Added support for the following new printers:
  + HP Envy 6400 series

* Fri Feb 26 2021 Andrey Cherepanov <cas@altlinux.org> 1:3.21.2-alt2
- Add M125ra model.

* Fri Feb 19 2021 Andrey Cherepanov <cas@altlinux.org> 1:3.21.2-alt1
- New version.
- Added support for the following new printers:
  + HP LaserJet Enterprise M406dn
  + HP LaserJet Enterprise M407dn
  + HP LaserJet Enterprise MFP M430f
  + HP LaserJet Enterprise MFP M431f
  + HP LaserJet Managed E40040dn
  + HP LaserJet Managed MFP E42540f
  + HP Color LaserJet Enterprise M455dn
  + HP Color LaserJet Enterprise MFP M480f
  + HP Color LaserJet Managed E45028dn
  + HP Color LaserJet Managed MFP E47528f
  + HP PageWide XL 3920 MFP
  + HP PageWide XL 4200 Printer, 4200 Multifunction Printer
  + HP PageWide XL 4700 Printer, 4700 Multifunction Printer
  + HP PageWide XL 5200 Printer, 5200 Multifunction Printer
  + HP PageWide XL 8200 Printer
  + HP Laserjet M207d, M207dw
  + HP Laserjet M208d, M208dw
  + HP Laserjet M209d, M209dw, M209dwe
  + HP Laserjet M210d, M210dw, M210dwe
  + HP Laserjet M211d, M211dw
  + HP Laserjet M212d, M212dw, M212dwe
  + HP LaserJet MFP M232d, M232dw, M232dwc, M232sdn, M232sdw
  + HP LaserJet MFP M233d, M233dw, M233sdn, M233sdw
  + HP LaserJet MFP M234dw, M234dwe, M234sdn, M234sdne, M234sdw, M234sdwe
  + HP LaserJet MFP M235d, M235dw, M235dwe, M235sdn, M235sdne, M235sdw, M235sdwe
  + HP LaserJet MFP M236d, M236dw, M236sdn, M236sdw
  + HP LaserJet MFP M237d, M237dw, M237dwe, 237sdne, M237sdn, 237sdwe, M237sdw

* Thu Dec 10 2020 Andrey Cherepanov <cas@altlinux.org> 1:3.20.11-alt2
- Fix hp-systray for $XDG_SESSION_DESKTOP = KDE (ALT #39401).

* Wed Dec 02 2020 Andrey Cherepanov <cas@altlinux.org> 1:3.20.11-alt1
- New version.
- Replace symlink by shell wrapper to correct behaviour of right mouse button.

* Fri Oct 02 2020 Andrey Cherepanov <cas@altlinux.org> 1:3.20.9-alt1
- New version.
- Added support for the following new Printers:
  + HP LaserJet MFP M234dw, M234dwe
  + HP Color LaserJet Managed MFP E57540dn
  + HP Color LaserJet Managed Flow MFP E57540c
  + HP Color LaserJet Enterprise MFP M578dn, M578f
  + HP Color LaserJet Enterprise Flow MFP M578c, M578z
  + HP Color LaserJet Managed E55040dw, E55040dn
  + HP Color LaserJet Enterprise M554dn
  + HP Color LaserJet Enterprise M555dn, M555x

* Fri Jun 19 2020 Andrey Cherepanov <cas@altlinux.org> 1:3.20.6-alt1
- New version.
- Added support for the following new Printers:
  + HP Color LaserJet Managed MFP E78223a
  + HP Color LaserJet Managed MFP E78223dv
  + HP Color LaserJet Managed MFP E78223dn
  + HP Color LaserJet Mngd MFP E78223dn Plus
  + HP Color LaserJet Mngd MFP E78223dn CN
  + HP Color LaserJet Managed MFP E78228dn 
  + HP Color LaserJet Managed MFP E78228dn Plus
  + HP Color LaserJet Managed MFP E78228dn CN
  + HP Color LaserJet Managed Flow MFP E78330z Plus
  + HP Color LaserJet Managed Flow MFP E78330z CN
  + HP Color LaserJet Managed MFP E78330dn
  + HP Color LaserJet Mngd MFP E78330dn Plus
  + HP Color LaserJet Mngd MFP E78330dn CN
  + HP Color LaserJet Managed MFP E78330z
  + HP Color LaserJet Managed Flow MFP E78325z Plus
  + HP Color LaserJet Managed Flow MFP E78325dn CN
  + HP Color LaserJet Managed Flow MFP E78325z CN
  + HP Color LaserJet Managed MFP E78325dn
  + HP Color LaserJet Managed MFP E78325z
  + HP Color LaserJet Managed Flow MFP E78323z
  + HP Color LaserJet Mgd Flw MFPE78323Z Plus
  + HP Color LaserJet Mgd Flw MFPE78323z CN
  + HP Color LaserJet Managed MFP E78323dn
  + HP Color LaserJet Mngd MFP E78323dn Plus
  + HP Color LaserJet Mngd MFP E78323dn CN

* Mon May 18 2020 Andrey Cherepanov <cas@altlinux.org> 1:3.20.5-alt1
- New version.
- Added support for the following new Printers:
  + HP DeskJet 1200
  + HP DeskJet Ink Advantage 1200
  + HP DeskJet 2300 All-in-One
  + HP DeskJet Ink Advantage 2300 All-in-One
  + HP ENVY 6000 series
  + HP DeskJet Plus 6000 series
  + HP ENVY Pro 6400 series
  + HP DeskJet Plus 6400 series
  + HP DeskJet 2700 All-in-One Printer series
  + HP DeskJet Ink Advantage 2700 All-in-One Printer series
  + HP DeskJet Plus 4100 All-in-One Printer series
  + HP DeskJet Ink Advantage 4100 All-in-One Printer series
  + HP LaserJet Enterprise M610dn
  + HP LaserJet Enterprise M611dn
  + HP LaserJet Enterprise M611x
  + HP LaserJet Enterprise M612dn
  + HP LaserJet Enterprise M612x
  + HP LaserJet Enterprise MFP M634dn
  + HP LaserJet Enterprise MFP M634z
  + HP LaserJet Enterprise Flow MFP M634h
  + HP LaserJet Enterprise MFP M635h
  + HP LaserJet Enterprise MFP M635fht
  + HP LaserJet Enterprise Flow MFP M635z
  + HP LaserJet Enterprise MFP M636fh
  + HP LaserJet Enterprise Flow MFP M636z

* Wed Apr 01 2020 Andrey Cherepanov <cas@altlinux.org> 1:3.20.3-alt4
- Add requirement of %_bindir/lsusb for hplip-gui (ALT #38312).

* Thu Mar 19 2020 Andrey Cherepanov <cas@altlinux.org> 1:3.20.3-alt3
- Returned Python autorequires, required distro python module.

* Mon Mar 16 2020 Andrey Cherepanov <cas@altlinux.org> 1:3.20.3-alt2
- Apply patch (ALT #38043).

* Thu Mar 12 2020 Andrey Cherepanov <cas@altlinux.org> 1:3.20.3-alt1
- New version (ALT #38043).
- Fix systray icon menu (ALT #38147).

* Fri Feb 28 2020 Andrey Cherepanov <cas@altlinux.org> 1:3.20.2-alt1
- New version.
- Added support for the following new Printers:
  + HP Neverstop Laser MFP 1200n
  + HP Neverstop Laser MFP 1201n
  + HP Neverstop Laser MFP 1200nw
  + HP Neverstop Laser MFP 1202nw
  + HP Laser NS MFP 1005n
  + HP Neverstop Laser 1000n
  + HP Neverstop Laser 1001nw
  + HP Laser NS 1020n
  + HP ScanJet Pro 2000 s2
  + HP ScanJet Pro 3000 s4
  + HP ScanJet Pro N4000 snw1
  + HP ScanJet Enterprise Flow 5000 s5
  + HP ScanJet Enterprise Flow N7000 snw1

* Thu Feb 27 2020 Andrey Cherepanov <cas@altlinux.org> 1:3.19.12-alt3
- Do not generate provides with Python scripts that are not packaged as library.
- Fix path to Python3 includes for python3 >= 3.8.
- Spec cleanup.

* Fri Feb 14 2020 Andrey Cherepanov <cas@altlinux.org> 1:3.19.12-alt2
- Use python3 in service file.

* Mon Dec 16 2019 Andrey Cherepanov <cas@altlinux.org> 1:3.19.12-alt1
- New version.
- Added support for the following new Printers:
  + HP Color LaserJet Pro M155a
  + HP Color LaserJet Pro M155nw
  + HP Color LaserJet Pro M156a
  + HP Color LaserJet Pro M156nw
  + HP Color LaserJet Pro M255dn
  + HP Color LaserJet Pro M255dw
  + HP Color LaserJet Pro M255nw
  + HP Color LaserJet Pro M256dn
  + HP Color LaserJet Pro M256dw
  + HP Color LaserJet Pro M256nw
  + HP Color LaserJet Pro MFP M182n
  + HP Color LaserJet Pro MFP M182nw
  + HP Color LaserJet Pro MFP M183fw
  + HP Color LaserJet Pro MFP M184n
  + HP Color LaserJet Pro MFP M184nw
  + HP Color LaserJet Pro MFP M185fw
  + HP Color LaserJet Pro MFP M282nw
  + HP Color LaserJet Pro MFP M283cdw
  + HP Color LaserJet Pro MFP M283fdn
  + HP Color LaserJet Pro MFP M283fdw
  + HP Color LaserJet Pro MFP M284nw
  + HP Color LaserJet Pro MFP M285cdw
  + HP Color LaserJet Pro MFP M285fdn
  + HP Color LaserJet Pro MFP M285fdw
- Fix select PPD file in Qt5 GUI (ALT #37610).

* Wed Nov 06 2019 Andrey Cherepanov <cas@altlinux.org> 1:3.19.11-alt1
- New version.
- Added support for the following new Printers:
  + HP Color LaserJet MFP M776dn
  + HP Color LaserJet Flow MFP M776z
  + HP Color LaserJet Flow MFP M776zs
  + HP Color LaserJet M856dn
  + HP Color LaserJet M856x
  + HP Color LaserJet E85055dn

* Thu Oct 31 2019 Andrey Cherepanov <cas@altlinux.org> 1:3.19.10-alt1
- New version.
- Added support for the following new Printers:
  + HP Color LaserJet MFP M776dn
  + HP Color LaserJet Flow MFP M776z
  + HP Color LaserJet Flow MFP M776zs
  + HP Color LaserJet M856dn
  + HP Color LaserJet M856x
  + HP Color LaserJet E85055dn
- Build with Python3 (ALT #37289).

* Thu Aug 29 2019 Andrey Cherepanov <cas@altlinux.org> 1:3.19.8-alt1
- New version.
- Added support for new printers:
  + HP DesignJet T1530 Postscript
  + HP DesignJet T2530 Postscript
  + HP DesignJet T930 Postscript
  + HP DesignJet T1600 Postscript Printer
  + HP DesignJet T1600dr Postscript Printer
  + HP DesignJet T2600 Postscript MFP
  + HP LaserJet Pro MFP M329dn
  + HP LaserJet Pro MFP M329dw
  + HP LaserJet Pro M305d
  + HP LaserJet Pro M304a
  + HP LaserJet Pro M305dn
  + HP LaserJet Pro M305dw

* Sat Jun 29 2019 Andrey Cherepanov <cas@altlinux.org> 1:3.19.6-alt1
- New version.
- Added support for new printers:
  + HP Smart Tank 500 series
  + HP Smart Tank 530 series
  + HP Smart Tank Plus 570 series
  + HP Smart Tank Plus 650
  + HP Smart Tank 610
  + HP Smart Tank Plus 550
  + HP Smart Tank 510
  + HP Neverstop Laser MFP 1200a
  + HP Neverstop Laser MFP 1200w
  + HP Laser NS MFP 1005
  + HP Laser NS MFP 1005w
  + HP Neverstop Laser 1000a
  + HP Neverstop Laser 1000w
  + HP Laser NS 1020
  + HP Laser NS 1020w
  + HP DesignJet T2600dr Postscript MFP
  + HP DesignJet XL 3600 PS MFP
  + HP Color LaserJet Pro M453cdn
  + HP Color LaserJet Pro M454dn
  + HP Color LaserJet Pro M454cdn
  + HP Color LaserJet Pro M453cdw
  + HP Color LaserJet Pro M454nw
  + HP Color LaserJet Pro M454dw
  + HP Color LaserJet Pro M454cdw
  + HP Color LaserJet Pro MFP M479dw
  + HP Color LaserJet Pro MFP M478fcdn
  + HP Color LaserJet Pro MFP M479fdn
  + HP Color LaserJet Pro MFP M479fcdn
  + HP Color LaserJet Pro MFP M478fcdw
  + HP Color LaserJet Pro MFP M479fdw
  + HP Color LaserJet Pro MFP M479fnw
  + HP Color LaserJet Pro MFP M479fcdw
  + HP LaserJet Pro MFP M428dw
  + HP LaserJet Pro MFP M429dw
  + HP LaserJet Pro MFP M428fdn
  + HP LaserJet Pro MFP M428c1
  + HP LaserJet Pro MFP M428c3
  + HP LaserJet Pro MFP M428m
  + HP LaserJet Pro MFP M429fdn
  + HP LaserJet Pro MFP M428fdw
  + HP LaserJet Pro MFP M428c2
  + HP LaserJet Pro MFP M428c4
  + HP LaserJet Pro MFP M429fdw
  + HP LaserJet Pro M404d
  + HP LaserJet Pro M405d
  + HP LaserJet Pro M404n
  + HP LaserJet Pro M405n
  + HP LaserJet Pro M404dn
  + HP LaserJet Pro M404c1
  + HP LaserJet Pro M404c3
  + HP LaserJet Pro M404m
  + HP LaserJet Pro M405dn
  + HP LaserJet Pro M404dw
  + HP LaserJet Pro M404c2
  + HP LaserJet Pro M404c4
  + HP LaserJet Pro M405dw

* Thu May 23 2019 Andrey Cherepanov <cas@altlinux.org> 1:3.19.5-alt2
- Add Russian localization to desktop file.
- Remove hp-uiscan.desktop.

* Tue May 14 2019 Andrey Cherepanov <cas@altlinux.org> 1:3.19.5-alt1
- New version.
- Added support for new printers:
  + HP LaserJet Enterprise M507n
  + HP LaserJet Enterprise M507dn
  + HP LaserJet Enterprise M507x
  + HP LaserJet Enterprise M507dng
  + HP LaserJet Managed E50145dn
  + HP LaserJet Managed E50145x
  + HP LaserJet Enterprise MFP M528dn
  + HP LaserJet Enterprise MFP M528f
  + HP LaserJet Enterprise Flow MFP M528c
  + HP LaserJet Enterprise Flow MFP M528z
  + HP LaserJet Managed MFP E52645dn
  + HP LaserJet Managed Flow MFP E52645c
  + HP Color LaserJet Managed E75245dn
  + HP Color LaserJet Enterprise M751n
  + HP Color LaserJet Enterprise M751dn
  + HP PageWide XL 3900PS MFP
  + HP OfficeJet Pro 8030 All-in-One Printer series
  + HP OfficeJet Pro 8020 All-in-One Printer series
  + HP OfficeJet 8020 All-in-One Printer Series
  + HP OfficeJet 8010 All-in-One Printer series

* Thu Mar 28 2019 Andrey Cherepanov <cas@altlinux.org> 1:3.19.3-alt1
- New version.
- Added support for new printers:
  + HP OfficeJet Pro All-in-One 9010
  + HP OfficeJet Pro All-in-One 9020
  + HP OfficeJet All-in-One 9010
  + HP PageWide XL 4100 Printer
  + HP PageWide XL 4100 MFP
  + HP PageWide XL 4600 Printer
  + HP PageWide XL 4600PS MFP
  + HP Color LaserJet Managed MFP E77422a
  + HP Color LaserJet Managed MFP E77422dv
  + HP Color LaserJet Managed MFP E77422dn
  + HP Color LaserJet Managed MFP E77428dn
  + HP LaserJet MFP E72425a
  + HP LaserJet MFP E72425dv
  + HP LaserJet MFP E72425dn
  + HP LaserJet MFP E72430dn
  + HP LaserJet Managed MFP E62655dn
  + HP LaserJet Managed MFP E62665hs
  + HP LaserJet Managed Flow MFP E62665h
  + HP LaserJet Managed Flow MFP E62675z
  + HP LaserJet Managed Flow MFP E62665z
  + HP LaserJet Managed E60155dn
  + HP LaserJet Managed E60165dn
  + HP LaserJet Managed E60175dn
  + HP Color LaserJet Managed E65150dn
  + HP Color LaserJet Managed E65160dn
  + HP Color LaserJet Managed MFP E67650dh
  + HP Color LaserJet Managed Flow MFP E67660z

* Thu Feb 07 2019 Andrey Cherepanov <cas@altlinux.org> 1:3.19.1-alt2
- Autodetect auth type for modern ALT distro (ALT #36053).

* Fri Feb 01 2019 Andrey Cherepanov <cas@altlinux.org> 1:3.19.1-alt1
- New version.
- Added support for new printers:
  + HP LaserJet Managed MFP E82540du, E82550du, E82560du;
  + HP Color LaserJet Managed MFP E87640du, E87650du, E87660du.
- Added support for the HP Scanjet Pro 2500 f1.

* Wed Dec 05 2018 Andrey Cherepanov <cas@altlinux.org> 1:3.18.12-alt1
- New version.

* Mon Nov 12 2018 Andrey Cherepanov <cas@altlinux.org> 1:3.18.10-alt1
- New version.

* Fri Nov 02 2018 Andrey Cherepanov <cas@altlinux.org> 1:3.18.9-alt1
- New version (ALT #35531).
- Build with Qt5 (ALT #35571).

* Fri Jul 27 2018 Pavel Akopov <pak@altlinux.ru> 1:3.18.6-alt2
- added translation patch

* Fri Jul 13 2018 Igor Vlasenko <viy@altlinux.ru> 1:3.18.6-alt1
- new version

* Tue Mar 13 2018 Igor Vlasenko <viy@altlinux.ru> 1:3.17.11-alt1
- new version

* Wed Oct 25 2017 Igor Vlasenko <viy@altlinux.ru> 1:3.17.10-alt1
- new version

* Sat Oct 14 2017 Igor Vlasenko <viy@altlinux.ru> 1:3.17.9-alt1
- new version

* Tue Aug 01 2017 Sergey V Turchin <zerg@altlinux.org> 1:3.16.11-alt4
- fix download plugin
- fix fax setup
- fix polkit action placement

* Thu Feb 23 2017 Igor Vlasenko <viy@altlinux.ru> 1:3.16.11-alt3
- added hplip-3.16.11-alt-auth.patch
- disabled noernie patch
- added license for ErnieFilter code

* Wed Feb 22 2017 Igor Vlasenko <viy@altlinux.ru> 1:3.16.11-alt2
- Sisyphus release (closes: #33106)
- PPD* subpackages are now optional as they are deprecated
- cups/filter/foomatic-rip dependency disabled by default
- foomatic-db moved out from requires

* Thu Feb 09 2017 Igor Vlasenko <viy@altlinux.ru> 1:3.16.11-alt1
- new version

* Wed Feb 08 2017 Igor Vlasenko <viy@altlinux.ru> 1:3.16.10-alt2
- 3.16.10 build

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
