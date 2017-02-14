# SPEC file for squidview package

Name:    squidview
Version: 0.86
Release: alt1

Summary: console program to monitor and display Squid logs

License: %gpl2plus
Group:   Monitoring
URL:     http://www.rillion.net/squidview/index.html

Packager: Nikolay A. Fetisov <naf@altlinux.ru>

Source0: %name-%version.tar

BuildRequires(pre): rpm-build-licenses


# Automatically added by buildreq on Wed Jun 15 2011
# optimized out: libstdc++-devel libtinfo-devel
BuildRequires: gcc-c++ libncurses-devel

%description
Squidview is an interactive console program which monitors and
displays Squid logs in a nice fashion,  and may then go deeper
with searching and reporting functions.

To use squidview you must at least have read access to Squid's
access.log file. Squidview uses this text log file for all
operations. It does not generate its own database for tasks.

%prep
%setup

mv -f -- COPYING COPYING.orig
ln -s -- $(relative %_licensedir/GPL-2 %_docdir/%name/COPYING) COPYING

%build
%autoreconf
%configure
%make_build

%install
%make_install DESTDIR=%buildroot install

%files
%doc ChangeLog README
%doc --no-dereference COPYING

%_bindir/%name
%_man1dir/%{name}*
%_datadir/%name

%changelog
* Tue Feb 14 2017 Nikolay A. Fetisov <naf@altlinux.org> 0.86-alt1
- New version

* Sun Jan 29 2017 Nikolay A. Fetisov <naf@altlinux.org> 0.85-alt1
- New version

* Sat Jan 21 2017 Nikolay A. Fetisov <naf@altlinux.org> 0.84-alt1
- New version

* Sun Jun 12 2016 Nikolay A. Fetisov <naf@altlinux.ru> 0.83-alt1
- New version

* Sat May 30 2015 Nikolay A. Fetisov <naf@altlinux.ru> 0.81-alt1
- New version

* Sun Dec 01 2013 Nikolay A. Fetisov <naf@altlinux.ru> 0.80-alt1
- New version

* Tue Jun 21 2011 Nikolay A. Fetisov <naf@altlinux.ru> 0.79-alt1
- Initial build for ALT Linux Sisyphus
