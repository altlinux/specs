%define _libexecdir /usr/libexec

Name:    catatonit
Version: 0.2.0
Release: alt1

Summary: A signal-forwarding process manager for containers
License: GPL-2.0-or-later
Group:   System/Configuration/Boot and Init
Url:     https://github.com/openSUSE/catatonit

Source: %name-%version.tar

BuildRequires: glibc-devel-static

%description
Catatonit is a /sbin/init program for use within containers. It
forwards (almost) all signals to the spawned child, tears down
the container when the spawned child exits, and otherwise
cleans up other exited processes (zombies).

This is a reimplementation of other container init programs (such as
"tini" or "dumb-init"), but uses modern Linux facilities (such as
signalfd(2)) and has no additional features.

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
%_bindir/%name

%changelog
* Tue Dec 05 2023 Ivan Pepelyaev <fl0pp5@altlinux.org> 0.2.0-alt1
- Initial build for ALT (based on Alenka Glukhovskaya <alenka@altlinux.org> repository)

