%define _unpackaged_files_terminate_build 1

Name: facad
Version: 2.20.16
Release: alt1

Summary: A modern, colorful directory listing tool for the command line
License: MIT
Group: System/Libraries
Url: https://github.com/yellow-footed-honeyguide/facad
VCS: https://github.com/yellow-footed-honeyguide/facad.git

Source: %name-%version.tar

BuildRequires: meson

%description
facad is a modern, user-friendly command-line tool for
listing directory contents with colorized, visually intuitive output.
Written in pure C, it has zero external dependencies, making it fast,
lightweight, and easy to deploy. It is designed to be a practical
alternative to traditional ls, offering a clean layout and useful
features for both beginners and experienced users.

%prep
%setup

%build
%meson
%meson_build -v

%install
%meson_install

%check
%meson_test

%files
%doc LICENSE README.md
%_bindir/facad
%_man1dir/facad.1.xz

%changelog
* Wed Aug 13 2025 Martynenko Evgeniy <enimalojd@altlinux.org> 2.20.16-alt1
- Initial build for ALT.
