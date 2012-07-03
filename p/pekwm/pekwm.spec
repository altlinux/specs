Name: pekwm
Version: 0.1.13
Release: alt2.git.c78330ee
Summary: Fast & lightweight window manager
License: GPLv2
Group: Graphical desktop/Other
Url: http://pekwm.org
Packager: Egor Glukhov <kaman@altlinux.org>
Source0: %name-%version.tar
Source1: %name.wmsession

BuildRequires: gcc-c++ imake libSM-devel libXft-devel libXinerama-devel
BuildRequires: libXpm-devel libXrandr-devel libjpeg-devel libpng-devel
BuildRequires: xorg-cf-files libXext-devel libICE-devel

%description
pekwm is a window manager that once up on a time was based on the aewm++
window manager, but it has evolved enough that it no longer resembles
aewm++ at all. It has a much expanded feature-set, including window
grouping (similar to ion, pwm, or fluxbox), autoproperties, xinerama,
keygrabber that supports keychains, and much more.

%prep
%setup

%build
%autoreconf
%configure
%make_build

%install
%makeinstall_std
mkdir -p %buildroot/%_sysconfdir/X11/wmsession.d
install -pD -m644 %SOURCE1 %buildroot/%_sysconfdir/X11/wmsession.d/08%name

%files
%doc README
%_bindir/*
%_sysconfdir/%name
%_sysconfdir/X11/wmsession.d/*
%_datadir/%name
%_man1dir/%name.1.gz

%changelog
* Mon May 30 2011 Egor Glukhov <kaman@altlinux.org> 0.1.13-alt2.git.c78330ee
- XShape support (Closes: #25689)

* Sun Mar 06 2011 Egor Glukhov <kaman@altlinux.org> 0.1.13-alt1.git.c78330ee
- Initial build for Sisyphus
