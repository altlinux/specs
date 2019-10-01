Name: purple-plugin-matrix
Version: 0.0.0
Release: alt2.git.133.g4494ba2
Summary: Matrix Plugin for Pidgin
License: GPL2
Group: Networking/Instant messaging
URL: https://github.com/matrix-org/purple-matrix

Source: %name-%version.tar
Source44: %name.watch

# Automatically added by buildreq on Tue Oct 01 2019
# optimized out: glib2-devel glibc-kernheaders-generic glibc-kernheaders-x86 libgio-devel libgpg-error-devel libhttp-parser libjson-glib pkg-config python-base python-modules sh4
BuildRequires: libgcrypt-devel libhttp-parser-devel libjson-glib-devel libolm-devel libpurple-devel libsqlite3-devel

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
# quick fix for libpurple using deprecated things
subst 's/.Werror//' Makefile.common

%build
%make_build \
	#MATRIX_NO_E2E=1

%install
%makeinstall_std

%files
%doc AUTHORS.rst CHANGES.md CONTRIBUTING.rst README.md
%_libdir/purple-2/libmatrix.so
%_pixmapsdir/pidgin/protocols/*/matrix.png

%changelog
* Tue Oct 01 2019 Ildar Mulyukov <ildar@altlinux.ru> 0.0.0-alt2.git.133.g4494ba2
- quick fix for libpurple using deprecated things

* Thu Jan 17 2019 Ildar Mulyukov <ildar@altlinux.ru> 0.0.0-alt1.git.122.gf26edd5
- new snapshot

* Fri Mar 30 2018 Ildar Mulyukov <ildar@altlinux.ru> 0.0.0-alt1.git.79.g49ea988
- initial build for ALT Linux Sisyphus
