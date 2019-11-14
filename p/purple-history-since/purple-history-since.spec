Name: purple-history-since
Version: 1.0
Release: alt1

Summary: Avoid duplicated chat history on some XMPP servers

License: GPL-2.0-or-later
Group: Networking/Instant messaging
Url: https://github.com/kgraefe/purple-history-since/

# repacked https://github.com/kgraefe/purple-history-since/releases/ %name-%version.tar.gz
Source: %name-%version.tar
Source1: %name.watch
Patch1: 0001-ALT-plugindir.patch

BuildRequires: autoconf intltool glib2-devel libpurple-devel

%description
Some servers, mainly on the XMPP protocol, send a fixed part of the chat
history to each client, regardless of whether or not the client has already
received those messages. This plugin for libpurple clients, such as Pidgin or
finch, sets the `history_since` property of a chat when a message is received.
When connecting to the server the next time, the XMPP protocol plugin uses this
property to tell the server to exclude messages before that timestamp from the
history.

Purple History Since is not limited to XMPP, but it is the only libpurple
protocol plugin known to use the `history_since` property.


%prep
%setup
%autopatch -p2

%build
%autoreconf
%configure \
	--disable-static \
	#
%make_build

%install
%makeinstall_std
%find_lang %name

find %buildroot -name '*\.la' -delete

%files -f %name.lang
%doc CHANGES.md COPYING
%_libdir/purple-2/purple_history_since.so

%changelog
* Thu Nov 14 2019 Vladimir D. Seleznev <vseleznv@altlinux.org> 1.0-alt1
- Initial build for ALT Sisyphus.
