%define binname zelax-pflash

Name: zelax-pflash
Version: 1.0.11
Release: alt2
Packager: Sergey Y. Afonin <asy@altlinux.ru>

Summary: Utility for flash programming for Zelax modems.

License: GPL
Group: Communications
Url: http://www.zelax.ru/support/soft/pflash
Source0: %name-%version.tar.gz
Source1: %name.README.alt
Source2: %name.README.alt.koi8-r

Patch0: %name-Makefile.am.altlinux.diff
Patch1: %name-pflash.c.progname.patch

# Automatically added by buildreq on Thu Jun 02 2005
BuildRequires: gcc-c++ libreadline-devel libtinfo-devel

%description
Utility for flash programming for Zelax modems. Supported models: M-144, M-144A,
M-1, M-30, M-30A and other. See full list on http://www.zelax.ru

%prep

%setup -q

%patch0 -p0
%patch1 -p0

%__sed -e 's|@@NAME@@|%binname|g' < %SOURCE1 > README.alt
%__sed -e 's|@@NAME@@|%binname|g' < %SOURCE2 > README.alt.koi8-r

aclocal
autoconf
automake

libtoolize -i

%configure

%build

%make_build

%install

#install bin

%__install -d -m 0750 %buildroot%_bindir
%__install -m 755 pflash %buildroot%_bindir/%binname

%post

%postun

%files
%_bindir/*
%doc README.alt README.alt.koi8-r NEWS AUTHORS

%changelog
* Tue Sep 29 2009 Sergey Y. Afonin <asy@altlinux.ru> 1.0.11-alt2
- Fixed in spec:
  Added "libtoolize -i" for building with libtool_2.2.
- Removed Russian descriptions.
- Fixed English descriptions.

* Wed Sep 03 2008 Sergey Y. Afonin <asy@altlinux.ru> 1.0.11-alt1.2
- Rebuilt for fixing repocop's warning:
  package is too old, rpmsign failed sisyphus_check.

* Sun Dec 30 2005 ALT QA Team Robot <qa-robot at altlinux.org> 1.0.11-alt1.1
- Rebuilt with libreadline.so.5.

* Wed Jun 01 2005 Sergey Y. Afonin <asy@altlinux.ru> 1.0.11-alt1
- Initial build for AltLinux
