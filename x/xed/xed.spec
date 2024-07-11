%define _libexecdir %_prefix/libexec

%define api_ver 3.0

Name: xed
Version: 3.6.4
Release: alt1

Summary: xed is a small and lightweight text editor.
License: GPL-2.0-or-later
Group: Editors
Url: https://github.com/linuxmint/xed

# Source-url: https://github.com/linuxmint/xed/archive/refs/tags/%version.tar.gz
Source: %name-%version.tar

%define pkglibdir %_libdir/%name
%define pkgdatadir %_datadir/%name
%define pluginsdir %_libdir/%name/plugins

Requires: %name-data = %version-%release
Requires: dconf gnome-icon-theme gvfs zenity
%{?_enable_zeitgeist:Requires: zeitgeist}
Requires: xapps-icons

Obsoletes: xed-data < %EVR
Provides: xed-data = %EVR
Provides: typelib(Xed)

BuildPreReq: rpm-build-gnome
BuildPreReq: rpm-build-python3

BuildPreReq: intltool
BuildRequires: yelp-tools xmllint itstool
BuildPreReq: gtk-doc
BuildPreReq: desktop-file-utils
BuildPreReq: libenchant-devel
BuildPreReq: iso-codes-devel
BuildPreReq: libgio-devel
BuildPreReq: libgtk+3-devel
BuildPreReq: libgtksourceview4-devel
BuildRequires: meson
BuildRequires: libattr-devel gnome-common libxml2-devel libsoup-devel gsettings-desktop-schemas-devel
BuildRequires: libSM-devel
BuildRequires: libpeas-devel
BuildRequires: python3-dev
BuildRequires: libgtk+3-gir-devel
BuildRequires: libgtksourceview4-gir-devel
BuildRequires: libgspell-devel
BuildRequires: libxapps-devel

%add_python3_path %pluginsdir

%description
xed is a small and lightweight text editor.

xed supports most standard editing features, plus several not found in your
average text editor (plugins being the most notable of these).

%package devel
Group: Development/C
Summary: Libraries needed to develop plugins for xed
Requires: %name = %version-%release
Requires: libgtksourceview-devel

%description devel
Libraries needed to develop plugins for xed.

%prep
%setup

%build
%meson
%meson_build

%install
%meson_install

# additional mime types
desktop-file-install --dir %buildroot%_desktopdir \
	--add-mime-type=text/css \
	--add-mime-type=text/csv \
	--add-mime-type=text/english \
	--add-mime-type=text/plain \
	--add-mime-type=text/tab-separated-values \
	--add-mime-type=text/x-adasrc \
	--add-mime-type=text/x-bibtex \
	--add-mime-type=text/x-c++ \
	--add-mime-type=text/x-chdr \
	--add-mime-type=text/x-c++hdr \
	--add-mime-type=text/x-csharp \
	--add-mime-type=text/x-csrc \
	--add-mime-type=text/x-c++src \
	--add-mime-type=text/x-dsrc \
	--add-mime-type=text/x-fortran \
	--add-mime-type=text/x-gle \
	--add-mime-type=text/x-java \
	--add-mime-type=text/x-javascript \
	--add-mime-type=text/x-log \
	--add-mime-type=text/x-makefile \
	--add-mime-type=text/x-objcsrc \
	--add-mime-type=text/x-pascal \
	--add-mime-type=text/x-patch \
	--add-mime-type=text/x-perl \
	--add-mime-type=text/x-php \
	--add-mime-type=text/x-python \
	--add-mime-type=text/x-sql \
	--add-mime-type=text/x-sh \
	--add-mime-type=text/x-tcl \
	--add-mime-type=text/x-tex \
	%buildroot%_desktopdir/%name.desktop

rm -f %buildroot%_libdir/%name/*.la

%find_lang --with-gnome %name

%files -f %name.lang
%_bindir/*
%pkglibdir
%pkgdatadir/
%_desktopdir/%name.desktop
%_mandir/man?/*
%config %_datadir/glib-2.0/schemas/*
%_datadir/metainfo/%name.appdata.xml
%_datadir/dbus-1/services/org.x.editor.*service
%doc README.md AUTHORS

# All xed python modules are intended for internal usage only
%filter_from_provides /python3/d

%files devel
%_includedir/*
%_pkgconfigdir/*

%changelog
* Thu Jul 11 2024 Anton Midyukov <antohami@altlinux.org> 3.6.4-alt1
- new version (3.6.4) with rpmgs script

* Fri Jun 21 2024 Anton Midyukov <antohami@altlinux.org> 3.6.3-alt1
- new version (3.6.3) with rpmgs script

* Tue Jun 18 2024 Anton Midyukov <antohami@altlinux.org> 3.6.2-alt1
- new version (3.6.2) with rpmgs script

* Sat Jun 08 2024 Anton Midyukov <antohami@altlinux.org> 3.6.1-alt1
- new version (3.6.1) with rpmgs script

* Fri Jan 05 2024 Anton Midyukov <antohami@altlinux.org> 3.4.5-alt1
- new version (3.4.5) with rpmgs script

* Mon Dec 04 2023 Anton Midyukov <antohami@altlinux.org> 3.4.4-alt1
- 3.4.4
- Remove data subpackage
- Fix License

* Fri Dec 01 2023 Anton Midyukov <antohami@altlinux.org> 3.4.3-alt2
- Rebuild with cinnamon 6.0

* Mon Jul 10 2023 Vladimir Didenko <cow@altlinux.org> 3.4.3-alt1
- New version

* Fri Jun 9 2023 Vladimir Didenko <cow@altlinux.org> 3.4.1-alt1
- New version

* Mon Nov 21 2022 Vladimir Didenko <cow@altlinux.org> 3.2.8-alt1
- New version

* Tue Aug 2 2022 Vladimir Didenko <cow@altlinux.org> 3.2.7-alt1
- New version

* Thu Jul 21 2022 Vladimir Didenko <cow@altlinux.org> 3.2.6-alt1
- New version

* Wed Jul 13 2022 Vladimir Didenko <cow@altlinux.org> 3.2.4-alt1
- New version

* Tue Jun 21 2022 Vladimir Didenko <cow@altlinux.org> 3.2.3-alt1
- New version

* Thu Jan 13 2022 Vladimir Didenko <cow@altlinux.org> 3.2.2-alt1
- New version

* Wed Dec 15 2021 Vladimir Didenko <cow@altlinux.org> 3.2.1-alt1
- New version

* Tue Nov 30 2021 Vladimir Didenko <cow@altlinux.org> 3.2.0-alt1
- New version

* Tue Jun 29 2021 Vladimir Didenko <cow@altlinux.org> 3.0.2-alt1
- New version

* Thu Jun 17 2021 Vladimir Didenko <cow@altlinux.org> 3.0.1-alt1
- New version

* Tue Jun 1 2021 Vladimir Didenko <cow@altlinux.org> 3.0.0-alt1
- New version

* Tue Jan 12 2021 Vladimir Didenko <cow@altlinux.org> 2.8.4-alt1
- New version

* Tue Dec 22 2020 Vladimir Didenko <cow@altlinux.org> 2.8.3-alt1
- New version (2.8.3-1-g3940e04)

* Fri Dec 11 2020 Vladimir Didenko <cow@altlinux.org> 2.8.2-alt1
- New version

* Thu Dec 3 2020 Vladimir Didenko <cow@altlinux.org> 2.8.0-alt1
- New version

* Fri Jul 3 2020 Vladimir Didenko <cow@altlinux.org> 2.6.2-alt1
- New version

* Mon Jun 1 2020 Vladimir Didenko <cow@altlinux.org> 2.6.0-alt2
- add xapps-icons to dependencies

* Thu May 14 2020 Vladimir Didenko <cow@altlinux.org> 2.6.0-alt1
- New version

* Mon Dec 23 2019 Vladimir Didenko <cow@altlinux.org> 2.4.2-alt1
- New version (2.4.2-5-gc19752e)

* Thu Nov 28 2019 Vladimir Didenko <cow@altlinux.org> 2.4.1-alt1
- New version

* Mon Nov 25 2019 Vladimir Didenko <cow@altlinux.org> 2.4.0-alt1
- New version

* Wed Jul 31 2019 Vladimir Didenko <cow@altlinux.org> 2.2.3-alt1
- New version

* Wed Jul 10 2019 Vladimir Didenko <cow@altlinux.org> 2.2.1-alt1
- New version
- Cleaner fix for Python3 build

* Fri Jul 5 2019 Vladimir Didenko <cow@altlinux.org> 2.2.0-alt2
- fix build for Python 3

* Mon Jul 1 2019 Vladimir Didenko <cow@altlinux.org> 2.2.0-alt1
- New version

* Tue Dec 25 2018 Vladimir Didenko <cow@altlinux.org> 2.0.2-alt1
- New version

* Wed Dec 5 2018 Vladimir Didenko <cow@altlinux.org> 2.0.1-alt1
- New version

* Wed Nov 21 2018 Vladimir Didenko <cow@altlinux.org> 2.0.0-alt1
- New version

* Mon Jul 23 2018 Vladimir Didenko <cow@altlinux.org> 1.8.3-alt1
- New version

* Wed Jun 13 2018 Vladimir Didenko <cow@altlinux.org> 1.8.1-alt1
- New version (1.8.1-2-g8c6125e)

* Mon May 7 2018 Vladimir Didenko <cow@altlinux.org> 1.8.0-alt1
- New version

* Thu Nov 23 2017 Vladimir Didenko <cow@altlinux.org> 1.6.3-alt1
- New version

* Thu Aug 24 2017 Vladimir Didenko <cow@altlinux.org> 1.4.6-alt1
- New version

* Tue Jul 4 2017 Vladimir Didenko <cow@altlinux.org> 1.4.5-alt1
- New version

* Mon Jun 5 2017 Vladimir Didenko <cow@altlinux.org> 1.4.2-alt1
- 1.4.2-2-gc306c1b

* Thu May 18 2017 Vladimir Didenko <cow@altlinux.org> 1.4.1-alt1
- New version

* Wed Dec 14 2016 Vladimir Didenko <cow@altlinux.org> 1.2.2-alt1
- New version

* Sun Nov 13 2016 Vladimir Didenko <cow@altlinux.org> 1.2.1-alt1
- New version

* Tue May 26 2016 Vladimir Didenko <cow@altlinux.org> 1.0.5-alt1
- New version

* Thu Feb 25 2016 Vladimir Didenko <cow@altlinux.org> 1.0.3-alt1
- Initial build for Sisyphus
