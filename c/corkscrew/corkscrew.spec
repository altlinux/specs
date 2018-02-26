Name: corkscrew
Version: 2.0
Release: alt1

Summary: Tool for tunneling SSH through HTTP proxies
License: GPLv2+
Group: System/Libraries

Url: http://www.agroman.net/corkscrew/
Source: %url/corkscrew-%version.tar.gz
Source1: corkscrew.1
Patch0: corkscrew-2.0-from-debian.patch

%description
Corkscrew is a tool for tunneling SSH through HTTP proxies.

%prep
%setup
%patch0 -p1

%build
%configure
%make_build

%install
%make_install DESTDIR=%buildroot install
install -pD -m644 %_sourcedir/corkscrew.1 %buildroot%_man1dir/corkscrew.1

%files
%doc README
%_bindir/*
%_man1dir/*

%changelog
* Wed Nov 07 2007 Victor Forsyuk <force@altlinux.org> 2.0-alt1
- Initial build.
