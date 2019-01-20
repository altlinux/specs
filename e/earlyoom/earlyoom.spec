Name:     earlyoom
Version:  1.2
Release:  alt1

Summary:  Early OOM Daemon for Linux
License:  MIT
Group:    Other
Url:      http://github.com/rfjakob/earlyoom

Packager: Anton Midyukov <antohami@altlinux.org>

Source:   %name-%version.tar

%ifarch %ix86 x86_64
BuildRequires: pandoc
%endif

%description
The oom-killer generally has a bad reputation among Linux users.
This may be part of the reason Linux invokes it only when it has
absolutely no other choice. It will swap out the desktop
environment, drop the whole page cache and empty every buffer
before it will ultimately kill a process. At least that's what
I think what it will do. I have yet to be patient enough to wait
for it, sitting in front of an unresponsive system.

%prep
%setup
sed -e '/systemctl/d' -i Makefile

%build
%make_build

%install
%makeinstall_std \
    PREFIX=%_prefix \
    SYSCONFDIR=%_sysconfdir \
    SYSTEMDUNITDIR=%_unitdir

%post
%post_service %name

%preun
%preun_service %name

%files
%doc README.md LICENSE
%_bindir/%name
%_unitdir/%name.service

%ifarch %ix86 x86_64
%_man1dir/%name.*
%endif

%config(noreplace) %_sysconfdir/default/%name

%changelog
* Sun Jan 20 2019 Anton Midyukov <antohami@altlinux.org> 1.2-alt1
- Initial build (Closes: 35924)
