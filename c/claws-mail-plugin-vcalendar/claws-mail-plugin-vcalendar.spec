%define _name vcalendar

Name: claws-mail-plugin-%_name
Version: 2.0.13
Release: alt1

Summary: Plugin handles the vCalendar for Claws Mail
License: %gpl3plus
Group: Networking/Mail

Url: http://www.claws-mail.org/plugin.php?plugin=%_name

Source: %_name-%version.tar

# The macro is defined inside claws-mail-devel.
# FIXME: Generally, this is bad. Each Claws Mail release causes to rebuild
# each and every plugin for it. Does it really matter so much?
Requires: claws-mail = %_claws_version

BuildRequires(pre): rpm-build-licenses claws-mail-devel

BuildPreReq: gettext-tools
BuildPreReq: glib2-devel >= 2.6.0
BuildPreReq: libgtk+2-devel >= 2.6.0
BuildPreReq: libcurl-devel

BuildRequires: flex

%description
This Claws Mail plugin handles the vCalendar format (or rather, the
meeting subset of it). It displays such mails in a nice format, lets you
create and send meetings, and creates a virtual folder with the meetings
you sent or received.

%prep
%setup -q -n %_name-%version

%build
%autoreconf
%configure \
	--disable-static
%make

%install
%makeinstall_std
%find_lang %_name

%files -f %_name.lang
%_libdir/claws-mail/plugins/%_name.so

%exclude %_includedir/claws-mail/plugins/*/*.h
%exclude %_libdir/*/*/*.la

%changelog
* Fri Jun 29 2012 Mikhail Efremov <sem@altlinux.org> 2.0.13-alt1
- Updated to 2.0.13.

* Wed Jan 18 2012 Mikhail Efremov <sem@altlinux.org> 2.0.12-alt1
- Updated to 2.0.12.

* Tue Dec 13 2011 Mikhail Efremov <sem@altlinux.org> 2.0.11-alt2
- Fix build: drop unneeded BR.

* Fri Sep 02 2011 Mikhail Efremov <sem@altlinux.org> 2.0.11-alt1
- 2.0.11.

* Wed May 04 2011 Mikhail Efremov <sem@altlinux.org> 2.0.10-alt1
- 2.0.10.

* Thu Dec 30 2010 Mikhail Efremov <sem@altlinux.org> 2.0.9-alt2
- rebuild for claws-mail 3.7.8

* Mon Nov 29 2010 Mikhail Efremov <sem@altlinux.org> 2.0.9-alt1
- 2.0.9.

* Tue Aug 24 2010 Mikhail Efremov <sem@altlinux.org> 2.0.8-alt1
- 2.0.8

* Sat Jan 30 2010 Alexey Rusakov <ktirf@altlinux.org> 2.0.7-alt1
- 2.0.7

* Thu Oct 29 2009 Alexey Shabalin <shaba@altlinux.ru> 2.0.6-alt1
- 2.0.6

* Fri Jul 10 2009 Alexey Shabalin <shaba@altlinux.ru> 2.0.5-alt1
- 2.0.5

* Fri May 29 2009 Alexey Shabalin <shaba@altlinux.ru> 2.0.4-alt1
- 2.0.4

* Mon Oct 27 2008 Alexey Shabalin <shaba@altlinux.ru> 2.0.2-alt1
- 2.0.2

* Sat Jun 28 2008 Alexey Shabalin <shaba@altlinux.ru> 2.0-alt1
- Initial Sisyphus version.

