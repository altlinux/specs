%define _unpackaged_files_terminate_build 1

Name: numix-gtk-theme
Version: 2.6.7
Release: alt1

Summary: Modern flat theme from the Numix project
License: GPLv3
Group: Graphical desktop/GNOME
Url: https://github.com/numixproject/numix-gtk-theme

Source: %name-%version.tar

BuildRequires: sassc
BuildRequires: libgio
BuildRequires: libgdk-pixbuf-devel

Requires: libgtk-engine-murrine
Requires: numix-icon-theme

BuildArch: noarch

%description
Numix is a modern flat theme with a combination of light and dark
elements for any GTK-based desktop environment, including GNOME Shell,
Unity, MATE, Cinnamon and more.

%prep
%setup

%build
%make_build

%install
%makeinstall_std

%files
%doc CHANGES CREDITS LICENSE README.md
%dir %_datadir/themes/Numix
%_datadir/themes/Numix/*

%changelog
* Sun Feb 09 2025 Nikolay Strelkov <snk@altlinux.org> 2.6.7-alt1
- Initial build for Sisyphus
