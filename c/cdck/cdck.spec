Name: cdck
Version: 0.7.0
Release: alt1.1

Summary: CD/DVD check tools

Group: File tools
License: GPL
Url: http://swaj.net/unix/index.html#cdck

Packager: Vitaly Lipatov <lav@altlinux.ru>

Source: http://swaj.net/unix/cdck/%name-%version.tar.bz2

BuildRequires: gcc-c++ glibc-devel
BuildRequires: perl-podlators

%description
Actually cdck is a simple program to verify CD/DVD quality. The known
fact is that even if all files on the disc are readable, some sectors
having bad timing can easily turn into unreadable ones in the future.

To get an idea about disc cdck reads it sector by sector, keeping all
reading timings and then tells you its verdict. Optionally it can write
timing table into text file usable by gnuplot(1) program, so you can draw
some graphs out of it.

%prep
%setup -q
%__subst "s|/bin/env|%_bindir/env|g" src/template*

%build
%configure
# SMP incompatible
%make

%install
%makeinstall_std
rm -f %buildroot%_libdir/libcdck.a

%files
%doc README ChangeLog NEWS THANKS AUTHORS
%doc src/template*
%_bindir/%name
%_man1dir/*

%changelog
* Wed Nov 24 2010 Igor Vlasenko <viy@altlinux.ru> 0.7.0-alt1.1
- repair after perl 5.12 upgrade using girar-nmu

* Thu Jan 14 2010 Vitaly Lipatov <lav@altlinux.ru> 0.7.0-alt1
- new version (0.7.0) 

* Thu May 03 2007 Vitaly Lipatov <lav@altlinux.ru> 0.6.0-alt1
- new version 0.6.0 (with rpmrb script)

* Sun Jun 18 2006 Vitaly Lipatov <lav@altlinux.ru> 0.5.2-alt0.1
- new version 0.5.2 (with rpmrb script)
- add template

* Sun Apr 02 2006 Vitaly Lipatov <lav@altlinux.ru> 0.5.1-alt0.1
- initial build for ALT Linux Sisyphus
