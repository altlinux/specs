%define dnh dnh
Name: ctorrent
Version: 3.3.2
Release: alt1.1
Summary: BitTorrent Client written in C
Group: Networking/File transfer
License: GPL
Packager: Pavlov Konstantin <thresh at altlinux.ru>
Url: http://www.rahul.net/dholmes/ctorrent/
Source0: http://www.rahul.net/dholmes/ctorrent/%name-%dnh%version.tar.gz

Patch0: %name-%dnh%version-security-fix.patch

# Automatically added by buildreq on Sat Jan 31 2009 (-bi)
BuildRequires: gcc-c++ libssl-devel

%description
CTorrent is a BitTorrent Client written in C that
doesn't require any graphical component, such as an X server.

%prep
%setup -q -n %name-%dnh%version
%patch0 -p0

%build
%configure

%make

%install
%make_install DESTDIR=%buildroot install

%files
%doc AUTHORS COPYING ChangeLog NEWS README README-DNH.TXT UserGuide
%_bindir/ctorrent

%changelog
* Wed Dec 08 2010 Igor Vlasenko <viy@altlinux.ru> 3.3.2-alt1.1
- rebuild with new openssl and/or boost by request of git.alt administrator

* Thu May 21 2009 Andrew Clark <andyc@altlinux.ru> 3.3.2-alt1
- dnh 3.3.2 update
- Fix #20131.

* Sat Aug 09 2008 ALT QA Team Robot <qa-robot@altlinux.org> 1.3.4-alt2.dnh3.2.1
- Automated rebuild due to libcrypto.so.6 -> libcrypto.so.7 soname change.

* Mon Jan 28 2008 Pavlov Konstantin <thresh@altlinux.ru> 1.3.4-alt2.dnh3.2
- Fix #13930.

* Wed Aug 22 2007 Pavlov Konstantin <thresh@altlinux.ru> 1.3.4-alt1.dnh3.2
- dnh3.2 update.

* Wed Jun 27 2007 Pavlov Konstantin <thresh@altlinux.ru> 1.3.4-alt1.dnh3.1
- dnh3.1 update.

* Tue May 29 2007 Pavlov Konstantin <thresh@altlinux.ru> 1.3.4-alt1.dnh3
- Initial build for ALT.

* Wed Nov 01 2006 Dominik 'Rathann' Mierzejewski <rpm@greysector.net> 1.3.4-3.dnh2.1
- upstream has stopped development, rebase to Enhanced CTorrent, fixes #212307
- add more docs

* Tue Oct 03 2006 Dominik 'Rathann' Mierzejewski <rpm@greysector.net> 1.3.4-2
- rebuilt for unwind info generation, broken in gcc-4.1.1-21

* Thu Sep 21 2006 Dominik 'Rathann' Mierzejewski <rpm@greysector.net> 1.3.4-1
- update to 1.3.4
- mass rebuild

* Wed May 24 2006 Andrea Veri <bluekuja@ubuntu.com> 1.3.2-3
 - Added openssl-devel to BR
 - Removed libc.so.6 libc.so.6(GLIBC_2.0), libc.so.6(GLIBC_2.1) in BR
 - Description Changed
 - Fixed URL

* Sun Feb 1 2004 YuHong <bsdi@sina.com> 1.3.2
 - First Release
