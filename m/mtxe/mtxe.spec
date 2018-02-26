Name: mtxe
Version: 1.0.2
Release: alt1

License: GPL
Url: http://koti.mbnet.fi/midiania/hack
Packager: Pavlov Konstantin <thresh@altlinux.ru>
Summary: Yet another matrix engine.
Group: Toys
Source: %name-%version.tar.bz2
Patch1: mtxe-0.99.2-lncurses.patch

# Automatically added by buildreq on Mon Mar 14 2005
BuildRequires: libfrag-opt-devel hostinfo libncurses-devel libtinfo-devel

%description
Yet another matrix engine.

%prep
%setup -q -n %name-%version

%patch1 -p1

%build
%configure

%make_build

%install

%make_install DESTDIR="%buildroot" install

%files
%_bindir/%name
%_man1dir/*

%changelog
* Fri Jan 05 2007 Pavlov Konstantin <thresh@altlinux.ru> 1.0.2-alt1
- 1.0.2 release. 

* Tue Mar 07 2006 Pavlov Konstantin <thresh@altlinux.ru> 0.99.2-alt3
- Fixed build with --as-needed.

* Fri Oct 07 2005 Pavlov Konstantin <thresh@altlinux.ru> 0.99.2-alt2
- Fixed BuildRequires.

* Sat Jun 11 2005 Pavlov Konstantin <thresh@altlinux.ru> 0.99.2-alt1
- 0.99.2 release.

* Mon Apr 04 2005 Pavlov Konstantin <thresh@altlinux.ru> 0.99.1-alt1
- 0.99.1 release. Initial build for ALT Sisyphus.

