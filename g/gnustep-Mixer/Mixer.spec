%set_verify_elf_method unresolved=strict

Name: gnustep-Mixer
Version: 1.8.0
Release: alt1
Summary: Mixer application designed for WindowMaker
License: GPLv2
Group: Graphical desktop/GNUstep
Url: http://packages.debian.org/ru/squeeze/gnustep/mixer.app
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar

BuildPreReq: gcc-objc gnustep-make-devel libgnustep-objc2-devel /proc
BuildPreReq: gnustep-gui-devel gcc-c++
BuildPreReq: libgmp-devel libgnutls-devel libgcrypt-devel
BuildPreReq: libxslt-devel libffi-devel libicu-devel zlib-devel
BuildPreReq: libX11-devel libXpm-devel libXext-devel

Requires: gnustep-back

%description
There's nothing in the program that makes it *require* WindowMaker,
except maybe the look. Mixer.app is a mixer utility for Linux systems.
Requires /dev/mixer to work. Provides three customizable controls on a
tiny 64x64 app.

For work this application You need run `/sbin/modprobe snd-pcm-oss'.

%prep
%setup

%build
%make_build \
	messages=yes \
	debug=yes \
	strip=no \
	shared=yes \
	AUXILIARY_CPPFLAGS='-O2 -DGNUSTEP' \
	GNUSTEP_MAKEFILES=%_datadir/GNUstep/Makefiles
 
%install
%makeinstall_std GNUSTEP_INSTALLATION_DOMAIN=SYSTEM \
	GNUSTEP_MAKEFILES=%_datadir/GNUstep/Makefiles

%files
%doc ChangeLog README
%_bindir/*

%changelog
* Thu Jan 30 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.8.0-alt1
- Initial build for Sisyphus

