Name: xeyes
Version: 1.3.1
Release: alt1

Summary: A "follow the mouse" X demo
License: X11
Group: System/X11

Url: http://xorg.freedesktop.org
Source: %name-%version.tar.gz

# Automatically added by buildreq on Wed Nov 17 2021
# optimized out: glibc-kernheaders-generic glibc-kernheaders-x86 libICE-devel libSM-devel libX11-devel libXext-devel libXfixes-devel libXt-devel libgpg-error libxcb-devel perl pkg-config python3-base sh4 xorg-proto-devel
BuildRequires: libXi-devel libXmu-devel libXrender-devel

BuildRequires: xorg-proto-devel xorg-util-macros

%description
XEyes - a "follow the mouse" X demo, using the X SHAPE extension.

%prep
%setup

%build
%autoreconf
%configure --disable-xprint

%make_build

%install
%make DESTDIR=%buildroot install

%files
%doc *.md
%_bindir/*
%_man1dir/*

%changelog
* Sat Dec 13 2025 Fr. Br. George <george@altlinux.org> 1.3.1-alt1
- Autobuild version bump to 1.3.1

* Thu Apr 18 2024 Fr. Br. George <george@altlinux.org> 1.3.0-alt1
- Autobuild version bump to 1.3.0

* Wed Nov 17 2021 Fr. Br. George <george@altlinux.ru> 1.2.0-alt1
- Autobuild version bump to 1.2.0

* Wed Sep 19 2018 Fr. Br. George <george@altlinux.ru> 1.1.2-alt1
- Autobuild version bump to 1.1.2

* Mon Apr 15 2013 Dmitry V. Levin (QA) <qa_ldv@altlinux.org> 1.1.1-alt1.qa1
- NMU: rebuilt for debuginfo.

* Wed Dec 08 2010 Fr. Br. George <george@altlinux.ru> 1.1.1-alt1
- Autobuild version bump to 1.1.1

* Wed Sep 22 2010 Fr. Br. George <george@altlinux.ru> 1.1.0-alt1
- Autobuild version bump to 1.1.0

* Wed Sep 22 2010 Fr. Br. George <george@altlinux.ru> 1.0.99-alt1
- Initial build from scratch

