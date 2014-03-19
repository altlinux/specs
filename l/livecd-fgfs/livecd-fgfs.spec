Name: livecd-fgfs
Version: 0.1
Release: alt1

Summary: start FlightGear
License: Public domain
Group: System/X11

Url: http://altlinux.org/m-p
Packager: Michael Shigorin <mike@altlinux.org>
BuildArch: noarch

Requires: xinit

%define skeldir %_sysconfdir/skel
%define xsfile %skeldir/.xsession

%description
%summary

%prep

%build

%install
mkdir -p %buildroot%skeldir

cat > %buildroot%xsfile << _EOF_
#!/bin/sh

FGFS="fgfs --enable-fullscreen"
[ -d /usr/share/flightgear/Aircraft/tu154b ] && FGFS="\$FGFS --aircraft=tu154b"

EXPENSIVE="--enable-enhanced-lighting --enable-clouds3d"
EXPENSIVE="\$EXPENSIVE --enable-horizon-effect --enable-specular-highlight"
EXPENSIVE="\$EXPENSIVE --enable-distance-attenuation --fog-nicest"

PRIMUSRUN=/usr/bin/primusrun
\$PRIMUSRUN \$FGFS \$EXPENSIVE || \$FGFS
_EOF_
chmod +x %buildroot%xsfile

%files
%xsfile

%changelog
* Thu Mar 20 2014 Michael Shigorin <mike@altlinux.org> 0.1-alt1
- initial release

