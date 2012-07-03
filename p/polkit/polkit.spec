Name: polkit
Version: 0.105
Release: alt1
Summary: PolicyKit Authorization Framework
License: LGPLv2+
Group: System/Libraries
URL: http://www.freedesktop.org/wiki/Software/PolicyKit
Packager: Valery Inozemtsev <shrek@altlinux.ru>

Requires: lib%name = %version-%release
PreReq: dbus

Source: %name-%version.tar
Patch: %name-%version-%release.patch

BuildRequires: gobject-introspection-devel gtk-doc intltool libexpat-devel libpam-devel
BuildRequires: libsystemd-login-devel

%description
PolicyKit is a toolkit for defining and handling authorizations.
It is used for allowing unprivileged processes to speak to privileged
processes.

%package -n lib%name
Summary: PolicyKit libraries
Group: System/Libraries
Provides: lib%{name}1 = %version-%release
Obsoletes: lib%{name}1 < %version

%description -n lib%name
Libraries for interacting with PolicyKit

%package -n lib%name-devel
Summary: Development libraries and headers for PolicyKit
Group: Development/C
Requires: lib%name = %version-%release
Provides: lib%{name}1-devel = %version-%release
Obsoletes: lib%{name}1-devel < %version

%description -n lib%name-devel
Headers, libraries and API docs for PolicyKit

%package -n lib%name-gir
Summary: GObject introspection data for the Polkit-1.0 library
Group: System/Libraries
Requires: lib%name = %version-%release
Provides: lib%{name}1-gir = %version-%release
Obsoletes: lib%{name}1-gir < %version

%description -n lib%name-gir
GObject introspection data for the Polkit-1.0 library

%package -n lib%name-gir-devel
Summary: GObject introspection devel data for the Polkit-1.0 library
Group: System/Libraries
BuildArch: noarch
Requires: lib%name-gir = %version-%release lib%name-devel = %version-%release
Provides: lib%{name}1-gir-devel = %version-%release
Obsoletes: lib%{name}1-gir-devel < %version

%description -n lib%name-gir-devel
GObject introspection devel data for the Polkit-1.0 library

%prep
%setup -q
%patch -p1

touch ChangeLog

%build
%autoreconf
%configure \
	--libexecdir=%_prefix/libexec/%name-1 \
	--localstatedir=%_var \
	--enable-gtk-doc \
	--disable-static
%make

%install
%make DESTDIR=%buildroot install

%find_lang %name-1

%files -f %name-1.lang
%_sysconfdir/%name-1
%_sysconfdir/dbus-1/system.d/org.freedesktop.PolicyKit1.conf
%_sysconfdir/pam.d/polkit-1
%_bindir/pk[act]*
%attr(4511,root,root) %_bindir/pkexec
%dir %_libdir/%name-1
%dir %_libdir/%name-1/extensions
%_libdir/%name-1/extensions/*.so
%dir %_prefix/libexec/%name-1
%_prefix/libexec/%name-1/polkitd
%attr(4511,root,root) %_prefix/libexec/polkit-1/polkit-agent-helper-1
%dir %_datadir/%name-1
%dir %_datadir/%name-1/actions
%_datadir/%name-1/actions/org.freedesktop.policykit.policy
%_datadir/dbus-1/system-services/org.freedesktop.PolicyKit1.service
%_man1dir/*.1*
%_man8dir/*.8*
%attr(0700,root,root) %_var/lib/polkit-1

%files -n lib%name
%_libdir/*.so.*

%files -n lib%name-gir
%_libdir/girepository-1.0/*.typelib

%files -n lib%name-devel
%_includedir/*
%_libdir/*.so
%_pkgconfigdir/*.pc
%_datadir/gtk-doc/html/%name-1

%files -n lib%name-gir-devel
%_datadir/gir-1.0/*.gir

%changelog
* Sat May 12 2012 Valery Inozemtsev <shrek@altlinux.ru> 0.105-alt1
- 0.105

* Thu Jan 19 2012 Valery Inozemtsev <shrek@altlinux.ru> 0.104-alt1
- 0.104

* Fri Aug 19 2011 Valery Inozemtsev <shrek@altlinux.ru> 0.102-alt1
- 0.102

* Mon Apr 25 2011 Valery Inozemtsev <shrek@altlinux.ru> 0.101-alt2
- update to master git.7c59052 (fixed CVE-2011-1485)

* Tue Mar 08 2011 Valery Inozemtsev <shrek@altlinux.ru> 0.101-alt1
- 0.101

* Tue Feb 22 2011 Valery Inozemtsev <shrek@altlinux.ru> 0.100-alt1
- 0.100

* Tue Feb 08 2011 Valery Inozemtsev <shrek@altlinux.ru> 0.99-alt3
- rebuild

* Wed Oct 13 2010 Valery Inozemtsev <shrek@altlinux.ru> 0.99-alt2
- updated build dependencies

* Fri Oct 08 2010 Valery Inozemtsev <shrek@altlinux.ru> 0.99-alt1
- 0.99

* Thu Apr 01 2010 Valery Inozemtsev <shrek@altlinux.ru> 0.96-alt3
- rebuild

* Tue Mar 09 2010 Valery Inozemtsev <shrek@altlinux.ru> 0.96-alt2
- rebuild

* Sat Jan 16 2010 Valery Inozemtsev <shrek@altlinux.ru> 0.96-alt1
- 0.96

* Thu Nov 19 2009 Valery Inozemtsev <shrek@altlinux.ru> 0.95-alt1
- 0.95

* Wed Aug 12 2009 Valery Inozemtsev <shrek@altlinux.ru> 0.94-alt1
- 0.94

* Tue Aug 11 2009 Valery Inozemtsev <shrek@altlinux.ru> 0.93-alt1
- 0.93

* Wed May 27 2009 Valery Inozemtsev <shrek@altlinux.ru> 0.9-alt7
- relocated devel files

* Thu Feb 12 2009 Valery Inozemtsev <shrek@altlinux.ru> 0.9-alt6
- fixed D-Bus policy (fd.o #18948)

* Sat Nov 22 2008 Valery Inozemtsev <shrek@altlinux.ru> 0.9-alt5
- removed obsolete %%post_ldconfig/%%postun_ldconfig calls

* Fri Nov 21 2008 Valery Inozemtsev <shrek@altlinux.ru> 0.9-alt4
- added suid for polkit-grant-helper-pam

* Thu Nov 20 2008 Valery Inozemtsev <shrek@altlinux.ru> 0.9-alt3
- /usr/libexec/PolicyKit/polkit-*: fixed permission

* Sat Aug 02 2008 Valery Inozemtsev <shrek@altlinux.ru> 0.9-alt2
- API fixed in CK 0.3

* Fri Aug 01 2008 Valery Inozemtsev <shrek@altlinux.ru> 0.9-alt1
- 0.9

* Thu Apr 17 2008 Valery Inozemtsev <shrek@altlinux.ru> 0.8-alt1
- 0.8
- rename subpackage libPolicyKit to libpolkit

* Fri Apr 04 2008 Valery Inozemtsev <shrek@altlinux.ru> 0.7-alt3
- fixed CVE-2008-1658
- drop polkit-bash-completion.sh (close #15232)

* Tue Apr 01 2008 Valery Inozemtsev <shrek@altlinux.ru> 0.7-alt2
- fixed read default policy on reiserfs/xfs

* Fri Jan 25 2008 Valery Inozemtsev <shrek@altlinux.ru> 0.7-alt1
- 0.7

* Fri Oct 12 2007 Valery Inozemtsev <shrek@altlinux.ru> 0.6-alt1
- 0.6

* Sun Jul 29 2007 Valery Inozemtsev <shrek@altlinux.ru> 0.4-alt1
- 0.4

* Mon Jun 25 2007 Valery Inozemtsev <shrek@altlinux.ru> 0.3-alt1
- 0.3

* Mon Jun 11 2007 Igor Zubkov <icesik@altlinux.org> 0.2-alt7.git20060822
- move gtk-doc documentation to devel subpackage (closes #12008)
- buildreq

* Tue Feb 20 2007 Igor Zubkov <icesik@altlinux.org> 0.2-alt6.git20060822
- fix attr's for %%_var/run/polkit

* Mon Dec 25 2006 Igor Zubkov <icesik@altlinux.org> 0.2-alt5.git20060822
- rebuild with new dbus

* Tue Nov 28 2006 Igor Zubkov <icesik@altlinux.org> 0.2-alt4.git20060822
- small fix for thresh@ changes
- s/%%make_build/make/ (fix build in hasher)
- change polkit group to _polkit
- change polkit user to _polkit

* Mon Nov 27 2006 Pavlov Konstantin <thresh@altlinux.ru> 0.2-alt3.git20060822
- Some spec cleanup.
- Some buildrequires cleanup.
- Some descriptions cleanup.
- Fix docs packaging.
- Altify user creation in %%pre.

* Mon Nov 20 2006 Igor Zubkov <icesik@altlinux.org> 0.2-alt2.git20060822
- disable -Werror

* Mon Nov 20 2006 Igor Zubkov <icesik@altlinux.org> 0.2-alt1.git20060822
- rename spec from policykit.spec to PolicyKit.spec
- s/%%make/%%make_build/
- add HACKING to docs
- remove INSTALL from docs
- correct License from GPL to AFL/GPL
- add Packager tag
- add pam module subpackage
- build with -Werror by default
- add PolicyKit-devel-static subpackage

* Tue Nov 14 2006 Alexey Shabalin <shaba@altlinux.ru> 0.2_git20060822-alt0.1
- initial build
