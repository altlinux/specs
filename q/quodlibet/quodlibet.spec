%def_disable snapshot
%define gst_api_ver 1.0
%define rdn_name io.github.quodlibet.QuodLibet
%define rdn_name_ef io.github.quodlibet.ExFalso

Name: quodlibet
Version: 4.5.0
Release: alt1.1

Summary: audio library tagger, manager, and player for GTK+
Group: Sound
License: GPLv2
Url: https://github.com/%name/%name

%if_disabled snapshot
Source: %url/releases/download/release-%version/%name-%version.tar.gz
%else
Source: %name-%version.tar
%endif

BuildArch: noarch

Requires(pre): exfalso = %version-%release
Requires: python3 >= 3.7
# explicitly required gtk+3 and soup-2.4
Requires: typelib(Gtk) = 3.0
Requires: typelib(Soup) = 2.4
Requires: gvfs dbus dconf
Requires: python3-module-musicbrainzngs >= 0.6

# required GStreamer plugins
Requires: gst-plugins-base%gst_api_ver
Requires: gst-plugins-good%gst_api_ver
Requires: gst-plugins-bad%gst_api_ver
Requires: gst-plugins-ugly%gst_api_ver

# remove ubuntu and Mac-specific dependencies
%add_typelib_req_skiplist typelib(Unity) typelib(AppIndicator3) typelib(Dbusmenu)
%add_typelib_req_skiplist typelib(GtkosxApplication)

# abnormally detected python3 dep. See quodlibet/util/http.py
%add_python3_req_skip gi.repository.GObject

BuildRequires(pre): rpm-build-gir rpm-build-python3
BuildRequires: desktop-file-utils
BuildRequires: python3-devel python3-module-mutagen

%description
Quod Libet is a music management program. It provides several different
ways to view your audio library, as well as support for Internet radio
and audio feeds. It has extremely flexible metadata tag editing and
searching capabilities.

%package -n exfalso
Summary: audio tag editor for GTK+
Group: Sound

%add_python3_self_prov_path %buildroot%python3_sitelibdir_noarch/%name/packages/senf

%description -n exfalso
exfalso lets you display and edit any tags you want in the file. And it
lets you do this for all the file formats it supports -- Ogg Vorbis,
FLAC, MP3, Musepack, and MOD.

%prep
%setup

# fix appdata install path
subst "s|\('share', '\)appdata'|\1metainfo'|" gdist/appdata.py

%build
%python3_build

%install
%python3_install

%find_lang %name

%files
%_bindir/%name
# cli tagger
%_bindir/operon
%_datadir/dbus-1/services/net.sacredchao.QuodLibet.service
%_datadir/gnome-shell/search-providers/%rdn_name-search-provider.ini
%_iconsdir/hicolor/*/*/%{rdn_name}*.*
%_desktopdir/%rdn_name.desktop
%_datadir/metainfo/%rdn_name.appdata.xml
%_datadir/bash-completion/completions/%name
%_datadir/bash-completion/completions/operon
%_datadir/zsh/site-functions/_quodlibet
%_man1dir/%name.*
%_man1dir/operon.*
%doc NEWS* README*

%files -n exfalso -f %name.lang
%_bindir/exfalso
%_iconsdir/hicolor/*/*/%{rdn_name_ef}*.*
%_desktopdir/%rdn_name_ef.desktop
%_datadir/metainfo/%rdn_name_ef.appdata.xml
%_man1dir/exfalso.*
%python3_sitelibdir_noarch/%name
%python3_sitelibdir_noarch/%name-%version-py*

%changelog
* Sun Nov 13 2022 Daniel Zagaynov <kotopesutility@altlinux.org> 4.5.0-alt1.1
- NMU: used %%add_python3_self_prov_path macro to skip self-provides from dependencies.

* Wed Mar 30 2022 Yuri N. Sedunov <aris@altlinux.org> 4.5.0-alt1
- 4.5.0

* Tue Mar 02 2021 Yuri N. Sedunov <aris@altlinux.org> 4.4.0-alt1
- 4.4.0

* Mon Mar 16 2020 Yuri N. Sedunov <aris@altlinux.org> 4.3.0-alt1
- 4.3.0

* Tue Jan 01 2019 Yuri N. Sedunov <aris@altlinux.org> 4.2.1-alt1
- 4.2.1

* Sun Nov 04 2018 Yuri N. Sedunov <aris@altlinux.org> 4.2.0-alt1
- 4.2.0

* Mon Jun 04 2018 Yuri N. Sedunov <aris@altlinux.org> 4.1.0-alt1
- 4.1.0

* Sat Feb 17 2018 Yuri N. Sedunov <aris@altlinux.org> 4.0.2-alt1
- 4.0.2 (ported to Python3, GTK+3, GStreamer-1.0)

* Tue Oct 09 2012 Vladimir Lettiev <crux@altlinux.ru> 2.4.1-alt1
- New version 2.4.1

* Mon Apr 16 2012 Vitaly Kuznetsov <vitty@altlinux.ru> 2.2.1-alt1.qa1.1.1
- Rebuild to remove redundant libpython2.7 dependency

* Sat Oct 22 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 2.2.1-alt1.qa1.1
- Rebuild with Python-2.7

* Tue May 24 2011 Repocop Q. A. Robot <repocop@altlinux.org> 2.2.1-alt1.qa1
- NMU (by repocop). See http://www.altlinux.org/Tools/Repocop
- applied repocop fixes:
  * freedesktop-desktop-file-proposed-patch for exfalso

* Sun Mar 28 2010 Vladimir Lettiev <crux@altlinux.ru> 2.2.1-alt1
- New version 2.2.1

* Wed Mar 17 2010 Vladimir Lettiev <crux@altlinux.ru> 2.2-alt1
- initial build

