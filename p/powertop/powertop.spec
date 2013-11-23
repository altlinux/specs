Name: powertop
Version: 2.5
Release: alt1

Summary: Tool that helps you find what software is using the most power
License: GPLv2 only
Group: System/Kernel and hardware

Url: https://01.org/powertop/
Source0: https://01.org/powertop/sites/default/files/downloads/%name-%version.tar.gz
Source100: %name.watch

# Automatically added by buildreq on Tue May 15 2012
# optimized out: libncurses-devel libstdc++-devel libtinfo-devel pkg-config xz
BuildRequires: gcc-c++ libncursesw-devel libnl-devel libpci-devel zlib-devel

%description
PowerTOP is a Linux tool that finds the software component(s) that make
your laptop use more power than necessary while it is idle.

PowerTOP works best on a laptop computer, or at least a computer with an
Intel mobile processor (certain small non-laptop devices also contain a
mobile processor). When using PowerTOP on a laptop, do so when running
on battery.

Please note that it also runs just fine with e.g. AMD CPUs. :)

%prep
%setup

%build
%autoreconf
%configure
%make_build

%install
%makeinstall_std
%find_lang %name
install -d %buildroot%_cachedir/%name

%files -f %name.lang
%_sbindir/*
%_man8dir/*
%doc README
%dir %_cachedir/%name

%changelog
* Sat Nov 23 2013 Michael Shigorin <mike@altlinux.org> 2.5-alt1
- new version (watch file uupdate)

* Mon Jul 22 2013 Michael Shigorin <mike@altlinux.org> 2.4-alt1
- new version (watch file uupdate)

* Mon Apr 08 2013 Michael Shigorin <mike@altlinux.org> 2.3-alt1
- new version (watch file uupdate)

* Mon Apr 08 2013 Michael Shigorin <mike@altlinux.org> 2.1-alt2
- added watch file (thanks debian with its #695891)

* Mon Sep 03 2012 Michael Shigorin <mike@altlinux.org> 2.1-alt1
- 2.1

* Wed May 16 2012 Michael Shigorin <mike@altlinux.org> 2.0-alt2
- re-added %_cachedir/%name created by hand
- NB: Url: has changed

* Tue May 15 2012 Michael Shigorin <mike@altlinux.org> 2.0-alt1
- 2.0
  + autoconf based build
  + binary moved from %_bindir to %_sbindir
- added a tiny explanatory note to package description :)

* Sat Aug 20 2011 Victor Forsiuk <force@altlinux.org> 1.98-alt1
- 1.98

* Wed Aug 04 2010 Victor Forsiuk <force@altlinux.org> 1.13-alt1
- 1.13

* Fri Jan 15 2010 Victor Forsyuk <force@altlinux.org> 1.11-alt2
- Increase config lines buffer size. Closes ALT #22750.

* Thu Jun 18 2009 Victor Forsyuk <force@altlinux.org> 1.11-alt1
- 1.11

* Tue Jun 17 2008 Victor Forsyuk <force@altlinux.org> 1.10-alt1
- 1.10

* Thu Dec 27 2007 Victor Forsyuk <force@altlinux.org> 1.9-alt1
- 1.9

* Thu Aug 30 2007 Victor Forsyuk <force@altlinux.org> 1.8-alt1
- 1.8

* Mon Jul 09 2007 Victor Forsyuk <force@altlinux.org> 1.7-alt1
- 1.7

* Tue May 29 2007 Victor Forsyuk <force@altlinux.org> 1.5-alt1
- 1.5

* Wed May 16 2007 Victor Forsyuk <force@altlinux.org> 1.2-alt1
- 1.2

* Mon May 14 2007 Victor Forsyuk <force@altlinux.org> 1.1-alt1
- Initial build.
