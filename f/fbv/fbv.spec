Name: fbv
Version: 1.0b
Release: alt2

Summary: Framebuffer image viewer
License: GPLv2+
Group: Graphics

URL: http://s-tech.elsat.net.pl/fbv
Source0: %url/%name-%version.tar.gz
Patch1: fbv-nocenter.patch
Patch2: fbv-1.0b-features.h.patch

# Automatically added by buildreq on Fri Mar 28 2008
BuildRequires: libjpeg-devel libpng-devel libungif-devel

%description
A simple program to view pictures on a framebuffer console. It supports PNG,
JPEG, GIF and BMP files.

%prep
%setup
%patch1 -p1
%patch2 -p1

%build

./configure --prefix=/usr --mandir=%_mandir

%make_build CC="gcc %optflags"

%install
mkdir -p %buildroot{%_bindir,%_man1dir}
%makeinstall

%files
%_bindir/*
%_man1dir/*
%doc ChangeLog README TODO

%changelog
* Fri Mar 28 2008 Victor Forsyuk <force@altlinux.org> 1.0b-alt2
- Fix FTBFS due to new glibc-kernheaders.

* Wed Mar 30 2005 Victor Forsyuk <force@altlinux.ru> 1.0b-alt1
- Add URL.
- Apply patch to add nocentering option.

* Wed Oct 23 2002 Konstantin Volckov <goldhead@altlinux.ru> 0.96-alt1
- 0.96

* Thu Oct 11 2001 Konstantin Volckov <goldhead@altlinux.ru> 0.95-alt2
- Rebuilt with libpng.so.3

* Mon Sep 17 2001 Konstantin Volckov <goldhead@altlinux.ru> 0.95-alt1
- First build for Sisyphus
