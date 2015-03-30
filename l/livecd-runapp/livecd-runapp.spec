Name: livecd-runapp
Version: 0.2
Release: alt1

Summary: start an (OpenGL) X11 application in kiosk mode
License: Public domain
Group: System/X11

Url: http://altlinux.org/m-p
Packager: Michael Shigorin <mike@altlinux.org>
BuildArch: noarch

Requires: xinit
Conflicts: livecd-webkiosk

%define confdir %_sysconfdir/sysconfig
%define conffile %confdir/%name
%define skeldir %_sysconfdir/skel
%define xsfile %skeldir/.xsession

%description
%summary
(the particular app is specified via %conffile).

NVIDIA Optimus might be supported through primusrun
(requires primus package installed within LiveCD),
and additional arguments can be specified in that case
to tweak the application's performance estimation.

%prep

%build

%install
mkdir -p %buildroot{%skeldir,%confdir}

touch %buildroot%conffile

cat > %buildroot%xsfile << _EOF_
#!/bin/sh

export DRI_PRIME=1

[ -s %conffile ] && . %conffile || exit 1

PRIMUSRUN=/usr/bin/primusrun
\$PRIMUSRUN \$BINARY \$COMMON_ARGS \$EXPENSIVE_ARGS || \$BINARY \$COMMON_ARGS

POWEROFF=/usr/bin/poweroff
[ -x \$POWEROFF ] && \$POWEROFF ||:
_EOF_
chmod +x %buildroot%xsfile

%files
%ghost %conffile
%xsfile

%changelog
* Mon Mar 30 2015 Michael Shigorin <mike@altlinux.org> 0.2-alt1
- set DRI_PRIME by default (thanks Sluggard at opennet for the hint)

* Tue Mar 17 2015 Michael Shigorin <mike@altlinux.org> 0.1-alt1
- initial release (based on livecd-fgfs 0.1-alt3)

