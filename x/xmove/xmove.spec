%define beta	2

Name: xmove
Version: 2.0
Release: alt1
Summary: X11 pseudoserver to dynamically move X11 applications
%if %beta
Source0: ftp://ftp.cs.columbia.edu/pub/xmove/%name.%{version}beta%beta.tar.bz2
%else
Source0: ftp://ftp.cs.columbia.edu/pub/xmove/%name.%version.tar.bz2
%endif
License: MIT
Group: System/X11
Packager: Fr. Br. George <george@altlinux.ru>
Url: ftp://ftp.cs.columbia.edu/pub/xmove/
Patch0: xmove-2.0-unix-domain.patch.bz2

# Automatically added by buildreq on Wed Aug 29 2007
BuildRequires: imake libX11-devel xorg-cf-files

%description
xmove is a pseudoserver (aka proxy server) which allows you
to dynamically move an X application between servers, and screens
within a server.

%prep
%setup -q -n %name
%patch0 -p1 -b .unix-domain
chmod 644 doc/*

%build
for i in xmove xmovectrl; do
	cd $i
	ln -sf ../man/man1/$i.1 $i.man
	xmkmf
	%make
	cd $OLDPWD
done

%install
install -d -m755 %buildroot%_man1dir/
for i in xmove xmovectrl; do
	cd $i
	%makeinstall DESTDIR=%buildroot
	cd $OLDPWD
	install -m 644 man/man1/$i.1 %buildroot%_man1dir/
done

%clean
rm -rf %buildroot

%files
%doc README doc/*
%_bindir/xmove*
%_man1dir/xmove*

%changelog
* Wed Aug 29 2007 Fr. Br. George <george@altlinux.ru> 2.0-alt1
- Initial build for ALT

* Sat Sep 03 2005 Marcel Pol <mpol@mandriva.org> 2.0-0.beta2.2mdk
- buildrequires x11

* Thu Aug  4 2005 Olivier Blin <oblin@mandriva.com> 2.0-0.beta2.1mdk
- initial Mandriva release
- Patch0: Unix domain sockets support (from Debian)
