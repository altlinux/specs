Name: nautilus-dropbox
Version: 0.6.7
Release: alt2.1

Summary: Dropbox integration for Nautilus
Summary(ru_RU.UTF-8): Интеграция Dropbox с Nautilus
License: GPL, CC BY-ND 3.0
Group: Graphical desktop/GNOME
Url: http://www.dropbox.com/

Packager: Maxim Zhukov <mzhukov@altlinux.org>
Source: %name-%version.tar
Source1: dropbox.desktop
Source2: dropbox-wrapper

BuildRequires:glib2-devel >= 2.14.0
BuildRequires:gtk+2-devel >= 2.12.0
BuildRequires:libnautilus-devel >= 2.20.0
BuildRequires:pkg-config
BuildRequires:python-module-docutils
BuildRequires:python-module-pygtk

Requires:nautilus >= 2.16.0
Requires: dropbox = %version-%release

%description
Nautilus Dropbox is an extension that integrates
the Dropbox web service with your GNOME Desktop.

Check us out at http://www.dropbox.com/

%description -l ru_RU.UTF-8
Nautilus Dropbox - это расширения интегрирующее
веб-сервис Dropbox с Вашим рабочим столом GNOME.

Ищите нас на http://www.dropbox.com/

%package -n dropbox
Summary: Dropbox command-line utility
Group: Networking/Other
License: GPL
Requires:wget >= 1.10.0

%description -n dropbox
The *dropbox* command provides a command line interface to the Dropbox.

%prep
%setup

%build
%configure \
--disable-dependency-tracking \
--enable-static=no \

%make_build

%install
%makeinstall_std

install -Dm0644 %SOURCE1 %buildroot%_desktopdir/dropbox.desktop
install -Dm755 %SOURCE2 %buildroot%_bindir/dropbox-wrapper

%files
%doc AUTHORS COPYING ChangeLog NEWS README
%_libdir/nautilus/extensions-*/libnautilus-dropbox.so
%_datadir/%name

%exclude %_libdir/nautilus/extensions-*/*.la

%files -n dropbox
%_bindir/dropbox*
%_iconsdir/hicolor/*/*/*
%_desktopdir/dropbox.desktop
%_man1dir/*.1*

%changelog
* Sat Oct 22 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.6.7-alt2.1
- Rebuild with Python-2.7

* Wed Jun 29 2011 Mikhail Efremov <sem@altlinux.org> 0.6.7-alt2
- Fix dropbox-wrapper script.

* Mon Jun 27 2011 Mikhail Efremov <sem@altlinux.org> 0.6.7-alt1
- Drop libnotify from BR.
- Fix license.
- Move dropbox utility to the subpackage (closes: #25805).
- Add dropbox-wrapper.
- Fix Url.
- sources: tar.bz2 -> tar.
- Updated to 0.6.7 (closes: #25167).

* Wed Apr 28 2010 Maxim Zhukov <mzhukov@altlinux.org> 0.6.2-alt1
- initial build
