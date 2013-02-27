Name: livecd-regular-xmonad
Version: 0.0.1
Release: alt1

Summary: Simple xmonad-based livecd enviromnet
License: Public domain
Group: System/X11

Url: http://altlinux.org/m-p
BuildArch: noarch

%define skeldir %_sysconfdir/skel
%define xsdir %skeldir/.xsession.d

Requires: pcmanfm2

%description
%summary

%prep
%build
%install
mkdir -p %buildroot%xsdir

cat > %buildroot%xsdir/pcmanfm2 << _EOF_
#!/bin/sh
pcmanfm2 --desktop &
_EOF_

chmod +x %buildroot%xsdir/pcmanfm2

%files
%xsdir/*

%changelog
* Wed Feb 27 2013 Denis Smirnov <mithraen@altlinux.ru> 0.0.1-alt1
- first build for Sisyphus
