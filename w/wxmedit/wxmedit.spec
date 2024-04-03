%define _unpackaged_files_terminate_build 1

Name: wxmedit
Version: 3.2
Release: alt1

Summary: A cross-platform Text/Hex Editor
License: GPL-3.0-only
Group: Editors
Url: https://wxmedit.github.io
VCS: https://github.com/wxMEdit/wxMEdit

Source: %name-%version.tar

BuildRequires: boost-devel-headers
BuildRequires: gcc-c++
BuildRequires: libcurl-devel
BuildRequires: libgtk+3-devel
BuildRequires: libwxBase3.2-devel

%description
wxMEdit is a fork of MadEdit with bug fixes and improvements.

%prep
%setup

%build
%configure
%make_build

%install
%makeinstall_std

%find_lang %name

%files -f %name.lang
%_bindir/%name
%_desktopdir/%name.desktop
%_defaultdocdir/%name
%_datadir/%name
%_pixmapsdir/%{name}*
%_iconsdir/hicolor/*/*/%name.*

%changelog
* Mon Apr 01 2024 Dmitrii Fomchenkov <sirius@altlinux.org> 3.2-alt1
- Initial build for ALT Linux
