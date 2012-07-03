# override definition from apache-devel
%define apache_addonconfdir %apache_confdir/addon-modules.d
%define apache_moduledir %_libdir/apache

Name: mod_gunzip
Version: 3
Release: alt3

Summary: Apache module: On-the-fly decompression of documents
Group: System/Servers
License: GPL
URL: http://www.oldach.net/

Source: http://www.oldach.net/mod_gunzip.tar.gz
Source2: mod_gunzip.conf

Requires: apache

# Automatically added by buildreq on Fri Oct 15 2004
BuildRequires: apache-devel zlib-devel

%description
Apache module: On-the-fly decompression of gzip-compressed documents.

%prep
%setup -q

%build
%apache_apxs -Wc,"$RPM_OPT_FLAGS" -c mod_gunzip.c -o mod_gunzip.so -lz

%install
%__mkdir_p %buildroot{%apache_moduledir,%apache_addonconfdir}

%__install -m755 %name.so %buildroot%apache_moduledir
%__install -m644 %_sourcedir/%name.conf %buildroot%apache_addonconfdir

%post
/sbin/service httpd condrestart

%postun
/sbin/service httpd condrestart

%files
%apache_moduledir/*
%config(noreplace) %apache_addonconfdir/*
%doc README

%changelog
* Wed Feb 07 2007 Victor Forsyuk <force@altlinux.org> 3-alt3
- Requires apache (fix ALT#10381).

* Tue May 23 2006 Victor Forsyuk <force@altlinux.ru> 3-alt2
- Fix build with new stricter packaging checks.

* Fri Oct 15 2004 Victor Forsyuk <force@altlinux.ru> 3-alt1
- Initial build for Sisyphus.
