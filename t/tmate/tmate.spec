Name:    tmate
Version: 2.4.0
Release: alt2

Summary: Instant Terminal Sharing
License: BSD
Group:   Terminals
Url:     https://github.com/tmate-io/tmate

Source: %name-%version.tar
Patch: %name-2.4.0-alt-msgpack-c-name.patch

BuildRequires: libevent-devel
BuildRequires: libncurses-devel
BuildRequires: libmsgpack-c-devel
BuildRequires: libssh-devel

%description
%summary

%prep
%setup
%autopatch -p1

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
* Mon Apr 10 2023 Vladimir Didenko <cow@altlinux.org> 2.4.0-alt2
- Rebuild with msgpack-c 6.0.0

* Wed Jan 11 2023 Anton Vyatkin <toni@altlinux.org> 2.4.0-alt1
- Initial build for Sisyphus.
