# override definition from apache-devel
%define apache_addonconfdir %apache_confdir/addon-modules.d
%define apache_moduledir %_libdir/apache
# Note: this macros should be provided by apache-devel
%define apache_moddocdir  %apache_htdocsdir/addon-modules

Name: mod_gzip
Version: 1.3.26.1a
Release: alt3

Summary: Apache module: On-the-fly compression of HTML documents
Group: System/Servers
License: Apache
URL: http://sourceforge.net/projects/mod-gzip/

Source: http://dl.sourceforge.net/mod-gzip/mod_gzip-%version.tgz
Source2: mod_gzip.conf

Requires: apache

# Automatically added by buildreq on Tue May 23 2006
BuildRequires: apache-devel

%description
Apache module: On-the-fly compression of HTML documents. Browser will
transparently decompress and display such documents.

%prep
%setup -q

%build
%apache_apxs -c mod_gzip.c mod_gzip_debug.c mod_gzip_compress.c -o mod_gzip.so

%install
mkdir -p %buildroot{%apache_moduledir,%apache_addonconfdir,%apache_moddocdir}

install -m755 %name.so %buildroot%apache_moduledir
install -m644 %_sourcedir/%name.conf %buildroot%apache_addonconfdir

# docs
ln -s %_docdir/%name-%version/ %buildroot%apache_moddocdir/%name

%post
/sbin/service httpd condrestart

%postun
/sbin/service httpd condrestart

%files
%apache_moduledir/*
%apache_moddocdir/*
%config(noreplace) %apache_addonconfdir/*
%doc ChangeLog docs/manual/english/*

%changelog
* Wed Feb 07 2007 Victor Forsyuk <force@altlinux.org> 1.3.26.1a-alt3
- Requires apache (fix ALT#10380).

* Tue May 23 2006 Victor Forsyuk <force@altlinux.ru> 1.3.26.1a-alt2
- Fix build.

* Thu Oct 07 2004 Victor Forsyuk <force@altlinux.ru> 1.3.26.1a-alt1
- Initial build for Sisyphus.
