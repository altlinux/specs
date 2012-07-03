# vim: set ft=spec: -*- rpm-spec -*-
# $Id: rbot,v 1.5 2006/03/14 22:31:15 raorn Exp $

Name: rbot
Version: 0.9.14
Release: alt1

Summary: ruby IRC bot
Group: Networking/IRC
License: BSD
Url: http://linuxbrit.co.uk/%name

Packager: Sir Raorn <raorn@altlinux.ru>

BuildArch: noarch

# git://git.altlinux.org/people/raorn/packages/rbot.git
Source: %name-%version.tar
Patch: %name-%version-%release.patch

# Automatically added by buildreq on Sat Sep 13 2008 (-bi)
BuildRequires: rpm-build-ruby ruby-tool-rdoc ruby-tool-setup

%description
rbot is a ruby IRC bot. Think of him as a ruby bot framework
with a highly modular design based around plugins.

By default he behaves a lot like an infobot.

%prep
%setup -q
%patch -p1
%update_setup_rb

%build
%ruby_config
%ruby_build

%install
%ruby_install
%rdoc lib/

%files
%doc AUTHORS ChangeLog README COPYING INSTALL REQUIREMENTS TODO
%_bindir/%name
%ruby_sitelibdir/%name
%_datadir/%name
%doc %ruby_ri_sitedir/Irc*

%changelog
* Tue Jun 30 2009 Alexey I. Froloff <raorn@altlinux.org> 0.9.14-alt1
- [0.9.14]

* Sat Sep 13 2008 Sir Raorn <raorn@altlinux.ru> 0.9.13-alt1
- [0.9.13]

* Sat Mar 29 2008 Sir Raorn <raorn@altlinux.ru> 0.9.10-alt3
- Updated to trunk
- Rebuilt with new rpm-build-ruby

* Fri Dec 01 2006 Sir Raorn <raorn@altlinux.ru> 0.9.10-alt2
- Fixed cyrillic input handling in 8-bit locales (closes: #10142)

* Mon Aug 07 2006 Sir Raorn <raorn@altlinux.ru> 0.9.10-alt1
- [0.9.10]
- All patches (except rubygems) merged upstream

* Wed Mar 15 2006 Sir Raorn <raorn@altlinux.ru> 0.9.9-alt3
- Escape bot.nick in regular expressions (closes: #9244)

* Thu Aug 11 2005 Sir Raorn <raorn@altlinux.ru> 0.9.9-alt2
- Do not even try to use rubygems
- Default homedir changed from "/home/#{Etc.getlogin}/"
  to "#{Etc.getpwnam(Etc.getlogin).dir}/"
- Do not try to load same plugin from different locations.
- Added ability to disable system-wide plugins - create
  PLIGUN.rb.disabled in user's plugin directory

* Sat Aug 06 2005 Sir Raorn <raorn@altlinux.ru> 0.9.9-alt1
- Built for Sisyphus

