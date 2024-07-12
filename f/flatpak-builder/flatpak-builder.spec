%def_disable snapshot

%define _localstatedir %_var
%define _libexecdir %_prefix/libexec
%define _userunitdir %_prefix/lib/systemd/user

%def_with system_debugedit
%def_enable docs
%{?_enable_docs:%def_enable docbook_docs}
%def_disable check
%def_enable installed_tests

Name: flatpak-builder
Version: 1.4.4
Release: alt1
Epoch:1

Summary: Tool to build flatpaks from source
Group: Development/Other
License: LGPL-2.1
Url: http://flatpak.org/

%if_disabled snapshot
Source: https://github.com/flatpak/flatpak-builder/releases/download/%version/%name-%version.tar.xz
%else
Vcs: https://github.com/flatpak/flatpak-builder.git
Source: %name-%version.tar
%endif

%define glib_ver 2.66
%define ostree_ver 2017.14
%define flatpak_ver 1.12.4
%define debugedit_ver 5.0
%define libdw_ver 0.172
%define appstream_ver 0.16.4-alt2

Requires(pre): flatpak >= %flatpak_ver
# /usr/bin/appstreamcli with compose support
Requires: /usr/bin/appstreamcli appstream-compose >= %appstream_ver
Requires: libostree >= %ostree_ver
Requires: /usr/bin/bzip2
Requires: /usr/bin/brz
Requires: /usr/bin/eu-strip
Requires: /usr/bin/git
Requires: /usr/bin/patch
Requires: /usr/bin/rofiles-fuse
Requires: /usr/bin/strip
Requires: /usr/bin/svn
Requires: /bin/tar
Requires: /usr/bin/unzip
Requires: /usr/bin/7z
%{?_with_system_debugedit:Requires: debugedit >= %debugedit_ver}

%{?_enable_installed_tests:%add_python3_path %_libexecdir/installed-tests/%name
%filter_from_requires /python2/d
%add_python_compile_exclude %_libexecdir/installed-tests/%name/testpython.py
}

BuildRequires(pre): rpm-macros-meson
BuildRequires: meson
BuildRequires: flatpak >= %flatpak_ver
BuildRequires: /usr/bin/appstreamcli appstream-compose >= %appstream_ver
BuildRequires: libcap-devel
BuildRequires: libdwarf-devel
BuildRequires: pkgconfig(glib-2.0) >= %glib_ver
BuildRequires: pkgconfig(gobject-introspection-1.0)
BuildRequires: pkgconfig(json-glib-1.0)
BuildRequires: pkgconfig(libelf)
BuildRequires: pkgconfig(libsoup-2.4)
BuildRequires: pkgconfig(ostree-1) >= %ostree_ver
BuildRequires: pkgconfig(yaml-0.1)
BuildRequires: pkgconfig(libxml-2.0)
BuildRequires: libcurl-devel
BuildRequires: xsltproc
%{?_with_system_debugedit:BuildRequires: /usr/bin/debugedit libdw-devel >= %libdw_ver}
%{?_enable_docs:BuildRequires: xsltproc docbook-dtds docbook-style-xsl}
%{?_enable_docbook_docs:BuildRequires: xmlto}
%{?_enable_installed_tests:BuildRequires: rpm-build-python3 rpm-build-python}

%description
Flatpak-builder is a tool for building flatpaks from sources.

See http://flatpak.org/ for more information.

%package tests
Summary: Tests for %name
Group: Development/Other
Requires: %name = %EVR

%description tests
This package provides tests programs that can be used to verify
the functionality of the installed Flatpak-builder.

%prep
%setup

%build
%meson \
    %{subst_enable_meson_feature docs docs} \
    %{subst_enable_meson_bool installed_tests installed_tests}
%nil
%meson_build

%install
%meson_install

%check
%__meson_test

%files
%_bindir/%name
%{?_without_system_debugedit:%_libexecdir/%name-debugedit}
%{?_enable_docs:%_man1dir/%name.1*
%_man5dir/flatpak-manifest.5*
%{?_enable_docbook_docs:%doc %_docdir/%name}}

%files tests
%_libexecdir/installed-tests/%name
%_datadir/installed-tests/%name

%changelog
* Fri Jul 12 2024 Yuri N. Sedunov <aris@altlinux.org> 1:1.4.4-alt1
- 1.4.4

* Wed Mar 27 2024 Yuri N. Sedunov <aris@altlinux.org> 1:1.4.3-alt1
- 1.4.3

* Fri Mar 01 2024 Yuri N. Sedunov <aris@altlinux.org> 1:1.4.2-alt1
- updated to 1.4.2-2-g8c036e00
- build with Meson
- new -tests subpackage

* Sun Feb 11 2024 Yuri N. Sedunov <aris@altlinux.org> 1:1.4.1-alt1
- 1.4.1

* Wed Dec 13 2023 Yuri N. Sedunov <aris@altlinux.org> 1:1.4.0-alt1
- 1.4.0

* Mon Nov 28 2022 Yuri N. Sedunov <aris@altlinux.org> 1:1.2.3-alt1
- 1.2.3

* Wed Jan 19 2022 Yuri N. Sedunov <aris@altlinux.org> 1:1.2.2-alt1
- 1.2.2 (fixed CVE-2022-21682)

* Sun Jan 09 2022 Yuri N. Sedunov <aris@altlinux.org> 1:1.2.1-alt1
- 1.2.1

* Mon Oct 11 2021 Yuri N. Sedunov <aris@altlinux.org> 1:1.2.0-alt1
- 1.2.0

* Sun Aug 15 2021 Yuri N. Sedunov <aris@altlinux.org> 1:1.0.14-alt1
- 1.0.14
- required brz instead of bzr

* Thu Feb 18 2021 Yuri N. Sedunov <aris@altlinux.org> 1:1.0.12-alt1
- 1.0.12

* Sun Jul 05 2020 Yuri N. Sedunov <aris@altlinux.org> 1:1.0.11-alt1
- 1.0.11

* Sat Apr 11 2020 Yuri N. Sedunov <aris@altlinux.org> 1:1.0.10-alt1.1
- improved "docs" knob

* Sat Mar 21 2020 Yuri N. Sedunov <aris@altlinux.org> 1:1.0.10-alt1
- 1.0.10

* Sun Nov 03 2019 Yuri N. Sedunov <aris@altlinux.org> 1:1.0.9-alt1
- 1.0.9

* Fri Jun 28 2019 Yuri N. Sedunov <aris@altlinux.org> 1:1.0.8-alt1
- 1.0.8

* Sat May 11 2019 Yuri N. Sedunov <aris@altlinux.org> 1:1.0.7-alt1
- 1.0.7

* Sun Apr 07 2019 Yuri N. Sedunov <aris@altlinux.org> 1:1.0.6-alt1
- 1.0.6

* Sun Feb 10 2019 Yuri N. Sedunov <aris@altlinux.org> 1:1.0.5-alt1
- 1.0.5

* Fri Feb 08 2019 Yuri N. Sedunov <aris@altlinux.org> 1:1.0.4-alt1
- 1.0.4

* Tue Jan 29 2019 Yuri N. Sedunov <aris@altlinux.org> 1:1.0.3-alt1
- 1.0.3

* Wed Jan 16 2019 Yuri N. Sedunov <aris@altlinux.org> 1:1.0.2-alt1
- 1.0.2

* Thu Nov 29 2018 Yuri N. Sedunov <aris@altlinux.org> 1:1.0.1-alt1
- 1.0.1

* Wed Aug 22 2018 Yuri N. Sedunov <aris@altlinux.org> 1:1.0.0-alt1
- 1.0.0

* Sun May 27 2018 Yuri N. Sedunov <aris@altlinux.org> 1:0.10.10-alt1
- first build for Sisyphus

