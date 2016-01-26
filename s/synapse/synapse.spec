Name: synapse
Version: 0.2.99.1
Release: alt3
Summary: A semantic launcher written in Vala
Summary(ru_RU.UTF-8): Семантический запуск приложений

Group: System/Base
License: GPLv3+
Url: http://synapse.zeitgeist-project.com
Packager: Konstantin Artyushkin <akv@altlinux.org>

Source: %name-%version.tar.xz

BuildRequires: desktop-file-utils
BuildRequires: gettext-tools
BuildRequires: libgtk+3-devel libwebkitgtk3-gir-devel
BuildRequires: intltool
BuildRequires: libjson-glib-devel libjson-glib-gir-devel
BuildRequires: libgee0.8-devel
BuildRequires: libgtkhotkey-devel
BuildRequires: libnotify-devel
BuildRequires: libzeitgeist2.0-devel
BuildRequires: librest
BuildRequires: libdbus-glib-devel
BuildRequires: libunique-devel
BuildRequires: vala
BuildRequires: libkeybinder3-devel libkeybinder3-gir-devel
Requires: zeitgeist

%description
Synapse is a semantic launcher written in Vala that you can use to start
applications as well as find and access relevant documents and files by making
use of the Zeitgeist engine.

%description -l ru_RU.UTF-8
Synapse запуск приожений, похожий на gnome-do. Написано на Vala. Позволяет запускать
приложения и выполнять кучу разных базовых действий. Имеет плагины. Работает с
движком Zeitgeist.

%package devel
Summary: Development files for %name
Group: System/Libraries
Requires: %name = %version-%release

%description devel
The %name-devel package contains libraries and header files for
developing applications that use %name.

%prep
%setup

%build
%autoreconf
%configure --disable-static --enable-zeitgeist=yes
%make

%install
%makeinstall_std
install -d -p -m 755 %buildroot%_datadir/vala/vapi
install -D -p -m 644 vapi/*.vapi %buildroot%_datadir/vala/vapi

# language files
%find_lang %name

# install desktop files
desktop-file-install                                    \
--delete-original                                       \
--dir=%buildroot%_desktopdir              \
%buildroot%_desktopdir/synapse.desktop
#  validate desktop file
desktop-file-validate %buildroot/%_desktopdir/synapse.desktop

%post
touch --no-create %_iconsdir/hicolor &>/dev/null || :

%postun
if [ $1 -eq 0 ] ; then
    touch --no-create %_iconsdir/hicolor &>/dev/null
    gtk-update-icon-cache %_iconsdir/hicolor &>/dev/null || :
fi

# posttrans
#gtk-update-icon-cache %%_iconsdir/hicolor &>/dev/null || :

%files -f %name.lang
%doc COPYING README
%_bindir/synapse
%_desktopdir/synapse.desktop
%_iconsdir/hicolor/scalable/apps/synapse.svg
%_man1dir/%name.*

%files devel
%doc AUTHORS
%_datadir/vala/vapi/*

%changelog
* Tue Jan 26 2016 Konstantin Artyushkin <akv@altlinux.org> 0.2.99.1-alt3
- replace man file extension

* Sat Sep 19 2015 Konstantin Artyushkin <akv@altlinux.org> 0.2.99.1-alt2
- inital build 0.2.99.1  

* Wed Aug 26 2015 Konstantin Artyushkin <akv@altlinux.org> 0.2.10-alt2
- inital build 0.2.10  

* Fri Oct 14 2011 Rahul Sundaram <sundaram@fedoraproject.org> - 0.2.6-1
- New upstream release

* Sun Apr 10 2011 Rahul Sundaram <sundaram@fedoraproject.org> - 0.2.6-1
- New upstream release
- Dropped no longer required patch

* Sat Apr 02 2011 Renich Bon Ciric <renich@woralelandia.com> - 0.2.4.1-4
- Moved README from devel to the main package

* Thu Mar 31 2011 Renich Bon Ciric <renich@woralelandia.com> - 0.2.4.1-3
- Changed the license to GPLv3+
- Implemented the isa macro on the devel package
- Removed BuildRoot
- Removed the check macro since it does nothing
- Removed empty docs
- Removed repeated docs on devel
- Removed INSTALL from documentation

* Mon Mar 28 2011 Renich Bon Ciric <renich@woralelandia.com> - 0.2.4.1-1
- Updated to 0.2.4.1
- Applied patch for bug https://launchpad.net/bugs/738153
- Added rest-devel as build dependency
- Added many missing dependencies
- Implemented the arch macro
- Removed the clean section
- Updated the install section
- Added proper desktop-file installation and validation procedures
- Added a make check section

* Fri Mar 25 2011 Renich Bon Ciric <renich@woralelandia.com> - 0.2.4-2
- Enabled Zeitgeist plugin

* Thu Feb 24 2011 Renich Bon Ciric <renich@woralelandia.com> - 0.2.4-1
- Updated to latest version

* Thu Jan 28 2011 Renich Bon Ciric <renich@woralelandia.com> - 0.2.2.2-1
- First build
