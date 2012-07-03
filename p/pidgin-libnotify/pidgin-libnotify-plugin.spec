%global	pidgin_version 2.0.0

Name: pidgin-libnotify
Version: 0.14
Release: alt5
Summary: Libnotify Pidgin plugin
Summary (ru_RU.UTF8): Дополнение к интернет пейджеру Pidgin позволяющее отображать всплывающие сообщения

Group: Networking/Instant messaging
License: GPLv2
Url: http://gaim-libnotify.sourceforge.net/

Source0: http://downloads.sourceforge.net/gaim-libnotify/%name-%version.tar.gz
Patch: show_button_fix.patch
Patch2: pidgin-libnotify-0.14-libnotify-0.7.0.patch
Packager: Denis Koryavov <dkoryavov@altlinux.org>

BuildRequires: gettext, gettext-tools, gettext-tools-java
BuildRequires: libnotify-devel >= 0.3.2
BuildRequires: perl-XML-Parser
BuildRequires: pidgin-devel >= %pidgin_version
BuildRequires: intltool

Requires: pidgin >= %pidgin_version

%description
This is a plugin for the open-source Pidgin instant messaging client that uses
libnotify to display graphic notifications of new messages and other events
such as a buddy signing on or off.

%description -l ru_RU.UTF8
Данный пакет содержит в себе дополнение к интернет пейджеру Pidgin позволяющее отображать
"всплывающие" сообщения и уведомления с помощью службы уведомлений libnotify.

%prep
%setup
%patch -p1
%patch2 -p1

%build
%undefine __libtoolize
%configure --disable-static --disable-deprecated
%make

%install
%makeinstall_std
%find_lang %name

%files -f %name.lang
%doc AUTHORS ChangeLog COPYING NEWS TODO
%exclude %_libdir/purple-2/*.la
%_libdir/purple-2/%name.so

%changelog
* Wed Jun 08 2011 Alexey Shabalin <shaba@altlinux.ru> 0.14-alt5
- fix for libnotify 0.7

* Wed May 13 2009 Denis Koryavov <dkoryavov@altlinux.org> 0.14-alt4
- Fix for bug #19990

* Fri May 08 2009 Denis Koryavov <dkoryavov@altlinux.org> 0.14-alt3
- Added show_button_fix.patch that allows to show conversation window by clicking on button 'Show'.

* Mon Apr 20 2009 Denis Koryavov <dkoryavov@altlinux.org> 0.14-alt2
Spec cleunup. Added russian description.

* Mon Mar 23 2009 2009 Denis Koryavov <dkoryavov@altlinux.org> 0.14-alt1
- First build

