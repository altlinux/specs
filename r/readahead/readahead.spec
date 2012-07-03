Name: readahead
Version: 1.5.6
Release: alt1

Packager: Victor Forsiuk <force@altlinux.org>

Summary: Read a preset list of files into memory
License: GPLv2+
Group: System/Configuration/Boot and Init

Url: http://fedorahosted.org/readahead/
# Source available only via git. Commands to get archive with latest released
# tag looks like:
# git clone git://git.fedorahosted.org/readahead
# git archive --prefix=readahead-1.5.4/ v1.5.4 |bzip2 -9 >readahead-1.5.4.tar.bz2
Source: readahead-%version.tar.bz2
Source1: readahead_early.init
Source2: readahead_later.init

# Automatically added by buildreq on Tue Oct 12 2010
BuildRequires: libaudit-devel libblkid-devel libe2fs-devel

# NB! ALT Linux doesn't use upstart (as Fedora) and support for readahead not
# yet added to rc.sysinit (as in Mandriva). So, we need to use own startup
# scripts for a while.

# Note for myself: 1.5.7 will support systemd!

%description
readahead reads the contents of a list of files into memory, which causes them
to be read from cache when they are actually needed. Its goal is to speed up the
boot process.

%prep
%setup

%build
./autogen.sh
%configure --sbindir=/sbin
%make_build
# To convert list from arch independent to arch specific format.
# Commented for now as default lists does not need this rebuild.
#%make rpm-lists-rebuild RPM_LIB="%_lib" RPM_ARCH="%_arch" FILES="default.early default.later"

%install
install -pD -m755 %_sourcedir/readahead_early.init %buildroot%_initdir/readahead_early
install -pD -m755 %_sourcedir/readahead_later.init %buildroot%_initdir/readahead_later

%makeinstall_std
install -d %buildroot/var/lib/readahead

%find_lang %name

%post
%post_service readahead_early
%post_service readahead_later

%preun
%preun_service readahead_early
%preun_service readahead_later

%files -f %name.lang
%config(noreplace) %_sysconfdir/readahead.conf
%config(noreplace) %_sysconfdir/sysconfig/readahead
%dir /var/lib/readahead
# We don't use upstart
%exclude %_sysconfdir/init
%_sysconfdir/cron.daily/*
%_sysconfdir/cron.monthly/*
%_initdir/*
/sbin/*

%changelog
* Tue Oct 12 2010 Victor Forsiuk <force@altlinux.org> 1.5.6-alt1
- 1.5.6
- Fix init-scripts, they expect executable in wrong directory (closes: #24275).

* Fri Jul 02 2010 Victor Forsiuk <force@altlinux.org> 1.5.4-alt2
- Rebuild with new libaudit package.

* Thu Jan 14 2010 Victor Forsyuk <force@altlinux.org> 1.5.4-alt1
- 1.5.4
- Refresh build requirements.

* Fri Dec 12 2008 Anton Farygin <rider@altlinux.ru> 1.4.4-alt1.1
- NMU: fixed build with libaudit-1.7.9

* Mon Sep 29 2008 Victor Forsyuk <force@altlinux.org> 1.4.4-alt1
- Initial build.
