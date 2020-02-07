%define _unpackaged_files_terminate_build 1

Name: xtrace
Version: 1.4.0
Release: alt1
Summary: X11 protocol trace utility 
License: GPLv2
Group: Development/Debuggers
URL: https://salsa.debian.org/debian/xtrace

# https://salsa.debian.org/debian/xtrace
Source: %name-%version.tar

BuildRequires: libX11-devel
BuildRequires: libXext-devel
BuildRequires: xorg-proto-devel

%description
What strace is for system calls, xtrace is for X11 connections:
you hook it between one or more X11 clients and an X server and
it prints the requests going from client to server and the replies,
events and errors going the other way.

%prep
%setup

%build
# rename application from xtrace to x11trace to prevent collision
# with glibc application

%autoreconf
%configure \
	--program-transform-name="s/^x/x11/" \
	%nil

%make_build

%install
%makeinstall_std

%files
%doc COPYING
%doc AUTHORS ChangeLog INSTALL NEWS README
%_bindir/x11trace
%_man1dir/x11trace.1*
%_datadir/%name

%changelog
* Fri Feb 07 2020 Aleksei Nikiforov <darktemplar@altlinux.org> 1.4.0-alt1
- Initial build for ALT.
