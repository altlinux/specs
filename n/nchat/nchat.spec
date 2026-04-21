%define _unpackaged_files_terminate_build 1 

Name:    nchat
Version: 5.14.44
Release: alt1

Summary: Terminal-based Telegram / WhatsApp client for Linux and macOS
License: MIT
Group:   Networking/Chat
Url:     https://github.com/d99kris/nchat

Source0: %name-%version.tar
Source1: vendor.tar

BuildRequires(pre): cmake ninja-build rpm-build-python3

BuildRequires: gcc-c++
BuildRequires: golang
BuildRequires: libssl-devel
BuildRequires: libncursesw-devel
BuildRequires: libsqlite3-devel
BuildRequires: libreadline-devel
BuildRequires: zlib-devel
BuildRequires: gperf
BuildRequires: libmagic-devel

%description
nchat is a terminal-based chat client for Linux and macOS
with support for Telegram and WhatsApp.

Features
  - Customizable color schemes and key bindings
  - Jump to unread chat
  - Message history cache with support for text export
  - Message read receipt
  - Receive / send markdown formatted messages
  - Reply / delete / edit / forward / send messages
  - List dialogs for selecting chats, contacts, emojis, files
  - Show user status (online, away, typing)
  - Toggle to view textized emojis vs. graphical
  - View / save media files (documents, photos, videos)
  - Send and display reactions

%prep
%setup

tar -xvf %SOURCE1 -C lib/wmchat/go

%build
%cmake -G Ninja \
       -DHAS_DYNAMICLOAD=OFF \
       -DCMAKE_INSTALL_LIBDIR=%_libdir \
       -DCMAKE_INSTALL_PREFIX=%_prefix \
       -DCMAKE_INSTALL_MANDIR=%_mandir
%cmake_build

%install
%cmake_install

%files
%doc *.md LICENSE
%_bindir/%name
%_libdir/libtdclientshared.so
%_libdir/libduchat.so
%_libdir/libncutil.so
%_libdir/libtgchat.so
%_libdir/libwmchat.so
%_usr/libexec/%name
%_man1dir/%name.1.*
%_datadir/%name

%changelog
* Mon Apr 20 2026 Nikita Shmatko <nash@altlinux.org> 5.14.44-alt1
- New version 5.14.44.

* Mon Jan 19 2026 Nikita Shmatko <nash@altlinux.org> 5.12.21-alt1
- New version 5.12.21.

* Mon Nov 24 2025 Nikita Shmatko <nash@altlinux.org> 5.11.32-alt1
- Initial build for Sisyphus.
