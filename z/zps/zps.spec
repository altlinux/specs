%define _unpackaged_files_terminate_build 1

Name: zps
Version: 2.0.0
Release: alt1
Summary: A small utility for listing and reaping zombie processes on GNU/Linux.
License: GPL-3.0
Group: Terminals
Url: https://github.ink/orhun/zps

Source: %name-%version.tar

BuildRequires: desktop-file-utils
BuildRequires: glibc >= 2.38

%description
zps lists the running processes with theirs stats and indicates/reaps the zombie processes.

%prep
%setup

%build
%make_build CFLAGS="%optflags" 

%install
%makeinstall_std TARGET=%buildroot
mkdir -p %buildroot%_man1dir
install -D -m644 man/%name.1 %buildroot%_man1dir/%name.1
desktop-file-install --dir %buildroot%_datadir/applications/ .application/%name.desktop

%files
%doc README.md
%_bindir/%name
%_man1dir/*
%_datadir/applications/%name.desktop

%changelog
* Wed Feb 28 2024 Pavel Shilov <zerospirit@altlinux.org> 2.0.0-alt1
- Initial build for Sisyphus
