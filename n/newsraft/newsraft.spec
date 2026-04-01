%def_without check

Name:    newsraft
Version: 0.36
Release: alt1

Summary: Newsraft is a feed reader with ncurses user interface
License: ISC
Group:   Networking/News
Url:     https://newsraft.codeberg.page
Vcs:     https://codeberg.org/newsraft/newsraft.git

Source: %name-%version.tar

BuildRequires: pkgconfig(libcurl)
BuildRequires: pkgconfig(ncursesw)
BuildRequires: pkgconfig(expat)
BuildRequires: pkgconfig(gumbo)
BuildRequires: pkgconfig(sqlite3)

Requires: notify-send

%description
%summary.
It's greatly inspired by Newsboat and tries to be its lightweight counterpart.

%prep
%setup

%build
%make_build PREFIX=%_prefix

%install
%makeinstall_std PREFIX=%_prefix

%check
%make check

%files
%doc *.md
%_bindir/%name
%_iconsdir/hicolor/scalable/apps/%name.svg
%_datadir/%name
%_man1dir/%name.1.*

%changelog
* Wed Apr 01 2026 Sergey Gvozdetskiy <serjigva@altlinux.org> 0.36-alt1
- New version.

* Thu Jan 01 2026 Sergey Gvozdetskiy <serjigva@altlinux.org> 0.35-alt1
- New version.

* Wed Oct 08 2025 Sergey Gvozdetskiy <serjigva@altlinux.org> 0.34-alt1
- New version.

* Thu Jul 24 2025 Sergey Gvozdetskiy <serjigva@altlinux.org> 0.32-alt1
- New version.

* Mon Jun 16 2025 Sergey Gvozdetskiy <serjigva@altlinux.org> 0.31-alt1
- New version.

* Wed May 14 2025 Sergey Gvozdetskiy <serjigva@altlinux.org> 0.30-alt1
- Initial build for Sisyphus.
