# SPEC file for trickle package

Name:    trickle
Version: 1.07
Release: alt5

Summary: a portable lightweight userspace bandwidth shaper

License: BSD-3-Clause
Group:   Networking/Other
URL:     https://github.com/mariusae/trickle

Packager: Nikolay A. Fetisov <naf@altlinux.ru>

Source0: %name-%version.tar
Source1: %{name}d.conf

Patch0:  %name-1.07-debian-autoreconf_patch.patch
Patch1:  %name-1.07-debian-library_path.patch
Patch2:  %name-1.07-debian-man_pages.patch
Patch3:  %name-1.07-debian-trickle-overload.patch
Patch4:  %name-1.07-sunrpc.patch

# Automatically added by buildreq on Tue Mar 09 2021
# optimized out: glibc-kernheaders-generic glibc-kernheaders-x86 gnu-config perl python-modules python2-base python3 python3-base python3-module-paste ruby ruby-stdlibs sh4
BuildRequires: glibc-devel-static libbsd-devel libevent-devel libtirpc-devel

%description
trickle is a portable lightweight userspace bandwidth shaper. It can run in
collaborative mode (together with trickled) or in stand alone mode.

trickle works by taking advantage of the unix loader preloading. Essentially
it provides, to the application, a new version of the functionality that is
required to send and receive data through sockets. It then limits traffic
based on delaying the sending and receiving of data over a socket.

trickle runs entirely in userspace and does not require root privileges.

%prep
%setup
%patch0
%patch1
%patch2
%patch3
%patch4

%build
%autoreconf
sed -e 's#/lib/trickle#/%_lib/trickle#' -i configure.in
%configure
%make

%install
%make_install DESTDIR=%buildroot install

mkdir -p %buildroot%_sysconfdir
install -m 0644 %SOURCE1 %buildroot%_sysconfdir/%{name}d.conf

%files
%doc LICENSE README TODO

%config(noreplace) %_sysconfdir/%{name}d.conf

%_bindir/%name
%_bindir/%{name}d
%_bindir/%{name}ctl

%_man1dir/%{name}*
%_man5dir/%{name}*
%_man8dir/%{name}*
%_libdir/%name

%changelog
* Tue Mar 09 2021 Nikolay A. Fetisov <naf@altlinux.org> 1.07-alt5
- Fix for SunRPC intercace removal from glibc

* Thu Dec 12 2019 Grigory Ustinov <grenka@altlinux.org> 1.07-alt4
- NMU: Fix license.

* Mon Sep 17 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 1.07-alt3
- NMU: fixed build.

* Sat Jun 25 2016 Nikolay A. Fetisov <naf@altlinux.ru> 1.07-alt2
- Fix build: updating BuildRequires
- Updating URL

* Sat Oct 1 2011 Nikolay A. Fetisov <naf@altlinux.ru> 1.07-alt1
- Initial build
