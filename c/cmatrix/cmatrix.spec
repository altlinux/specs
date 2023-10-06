%define _unpackaged_files_terminate_build 1

Name: cmatrix
Version: 2.0
Release: alt2

Summary: CMatrix is based on the screensaver from The Matrix website

License: GPLv3
Group: Other

Url: https://github.com/abishekvashok/cmatrix

Source0: %name-%version.tar

Patch1: 0001-update-actual-paths.patch

BuildRequires: libncurses-devel
BuildRequires: glibc-core
BuildRequires: kbd
BuildRequires: kbd-data
BuildRequires: suite3270

%description
It shows text flying in and out in a terminal like as seen
in "The Matrix" movie. It can scroll lines all at the same
rate or asynchronously and at a user-defined speed.

%prep
%setup
%patch1 -p1

%build
%autoreconf
%configure
%make_build

%install
%makeinstall_std

%check
%make_build check

%files
%doc AUTHORS ChangeLog NEWS README
%_bindir/*
%_man1dir/%name.1*

%changelog
* Mon Jun 26 2023 Vasiliy Kovalev <kovalev@altlinux.org> 2.0-alt2
- Modify spec and update actual paths in configure.ac

* Fri Apr 22 2022 Vasiliy Kovalev <kovalev@altlinux.org> 2.0-alt1
- Update to 2.0

* Thu Apr 21 2022 Vasiliy Kovalev <kovalev@altlinux.org> 1.2-alt1
- Initial build for Sisyphus
