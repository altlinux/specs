Summary: Simple FastCGI wrapper for CGI scripts
Name: fcgiwrap
Version: 1.0.3
Release: alt1
License: BSD-style
Group: System/Servers
URL: http://nginx.localdomain.pl/wiki/FcgiWrap
Source: %name-%version.tar
# git://github.com/gnosek/fcgiwrap.git
Patch0: %name-%version-%release.patch

# Automatically added by buildreq on Tue Oct 19 2010
BuildRequires: libfcgi-devel

%description
fcgiwrap  is a simple server for running CGI applications over FastCGI.
It hopes to provide clean CGI support to Nginx (and other  web  servers
that may need it).


%prep
%setup -q
%patch0 -p1


%build
autoreconf -fisv
%configure
%make

%install
%makeinstall_std

%files
%_sbindir/fcgiwrap
%_man8dir/*

%changelog
* Tue Oct 19 2010 Anton Farygin <rider@altlinux.ru> 1.0.3-alt1
- first build for Sisyphus
