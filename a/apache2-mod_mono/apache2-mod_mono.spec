Name: apache2-mod_mono
%define apache2_sysconfdir %(%apache2_apxs -q SYSCONFDIR)/conf.d
Obsoletes: mod_mono
%define modname mod_mono
%define apache2_libexecdir %(%apache2_apxs -q LIBEXECDIR)
%define apache_mmn        %(MMN=$(%apache2_apxs -q LIBEXECDIR)_MMN; test -x $MMN && $MMN)
Url: http://go-mono.com/
License: Apache Software License
Group: Networking/WWW
Version: 3.12
Release: alt2
Summary: Run ASP.NET Pages on Unix with Apache and Mono
Packager: Denis Medvedev <nbr@altlinux.org>

Source: %modname-%version.tar.bz2

Provides: mod_mono = %version-%release
# This must be manually entered according to xsp's protocol version
Requires: mono4-xsp >= %version
BuildPreReq: apache-base rpm-macros-apache2 >= 2.4.18-alt1
BuildRequires: pkg-config
BuildRequires: apache2-devel mono4-devel
BuildRequires: libaprutil1-devel
Requires: apache2 %apache_mmn

%description
mod_mono is a module that interfaces Apache with Mono and allows
running ASP.NET pages on Unix and Unix-like systems. To load the module
into Apache, run the command "a2enmod mono" as root.

%prep
%setup -n mod_mono-%version

%build
chmod +x ./autogen.sh
%define _configure_script ./autogen.sh
%configure --with-apxs=%apache2_apxs
make

%install
%makeinstall_std APXS_SYSCONFDIR="%apache2_sysconfdir"




%files
%apache2_libexecdir/*
%apache2_sysconfdir/*
%_man8dir/mod_mono.8*

%changelog
* Fri Nov 18 2016 Denis Medvedev <nbr@altlinux.org> 3.12-alt2
- rebuild with mono-4.6

* Tue Apr 05 2016 Sergey Alembekov <rt@altlinux.ru> 3.12-alt1.1
- rebuild with apache-2.4

* Mon Feb 22 2016 Denis Medvedev <nbr@altlinux.org> 3.12-alt1
- initial build for ALT Linux Sisyphus

