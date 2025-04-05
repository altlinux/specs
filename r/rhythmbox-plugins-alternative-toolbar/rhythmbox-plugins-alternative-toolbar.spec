%def_enable snapshot

%define _name alternative-toolbar
%define ver_major 0.20
%define beta %nil
%define xdg_name org.gnome.rhythmbox.plugins.alternative_toolbar

Name: rhythmbox-plugins-%_name
Version: %ver_major.4
Release: alt3%beta

Summary: An alternative toolbar for Rhythmbox
Group: Sound
License: GPL-3.0-or-later
Url: https://github.com/fossfreedom/alternative-toolbar

Vcs: https://github.com/fossfreedom/alternative-toolbar.git

%if_disabled snapshot
Source: https://github.com/fossfreedom/alternative-toolbar/releases/download/v%version/%_name-%version%beta.tar.xz
%else
Source: %_name-%version%beta.tar
%endif

Requires: rhythmbox-plugins-python >= 3.4.7-alt2

%add_python3_path %_libdir/rhythmbox/plugins/%_name

BuildRequires(pre): rpm-build-python3 rpm-build-gir
BuildRequires: libgio-devel python3(gi)
BuildRequires: typelib(Peas) = 1.0
BuildRequires: typelib(GIRepository) = 2.0
BuildRequires: librhythmbox-gir
BuildRequires: intltool

%description
Replace the Rhythmbox large toolbar with a Client-Side Decorated or
Compact toolbar which can be hidden.

%prep
%setup -n %_name-%version%beta
# With pygobject >= 3.52.0, importing GIRepository-2.0 is no longer
# supported.

sed -i 's/^AC_PYTHON.*Peas/#&/' configure.ac

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
* Sat Apr 05 2025 Yuri N. Sedunov <aris@altlinux.org> 0.20.4-alt3
- fixed FTBFS with PyGobject-3.52

* Sun Mar 23 2025 Yuri N. Sedunov <aris@altlinux.org> 0.20.4-alt2
- updated to v0.20.4-2-ga03f1b3
- fixed BR

* Wed Nov 22 2023 Yuri N. Sedunov <aris@altlinux.org> 0.20.4-alt1
- 0.20.4

* Thu Sep 14 2023 Yuri N. Sedunov <aris@altlinux.org> 0.20.3-alt1.1
- explicitly required rhythmbox-plugins-python (ALT #47567)

* Sun Sep 10 2023 Yuri N. Sedunov <aris@altlinux.org> 0.20.3-alt1
- first build for Sisyphus (ALT #47510)

