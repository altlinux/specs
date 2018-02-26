Name: ovz-web-panel
Version: 2.0
Release: alt7
BuildArch: noarch

Group: Networking/WWW
Summary: Web Panel for controlling OpenVZ server
Url: http://code.google.com/p/ovz-web-panel
License: GNU GPL v2
Packager: Denis Baranov <baraka@altlinux.org>

Requires: ruby1.8 ruby1.8-rubygems libruby1.8 sqlite3-ruby1.8

Source: http://ovz-web-panel.googlecode.com/files/%name-2.0.tar
Source1: ovz-daemon

Patch1: fix-path-in-daemon-ruby.patch
Patch2: cant-check-version-ruby.patch

#Fixme: do templates in ruby
AutoReq: yes, noruby

%description
OpenVZ Web Panel is a GUI web-based frontend for controlling of the
hardware and virtual servers with the OpenVZ virtualization technology.

%package -n ovz-daemon
Summary: Daemon for Web Panel OpenVZ
Group: Networking/WWW
License: GNU GPL v2
Requires: ruby rubygems

%description -n ovz-daemon
Hardware daemon on the server with OpenVZ for controll from
OpenVZ Web Panel.

%package -n ruby1.8-ovz-daemon
Summary: Daemon for Web Panel OpenVZ
Group: Networking/WWW
License: GNU GPL v2
Requires: ruby1.8 ruby1.8-rubygems

%description -n ruby1.8-ovz-daemon
Hardware daemon on the server with OpenVZ for controll from
OpenVZ Web Panel.

%prep
%setup
%patch1 -p2
%patch2 -p2
%__subst 's|/opt/%name|%_datadir/%name|g' script/owp
%__subst 's|/opt/%name|%_datadir/%name|g' config/owp.conf.sample

%build
%install
mkdir -p %buildroot%_datadir/%name
cp -a * %buildroot%_datadir/%name/
mkdir -p %buildroot%_initrddir/
install script/owp %buildroot%_initrddir/
cp -a config/owp.conf.sample %buildroot%_sysconfdir/owp.conf

mkdir -p %buildroot%_datadir/ovz-daemon
cp -a utils/hw-daemon/hw-daemon.rb %buildroot%_datadir/ovz-daemon/

mkdir -p %buildroot%_sysconfdir/ovz-daemon
cp -a utils/hw-daemon/hw-daemon.ini.sample %buildroot%_sysconfdir/ovz-daemon/hw-daemon.ini
cp -a utils/hw-daemon/certs %buildroot%_sysconfdir/ovz-daemon/

mkdir -p %buildroot%_initrddir/
install %SOURCE1 %buildroot%_initrddir/

%files
%_datadir/%name/
%_initrddir/owp
%_sysconfdir/owp.conf

%files -n ovz-daemon
%_datadir/ovz-daemon/
%_sysconfdir/ovz-daemon/
%_initrddir/ovz-daemon

%files -n ruby1.8-ovz-daemon
%_datadir/ovz-daemon/
%_sysconfdir/ovz-daemon/
%_initrddir/ovz-daemon

%changelog
* Sat Apr 23 2011 Denis Baranov <baraka@altlinux.ru> 2.0-alt7
- Fix requires for ovz-daemon

* Sat Apr 23 2011 Denis Baranov <baraka@altlinux.ru> 2.0-alt6
- Add ovz-daemon for ruby 1.9

* Sat Apr 23 2011 Denis Baranov <baraka@altlinux.ru> 2.0-alt5
- Fix path in config file

* Sat Apr 23 2011 Denis Baranov <baraka@altlinux.ru> 2.0-alt4
- Fix error with build

* Sat Apr 23 2011 Denis Baranov <baraka@altlinux.ru> 2.0-alt3
- Fix requires

* Sat Apr 23 2011 Denis Baranov <baraka@altlinux.ru> 2.0-alt2
- Fix problem with build
- add daemon package

* Fri Apr 22 2011 Denis Baranov <baraka@altlinux.ru> 2.0-alt1
- Initial build for ALTLinux

