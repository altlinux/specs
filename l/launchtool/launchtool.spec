Name: launchtool
Version: 0.7
Release: alt1

Packager: Victor Forsyuk <force@altlinux.org>

Summary: Runs a command supervising its execution
License: GPLv2+
Group: System/Base

Url: http://people.debian.org/~enrico/launchtool.html
Source: http://ftp.de.debian.org/debian/pool/main/l/launchtool/launchtool_%version-1.1.tar.gz
#http://bugs.debian.org/cgi-bin/bugreport.cgi?bug=337876
Patch1: launchtool-0.7-pidfile.patch

# Automatically added by buildreq on Mon Jan 05 2009
BuildRequires: gcc-c++ libpopt-devel

%description
launchtool is a tool that runs a user-supplied command and can supervise its
execution in many ways, such as controlling its environment, blocking signals,
logging its output, changing user and group permissions, limiting resource
usage, restarting it if it fails, running it continuously and turn it into a
daemon.

%prep
%setup
%patch1 -p1

%build
%configure --localstatedir=/var
%make_build

%install
%make_install install DESTDIR=%buildroot
install -pD -m644 launchtool.1 %buildroot%_man1dir/launchtool.1

%files
%_bindir/*
%_man1dir/*

%changelog
* Mon Jan 05 2009 Victor Forsyuk <force@altlinux.org> 0.7-alt1
- Initial build.
