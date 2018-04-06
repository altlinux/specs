Name: zsync
Summary: Partial/differential file transfer client over HTTP
Version: 0.6.2
Release: alt1
License: Artistic License v2
Group: Networking/File transfer
Source: %name-%version.tar
Url: https://github.com/cph6/zsync.git

%description
Rsync uses a quick and reliable algorithm to very quickly bring
remote and host files into sync.  Rsync is fast because it just
sends the differences in the files over the network (instead of
sending the complete files).  Rsync is often used as a very powerful
mirroring process or just as a more capable replacement for the
rcp command.  A technical report which describes the rsync algorithm
is included in this package.

%prep
%setup

%build
%autoreconf
%configure
%make_build

%install
%makeinstall_std BUILDROOT=%{buildroot}

%files
%doc README COPYING
%_bindir/*
%_man1dir/*

%changelog
* Fri Apr 06 2018 Lenar Shakirov <snejok@altlinux.ru> 0.6.2-alt1
- Initial build for ALT

