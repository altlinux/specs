%define _unpackaged_files_terminate_build 1

Name:    nchat
Version: 5.18.20
Release: alt1

Summary: Terminal-based Telegram / WhatsApp client for Linux and macOS
License: MIT AND GPL-3.0-only AND BSD-3-Clause AND BSL-1.0 AND MPL-2.0 AND Apache-2.0 AND ISC
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
BuildRequires: libxcb-devel libpng-devel

# The embedded auto-compose script invokes python3 and uses Python 3.10 syntax.
Requires: python3
# Wayland clipboard support invokes wl-copy and wl-paste at runtime.
Requires: wl-clipboard
# Links and attachments are opened with xdg-open by default.
Requires: xdg-utils

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
export CGO_CFLAGS="%optflags"
export CGO_CXXFLAGS="%optflags"

%cmake -G Ninja \
       -DHAS_DYNAMICLOAD=OFF \
       -DHAS_TELEGRAM=ON \
       -DHAS_WHATSAPP=ON \
       -DHAS_SIGNAL=OFF \
       -DHAS_SHARED_LIBS=ON \
       -DHAS_STATIC_EXTLIBS=OFF \
       -DCMAKE_GO_FLAGS="-trimpath;-tags=libsqlite3" \
       -DCMAKE_INSTALL_LIBDIR=%_lib/nchat \
       -DCMAKE_SKIP_INSTALL_RPATH=OFF \
       -DCMAKE_INSTALL_PREFIX=%_prefix \
       -DCMAKE_INSTALL_MANDIR=%_mandir \
       -DNCHAT_BUILD_ORIGIN=altlinux
%cmake_build

%install
%cmake_install

# Preserve the complete notices before replacing the upstream doc directory.
install -m 644 %buildroot%_defaultdocdir/%name/THIRD_PARTY_LICENSES THIRD_PARTY_LICENSES
# TDLib's bundled SQLCipher notice is missing from the upstream combined file.
install -m 644 lib/tgchat/ext/td/sqlite/sqlite/LICENSE LICENSE.SQLCipher
rm -rfv %buildroot%_defaultdocdir/%name

%files
%doc *.md LICENSE LICENSE.GPL-3.0 LICENSE.SQLCipher THIRD_PARTY_LICENSES
%doc doc/*.md themes
%dir %_libdir/%name
%_bindir/%name
%_libdir/%name/libtdclientshared.so
%_libdir/%name/libduchat.so
%_libdir/%name/libncutil.so
%_libdir/%name/libtgchat.so
%_libdir/%name/libwmchat.so
%_man1dir/%name.1.*

%changelog
* Mon Oct 26 2026 Nikita Shmatko <nash@altlinux.org> 5.18.20-alt1
- New version 5.18.20.
- Added the Python runtime dependency.
- Packaged the combined third-party notices and the SQLCipher license.
- Corrected the License tag.
- Enabled X11 clipboard and image support.
- Added wl-clipboard for Wayland clipboard support.
- Linked the WhatsApp component against the system SQLite.
- Packaged upstream feature documentation.
- Added xdg-utils for opening links and attachments.
- Moved shared libraries into the private nchat directory.
- Packaged example color themes.

* Mon Apr 20 2026 Nikita Shmatko <nash@altlinux.org> 5.14.44-alt1
- New version 5.14.44.

* Mon Jan 19 2026 Nikita Shmatko <nash@altlinux.org> 5.12.21-alt1
- New version 5.12.21.

* Mon Nov 24 2025 Nikita Shmatko <nash@altlinux.org> 5.11.32-alt1
- Initial build for Sisyphus.
