%define _unpackaged_files_terminate_build 1

Name: privacybrowser
Version: 0.9
Release: alt1

Summary: web browser that respects your privacy
License: GPL-3.0-or-later
Group: Networking/WWW
Url: https://www.stoutner.com/privacy-browser-pc/
Vcs: https://salsa.debian.org/soren/privacybrowser.git

Source: %name-%version.tar

BuildRequires(pre): rpm-macros-cmake
BuildRequires(pre): rpm-build-kf6

BuildRequires: cmake
BuildRequires: gcc-c++
BuildRequires: extra-cmake-modules
BuildRequires: qt6-base-devel
BuildRequires: pkgconfig(Qt6WebEngineCore)
BuildRequires: pkgconfig(cups)
BuildRequires: qt6-sql-interbase
BuildRequires: qt6-sql-mysql
BuildRequires: qt6-sql-odbc
BuildRequires: qt6-sql-postgresql
BuildRequires: kf6-kcompletion-devel
BuildRequires: kf6-kconfigwidgets-devel
BuildRequires: kf6-kcoreaddons-devel
BuildRequires: kf6-kcrash-devel
BuildRequires: kf6-kdbusaddons-devel
BuildRequires: kf6-kdoctools-devel
BuildRequires: kf6-ki18n-devel
BuildRequires: kf6-knotifications-devel
BuildRequires: kf6-kio-devel

ExcludeArch: i586 riscv64

%description
Privacy Browser is a web browser based on Qt WebEngine with a focus on
privacy and security. Features like JavaScript and cookies are disabled
by default but are easy to automatically enable on-the-fly or by domain.

%package docs
Summary: Documentation for Privacy Browser
Group: Documentation
BuildArch: noarch

%description docs
Privacy Browser is a web browser based on Qt WebEngine with a focus on
privacy and security. Features like JavaScript and cookies are disabled
by default but are easy to automatically enable on-the-fly or by domain.

%prep
%setup

%build
%cmake
%cmake_build

%install
%cmake_install

%files
%doc changelog COPYING
%_bindir/privacybrowser
%_desktopdir/com.stoutner.privacybrowser.desktop
%_iconsdir/hicolor/*/apps/privacybrowser.png
%_iconsdir/hicolor/scalable/apps/privacybrowser.svg
%_iconsdir/hicolor/symbolic/apps/privacybrowser-symbolic.svg
%_datadir/knotifications6/privacybrowser.notifyrc
%_datadir/kxmlgui5/privacybrowser/browserwindowui.rc
%_datadir/metainfo/com.stoutner.privacybrowser.metainfo.xml

%files docs
%dir %_datadir/doc/HTML/en/privacybrowser
%_datadir/doc/HTML/en/privacybrowser/cookies.png
%_datadir/doc/HTML/en/privacybrowser/index.cache.bz2
%_datadir/doc/HTML/en/privacybrowser/index.docbook
%_datadir/doc/HTML/en/privacybrowser/javascript.png
%_datadir/doc/HTML/en/privacybrowser/loading.gif
%_datadir/doc/HTML/en/privacybrowser/privacybrowser-monochrome.png
%_datadir/doc/HTML/en/privacybrowser/privacybrowser-window.png
%_datadir/doc/HTML/en/privacybrowser/privacybrowser.png

%changelog
* Sun Apr 26 2026 Nikolay Strelkov <snk@altlinux.org> 0.9-alt1
- New version 0.9.

* Fri Jan 30 2026 Nikolay Strelkov <snk@altlinux.org> 0.8-alt2
- Exclude riscv64 arch as not buildable.

* Sat Nov 01 2025 Nikolay Strelkov <snk@altlinux.org> 0.8-alt1
- Initial build for Sisyphus
