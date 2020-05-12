Name: horizon
Version: 1.1.1
Release: alt1

Summary: Horizon is a free EDA package
License: GPL-3.0
Group: Engineering
Url: https://github.com/horizon-eda/horizon

Packager: Anton Midyukov <antohami@altlinux.org>

Source: %name-%version.tar

BuildRequires: gcc-c++ libgtkmm3-devel
BuildRequires: libsqlite3-devel
BuildRequires: libzip-devel
BuildRequires: libuuid-devel
BuildRequires: libepoxy-devel
BuildRequires: librsvg-devel
BuildRequires: libpodofo-devel
BuildRequires: libzeromq-cpp-devel
BuildRequires: libgit2-devel
BuildRequires: libcurl-devel
BuildRequires: libglm-devel
BuildRequires: boost-devel-headers
BuildRequires: OCE-devel

%description
%summary

%prep
%setup

%build
#configure
%make_build

%install
%makeinstall_std PREFIX=%prefix

%files
%_bindir/*
%_desktopdir/*
%_iconsdir/hicolor/*/apps/*
%_datadir/metainfo/*
%doc *.md

%changelog
* Tue May 12 2020 Anton Midyukov <antohami@altlinux.org> 1.1.1-alt1
- Initial build for Sisyphus
