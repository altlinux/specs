Name: livecd-fgfs
Version: 0.2
Release: alt2

Summary: start FlightGear
License: Public domain
Group: System/X11

Url: http://altlinux.org/m-p
Packager: Michael Shigorin <mike@altlinux.org>
BuildArch: noarch

Requires: livecd-runapp SysVinit-usermode

%define confdir %_sysconfdir/sysconfig
%define conffile %confdir/livecd-runapp

%description
%summary

%prep

%build

%install
mkdir -p %buildroot%confdir

cat > %buildroot%conffile << _EOF_
BINARY=fgfs
COMMON_ARGS="--enable-fullscreen --time-match-local"

[ -d /usr/share/flightgear/Aircraft/tu154b ] &&
	COMMON_ARGS="\$COMMON_ARGS --aircraft=tu154b --airport=UNKM" ||:

EXPENSIVE_ARGS="--enable-enhanced-lighting --enable-clouds3d --enable-horizon-effect --enable-specular-highlight --enable-distance-attenuation --fog-nicest"
_EOF_

%files
%conffile

%changelog
* Mon Mar 30 2015 Michael Shigorin <mike@altlinux.org> 0.2-alt2
- set local time

* Tue Mar 17 2015 Michael Shigorin <mike@altlinux.org> 0.2-alt1
- rewrote using livecd-runapp

* Wed Oct 22 2014 Michael Shigorin <mike@altlinux.org> 0.1-alt3
- set UNKM for tu154

* Sun Mar 23 2014 Michael Shigorin <mike@altlinux.org> 0.1-alt2
- added Conflicts: indeed

* Thu Mar 20 2014 Michael Shigorin <mike@altlinux.org> 0.1-alt1
- initial release

