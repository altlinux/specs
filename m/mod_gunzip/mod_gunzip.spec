# override definition from apache-devel
%define apache_addonconfdir %apache_confdir/addon-modules.d
%define apache_moduledir %_libdir/apache

Name: mod_gunzip
Version: 3
Release: alt3.1

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
CFLAGS="%optflags" %apache_apxs -c mod_gunzip.c -o mod_gunzip.so -lz

%install
mkdir -p %buildroot{%apache_moduledir,%apache_addonconfdir}

install -m755 %name.so %buildroot%apache_moduledir
install -m644 %_sourcedir/%name.conf %buildroot%apache_addonconfdir

%post
/sbin/service httpd condrestart

%postun
/sbin/service httpd condrestart

%files
%apache_moduledir/*
%config(noreplace) %apache_addonconfdir/*
%doc README

%changelog
* Fri Dec 07 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3-alt3.1
- Fixed build with gcc 4.7

* Wed Feb 07 2007 Victor Forsyuk <force@altlinux.org> 3-alt3
- Requires apache (fix ALT#10381).

* Tue May 23 2006 Victor Forsyuk <force@altlinux.ru> 3-alt2
- Fix build with new stricter packaging checks.

* Fri Oct 15 2004 Victor Forsyuk <force@altlinux.ru> 3-alt1
- Initial build for Sisyphus.
