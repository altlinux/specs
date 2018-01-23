# Spec file for Icecast streaming server

Name: icecast
Version: 2.4.3
Release: alt1

Summary: Streaming Media Server
License: %gpl2only
Group: System/Servers
Url: http://www.icecast.org

Source0: %name-%version.tar
Source1: %name.init
Source2: %name.logrotate
Source3: %name.xml

Source4: %name.chroot.lib
Source5: %name.chroot.conf
Source6: %name.chroot.all

Source7: xspf.xsl
Patch1: %name-%version-alt.patch

BuildRequires(pre): rpm-build-licenses
# Automatically added by buildreq on Mon Jul 06 2009
BuildRequires: gcc-c++ libcurl-devel libspeex-devel libtheora-devel libvorbis-devel libxslt-devel

%description
Icecast is an Internet based broadcasting system based on the Mpeg Layer III
streaming technology. It is, however, not limited to streaming mp3 files.

%prep
%setup -q
%patch1 -p1

%build
%autoreconf
%configure \
	--datadir=%_localstatedir \
	--localstatedir=%_var

%make_build

%install
%make_install DESTDIR=%buildroot install

install -p -m755 -D %SOURCE1 %buildroot%_initdir/%name
install -p -m640 -D %SOURCE2 %buildroot%_sysconfdir/logrotate.d/%name
install -p -m640 -D %SOURCE3 %buildroot%_sysconfdir/%name.xml
install -p -m644 -D %SOURCE7 %buildroot%_localstatedir/%name/admin/xspf.xsl
mkdir -p %buildroot/var/run/%name
mkdir -p -m750 %buildroot%_localstatedir/%name/logs

mkdir -p %buildroot%_datadir/doc
mv %buildroot%_localstatedir/doc/%name-%version %buildroot%_datadir/doc/%name-%version
mv %buildroot%_datadir/doc/%name/* %buildroot%_datadir/doc/%name-%version/
rmdir %buildroot%_datadir/doc/%name

install -m 0755 -d -- %buildroot%_localstatedir/%name/etc
install -m 0755 -d -- %buildroot%_localstatedir/%name/%_lib
install -p -m 0750 -D -- %SOURCE4 %buildroot%_sysconfdir/chroot.d/%name.lib
install -p -m 0750 -D -- %SOURCE5 %buildroot%_sysconfdir/chroot.d/%name.conf
install -p -m 0750 -D -- %SOURCE6 %buildroot%_sysconfdir/chroot.d/%name.all

%pre
%_sbindir/groupadd -r -f %name &>/dev/null
%_sbindir/useradd -r -g %name -d %_datadir/%name -s /dev/null \
	-c "Icecast Streaming Media Server" -M -n %name &>/dev/null ||:

%post
%_sysconfdir/chroot.d/%name.all
%post_service %name

%preun
%preun_service %name

%files
%_datadir/doc/%name-%version

%attr(750,  root, %name) %dir %_localstatedir/%name
%attr(1770, root, %name) %dir %_localstatedir/%name/logs
%attr(1775, root, %name) %dir /var/run/%name

%config %_sysconfdir/logrotate.d/%name
%config (noreplace) %_sysconfdir/%name.xml
%config %_sysconfdir/chroot.d/%name.*

%_initdir/%name
%_bindir/%name
%_localstatedir/%name

%changelog
* Mon Jan 22 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 2.4.3-alt1
- Updated to upstream version 2.4.3 (Fixes: CVE-2011-4612).
- Fixed localstatedir.

* Sat May 26 2012 Nikolay A. Fetisov <naf@altlinux.ru> 2.3.2-alt4
- Fix build with --no-copy-dt-needed-entries

* Wed Dec 08 2010 Igor Vlasenko <viy@altlinux.ru> 2.3.2-alt3.1
- rebuild with new openssl and/or boost by request of git.alt administrator

* Tue Jul 14 2009 Nikolay A. Fetisov <naf@altlinux.ru> 2.3.2-alt3
- Fix init script to setup chroot environment

* Mon Jul 06 2009 Nikolay A. Fetisov <naf@altlinux.ru> 2.3.2-alt2
- Adding xspf.xsl from SVN@15785 (Closes: 20628)
- Adding resolver files into chroot environment (Closes: 9739)

* Fri Dec 12 2008 Nikolay A. Fetisov <naf@altlinux.ru> 2.3.2-alt1
- New version 2.3.2

* Wed Apr 11 2007 Pavlov Konstantin <thresh@altlinux.ru> 2.3.1-alt3
- Fixed logrotate script (closes #11448).

* Sat Mar 03 2007 Pavlov Konstantin <thresh@altlinux.ru> 2.3.1-alt2
- Added icecast-2.3.1-ugly-workaround-hack-newcurl.patch to fix build
  with newer curl.
- Removed macro abuse from spec.
- Fixed BuildRequires.

* Fri Dec 29 2006 ALT QA Team Robot <qa-robot@altlinux.org> 2.3.1-alt1.1
- Rebuilt due to libcrypto.so.4 -> libcrypto.so.6 soname change.

* Mon Dec 05 2005 Pavlov Konstantin <thresh@altlinux.ru> 2.3.1-alt1
- 2.3.1 release.

* Mon Oct 03 2005 Pavlov Konstantin <thresh@altlinux.ru> 2.3.0-alt1
- 2.3.0 release.
- icecast now comes chrooted with default config in /var/lib/icecast
- icecast now binds to localhost only by default.

* Thu Jan 20 2005 Pavlov Konstantin <thresh@altlinux.ru> 2.2.0-alt1
- 2.2.0 release

* Mon Nov 22 2004 Pavlov Konstantin <thresh@altlinux.ru> 2.1.0-alt1
- 2.1.0 release

* Tue Jul 13 2004 Pavlov Konstantin <thresh@altlinux.ru> 2.0.2-alt1
- 2.0.2 release

* Thu Dec 26 2002 Sergey Bolshakov <s.bolshakov@belcaf.com> 1.3.12-alt4
- rebuilt with new (shared) libwrap

* Sat Oct 19 2002 Sergey Bolshakov <s.bolshakov@belcaf.com> 1.3.12-alt3
- rebuilt in new env

* Wed Jun 26 2002 Sergey Bolshakov <s.bolshakov@belcaf.com> 1.3.12-alt2
- bug #1034 fixed

* Sat May 25 2002 Sergey Bolshakov <s.bolshakov@belcaf.com> 1.3.12-alt1
- 1.3.12 
- tcp_wrappers back

* Mon Sep  3 2001 Sergey Bolshakov <s.bolshakov@belcaf.com> 1.3.11-alt1
- 1.3.11
- buggy tcp_wrappers support removed

* Tue May 29 2001 Dmitry V. Levin <ldv@altlinux.ru> 1.3.10-alt2
- Fixed init script.
- Specfile cleanup.

* Wed Mar 21 2001 Sergey Bolshakov <s.bolshakov@belcaf.com>
- First build for ALT Linux distribution


