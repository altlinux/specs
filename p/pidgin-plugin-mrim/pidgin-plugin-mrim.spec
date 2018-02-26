Name: pidgin-plugin-mrim
Version: 0.1.28
Release: alt3
License: GPLv2+
Group: Networking/Instant messaging
Summary: MRIM Plugin for libpurple and derived IM clients
Url: http://code.google.com/p/mrim-prpl/

Packager: Anton A. Vinogradov <arc@altlinux.org>

Source: %name.tar
BuildRequires: libpurple-devel libgtk+2-devel

%description
MRIM Plugin for libpurple and derived IM clients. Support SMS sending via mail.ru

%prep
%setup -n %name
sed -i 's|FULL_LIBDIR=usr/${LIBDIR}|FULL_LIBDIR=${LIBDIR}|' Makefile

%build
export LIBDIR="%_libdir"

%configure \
	--gtk

%make_build
%makeinstall_std

%find_lang mrim-prpl-underbush

%files -f mrim-prpl-underbush.lang
%doc README LICENSE TODO
%_libdir/purple-2/mrim-underbush.so
%_pixmapsdir/pidgin/protocols/

%changelog
* Thu Feb 02 2012 Radik Usupov <radik@altlinux.org> 0.1.28-alt3
- New upstreame snapshot

* Mon Jul 18 2011 Radik Usupov <radik@altlinux.org> 0.1.28-alt2
- svn r296

* Mon May 16 2011 Radik Usupov <radik@altlinux.org> 0.1.28-alt1
- New version (0.1.28)
- Changed description
- Small cleanup spec

* Mon Dec 20 2010 Anton A. Vinogradov <arc@altlinux.org> 0.1.27-alt1
- Core
	? Fix bad package
- Roster
	Fix offline auth
	many minor fixes

* Tue Nov 16 2010 Anton A. Vinogradov <arc@altlinux.org> 0.1.26-alt1
- Core
	? Fix bad package
	Fix segfault
	Fix Email notify
	Russian translation fix
- Roster
	User info
	Search&Add Contacts
	Fix remove group issue
- Messages
	Fix segfault (at sending unicode-specific symbols)
	Fix html-formated text recieving

* Sun Oct 10 2010 Anton A. Vinogradov <arc@altlinux.org> 0.1.1-alt1.r16
- new revision

* Thu Sep 02 2010 Anton A. Vinogradov <arc@altlinux.org> 0.1.1-alt1.r8
- Core
	support pidgin 2.3.1+
	downgrade to protocol 1.9
- Account
	fix remove buddy issue
	fix authorize buddy issue
- Other
	Links "Set user info" and "Set avatar" 

* Thu Aug 26 2010 Anton A. Vinogradov <arc@altlinux.org> 0.1-alt1.r22
- Roster
	Group deletion fix (segfault)
	Add + Modify phones
	fix mrim_add_buddy bug(wrong pq->seq)
- Account
	Fix a crash on disconnect
- Messages
	Now, maximum mesage size is 65Kb. (1kb before)
	Free SMS

* Sat Jul 24 2010 Anton A. Vinogradov <arc@altlinux.org> 0.1-alt1.r21
- improve contact list

* Fri Jun 25 2010 Anton A. Vinogradov <arc@altlinux.org> 0.1-alt1.r19
- new revision
- initial build for ALT Linux Sisyphus

* Sat May 01 2010 Anton A. Vinogradov <arc@altlinux.org> 0.1-alt1.r15
- improve offline messages support

* Fri Apr 09 2010 Anton A. Vinogradov <arc@altlinux.org> 0.1-alt1.r13
- add avatars support
- depencies fix
- spec cleanup

* Sun Mar 28 2010 Anton A. Vinogradov <arc@altlinux.org> 0.1-alt0.r11.1
- add offline messages support

* Sun Mar 28 2010 Anton A. Vinogradov <arc@altlinux.org> 0.1-alt0.r10.1
- new revision

* Wed Mar 17 2010 Anton A. Vinogradov <arc@altlinux.org> 0.1-alt0.r9.1
- new revision

* Sun Mar 14 2010 Anton A. Vinogradov <arc@altlinux.org> 0.1-alt0.r8.1
- spec cleanup
- new revision

* Fri Mar 12 2010 Anton A. Vinogradov <arc@altlinux.org> r6-alt1
- initial build for ALT Linux

