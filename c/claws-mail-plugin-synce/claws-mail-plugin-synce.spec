%define _name synce
%define _name2 synce_plugin

Name: claws-mail-plugin-%_name
Version: 0.7.5
Release: alt10

Summary: Plugin assists in keeping the addressbook of a Windows CE device 
License: %gpl3plus
Group: Networking/Mail

Url: http://www.claws-mail.org/plugin.php?plugin=%_name

Source: %_name2-%version.tar

# The macro is defined inside claws-mail-devel.
# FIXME: Generally, this is bad. Each Claws Mail release causes to rebuild
# each and every plugin for it. Does it really matter so much?
Requires: claws-mail = %_claws_version

BuildRequires(pre): rpm-build-licenses claws-mail-devel

BuildPreReq: gettext-tools
BuildPreReq: glib2-devel >= 2.6.0
BuildPreReq: libgtk+2-devel >= 2.6.0
BuildPreReq: libsynce-devel >= 0.9.1
BuildPreReq: librapi-devel >= 0.9.1
BuildRequires: flex libgnutls-devel

%description
encryption of multipart messages very well (yet).
This plugin assists in keeping the addressbook of a Windows CE
device (Pocket PC/ iPAQ, Smartphone etc) in sync with Claws'
addressbook, with respect to email addresses.

%prep
%setup -q -n %_name2-%version

%build
%configure \
	--disable-static
%make

%install
%makeinstall_std
%find_lang %_name2

%files -f %_name2.lang
%_libdir/claws-mail/plugins/%_name2.so

%exclude %_libdir/*/*/*.la

%changelog
* Fri Jun 29 2012 Mikhail Efremov <sem@altlinux.org> 0.7.5-alt10
- rebuild for claws-mail 3.8.1

* Thu Jan 19 2012 Mikhail Efremov <sem@altlinux.org> 0.7.5-alt9
- rebuild for claws-mail 3.8.0

* Fri Sep 02 2011 Mikhail Efremov <sem@altlinux.org> 0.7.5-alt8
- rebuild for claws-mail 3.7.10

* Wed May 04 2011 Mikhail Efremov <sem@altlinux.org> 0.7.5-alt7
- rebuild for claws-mail 3.7.9

* Thu Dec 30 2010 Mikhail Efremov <sem@altlinux.org> 0.7.5-alt6
- rebuild for claws-mail 3.7.8

* Mon Nov 29 2010 Mikhail Efremov <sem@altlinux.org> 0.7.5-alt5
- rebuild for claws-mail 3.7.7

* Tue Aug 24 2010 Mikhail Efremov <sem@altlinux.org> 0.7.5-alt4
- rebuild for claws-mail 3.7.6

* Sat Jan 30 2010 Alexey Rusakov <ktirf@altlinux.org> 0.7.5-alt3
- rebuild for claws-mail 3.7.4

* Fri Jul 10 2009 Alexey Shabalin <shaba@altlinux.ru> 0.7.5-alt2
- rebuild for claws-mail 3.7.2

* Fri May 29 2009 Alexey Shabalin <shaba@altlinux.ru> 0.7.5-alt1
- 0.7.5

* Mon Oct 27 2008 Alexey Shabalin <shaba@altlinux.ru> 0.7.4-alt1
- 0.7.4

* Sat Jun 28 2008 Alexey Shabalin <shaba@altlinux.ru> 0.7.3-alt1
- Initial Sisyphus version.

