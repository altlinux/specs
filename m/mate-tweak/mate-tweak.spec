Name: mate-tweak
Version: 16.10.5
Release: alt2

Summary: Mate desktop configuration tool
License: GPLv2+
Group: Graphical desktop/MATE
Url: https://bitbucket.org/ubuntu-mate/mate-tweak

Packager: Anton Midyukov <antohami@altlinux.org>

Source: %name-%version.tar

BuildArch: noarch

BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-module-setuptools python3-module-distutils-extra intltool
Requires: libnotify-gir

%description
Configures some aspects of the MATE desktop not exposed via the
MATE Control Center applets.

Settings that can be handled via MATE Tweak:
 * Show/hide standard desktop icons.
 * Panel fine-tuning (icon visibility, in menus and on buttons,
   icon size, button labelling, contex menus, etc.).
 * Window manager fine-tuning.

%prep
%setup

# We don't provide xdg-su. Change it to use polkit.
%__subst "s/'pkexec', '/'xdg-su', '-c /g" %name
%__subst '/polkit/d' setup.py

%build
%python3_build

%install
%python3_install

%find_lang %name

%files -f %name.lang
%doc README.md
%_bindir/%name
%exclude %_bindir/marco*
%exclude %_bindir/metacity*
%_libexecdir/%name
%python3_sitelibdir/*egg-info
%exclude %_datadir/mate
%_datadir/%name
%_desktopdir/%name.desktop
%_man1dir/%name.1.*
%exclude %_man1dir/marco*
%exclude %_man1dir/metacity*

%changelog
* Sun Mar 12 2017 Anton Midyukov <antohami@altlinux.org> 16.10.5-alt2
- Added missing requires libnotify-gir.

* Sat Oct 15 2016 Anton Midyukov <antohami@altlinux.org> 16.10.5-alt1
- new version 16.10.5

* Sat Jun 04 2016 Anton Midyukov <antohami@altlinux.org> 3.5.10-alt1
- Initial build for ALT Linux Sisyphus.
