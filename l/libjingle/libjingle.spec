Name: libjingle
Version: 0.3.12
Release: alt4.1

Summary: GoogleTalk implementation of Jingle
Group: System/Libraries
License: BSD
URL: http://farsight.freedesktop.org/releases/libjingle

Source0: %name-%version.tar

Patch0: libjingle-0.3.12-alt-unresolved.patch
Patch1: libjingle-0.3.12-fix-gcc4.4-build.patch
Patch2: libjingle-0.3.12-alt-unique-install.patch
#debian patches
Patch6: libjingle-0.3.11-deb-03_fix_bsd_ftbfs.patch

Packager: Afanasov Dmitry <ender@altlinux.org>

#file /usr/bin/relayserver from install of kdenetwork-kopete-3.5.9-alt1 conflicts with file from package libjingle-0.3.11-alt2
#file /usr/bin/stunserver from install of kdenetwork-kopete-3.5.9-alt1 conflicts with file from package libjingle-0.3.11-alt2
Conflicts: kdenetwork-kopete <= 3.5.10-alt2

# Automatically added by buildreq on Thu Jul 03 2008
BuildRequires: gcc-c++ libexpat-devel libssl-devel

%description
Libjingle is Google Talk's implementation of Jingle and Jingle-Audio
(proposed extensions to XMPP) to interoperate with Google Talk's
peer-to-peer and voice calling capabilities.

This library aimed to work with farsight project.

%package devel
Summary: Development files for %name
Group: Development/C++
Requires: %name = %version-%release
Requires: libexpat-devel
Requires: libssl-devel

%description    devel
The %name-devel package contains libraries and header files for
developing applications that use %name.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1
# debian patches
%patch6

%build
%autoreconf
%configure --disable-static
%make_build

%install
%make_install DESTDIR=%buildroot install

%files
%doc AUTHORS COPYING ChangeLog DOCUMENTATION NEWS README
%_bindir/relayserver
%_bindir/stunserver
%_libdir/lib*.so.*

%files devel
%_includedir/%name-0.3/
%_libdir/lib*.so
%_pkgconfigdir/jinglebase-0.3.pc
%_pkgconfigdir/jinglep2p-0.3.pc

%changelog
* Mon Nov 08 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.3.12-alt4.1
- Rebuilt for soname set-versions

* Mon May 25 2009 Afanasov Dmitry <ender@altlinux.org> 0.3.12-alt4
- fix build with automake 1.11 (pass unique names to install command)

* Fri May 08 2009 Afanasov Dmitry <ender@altlinux.org> 0.3.12-alt3
- fix gcc4.4 build

* Tue May 05 2009 Afanasov Dmitry <ender@altlinux.org> 0.3.12-alt2
- update conflict with kopete

* Sun Dec 21 2008 Afanasov Dmitry <ender@altlinux.org> 0.3.12-alt1
- 0.3.12
- change upstream: this version was pick up from farsight project.
- remove applied patches:
  + debian tcp_wouldblock
  + gcc4.3 fix
  + debian ignore_invalid_sockets
- build with %%autoreconf now
- rework alt-unresolved patch for new version.

* Tue Nov 25 2008 Afanasov Dmitry <ender@altlinux.org> 0.3.11-alt5
- removed obsolete %%post_ldconfig/%%postun_ldconfig calls

* Wed Oct 29 2008 Afanasov Dmitry <ender@altlinux.org> 0.3.11-alt4
- update patch for gcc 4.3

* Wed Oct 29 2008 Afanasov Dmitry <ender@altlinux.org> 0.3.11-alt3
- add debian patches
- fix 4.3 build

* Sat Aug 09 2008 ALT QA Team Robot <qa-robot@altlinux.org> 0.3.11-alt2.1
- Automated rebuild due to libssl.so.6 -> libssl.so.7 soname change.

* Thu Jul 03 2008 Igor Zubkov <icesik@altlinux.org> 0.3.11-alt2
- buildreq

* Fri Sep 28 2007 Igor Zubkov <icesik@altlinux.org> 0.3.11-alt1
- build for Sisyphus

* Tue Aug 28 2007 Brian Pepple <bpepple@fedoraproject.org> - 0.3.11-4
- Rebuild for expat 2.0.

* Tue Aug 21 2007 Brian Pepple <bpepple@fedoraproject.org> - 0.3.11-3
- Rebuild.

* Wed Jun 27 2007 Brian Pepple <bpepple@fedoraproject.org> - 0.3.11-2
- Update URL.

* Fri May 18 2007 Brian Pepple <bpepple@fedoraproject.org> - 0.3.11-1
- Update 0.3.11.

* Mon Sep  4 2006 Brian Pepple <bpepple@fedoraproject.org> - 0.3.10-1
- Initial FE spec.
