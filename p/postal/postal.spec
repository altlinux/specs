Summary: A program for benchmarking mail servers
Name: postal
Version: 0.70
Release: alt6
License: GPLv3
Group: System/Servers
Packager: Denis Smirnov <mithraen@altlinux.ru>

Source: http://www.coker.com.au/%name/%name-%version.tar
Patch: %name-%version-%release.patch
Url: http://doc.coker.com.au/projects/postal/

# Automatically added by buildreq on Sat Mar 12 2011
BuildRequires: gcc-c++ libgcrypt-devel libgnutls-devel

%description
The Postal suite consists of an SMTP delivery benchmark (postal), a POP
retrieval benchmark (rabid) and other programs soon to be added.

%prep
%setup -q
%patch -p1

%build
./configure --prefix=%buildroot
%make_build

%install
%makeinstall_std eprefix=/usr prefix=/usr
mkdir -p %buildroot%_docdir/%name
install -m 644 debian/changelog %buildroot%_docdir/%name/ChangeLog

mkdir -p %buildroot%_man8dir

%files
%_sbindir/postal
%_sbindir/bhm
%_sbindir/rabid
%_bindir/postal-list
%_man8dir/*
%_man1dir/*
%_docdir/%name

%changelog
* Mon Jun 18 2012 Denis Smirnov <mithraen@altlinux.ru> 0.70-alt6
- fix build

* Sat Mar 12 2011 Denis Smirnov <mithraen@altlinux.ru> 0.70-alt5
- fix build

* Mon Oct 04 2010 Denis Smirnov <mithraen@altlinux.ru> 0.70-alt4
- build with gnutls

* Mon Oct 04 2010 Denis Smirnov <mithraen@altlinux.ru> 0.70-alt3
- add Url tag

* Mon Oct 04 2010 Denis Smirnov <mithraen@altlinux.ru> 0.70-alt2
- fix build with new openssl

* Fri Nov 14 2008 Denis Smirnov <mithraen@altlinux.ru> 0.70-alt1
- update to 0.70

* Tue Aug 16 2005 Denis Smirnov <mithraen@altlinux.ru> 0.62-alt1
- first build for Sisyphus

