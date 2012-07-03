Name: screen-message
Version: 0.6
Release: alt1

Summary: Screen message show given text in fullscreen
License: %gpl2plus
Group: System/X11
Packager: Evgenii Terechkov <evg@altlinux.ru>
Source: %name-%version.tar.gz

BuildPreReq: rpm-build-licenses
AutoReq: yes, nopython

# Automatically added by buildreq on Thu Nov 08 2007
BuildRequires: libgtk+2-devel

%description
Screen message show given text in fullscreen

Recommends: python-module-pygtk (needed by sm.py)

%prep
%setup

%build
%configure
make

%install
make install DESTDIR=%buildroot
install -m 755 sm.py %buildroot%_bindir

%files
%_bindir/*
%_man1dir/*

%changelog
* Tue Feb 19 2008 Terechkov Evgenii <evg@altlinux.ru> 0.6-alt1
- Rebuild with new sisyphus_check
- Url tag removed (was dummy anyway)

* Thu Aug  2 2007 Terechkov Evgenii <evg@altlinux.ru> 0.6-alt0
- Initial build for Sisyphus
