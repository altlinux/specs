Name: tcputils
Version: 0.6.2
Release: alt1

Summary: Utilities for TCP programming in shell-scripts

License: Public Domain
Group: Development/Tools
Url: ftp://ftp.lysator.liu.se/pub/unix/tcputils

Packager: Vitaly Lipatov <lav@altlinux.ru>

Source: ftp://ftp.lysator.liu.se/pub/unix/%name/%name-%version.tar

Patch: tcputils-0.6.2-makefile.patch

%description
This is a collection of programs to facilitate TCP programming in
shell-scripts. There is also a small library which makes it somewhat
easier to create TCP/IP sockets.

%prep
%setup
%patch0 -p1 -b .orig

%build
%make_build

%install
%makeinstall_std
chmod 0644 %buildroot%_man1dir/*

%files
%doc README
%_bindir/getpeername
%_bindir/mini-inetd
%_bindir/tcpbug
%_bindir/tcpconnect
%_bindir/tcplisten
%_man1dir/getpeername.1.*
%_man1dir/mini-inetd.1.*
%_man1dir/tcpbug.1.*
%_man1dir/tcpconnect.1.*
%_man1dir/tcplisten.1.*

%changelog
* Sun Dec 30 2012 Vitaly Lipatov <lav@altlinux.ru> 0.6.2-alt1
- initial build for ALT Linux Sisyphus

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.2-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Apr 13 2012 Jon Ciesla <limburgher@gmail.com> - 0.6.2-9
- Add hardened build.

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.2-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild


* Sat Sep  6 2008 Allisson Azevedo <allisson@gmail.com> 0.6.2-4
- Rebuild for F-10

* Mon Feb 18 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 0.6.2-3
- Autorebuild for GCC 4.3

* Fri Oct 19 2007 Allisson Azevedo <allisson@gmail.com> 0.6.2-2
- Keep timestamps on man files

* Fri Oct 19 2007 Allisson Azevedo <allisson@gmail.com> 0.6.2-1
- Initial RPM release
