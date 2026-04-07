%define _unpackaged_files_terminate_build 1

Name: cclip
Version: 3.3.1
Release: alt1

Summary: Clipboard manager for wayland
License: GPL-3.0-or-later
Group: Graphical desktop/Other
Url: https://github.com/heather7283/cclip
VCS: https://github.com/heather7283/cclip

# Source-url: https://github.com/heather7283/%name/archive/refs/tags/%version.tar.gz
Source: %name-%version.tar
Patch1: %name-%version-alt.patch

BuildRequires(pre): rpm-macros-meson
BuildRequires: meson
BuildRequires: pkgconfig(sqlite3)
BuildRequires: pkgconfig(wayland-client)
BuildRequires: pkgconfig(libxxhash)

%description
cclip is a set of two tools:
* cclipd daemon runs in the background, monitors wayland clipboard for
  changes and writes clipboard contents to a database
* cclip is a CLI tools for interacting with the database created by
  cclipd.

%prep
%setup
%patch1 -p1

%build
%meson
%meson_build

%install
%meson_install

%files
%doc README.md
%_bindir/%name
%_bindir/%{name}d
%_man1dir/%name.1*
%_man1dir/%{name}d.1*

%changelog
* Tue Apr 07 2026 Dmitrii Fomchenkov <sirius@altlinux.org> 3.3.1-alt1
- initial build for ALT Linux
