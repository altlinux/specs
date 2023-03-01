%define _localstatedir %_var
%define _libexecdir %_prefix/libexec

%define xdg_name org.freedesktop.Flatpak
%define api_ver 1.0

%def_enable p2p
%def_enable docs
%def_enable gtk_doc
%def_disable selinux
%def_with system_dbus_proxy
%def_with systemd
# cannot run bwrap in hasher
%def_disable check

Name: flatpak
Version: 1.14.3
Release: alt1

Summary: Application deployment framework for desktop apps
Group: Development/Tools
License: LGPLv2.1+
Url: https://flatpak.org/

Packager: Vitaly Lipatov <lav@altlinux.ru>

Vcs: https://github.com/flatpak/flatpak.git
# Source-url: https://github.com/flatpak/flatpak/releases/download/%version/%name-%version.tar.xz
Source: %name-%version.tar
Patch1: flatpak-1.12.2-alt-flatpak.sh.patch

%define flatpak_group %name
%define flatpak_user %name

%define glib_ver 2.60
%define ostree_ver 2020.8
%define bwrap_ver 0.4.1
%define libarchive_ver 2.8.0
%define zstd_ver 0.8.1
%define malcontent_ver 0.4.0
%define curl_ver 7.29
%define appstream_ver 0.12

Requires: lib%name = %version-%release
Requires: %_bindir/fusermount
Requires: %_bindir/bwrap
Requires: bubblewrap >= %bwrap_ver
%{?_with_system_dbus_proxy:Requires: xdg-dbus-proxy}
Requires: ostree >= %ostree_ver
Requires: dconf
Requires: fuse

BuildRequires(pre): rpm-build-python3 rpm-build-systemd
BuildRequires: gtk-doc gobject-introspection-devel
BuildRequires: pkgconfig(gio-unix-2.0) >= %glib_ver
BuildRequires: pkgconfig(json-glib-1.0)
BuildRequires: pkgconfig(libarchive) >= %libarchive_ver
BuildRequires: pkgconfig(libcurl) >= %curl_ver
BuildRequires: pkgconfig(ostree-1) >= %ostree_ver
BuildRequires: pkgconfig(polkit-gobject-1)
BuildRequires: pkgconfig(libseccomp)
BuildRequires: pkgconfig(appstream) >= %appstream_ver
BuildRequires: pkgconfig(libxml-2.0)
BuildRequires: pkgconfig(gdk-pixbuf-2.0)
BuildRequires: pkgconfig(xau)
BuildRequires: pkgconfig(dbus-1)
BuildRequires: pkgconfig(dconf)
BuildRequires: libattr-devel
BuildRequires: libcap-devel
BuildRequires: libgpgme-devel
BuildRequires: libfuse-devel
BuildRequires: udev-rules
BuildRequires: %_bindir/bwrap
BuildRequires: bubblewrap >= %bwrap_ver
%{?_with_system_dbus_proxy:BuildRequires: xdg-dbus-proxy}
%{?_with_systemd:BuildRequires: pkgconfig(systemd)}
%{?_enable_selinux:BuildRequires: selinux-policy-devel}
BuildRequires: %_bindir/xsltproc
%{?_enable_docs:BuildRequires: %_bindir/xmlto docbook-dtds docbook-style-xsl}
BuildRequires: /proc
%{?_enable_check:BuildRequires: dbus %_bindir/fusermount %_bindir/ostree}
# since 1.10.0 (optional  dependencies)
BuildRequires: pkgconfig(libzstd) >= %zstd_ver
BuildRequires: pkgconfig(malcontent-0) >= %malcontent_ver
# variant-schema-compiler
BuildRequires: python3-module-pyparsing

%description
Flatpak is a system for building, distributing and running sandboxed desktop
applications on Linux. See https://wiki.gnome.org/Projects/SandboxedApps for
more information.

%package -n lib%name
Summary: Libraries for %name
Group: Development/Other
License: LGPLv2+
Requires: %_bindir/bwrap

%description -n lib%name
This package contains libflatpak.

%package -n lib%name-devel
Summary: Development files for %name
Group: Development/Other
License: LGPLv2+
Requires: lib%name = %version-%release

%description -n lib%name-devel
This package contains the pkg-config file and development headers for %name.

%package -n lib%name-devel-doc
Summary: Development package for lib%name
Group: Development/Documentation
BuildArch: noarch
Conflicts: lib%name < %version

%description -n lib%name-devel-doc
This package contains developer documentation for lib%name.

%prep
%setup
%patch1

%build
NOCONFIGURE=1 ./autogen.sh
%configure --with-priv-mode=none \
           --with-system-bubblewrap \
           %{?_enable_docs:--enable-docbook-docs} \
           %{?_enable_gtk_doc:--enable-gtk-doc} \
           %{?_enable_selinux:--enable-selinux-module} \
           %{subst_with systemd} \
           %if_with systemd
           --with-systemdsystemunitdir=%_unitdir \
           --with-systemduserunitdir=%_userunitdir \
           --with-sysusersdir=%_sysusersdir \
           --with-systemdsystemenvgendir=%_env_gen_dir \
           %endif
           %{?_with_system_dbus_proxy:DBUS_PROXY=%_bindir/xdg-dbus-proxy}
%nil
%make_build

%install
%makeinstall_std
# The system repo is not installed by the flatpak build system.
install -d %buildroot%_localstatedir/lib/flatpak

%find_lang %name

%pre
%_sbindir/groupadd -r -f %flatpak_group 2>/dev/null ||:
%_sbindir/useradd -r -N -g %flatpak_group -d / \
	-s /sbin/nologin -c "User for flatpak system helper" %flatpak_user 2>/dev/null ||:

%post
# Create an (empty) system-wide repo.
%_bindir/flatpak remote-list --system >/dev/null 2>&1 ||:

%check
%make check

%files -f %name.lang
%_bindir/%name
%_bindir/%name-bisect
%_bindir/%name-coredumpctl
%_datadir/bash-completion/completions/%name
%_datadir/fish/vendor_conf.d/%name.fish
%_datadir/dbus-1/services/%xdg_name.service
%_datadir/dbus-1/system-services/%xdg_name.SystemHelper.service
%_datadir/%name
%_datadir/polkit-1/actions/%xdg_name.policy
%_datadir/polkit-1/rules.d/%xdg_name.rules
%_libexecdir/%name-portal
%{?_without_system_dbus_proxy:%_libexecdir/%name-dbus-proxy}
%_libexecdir/%name-session-helper
%_libexecdir/%name-system-helper
%_libexecdir/%name-validate-icon
%_libexecdir/revokefs-fuse
%_libexecdir/%name-oci-authenticator
%dir %_localstatedir/lib/%name
%_man1dir/%{name}*.1*
%attr(0755,root,root) %_sysconfdir/profile.d/%name.sh
%_sysconfdir/dbus-1/system.d/%xdg_name.SystemHelper.conf
%_datadir/dbus-1/interfaces/org.freedesktop.portal.Flatpak.xml
%_datadir/dbus-1/services/org.freedesktop.portal.Flatpak.service
%_datadir/dbus-1/interfaces/org.freedesktop.Flatpak.Authenticator.xml
%_datadir/dbus-1/services/org.flatpak.Authenticator.Oci.service

%if_with systemd
%_unitdir/%name-system-helper.service
%_userunitdir/%name-portal.service
%_userunitdir/%name-session-helper.service
%_sysusersdir/%name.conf
%_env_gen_dir/60-%name-system-only
%_user_env_gen_dir/60-%name
%_userunitdir/%name-oci-authenticator.service
%endif

%_man5dir/*
%_datadir/fish/vendor_completions.d/%name.fish
%_datadir/zsh/site-functions/_%name

%doc NEWS README.md
%{?_enable_docs:%doc %_docdir/%name/}

%files -n lib%name
%_libdir/lib%name.so.*
%_typelibdir/Flatpak-%api_ver.typelib

%files -n lib%name-devel
%_includedir/%name/
%_libdir/lib%name.so
%_pkgconfigdir/%name.pc
%_datadir/dbus-1/interfaces/%xdg_name.xml
%_girdir/Flatpak-%api_ver.gir

%if_enabled gtk_doc
%files -n lib%name-devel-doc
%_datadir/gtk-doc/html/%name
%endif


%changelog
* Wed Mar 01 2023 Yuri N. Sedunov <aris@altlinux.org> 1.14.3-alt1
- 1.14.3

* Tue Feb 07 2023 Yuri N. Sedunov <aris@altlinux.org> 1.14.2-alt1
- 1.14.2

* Thu Nov 24 2022 Yuri N. Sedunov <aris@altlinux.org> 1.14.1-alt1
- 1.14.1

* Wed Aug 24 2022 Yuri N. Sedunov <aris@altlinux.org> 1.14.0-alt1
- 1.14.0

* Tue Mar 15 2022 Yuri N. Sedunov <aris@altlinux.org> 1.12.7-alt1
- 1.12.7

* Tue Mar 08 2022 Yuri N. Sedunov <aris@altlinux.org> 1.12.6-alt1
- 1.12.6

* Wed Jan 19 2022 Yuri N. Sedunov <aris@altlinux.org> 1.12.4-alt1
- 1.12.4 (fixed CVE-2022-21682, CVE-2021-43860)

* Sat Dec 11 2021 Yuri N. Sedunov <aris@altlinux.org> 1.12.2-alt2.1
- /etc/profile.d/flatpak.sh: fixed syntax
- supressed output from %%post

* Fri Dec 03 2021 Yuri N. Sedunov <aris@altlinux.org> 1.12.2-alt2
- /etc/profile.d/flatpak.sh: made executable (ALT #41495)

* Sun Oct 17 2021 Yuri N. Sedunov <aris@altlinux.org> 1.12.2-alt1
- 1.12.2

* Mon Oct 11 2021 Yuri N. Sedunov <aris@altlinux.org> 1.12.1-alt1
- 1.12.1

* Fri Sep 03 2021 Yuri N. Sedunov <aris@altlinux.org> 1.10.3-alt1
- 1.10.3

* Thu Aug 19 2021 Yuri N. Sedunov <aris@altlinux.org> 1.10.2-alt3
- BR: +python3-module-pyparsing

* Mon May 03 2021 Yuri N. Sedunov <aris@altlinux.org> 1.10.2-alt2
- BR: +rpm-build-python3

* Thu Mar 11 2021 Yuri N. Sedunov <aris@altlinux.org> 1.10.2-alt1
- 1.10.2

* Mon Jan 25 2021 Yuri N. Sedunov <aris@altlinux.org> 1.10.1-alt1
- 1.10.1

* Sun Jan 17 2021 Yuri N. Sedunov <aris@altlinux.org> 1.10.0-alt1
- 1.10.0

* Fri Jan 15 2021 Yuri N. Sedunov <aris@altlinux.org> 1.8.5-alt1
- 1.8.5

* Thu Nov 19 2020 Yuri N. Sedunov <aris@altlinux.org> 1.8.3-alt1
- 1.8.3

* Fri Sep 18 2020 Yuri N. Sedunov <aris@altlinux.org> 1.8.2-alt1
- 1.8.2

* Sat Jul 04 2020 Yuri N. Sedunov <aris@altlinux.org> 1.8.1-alt1
- 1.8.1

* Thu Jun 25 2020 Yuri N. Sedunov <aris@altlinux.org> 1.8.0-alt1
- 1.8.0

* Mon Jun 22 2020 Yuri N. Sedunov <aris@altlinux.org> 1.6.4-alt1
- 1.6.4

* Tue Mar 31 2020 Yuri N. Sedunov <aris@altlinux.org> 1.6.3-alt1
- 1.6.3

* Thu Feb 13 2020 Yuri N. Sedunov <aris@altlinux.org> 1.6.2-alt1
- 1.6.2

* Mon Jan 27 2020 Yuri N. Sedunov <aris@altlinux.org> 1.6.1-alt1
- 1.6.1

* Sat Dec 21 2019 Yuri N. Sedunov <aris@altlinux.org> 1.6.0-alt1
- 1.6.0

* Fri Dec 13 2019 Yuri N. Sedunov <aris@altlinux.org> 1.5.2-alt1
- 1.5.2

* Sun Nov 03 2019 Yuri N. Sedunov <aris@altlinux.org> 1.5.0-alt1
- 1.5.0

* Sat Sep 07 2019 Yuri N. Sedunov <aris@altlinux.org> 1.4.2-alt1.1
- rebuilt with system dbus-proxy

* Fri Jun 14 2019 Yuri N. Sedunov <aris@altlinux.org> 1.4.2-alt1
- 1.4.2
- %%pre: create flatpak group/user

* Wed May 29 2019 Yuri N. Sedunov <aris@altlinux.org> 1.4.0-alt1
- 1.4.0

* Sun Apr 07 2019 Yuri N. Sedunov <aris@altlinux.org> 1.2.4-alt1
- 1.2.4 (fixed CVE-2019-10063)

* Tue Feb 12 2019 Yuri N. Sedunov <aris@altlinux.org> 1.2.3-alt1
- 1.2.3

* Fri Feb 08 2019 Yuri N. Sedunov <aris@altlinux.org> 1.2.2-alt1
- 1.2.2

* Tue Jan 29 2019 Yuri N. Sedunov <aris@altlinux.org> 1.2.0-alt1
- 1.2.0

* Thu Nov 29 2018 Yuri N. Sedunov <aris@altlinux.org> 1.0.6-alt1
- 1.0.6

* Sun Sep 16 2018 Yuri N. Sedunov <aris@altlinux.org> 1.0.2-alt1
- 1.0.2

* Mon Sep 03 2018 Yuri N. Sedunov <aris@altlinux.org> 1.0.1-alt1
- 1.0.1

* Wed Aug 22 2018 Yuri N. Sedunov <aris@altlinux.org> 1.0.0-alt1
- 1.0.0

* Fri Jun 08 2018 Yuri N. Sedunov <aris@altlinux.org> 0.11.8-alt1
- 0.11.8

* Sun May 27 2018 Yuri N. Sedunov <aris@altlinux.org> 0.11.7-alt2
- removed -builder subpackage (since 0.9.9 flatpak-builder was split out into separate project)
- updated buildreqs
- removed obsolete metadata-xml.patch

* Mon May 21 2018 Vitaly Lipatov <lav@altlinux.ru> 0.11.7-alt1
- new version 0.11.7 (with rpmrb script)

* Tue Mar 20 2018 Vitaly Lipatov <lav@altlinux.ru> 0.11.3-alt1
- new version 0.11.3 (with rpmrb script)

* Sat Feb 24 2018 Vitaly Lipatov <lav@altlinux.ru> 0.10.4-alt1
- new version 0.10.4 (with rpmrb script)

* Wed Feb 07 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 0.10.3-alt1
- Updated to upstream version 0.10.3.

* Tue Dec 26 2017 Vitaly Lipatov <lav@altlinux.ru> 0.10.2.1-alt2
- move dbus-1/interfaces to libflatpak-devel

* Sun Dec 24 2017 Vitaly Lipatov <lav@altlinux.ru> 0.10.2.1-alt1
- new version 0.10.2.1 (with rpmrb script)

* Sun Dec 24 2017 Vitaly Lipatov <lav@altlinux.ru> 0.10.2-alt1
- new version 0.10.2 (with rpmrb script)

* Sat Nov 25 2017 Vitaly Lipatov <lav@altlinux.ru> 0.10.1-alt1
- new version 0.10.1 (with rpmrb script)

* Mon Nov 06 2017 Vitaly Lipatov <lav@altlinux.ru> 0.10.0-alt1
- new version 0.10.0 (with rpmrb script)

* Mon Oct 16 2017 Vitaly Lipatov <lav@altlinux.ru> 0.9.99-alt1
- new version 0.9.99 (with rpmrb script)

* Sun Oct 08 2017 Vitaly Lipatov <lav@altlinux.ru> 0.9.98.2-alt1
- new version 0.9.98.2 (with rpmrb script)

* Sat Oct 07 2017 Vitaly Lipatov <lav@altlinux.ru> 0.9.11-alt1
- new version 0.9.11 (with rpmrb script)

* Sat Jul 22 2017 Vitaly Lipatov <lav@altlinux.ru> 0.9.7-alt1
- new version (0.9.7) with rpmgs script

* Tue May 09 2017 Vitaly Lipatov <lav@altlinux.ru> 0.9.3-alt1
- new version 0.9.3 (with rpmrb script)

* Wed Mar 15 2017 Vitaly Lipatov <lav@altlinux.ru> 0.9.1-alt1
- new version 0.9.1 (with rpmrb script)

* Sun Sep 25 2016 Vitaly Lipatov <lav@altlinux.ru> 0.6.11-alt1
- new version 0.6.11 (with rpmrb script)

* Sun Sep 25 2016 Vitaly Lipatov <lav@altlinux.ru> 0.6.8-alt1
- initial build for ALT Linux Sisyphus

* Mon Aug 01 2016 David King <amigadave@amigadave.com> - 0.6.8-1
- Update to 0.6.8 (#1361823)

* Thu Jul 21 2016 David King <amigadave@amigadave.com> - 0.6.7-2
- Use system bubblewrap

* Fri Jul 01 2016 David King <amigadave@amigadave.com> - 0.6.7-1
- Update to 0.6.7

* Thu Jun 23 2016 David King <amigadave@amigadave.com> - 0.6.6-1
- Update to 0.6.6

* Fri Jun 10 2016 David King <amigadave@amigadave.com> - 0.6.5-1
- Update to 0.6.5

* Wed Jun 01 2016 David King <amigadave@amigadave.com> - 0.6.4-1
- Update to 0.6.4

* Tue May 31 2016 David King <amigadave@amigadave.com> - 0.6.3-1
- Update to 0.6.3
- Move bwrap to main package

* Tue May 24 2016 David King <amigadave@amigadave.com> - 0.6.2-1
- Rename from xdg-app to flatpak (#1337434)
