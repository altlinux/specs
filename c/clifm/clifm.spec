%define _unpackaged_files_terminate_build 1

Name: clifm
Version: 1.24
Release: alt2

Summary: Shell-like, command line terminal file manager
License: GPL-2.0
Group: File tools
Url: https://github.com/leo-arch/clifm

Source: %name-%version.tar

Patch: %name-%version-%release.patch

BuildRequires(pre): rpm-macros-cmake
BuildRequires: cmake
BuildRequires: gcc-c++
BuildRequires: libreadline-devel
BuildRequires: libcap-devel
BuildRequires: libmagic-devel
BuildRequires: libacl-devel
BuildRequires: rpm-build-python3

%description
CliFM is a file manager for the Unix terminal.

Unlike most file managers out there, based on the TUI, CliFM is entirely
based on command-line. It is also ultra-lightweight, lightning fast,
extensible, and written in C.

CliFM has the following features: Entirely command-line based (no TUI),
Fast and lightweight, Shell commands, Autocd, auto-open, auto-ls,
Profiles, Bookmarks, Files search and selection (REGEX),
Bulk rename/remove/link, Tab completion (with FZF/FZY/smenu modes),
Syntax highlighting, Auto-suggestions (Gemini), Auto-commands, Aliases,
Workspaces, Disk usage analyzer, File names cleaner (Bleach), Icons
support, Theming, Modern and customizable prompt, Customizable color
codes for file types and extensions, Directory jumper (Kangaroo),
Freedesktop compliant trash system, Resource opener (Lira),
Plugins (including files preview), Git status support, Files lister,
Files picker, Archiving support, Remote file systems management,
Secure commands/environment, Stealth mode, Light mode,
Virtual directories.

%prep
%setup
%patch -p1

%build
%cmake
%cmake_build

%install
%cmake_install

%files
%doc CHANGELOG LICENSE README.md
%_bindir/*
%_man1dir/*
%_desktopdir/*.desktop
%_datadir/bash-completion/completions/%name
%dir %_datadir/%name
%_datadir/%name/*
%_datadir/fish/vendor_completions.d/%name.fish
%_datadir/zsh/site-functions/_%{name}
%_iconsdir/hicolor/scalable/apps/%{name}.svg

%changelog
* Sat Mar 15 2025 Nikolay Strelkov <snk@altlinux.org> 1.24-alt2
- Use python3 executable instead of python

* Mon Mar 03 2025 Nikolay Strelkov <snk@altlinux.org> 1.24-alt1
- Initial build for Sisyphus
