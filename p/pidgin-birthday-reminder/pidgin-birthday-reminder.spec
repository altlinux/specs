Name: pidgin-birthday-reminder
Version: 1.13
Release: alt1
Summary: Birthday Reminder plugin for Pidgin

Group: Networking/Instant messaging
License: GPLv2+
Url: https://github.com/kgraefe/pidgin-birthday-reminder
Source0: http://launchpad.net/%name/trunk/%version/+download/%name-%version.tar.gz

# Automatically added by buildreq on Wed May 19 2010
BuildRequires: intltool pidgin-devel

Requires: pidgin

%description
Pidgin Birthday Reminder reminds you of your buddies birthdays. Birthdays can
be set by hand or be automatically filled-in for ICQ, MSN and XMPP protocols.

%prep
%setup -q

%build
%configure --disable-static
%make_build

%install
%make_install DESTDIR=%buildroot install

%find_lang %name

%files -f %name.lang
%doc AUTHORS.md CHANGES.md COPYING README.md
%_libdir/pidgin/*.so
%exclude %_libdir/pidgin/*.la
%_datadir/pixmaps/pidgin/birthday_reminder/
%_datadir/sounds/pidgin/birthday_reminder/
%_datadir/appdata/%name.metainfo.xml

%changelog
* Fri Oct 02 2020 Andrew A. Vasilyev <andy@altlinux.org> 1.13-alt1
- 1.13
- change Url of Home Page

* Mon Apr 15 2013 Dmitry V. Levin (QA) <qa_ldv@altlinux.org> 1.6-alt1.qa1
- NMU: rebuilt for debuginfo.

* Fri Aug 13 2010 Alexey Shabalin <shaba@altlinux.ru> 1.6-alt1
- 1.6
- change Url of Home Page

* Wed May 19 2010 Alexey Shabalin <shaba@altlinux.ru> 1.5-alt1
- initial build
