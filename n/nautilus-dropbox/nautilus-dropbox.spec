Name: nautilus-dropbox
Version: 2022.12.05
Release: alt1

Summary: Dropbox integration for Nautilus
Summary(ru_RU.UTF-8): Интеграция Dropbox с Nautilus

License: GPL-3.0-or-later and CC-BY-ND-3.0
Group: Graphical desktop/GNOME
Url: http://www.dropbox.com/

Source: https://www.dropbox.com/download?dl=packages/%name-%version.tar

BuildRequires(pre): rpm-build-python3
BuildRequires: glib2-devel >= 2.14.0
BuildRequires: libgtk4-devel
BuildRequires: libnautilus-devel >= 43.1
BuildRequires: pkg-config
BuildRequires: python3-module-docutils
BuildRequires: python3-module-pygobject3

Requires: nautilus
Requires: dropbox = %EVR
Requires: python3-module-gpg

%define _unpackaged_files_terminate_build 1

%description
Nautilus Dropbox is an extension that integrates the Dropbox web service with
your GNOME Desktop.

Check us out at http://www.dropbox.com/

%description -l ru_RU.UTF-8
Nautilus Dropbox - это расширения интегрирующее веб-сервис Dropbox с Вашим
рабочим столом GNOME.

Ищите нас на http://www.dropbox.com/

%package -n dropbox
Summary: Dropbox command-line utility
Group: Networking/Other
License: GPL-3.0-or-later
Requires: wget >= 1.10.0

%description -n dropbox
The *dropbox* command provides a command line interface to the Dropbox.

%prep
%setup

%build
%autoreconf
%configure \
    --disable-dependency-tracking \
    --enable-static=no \

%make_build

%install
%makeinstall_std

%files
%doc AUTHORS COPYING ChangeLog
%_libdir/nautilus/extensions-*/libnautilus-dropbox.so
%_datadir/%name/

%exclude %_libdir/nautilus/extensions-*/*.la

%files -n dropbox
%_bindir/dropbox*
%_iconsdir/hicolor/*/*/*
%_desktopdir/dropbox.desktop
%_man1dir/*.1*

%changelog
* Mon Jan 09 2023 Mikhail Efremov <sem@altlinux.org> 2022.12.05-alt1
- Dropped obsoleted patches.
- Updated to 2022.12.05.

* Tue Dec 06 2022 Mikhail Efremov <sem@altlinux.org> 2020.03.04-alt2
- Fixed license tag.
- Fixed build with nautilus-43.x.

* Fri May 07 2021 Andrey Cherepanov <cas@altlinux.org> 2020.03.04-alt1
- New version.
- Fix License tag according to SPDX.

* Thu Sep 19 2019 Mikhail Efremov <sem@altlinux.org> 2019.02.14-alt1
- Updated to 2019.02.14 (closes: #37198).

* Fri Nov 13 2015 Mikhail Efremov <sem@altlinux.org> 2015.10.28-alt1
- Updated to 2015.10.28.

* Wed Apr 08 2015 Mikhail Efremov <sem@altlinux.org> 2015.02.12-alt1
- Updated to 2015.02.12.

* Fri Nov 14 2014 Mikhail Efremov <sem@altlinux.org> 1.6.2-alt1
- Drop dropbox-wrapper.
- Updated to 1.6.2 (closes: #30278).

* Sat Apr 12 2014 Vitaly Lipatov <lav@altlinux.ru> 1.4.0-alt1
- new version 1.4.0 (with rpmrb script)

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
