%def_enable snapshot
%define ver_major 6.1
%define _name terminal
%define xdg_name org.pantheon.%_name
%define rdn_name io.elementary.%_name

Name: pantheon-terminal
Version: %ver_major.1
Release: alt1

Summary: Pantheon Terminal
Group: Terminals
License: LGPL-3.0
Url: https://github.com/elementary/terminal

%if_disabled snapshot
Source: %url/archive/%version/%_name-%version.tar.gz
%else
Vcs: https://github.com/elementary/terminal.git
Source: %_name-%version.tar
%endif

%define granite_ver 6.1.0
%define handy_ver 1.0
%define vala_ver 0.40
%define vte_ver 0.59

Requires: elementary-icon-theme
Provides: %rdn_name = %version-%release

BuildRequires(pre): rpm-macros-meson
BuildRequires: meson appstream desktop-file-utils
BuildRequires: libgranite-devel >= %granite_ver libnotify-devel
BuildRequires: libvte3-devel >= %vte_ver libpcre2-devel libgee0.8-devel
BuildRequires: vala-tools >= %vala_ver libgranite-vala
BuildRequires: pkgconfig(libhandy-1) >= %handy_ver

%description
Pantheon Terminal (referred to simply as "Terminal" when installed) is a super
lightweight, beautiful, and simple terminal.

It's designed to be setup with sane defaults and little to no configuration.
It's just a terminal, nothing more, nothing less.

%package vala
Summary: Vala language bindings for the %name
Group: Development/Other
BuildArch: noarch
#Requires: %name-devel = %version-%release

%description vala
This package provides Vala language bindings for the %name.


%prep
%setup -n %_name-%version

%build
%meson
%meson_build

%install
%meson_install

%find_lang %rdn_name

%files -f %rdn_name.lang
%doc README*
%_bindir/%rdn_name
%_datadir/%rdn_name/
%_desktopdir/%rdn_name.desktop
%_desktopdir/open-%name-here.desktop
%_datadir/glib-2.0/schemas/%rdn_name.gschema.xml
%_datadir/metainfo/%rdn_name.appdata.xml

%exclude %_datadir/fish/vendor_conf.d/pantheon_terminal_process_completion_notifications.fish

%if 0
%files vala
%_vapidir/*
%endif

%changelog
* Sun Nov 13 2022 Yuri N. Sedunov <aris@altlinux.org> 6.1.1-alt1
- updated to 6.1.1-7-g6f08bbdf

* Sat Aug 13 2022 Yuri N. Sedunov <aris@altlinux.org> 6.1.0-alt1
- updated to 6.1.0-4-ga08b1ed4

* Fri May 20 2022 Yuri N. Sedunov <aris@altlinux.org> 6.0.2-alt1
- updated to 6.0.2-1-g9bc0079c

* Sun Mar 27 2022 Yuri N. Sedunov <aris@altlinux.org> 6.0.1-alt2
- updated to 6.0.1-14-gc923bd3b (fixed build with meson >= 0.61)

* Wed Dec 15 2021 Yuri N. Sedunov <aris@altlinux.org> 6.0.1-alt1
- 6.0.1

* Mon Jul 19 2021 Yuri N. Sedunov <aris@altlinux.org> 6.0.0-alt1
- updated to 6.0.0-15-ge274f5c9

* Sun Mar 28 2021 Yuri N. Sedunov <aris@altlinux.org> 5.5.2-alt2
- updated to 5.5.2-169-g7946306b

* Sat Apr 04 2020 Yuri N. Sedunov <aris@altlinux.org> 5.5.2-alt1
- updated to 5.5.2-3-g87e33614

* Tue Mar 24 2020 Yuri N. Sedunov <aris@altlinux.org> 5.5.1-alt2
- updated to 5.5.1-70-g373e3741

* Tue Jan 21 2020 Yuri N. Sedunov <aris@altlinux.org> 5.5.1-alt1
- updated to 5.5.1-16-gf4b09f8e

* Wed Jan 08 2020 Yuri N. Sedunov <aris@altlinux.org> 5.5.0-alt1
- updated to 5.5.0-22-g75c6e722

* Tue Nov 26 2019 Yuri N. Sedunov <aris@altlinux.org> 5.4.0-alt1
- 5.4.0
- updated License tag

* Mon Jul 22 2019 Yuri N. Sedunov <aris@altlinux.org> 5.3.6-alt1
- 5.3.6

* Mon Jun 10 2019 Yuri N. Sedunov <aris@altlinux.org> 5.3.5-alt1
- 5.3.5

* Wed Apr 03 2019 Yuri N. Sedunov <aris@altlinux.org> 5.3.4-alt1
- updated to 5.3.4-8-gb4a611c

* Thu Jan 03 2019 Yuri N. Sedunov <aris@altlinux.org> 5.3.3-alt1
- 5.3.3

* Sat Jul 28 2018 Yuri N. Sedunov <aris@altlinux.org> 0.5.1-alt1
- 0.5.1

* Mon Jun 25 2018 Yuri N. Sedunov <aris@altlinux.org> 0.5-alt2
- rebuilt against libgranite.so.5

* Thu Jun 21 2018 Yuri N. Sedunov <aris@altlinux.org> 0.5-alt1
- 0.5

* Sat Jan 06 2018 Yuri N. Sedunov <aris@altlinux.org> 0.4.3-alt2
- rebuilt against libgranite.so.4

* Mon Jul 31 2017 Yuri N. Sedunov <aris@altlinux.org> 0.4.3-alt1
- 0.4.3

* Thu May 18 2017 Yuri N. Sedunov <aris@altlinux.org> 0.4.2-alt1
- 0.4.2

* Wed May 10 2017 Yuri N. Sedunov <aris@altlinux.org> 0.4.1-alt1
- 0.4.1

* Sat Mar 25 2017 Yuri N. Sedunov <aris@altlinux.org> 0.4.0.4-alt1
- 0.4.0.4

* Sun Jan 08 2017 Yuri N. Sedunov <aris@altlinux.org> 0.4.0.3-alt1
- 0.4.0.3

* Thu Sep 29 2016 Yuri N. Sedunov <aris@altlinux.org> 0.4-alt1
- 0.4

* Wed Sep 09 2015 Yuri N. Sedunov <aris@altlinux.org> 0.3.1.3-alt1
- 0.3.1.3

* Tue Oct 08 2013 Igor Zubkov <icesik@altlinux.org> 0.2.4.1-alt1
- 0.2.3 -> 0.2.4.1

* Mon Aug 12 2013 Igor Zubkov <icesik@altlinux.org> 0.2.3-alt1
- build for Sisyphus

