%define pear_name Net_SmartIRC

Name: pear-Net_SmartIRC
Version: 1.0.0
Release: alt3.qa1

Summary: Net_SmartIRC is a PHP class for communication with IRC networks

License: LGPL
Group: Development/Other
Url: http://pear.php.net/package/Net_SmartIRC

Packager: Vitaly Lipatov <lav@altlinux.ru>

Source: http://pear.php.net/get/Net_SmartIRC-%version.tar.bz2

BuildArchitectures: noarch

Requires: pear-core
BuildRequires: pear-core rpm-build-pear

%description
Net_SmartIRC is a PHP class for communication with IRC networks,
which conforms to the RFC 2812 (IRC protocol).
It's an API that handles all IRC protocol messages.
This class is designed for creating IRC bots, chats and show irc related
info on webpages.

Full featurelist of Net_SmartIRC
-------------------------------------
- full object oriented programmed
- every received IRC message is parsed into an ircdata object
  (it contains following info: from, nick, ident, host, channel, message,
type, rawmessage)
- actionhandler for the API
  on different types of messages (channel/notice/query/kick/join..)
callbacks can be registered
- messagehandler for the API
  class based messagehandling, using IRC reply codes
- time events
  callbacks to methods in intervals
- send/receive floodprotection
- detects and changes nickname on nickname collisions
- autoreconnect, if connection is lost
- autoretry for connecting to IRC servers
- debugging/logging system with log levels (destination can be file,
stdout, syslog or browserout)
- supports fsocks and PHP socket extension
- supports PHP 4.1.x to 4.3.2 (also PHP 5.0.0b1)
- sendbuffer with a queue that has 3 priority levels (high, medium, low)
plus a bypass level (critical)
- channel syncing (tracking of users/modes/topic etc in objects)
- user syncing (tracking the user in channels,
nick/ident/host/realname/server/hopcount in objects)
- when channel syncing is acticated the following functions are available:
  isJoined
  isOpped
  isVoiced
  isBanned
- on reconnect all joined channels will be rejoined, also when keys are
used
- own CTCP version reply can be set
- IRC commands:
  pass
  op
  deop
  voice
  devoice
  ban
  unban
  join
  part
  action
  message
  notice
  query
  ctcp
  mode
  topic
  nick
  invite
  list
  names
  kick
  who
  whois
  whowas
  quit

%prep
%setup -c

%build
%pear_build

%install
%pear_install_std

# It is the file in the package named Thumbs.db or Thumbs.db.gz, 
# which is normally a Windows image thumbnail database. 
# Such databases are generally useless in packages and were usually 
# accidentally included by copying complete directories from the source tarball.
find $RPM_BUILD_ROOT \( -name 'Thumbs.db' -o -name 'Thumbs.db.gz' \) -print -delete

%post
%register_pear_module

%preun
%unregister_pear_module

%files
%doc LICENSE CHANGELOG
%pear_dir/Net
%pear_docdir/%pear_name/
%pear_xmldir/%pear_name.xml

%changelog
* Wed Dec 02 2009 Repocop Q. A. Robot <repocop@altlinux.org> 1.0.0-alt3.qa1
- NMU (by repocop): the following fixes applied:
  * windows-thumbnail-database-in-package for pear-Net_SmartIRC
  * postclean-05-filetriggers for spec file

* Fri Jun 20 2008 Vitaly Lipatov <lav@altlinux.ru> 1.0.0-alt3
- autorebuild for correct requires(pre) (see bug #16086)

* Thu Jan 10 2008 Vitaly Lipatov <lav@altlinux.ru> 1.0.0-alt2
- update according to rpm-build-pear 0.3

* Sat Jan 05 2008 Vitaly Lipatov <lav@altlinux.ru> 1.0.0-alt1
- initial build for ALT Linux Sisyphus

