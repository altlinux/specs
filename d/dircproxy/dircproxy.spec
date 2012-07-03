Summary: IRC proxy server
Name: dircproxy
Version: 1.1.0
Release: alt1
License: GPL
Group: Networking/Chat
URL: http://kimihia.org.nz/projects/dircproxy/
Packager: Mikhail Pokidko <pma@altlinux.org>
Source0: dircproxy-%version.tar.gz
Source1: dircd
Patch0: dirc.patch
Patch1: dircdconf.patch
Patch2: dircmon.patch

%description
dircproxy is an IRC proxy server designed for people who use IRC from
lots of different workstations or clients, but wish to remain
connected and see what they missed while they were away.

You connect to IRC through dircproxy, and it keeps you connected to the
server, even after you detach your client from it. While you're detached,
it logs channel and private messages as well as important events, and
when you reattach it'll let you know what you missed.

%prep
%setup -q
%patch0 -p0
%patch1 -p0
%patch2 -p0

%build
%configure --enable-poll
%make

%install
mkdir -p %buildroot%_initdir %buildroot%_sysconfdir/%name
%make_install PREFIX=%buildroot/usr DESTDIR="%buildroot" install
cp %SOURCE1 %buildroot%_initdir
cp %buildroot%_datadir/%name/dircproxyrc  %buildroot%_sysconfdir/%name

%files
%doc AUTHORS ChangeLog FAQ NEWS PROTOCOL README*
%config(noreplace) %_sysconfdir/%name/*
%_initdir/*
%_man1dir/*.1.*
%_bindir/*
%_datadir/%name/*


%changelog
* Wed Jul 19 2006 Mikhail Pokidko <pma@altlinux.ru> 1.1.0-alt1
- Initial build. Added init-script, ALT-specific patches.
