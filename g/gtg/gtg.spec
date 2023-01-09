%define pymodule GTG

Name: gtg
Version: 0.6
Release: alt3

Summary: A personal tasks and TODO list items organizer.
License: GPL-3.0-or-later
Group: Office
Url: https://github.com/getting-things-gnome/gtg

Source: %name-%version.tar
BuildArch: noarch

Patch: %name-%version-%release.patch

BuildRequires(pre): rpm-build-python3
BuildRequires: libgtk+3-devel
BuildRequires: meson
BuildRequires: python3-dev
BuildRequires: libgtk+3-gir-devel
BuildRequires: itstool

%description
Getting Things GNOME! (GTG) is a personal tasks and TODO list items
organizer for the GNOME desktop environment inspired by the Getting
Things Done (GTD) methodology. GTG is designed with flexibility,
adaptability, and ease of use in mind so it can be used as more than
just GTD software. GTG is intended to help you track everything you
need to do and need to know, from small tasks to large projects.

%prep
%setup
%patch -p1

%build
%meson
%meson_build

%install
%meson_install

%filter_from_requires /python3[(]gi.repository.GObject[)]/d
# Export plugin uses "pdflatex", "pdftk" and "pdfjam" tools that
# generate dependency on texlive package that is overkill for
# simple todo application. If user really needs this functionality
# then he could install this dependencies on his own. Note that
# absence of this tools is not critical - code checks if it is
# installed and suggests user to install if he wants to enable export
# plugin.
%filter_from_requires /texlive/d
%filter_from_requires /texlive-collection-basic/d
%filter_from_requires /pdftk/d

%find_lang --with-gnome %name

%files -f %name.lang
%_bindir/*
%_desktopdir/*
%python3_sitelibdir/GTG
# We don't have Hamster in our repos yet
%exclude %python3_sitelibdir/GTG/plugins/hamster*
%_man1dir/*
%_datadir/metainfo/*
%_datadir/dbus-1/services/org.gnome.GTG.service
%_iconsdir/hicolor/scalable/apps/*.svg

%changelog
* Mon Jan 9 2023 Vladimir Didenko <cow@altlinux.org> 0.6-alt3
- Don't pack Hamster plugin (closes: #44809)

* Mon Mar 28 2022 Vladimir Didenko <cow@altlinux.org> 0.6-alt2
- Fix build requirements

* Thu Mar 3 2022 Vladimir Didenko <cow@altlinux.org> 0.6-alt1
- New version

* Thu Dec 16 2021 Vladimir Didenko <cow@altlinux.org> 0.5-alt3
- Fix build with the new version of meson

* Sat May 01 2021 Igor Vlasenko <viy@altlinux.org> 0.5-alt2
- NMU: removed depandency on pdftk

* Tue Apr 06 2021 Vladimir Didenko <cow@altlinux.org> 0.5-alt1
- New version

* Thu Jul 09 2020 Vladimir Didenko <cow@altlinux.org> 0.4.0-alt1
- Initial build for Sisyphus
