# SPEC file for trickle package

Name:    trickle
Version: 1.07
Release: alt1

Summary: a portable lightweight userspace bandwidth shaper

License: %bsd
Group:   Networking/Other
URL:     http://monkey.org/~marius/pages/?page=trickle

Packager: Nikolay A. Fetisov <naf@altlinux.ru>

Source0: %name-%version.tar
Source1: %{name}d.conf

Patch0:  %name-1.07-debian-autoreconf_patch.patch
Patch1:  %name-1.07-debian-library_path.patch
Patch2:  %name-1.07-debian-man_pages.patch
Patch3:  %name-1.07-debian-trickle-overload.patch

BuildRequires(pre): rpm-build-licenses

# Automatically added by buildreq on Sat Oct 01 2011
BuildRequires: libevent-devel

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

%build
%autoreconf
sed -e 's#/lib/trickle#/%_lib/trickle#' -i configure.in
%configure
%make_build

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
* Sat Oct 1 2011 Nikolay A. Fetisov <naf@altlinux.ru> 1.07-alt1
- Initial build

