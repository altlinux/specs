Name: xsecurelock
Version: 0.0.1
Release: alt1
URL: https://github.com/google/xsecurelock

Summary: X11 screen lock utility
License: Apache
Group: System/X11

Source: %name-%version.tar
Source1: %name.pam

# Automatically added by buildreq on Fri Aug 01 2014
# optimized out: libX11-devel xorg-scrnsaverproto-devel xorg-xf86miscproto-devel xorg-xproto-devel
BuildRequires: doxygen libXScrnSaver-devel libXxf86misc-devel libpam-devel

%description
XSecureLock is an X11 screen lock utility designed with the primary goal of
security.

Security is achieved using a modular design to avoid the usual pitfalls of
screen locking utility design.

%prep
%setup

%build
%autoreconf
%configure \
     --with-pam-service-name=%name

%make_build

%install
install -pm0644 -D %{S:1} %buildroot%_sysconfdir/pam.d/%name
%makeinstall


%files
%_bindir/%name
%_sysconfdir/pam.d/%name    
%dir %_libexecdir/%name

%_libexecdir/%name/auth_htpasswd
%_libexecdir/%name/auth_pamtester
%attr(2711,root,chkpwd) %_libexecdir/%name/auth_pam_x11
%_libexecdir/%name/saver_blank
%_libexecdir/%name/saver_mplayer
%_libexecdir/%name/saver_mpv
%_libexecdir/%name/saver_xscreensaver

%exclude /usr/share/doc/xsecurelock/
%doc README.md LICENSE CONTRIBUTING

%changelog
* Fri Aug 01 2014 Denis Smirnov <mithraen@altlinux.ru> 0.0.1-alt1
- first build for Sisyphus
