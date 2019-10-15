%define oname tcltls

Name: tcl-tls
Version: 1.7.19
Release: alt1

Summary: A tcl extension, wich adds SSL ability to any Tcl channel
License: BSD
Group: Development/Tcl
Url: https://core.tcl.tk/tcltls/

# repacked https://core.tcl-lang.org/tcltls/uv/tcltls-%version.tar.gz
Source: %oname-%version.tar
Source1: tcl-tls.watch

# Debian patches
# hasher chroot
Patch1: hostname-tests.patch

# ALT patches
Patch10: 0001-ALT-TEA.patch
Patch11: 0002-ALT-tests-auto_path.patch

BuildPreReq:  rpm-build-tcl >= 0.5-alt1
BuildRequires: libssl-devel tcl-devel >= 8.6.7-alt2
Requires: tcl >= 8.6.7-alt2

%description
TLS is a Tcl extension, wich adds SSL ability to any Tcl channel.
Both client and server-side sockets are possible, and this code should work
on any platform as it uses a generic mechanism for layering on SSL and Tcl.

%prep
%setup -q -n %oname-%version
%patch1 -p1
%patch10 -p2
%patch11 -p2
sed -i 's/@lib@/%_lib/g' pkgIndex.tcl.in

%build
%autoreconf
%configure \
	--disable-rpath \
	--enable-hardening \
	--with-openssl-dir="%prefix" \
	#
make

%install
%makeinstall

%check
make test AUTO_PATH=%buildroot%_tcllibdir/tcltls%version

%files
%doc ChangeLog README.txt license.terms tls.htm
%_tcllibdir/tcltls.so
%_tcllibdir/tcltls%version

%changelog
* Tue Oct 15 2019 Vladimir D. Seleznev <vseleznv@altlinux.org> 1.7.19-alt1
- 1.7.19.
- Fixed ALT TEA.
- Packed watch file from Debian project.

* Sat Aug 17 2019 Vladimir D. Seleznev <vseleznv@altlinux.org> 1.7.18-alt1
- 1.7.18.
- Enabled tests.

* Wed Aug 29 2018 Grigory Ustinov <grenka@altlinux.org> 1.7.12-alt2.1
- NMU: Rebuild with new openssl 1.1.0.

* Wed Oct 04 2017 Vladimir D. Seleznev <vseleznv@altlinux.org> 1.7.12-alt2
- adapted for new tcl/tk extension policy
- drop devel subpackage

* Mon Aug 21 2017 Vladimir D. Seleznev <vseleznv@altlinux.org> 1.7.12-alt1
- 1.7.12 released
- built devel subpackage
- updated upstream url

* Wed Apr 17 2013 Dmitry V. Levin (QA) <qa_ldv@altlinux.org> 1.6.1-alt1.qa1
- NMU: rebuilt for debuginfo.

* Mon Dec 06 2010 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.6.1-alt1
- 1.6.1 released

* Sat Aug 09 2008 ALT QA Team Robot <qa-robot@altlinux.org> 1.5.1-alt4.1
- Automated rebuild due to libssl.so.6 -> libssl.so.7 soname change.

* Mon Jun 25 2007 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.5.1-alt4
- CVS snapshot @20070623

* Fri Dec 29 2006 ALT QA Team Robot <qa-robot@altlinux.org> 1.5.1-alt3.1
- Rebuilt due to libcrypto.so.4 -> libcrypto.so.6 soname change.

* Sat Jul 22 2006 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.5.1-alt3
- fixed build on x86_64

* Fri Jan 20 2006 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.5.1-alt2
- fixed unresolved symbols, appeared in prev build

* Tue Jan 10 2006 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.5.1-alt1
- CVS snapshot @20050208

* Wed Nov  3 2004 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.5.0-alt2
- CVS snapshot @20040629

* Fri May 14 2004 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.5.0-alt1
- 1.5.0

* Wed May 12 2004 ALT QA Team Robot <qa-robot@altlinux.org> 1.4.1-alt9.1.1
- Rebuilt with openssl-0.9.7d.

* Wed May 12 2004 Dmitry V. Levin <ldv@altlinux.org> 1.4.1-alt9.1
- Fixed packager tag.

* Tue Sep 24 2002 Sergey Bolshakov <s.bolshakov@belcaf.com> 1.4.1-alt9
- rebuilt with tcl 8.4

* Fri Jun  7 2002 Sergey Bolshakov <s.bolshakov@belcaf.com> 1.4.1-alt8
- updated from cvs
- rebuilt in new env
- src rpm splitted
