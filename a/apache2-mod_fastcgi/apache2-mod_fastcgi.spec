%define program_name mod_fastcgi
%define program_version	2.4.6
%define program_release	alt3

Name: apache2-%program_name
Version: %program_version
Release: %program_release
Summary: Apache 2.x module odule provides support for the FastCGI protocol.
License: GPL
Url: http://www.fastcgi.com
Group: System/Servers
Packager: Andriy Stepanov <stanv@altlinux.ru>

Source0: %program_name-%program_version.tar

PreReq: apache2 >= %apache2_version-%apache2_release

# Automatically added by buildreq on Sun Feb 18 2007
BuildRequires(pre): apache2-devel

%description
This 3rd party module provides support for the FastCGI protocol.
FastCGI is a language independent, scalable, open extension to CGI
that provides high performance and persistence without the limitations
of server specific APIs.

%prep
%setup -q -n "%{program_name}-%{version}"

%build
%__make top_dir=%apache2_libdir -f Makefile.AP2

%install
install -d %buildroot%apache2_confdir/mods-available
install -pD -m 0755 .libs/mod_fastcgi.so %buildroot%apache2_moduledir/mod_fastcgi.so
echo "LoadModule fastcgi_module %apache2_moduledir/mod_fastcgi.so" > %buildroot%apache2_confdir/mods-available/fastcgi.load
chmod 644 %buildroot%apache2_confdir/mods-available/fastcgi.load

%files
%apache2_moduledir/mod_fastcgi.so
%apache2_confdir/mods-available/*
%doc README

%changelog
* Thu Oct 20 2011 Michael Bochkaryov <misha@altlinux.ru> 2.4.6-alt3
- Fix fastcgi.load for x86_64 platforms.

* Sat Feb 05 2011 Andriy Stepanov <stanv@altlinux.ru> 2.4.6-alt2
- Fix Build.

* Sat Feb 05 2011 Andriy Stepanov <stanv@altlinux.ru> 2.4.6-alt1
- Initial build.

