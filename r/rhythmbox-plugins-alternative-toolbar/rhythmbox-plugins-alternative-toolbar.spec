%def_disable snapshot

%define _name alternative-toolbar
%define ver_major 0.20
%define beta %nil
%define xdg_name org.gnome.rhythmbox.plugins.alternative_toolbar

Name: rhythmbox-plugins-%_name
Version: %ver_major.4
Release: alt1%beta

Summary: An alternative toolbar for Rhythmbox
Group: Sound
License: GPL-3.0
Url: https://github.com/fossfreedom/alternative-toolbar

%if_disabled snapshot
Source: https://github.com/fossfreedom/alternative-toolbar/releases/download/v%version/%_name-%version%beta.tar.xz
%else
Vcs: https://github.com/fossfreedom/alternative-toolbar.git
Source: %_name-%version%beta.tar
%endif

Requires: rhythmbox-plugins-python >= 3.4.7-alt2

%add_python3_path %_libdir/rhythmbox/plugins/%_name

BuildRequires(pre): rpm-build-python3 rpm-build-gir
BuildRequires: libgio-devel python3(gi)
BuildRequires: libpeas-gir librhythmbox-gir
BuildRequires: intltool

%description
Replace the Rhythmbox large toolbar with a Client-Side Decorated or
Compact toolbar which can be hidden.

%prep
%setup -n %_name-%version%beta

%build
%autoreconf
%configure
%make_build

%install
%makeinstall_std

%find_lang --with-gnome %_name

%files -f %_name.lang
%_libdir/rhythmbox/plugins/%_name/
%_datadir/rhythmbox/plugins/%_name/
%_datadir/glib-2.0/schemas/%xdg_name.gschema.xml
%_datadir/metainfo/*.appdata.xml
%doc ChangeLog README*

%changelog
* Wed Nov 22 2023 Yuri N. Sedunov <aris@altlinux.org> 0.20.4-alt1
- 0.20.4

* Thu Sep 14 2023 Yuri N. Sedunov <aris@altlinux.org> 0.20.3-alt1.1
- explicitly required rhythmbox-plugins-python (ALT #47567)

* Sun Sep 10 2023 Yuri N. Sedunov <aris@altlinux.org> 0.20.3-alt1
- first build for Sisyphus (ALT #47510)

