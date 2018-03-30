Name: purple-plugin-matrix
Version: 0.0.0
Release: alt1.git.79.g49ea988
Summary: Matrix Plugin for Pidgin
License: GPL2
Group: Networking/Instant messaging
URL: https://github.com/matrix-org/purple-matrix

Source: %name-%version.tar
Source44: %name.watch

# Automatically added by buildreq on Fri Mar 30 2018
# optimized out: glib2-devel glibc-kernheaders-generic glibc-kernheaders-x86 libgio-devel libhttp-parser libjson-glib pkg-config python-base python-modules
BuildRequires: libhttp-parser-devel libjson-glib-devel libpurple-devel

%description
This project is a plugin for
[libpurple](https://developer.pidgin.im/wiki/WhatIsLibpurple) which adds the
ability to communicate with [matrix.org](http://matrix.org) homeservers to any
libpurple-based clients (such as [Pidgin](http://www.pidgin.im)).

# Status

This project is somewhat alpha, and only basic functionality has been
implemented. Sending and receiving simple text messages is supported, as is
joining rooms you are invited to by other users.

%prep
%setup

%build
%make_build

%install
%makeinstall_std

%files
%doc AUTHORS.rst CHANGES.md CONTRIBUTING.rst README.md
%_libdir/purple-2/libmatrix.so
%_pixmapsdir/pidgin/protocols/*/matrix.png

%changelog
* Fri Mar 30 2018 Ildar Mulyukov <ildar@altlinux.ru> 0.0.0-alt1.git.79.g49ea988
- initial build for ALT Linux Sisyphus
