%set_verify_elf_method unresolved=strict

Name: gnustep-icons
Version: 1.0
Release: alt1
Summary: Several free icons for use with GNUstep and others
License: LGPLv2.1+
Group: Graphical desktop/GNUstep
Url: http://packages.debian.org/ru/jessie/gnustep-icons
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: gcc-objc gnustep-make-devel libgnustep-objc2-devel /proc
BuildPreReq: gnustep-gui-devel
BuildPreReq: libgmp-devel libgnutls-devel libgcrypt-devel
BuildPreReq: libxslt-devel libffi-devel libicu-devel zlib-devel

%description
They all have a basic NeXTSTEPish look and feel. These icons are placed
where the WindowMaker package expects them by default.

%prep
%setup

%install
install -d %buildroot%_datadir/icons
install -m644 icons/*.tiff %buildroot%_datadir/icons/

%files
%doc README.TXT
%_datadir/icons/*

%changelog
* Sat Jan 25 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0-alt1
- Initial build for Sisyphus

