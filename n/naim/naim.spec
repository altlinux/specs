Name: naim
Version: 0.11.8.3.2
Release: alt2

Summary: An ncurses-based console AIM, ICQ, IRC, and Lily client
Group: Networking/Instant messaging
License: GPLv2
URL: http://naim.n.ml.org
Source0: http://naim.googlecode.com/files/%name-%version.tar.bz2

Patch0: naim-0.11.8.3.2-alt-build.patch

Packager: Igor Zubkov <icesik@altlinux.org>

# Automatically added by buildreq on Wed Oct 21 2009
BuildRequires: gcc-c++ libncurses-devel

%description
naim is a console client for AOL Instant Messenger (AIM), AOL I Seek You (ICQ),
Internet Relay Chat (IRC), and The lily CMC.

%prep
%setup -q
%patch0 -p1

%build
%configure
%make_build

%install
%make_install DESTDIR=%buildroot install
rm -fr %buildroot/usr/share/doc/naim
rm -fr %buildroot/%_includedir

%files
%doc AUTHORS FAQ BUGS README NEWS ChangeLog doc/*.hlp
%_bindir/*
%_man1dir/*

%changelog
* Wed Oct 21 2009 Igor Zubkov <icesik@altlinux.org> 0.11.8.3.2-alt2
- Don't create group 'naim author' (closes: #16454)

* Sat Oct 17 2009 Igor Zubkov <icesik@altlinux.org> 0.11.8.3.2-alt1
- 0.11.8.3.1 -> 0.11.8.3.2

* Sun Aug 12 2007 Igor Zubkov <icesik@altlinux.org> 0.11.8.3.1-alt1
- build for Sisyphus

* Sun Sep  3 2006 Luke Macken <lmacken@redhat.com> 0.11.8.3-1
- 0.11.8.3-2007-09-02-1530 development snapshot

* Wed May 10 2006 Luke Macken <lmacken@redhat.com> 0.11.8.2-4
- 0.11.8.2 final

* Thu Mar 16 2006 Luke Macken <lmacken@redhat.com> 0.11.8.2-3
- 2006-02-28-2047 development snapshot

* Sat Feb 18 2006 Luke Macken <lmacken@redhat.com> 0.11.8.2-2
- Rebuild

* Thu Feb  9 2006 Luke Macken <lmacken@redhat.com> 0.11.8.2-1
- 0.11.8.2-2006-01-29-1935 snapshot

* Tue Dec 27 2005 Luke Macken <lmacken@redhat.com> 0.11.8.1-2
- Rebuild

* Thu Dec 15 2005 Luke Macken <lmacken@redhat.com> 0.11.8.1-1
- Bump to 0.11.8.1

* Sun Oct 02 2005 Luke Macken <lmacken@redhat.com> 0.11.8-1
- Bumped to 0.11.8

* Thu Jul 07 2005 Luke Macken <lmacken@redhat.com> 0.11.7.3.1-2
- Disable detach-mode, which seems to break the users shell upon detaching.
  Run naim in screen manually if you want this functionality.

* Tue Jul 05 2005 Luke Macken <lmacken@redhat.com> 0.11.7.3.1-1
- Packaged for Fedora Extras
