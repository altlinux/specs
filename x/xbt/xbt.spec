Name: xbt
Version: 0.2.9
Release: alt1.2

Summary: A BitTorrent tracker written in C++

License: GPLv2
Group: Networking/File transfer
Url: http://xbtt.sourceforge.net/tracker/

Packager: Ilya Shpigor <elly@altlinux.org>

Source: %name-%version.tar.bz2
Patch: xbt_tracker_etc_config.patch
Patch1: xbt_tracker_default_config.patch
Patch2: xbt_tracker_log_paths.patch
Patch3: xbt-tracker-gcc43.patch
Patch4: xbt-0.2.9-alt-DSO.patch

# Automatically added by buildreq on Wed Nov 25 2009
BuildRequires: boost-devel gcc-c++ libMySQL-devel zlib-devel cmake

%description
XBT Tracker is a BitTorrent tracker written in C++. It's designed to offer high
performance while consuming little resources (CPU and RAM). It's a pure
tracker, so it doesn't offer a frontend.

Authors:
--------
    Olaf van der Spek

%prep
%setup
%patch
%patch1
%patch2 -p1
%patch3 -p1
%patch4 -p2

%build
export CFLAGS="%optflags   -Wall"
export CXXFLAGS="%optflags -Wall"
cd Tracker
./make.sh

%install
install -d %buildroot%_bindir %buildroot%_sysconfdir %buildroot%_initdir
install -D -m 0755 Tracker/xbt_tracker %buildroot%_bindir/xbt_tracker
install -D -m 644 Tracker/xbt_tracker.conf.default %buildroot%_sysconfdir/xbt_tracker.conf

%files
%doc Tracker/xbt_tracker.sql
%doc Tracker/xbt_tracker.conf.default Tracker/htdocs/
%_bindir/xbt_tracker
%config(noreplace) %_sysconfdir/xbt_tracker.conf
#%config %_initrddir/xbt_tracker

%changelog
* Tue Jun 12 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.2.9-alt1.2
- Fixed build

* Tue Dec 07 2010 Igor Vlasenko <viy@altlinux.ru> 0.2.9-alt1.1
- rebuild with new libmysqlclient by request of libmysqlclient maintainer

* Wed Nov 25 2009 Ilya Shpigor <elly@altlinux.org> 0.2.9-alt1
- initial build for ALT Linux Sisyphus

* Thu Jul 17 2008 crrodriguez@suse.de
- fix openSUSE 11 build
* Wed Aug  1 2007 mrueckert@suse.de
- update to r1772
* Mon Apr  2 2007 mrueckert@suse.de
- update to r1752
* Mon Mar  5 2007 mrueckert@suse.de
- build with stackprotector if possible
* Mon Mar  5 2007 mrueckert@suse.de
- temporarily add dir entries for the apparmor profile path
* Mon Mar  5 2007 mrueckert@suse.de
- added server %%pre/%%post scripts
- renamed the user
* Mon Mar  5 2007 mrueckert@suse.de
- fixed paths:
  /var/{run,log,lib}/xbtt => /var/{run,log,lib}/xbt_tracker
- added log paths to the apparmor profile
* Mon Mar  5 2007 mrueckert@suse.de
- update to r1742
- added apparmor profile (disabled by default)
- added init script
- added xbt_tracker_default_config.patch:
  fix a few default settings
- added xbt_tracker_log_paths.patch:
  set proper path to the log files
- enabled debug package
* Sun Mar  4 2007 mrueckert@suse.de
- updated to r1740
- updated xbt_tracker_etc_config.patch
* Wed Feb 14 2007 mrueckert@suse.de
- added cmake.tar.bz2:
  hacked up a small cmake based build.
* Wed Feb 14 2007 mrueckert@suse.de
- update to r1734:
  - increased epoll_wait timeout by factor 5
  - clearified the sql schema
  - fixes to the php frontend
* Mon Jan  8 2007 mrueckert@suse.de
- initial version of r1718
