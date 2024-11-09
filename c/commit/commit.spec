%define APP_ID re.sonny.Commit
%def_enable check

Name: commit
Version: 4.2
Release: alt1

Summary: Commit message editor
License: GPL-3.0-or-later
Group: Graphical desktop/GNOME

Url: https://commit.sonny.re
Vcs: https://github.com/sonnyp/Commit
Source0: %name-%version.tar
Source1: troll.tar

Requires: typelib(Spelling)

BuildRequires(pre): rpm-macros-meson
BuildRequires: meson
BuildRequires: blueprint-compiler
BuildRequires: pkgconfig(gjs-1.0)
BuildRequires: typelib(GtkSource)
%if_enabled check
BuildRequires: %_bindir/desktop-file-validate
BuildRequires: %_bindir/appstreamcli
BuildRequires: %_bindir/glib-compile-schemas
%endif

%description
Commit is an editor that helps you write better Git and Mercurial commit
messages.

After installing make sure to launch the application and follow the
instructions.

Commit will pop up automatically when you make a commit in one of your projects.
To save your commit message, press the Commit button or the Ctrl+Return
shortcut. To abort and dismiss Commit, press the Abort button or the Escape key.

Features:

* Highlights overflow of the commit title
* Smart body wrapping
* Inserts a blank line between title and body
* Spell checking
* Comments are read-only and excluded from "Select All"
* Displays project folder and branch in window header
* Dark mode support
* Keyboard navigation and shortcuts
* Undo/Redo support
* Emoji picker
* Supports git commit, merge, tag --annotate, add --patch, rebase --interactive
* Supports Mercurial commit
* Auto capitalize the commit title
* Welcome window with settings and instructions
* Highlight syntax for Git, Mercurial and diffs

%prep
%setup -a1

%build
%meson
%meson_build

%install
%meson_install
# drop unknown languages, find known
rm -rf %buildroot%_datadir/locale/zh_Hans
%find_lang --with-gnome %APP_ID

%check
%__meson_test

%files -f %APP_ID.lang
%_bindir/%APP_ID
%_desktopdir/%APP_ID.desktop
%_datadir/glib-2.0/schemas/%APP_ID.gschema.xml
%_iconsdir/hicolor/*/apps/%{APP_ID}*.svg
%_datadir/metainfo/%APP_ID.metainfo.xml
%_datadir/%APP_ID

%changelog
* Tue Oct 22 2024 Oleg Shchavelev <oleg@altlinux.org> 4.2-alt1
- Initial build
