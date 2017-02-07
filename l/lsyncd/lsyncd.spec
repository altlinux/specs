Name: lsyncd
Version: 2.1.4
Release: alt1.git.3c9f8833.1
Summary: File change monitoring and synchronization daemon
Group: File tools
License: %gpl2plus
Url: https://github.com/axkibe/lsyncd
Source: %name-%version.tar

Requires: rsync

BuildRequires: lua-devel lua rpm-build-licenses asciidoc-a2x

%def_without tests

%if_with tests
BuildRequires: lua5-posix rsync openssh /proc
%endif

%description
Lsyncd watches a local directory trees event monitor interface (inotify).
It aggregates and combines events for a few seconds and then spawns one
(or more) process(es) to synchronize the changes. By default this is
rsync.

Lsyncd is thus a light-weight live mirror solution that is comparatively
easy to install not requiring new file systems or block devices and does
not hamper local file system performance.

%prep
%setup

subst "s|/path/to/trg/|%_sysconfdir|" examples/lecho.lua
subst "s|src|%_sysconfdir|" examples/lecho.lua

%build
%autoreconf
%configure
%make_build


%install
%makeinstall_std
install -D -m 0755 lsyncd.init %buildroot%_initdir/lsyncd
install -D -m 0644 examples/lecho.lua %buildroot%_sysconfdir/%name/lsyncd.conf.lua

%if_with tests
%check
%make check
%endif

%post
%post_service %name

%preun
%preun_service %name


%files
%dir %_sysconfdir/%name
%config(noreplace) %_sysconfdir/%name/*
%_bindir/%name
%_initdir/*
%_man1dir/%name.1*
%doc ChangeLog examples COPYING

%changelog
* Tue Feb 07 2017 Igor Vlasenko <viy@altlinux.ru> 2.1.4-alt1.git.3c9f8833.1
- NMU: rebuild with new lua 5.3

* Wed Jun 05 2013 Slava Dubrovskiy <dubrsl@altlinux.org> 2.1.4-alt1.git.3c9f8833
- Update to last git version
- Move to git
- Add init script
- Add config file

* Sat Jan  7 2012 Terechkov Evgenii <evg@altlinux.org> 2.0.5-alt1
- Initial build for ALT Linux Sisyphus
