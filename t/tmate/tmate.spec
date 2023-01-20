Name:    tmate
Version: 2.4.0
Release: alt1

Summary: Instant Terminal Sharing
License: BSD
Group:   Terminals
Url:     https://github.com/tmate-io/tmate

Source: %name-%version.tar

BuildRequires: libevent-devel
BuildRequires: libncurses-devel
BuildRequires: libmsgpack-devel
BuildRequires: libssh-devel

%description
%summary

%prep
%setup

%build
%autoreconf
%configure
%make_build

%install
%makeinstall_std

%files
%doc README.md COPYING
%_bindir/*
%_man1dir/*

%changelog
* Wed Jan 11 2023 Anton Vyatkin <toni@altlinux.org> 2.4.0-alt1
- Initial build for Sisyphus.
