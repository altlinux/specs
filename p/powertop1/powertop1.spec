%define origname powertop

Name: powertop1
Version: 1.13
Release: alt3.1

Summary: Tool that helps you find what software is using the most power
License: GPLv2 only
Group: System/Kernel and hardware

Url: http://www.lesswatts.org/projects/powertop
Source: %url/download/powertop-%version.tar.gz
Patch: powertop-1.13-kconfig.patch
Packager: Michael Shigorin <mike@altlinux.org>

# Automatically added by buildreq on Wed Aug 04 2010
BuildRequires: libncursesw-devel

%description
PowerTOP is a Linux tool that finds the software component(s) that
make your laptop use more power than necessary while it is idle.

PowerTOP works best on a laptop computer, or at least a computer
with a mobile processor (certain small non-laptop devices also
contain a mobile processor). When using PowerTOP on a laptop,
do so when running on battery.

Please note that it also runs just fine with e.g. AMD CPUs. :)

%prep
%setup -n %origname-%version
%patch -p1

%build
%make_build CC="gcc %optflags"

%install
%makeinstall_std
#find_lang %origname

%files
%doc Changelog README
%_bindir/*
#_man8dir/*

%changelog
* Wed May 16 2012 Michael Shigorin <mike@altlinux.org> 1.13-alt3.1
- dropped Conflicts: powertop (along with colliding translations
  and a manpage which becomes ambiguous and plain wrong for 2.x)
- added a tiny explanatory note to package description, too

* Thu May 03 2012 Michael Shigorin <mike@altlinux.org> 1.13-alt3
- added a patch to fix CONFIG_INOTIFY* detection/advice:
  http://bughost.org/pipermail/power/2010-September/001987.html

* Wed Dec 21 2011 Michael Shigorin <mike@altlinux.org> 1.13-alt2
- rebuilt as powertop1 conflicting with powertop
  since powertop 2.x UI is inferior to me so far
  even if its capabilities are remarkably higher

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
