%define nm_version 1.1.90
%define git_date %nil
#define git_date .git20151024

%define _unpackaged_files_terminate_build 1

%def_with gtk4

Name: NetworkManager-ssh
Version: 1.2.13
Release: alt1%git_date
License: GPLv2+
Group: System/Configuration/Networking
Summary: NetworkManager VPN plugin for SSH
Url: https://github.com/danfruehauf/NetworkManager-ssh
Vcs: https://github.com/danfruehauf/NetworkManager-ssh.git
Source0: %name-%version.tar
Patch: %name-%version-%release.patch

BuildRequires: intltool
BuildRequires: libnm-devel >= %nm_version
BuildRequires: libnma-devel
BuildRequires: libgtk+3-devel
BuildRequires: libsecret-devel
%{?_with_gtk4:BuildRequires: libgtk4-devel libnma-gtk4-devel}

Requires: NetworkManager-daemon   >= %nm_version
Requires: openssh-clients

%description
This package contains software for integrating VPN capabilities with
the OpenSSH server with NetworkManager.

%package gtk-common
Summary: Common part of %name GTK support
Group: Graphical desktop/GNOME
Requires: %name = %version-%release

%description gtk-common
This package contains common part for %name GTK support.

%package gtk3
Summary: Files for GTK3 applications to use %name
Group: Graphical desktop/GNOME
Requires: %name-gtk-common = %version-%release

Obsoletes: %name-gnome < 0.9.1-alt2
Provides: %name-gnome = %version-%release

Obsoletes: %name-gtk < 1.2.13-alt1
Provides: %name-gtk = %version-%release

%description gtk3
This package contains files for GTK3 applications to use %name.

%if_with gtk4
%package gtk4
Summary: Files for GTK4 applications to use %name
Group: Graphical desktop/GNOME
Requires: %name-gtk-common = %version-%release

Obsoletes: %name-gnome < 0.9.1-alt2
Provides: %name-gnome = %version-%release

%description gtk4
This package contains files for GTK4 applications to use %name.
%endif

%prep
%setup
%patch -p1

%build
%autoreconf
%configure \
	--disable-static \
	--libexecdir=%_libexecdir/NetworkManager \
	--localstatedir=%_var \
	--without-libnm-glib \
	%{subst_with gtk4} \
	--disable-silent-rules \
	--enable-more-warnings=error
%make_build

%install
%makeinstall_std
%find_lang %name

%check
make check

%files
%doc AUTHORS README README.md
%_libexecdir/NetworkManager/nm-ssh-service
%_libdir/NetworkManager/libnm-vpn-plugin-ssh.so
%config %_sysconfdir/dbus-1/system.d/nm-ssh-service.conf
%config %_libexecdir/NetworkManager/VPN/nm-ssh-service.name

%files gtk-common -f %name.lang
%_libexecdir/NetworkManager/nm-ssh-auth-dialog
%_datadir/metainfo/*.xml

%files gtk3
%_libdir/NetworkManager/libnm-gtk3-vpn-plugin-ssh-editor.so

%if_with gtk4
%files gtk4
%_libdir/NetworkManager/libnm-gtk4-vpn-plugin-ssh-editor.so
%endif

%exclude %_libdir/NetworkManager/*.la

%changelog
* Thu May 16 2024 Mikhail Efremov <sem@altlinux.org> 1.2.13-alt1
- Added gtk4 subpackage.
- Droped support for libnm-glib build.
- Fixed AppStream metadata path.
- Updated to 1.2.13.

* Tue Oct 10 2023 Mikhail Efremov <sem@altlinux.org> 1.2.12-alt2
- Require openssh-clients instead of openssh.
- Updated Vcs tag.

* Thu Apr 22 2021 Mikhail Efremov <sem@altlinux.org> 1.2.12-alt1
- Added Vcs tag.
- Updated to 1.2.12.

* Mon Feb 17 2020 Mikhail Efremov <sem@altlinux.org> 1.2.11-alt1
- Get rid of rpm-build-licenses.
- Updated to 1.2.11.

* Wed May 15 2019 Mikhail Efremov <sem@altlinux.org> 1.2.10-alt1
- Updated to 1.2.10.

* Tue Mar 19 2019 Mikhail Efremov <sem@altlinux.org> 1.2.9-alt1
- Updated to 1.2.9.

* Fri Nov 09 2018 Mikhail Efremov <sem@altlinux.org> 1.2.8-alt1
- Updated to 1.2.8.

* Tue Sep 18 2018 Mikhail Efremov <sem@altlinux.org> 1.2.7-alt3
- Temporary don't treat warnings as errors.

* Wed Aug 01 2018 Mikhail Efremov <sem@altlinux.org> 1.2.7-alt2
- Disable libnm-glib-* support.
- Fix build without libnm-glib-*.

* Tue Dec 19 2017 Mikhail Efremov <sem@altlinux.org> 1.2.7-alt1
- Updated to 1.2.7.

* Tue Jul 11 2017 Mikhail Efremov <sem@altlinux.org> 1.2.6-alt1
- Disable silent rules.
- Fix from upstream:
  + Update README.md.
- Updated to 1.2.6.

* Wed Oct 05 2016 Mikhail Efremov <sem@altlinux.org> 1.2.1-alt1
- Updated to 1.2.1.

* Thu Apr 28 2016 Mikhail Efremov <sem@altlinux.org> 1.2.0-alt1
- Updated to 1.2.0.

* Thu Jan 21 2016 Mikhail Efremov <sem@altlinux.org> 1.1.0-alt1.git20151024
- Upstream git snapshot (master branch).

* Fri Jul 17 2015 Mikhail Efremov <sem@altlinux.org> 0.9.4-alt1
- Updated BR.
- Updated to 0.9.4.

* Tue Jun 24 2014 Mikhail Efremov <sem@altlinux.org> 0.9.3-alt1
- Update requires: NetworkManager -> NetworkManager-daemon.
- Update BR: Use libnm-glib-vpn-devel.
- Updated to 0.9.3.

* Wed Apr 02 2014 Mikhail Efremov <sem@altlinux.org> 0.9.1-alt4
- Temporary don't treat warrnings as errors.
- Rebuild with NetworkManager-applet-gtk-0.9.9.

* Thu Oct 03 2013 Mikhail Efremov <sem@altlinux.org> 0.9.1-alt3
- Fix build: Avoid deprecation warnings.

* Mon Sep 16 2013 Mikhail Efremov <sem@altlinux.org> 0.9.1-alt2
- Don't reload DBUS configuration during install.
- Rename 'gnome' subpackage to 'gtk'.

* Mon Jul 22 2013 Mikhail Efremov <sem@altlinux.org> 0.9.1-alt1
- Updated from upstream git (e5e66fd96141).
- Updated to 0.9.1.

* Tue Apr 16 2013 Mikhail Efremov <sem@altlinux.org> 0.0.3-alt1.git20130405
- Initial build.

