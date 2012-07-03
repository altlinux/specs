%define apache_libdir %(%apache_apxs -q LIBEXECDIR)
%define apache_moddocdir %apache_htdocsdir/addon-modules
%define fastcgi_bindir %apache_datadir/fcgi-bin/

Name: mod_fastcgi
Version: 2.4.6
Release: alt2

Packager: Victor Forsyuk <force@altlinux.org>

Summary: FastCGI module for Apache
License: OpenMarket
Group: System/Servers

Url: http://www.fastcgi.com
Source: %url/dist/mod_fastcgi-%version.tar.gz

%define apache_version  1.3.6
PreReq: apache >= %apache_version

BuildPreReq: apache-devel >= %apache_version
BuildConflicts: apache2-devel

# Automatically added by buildreq on Mon Mar 31 2008
BuildRequires: apache-devel apache-suexec

%description
FastCGI module provides support for the FastCGI protocol. FastCGI is a
language independent, scalable, open extension to CGI that provides high
performance and persistence without the limitations of server specific APIs.

%prep
%setup

%build
%apache_apxs -Wc,"%optflags" -o mod_fastcgi.so -c *.c 

%install
mkdir -p %buildroot{%apache_libdir,%apache_modconfdir,%apache_moddocdir,%fastcgi_bindir}
install -m755 mod_fastcgi.so %buildroot%apache_libdir

# docs
ln -s %_docdir/mod_fastcgi-%version %buildroot%apache_moddocdir/mod_fastcgi

### === === Creating mod_fastcgi.conf
cat <<EOF >mod_fastcgi.conf
<IfModule !mod_fastcgi.c>
LoadModule fastcgi_module modules/mod_fastcgi.so
AddModule mod_fastcgi.c
</IfModule>
### mod_fastcgi.conf - configuration directives for the FastCGI Apache module.
### See %apache_moddocdir/mod_fastcgi/docs/mod_fastcgi.html for details.

## To configure Apache to handle all files (within the scope of the
## directive) as FastCGI applications (e.g. for a fcgi-bin directory):

# SetHandler fastcgi-script

## or to configure Apache to handle files (within the scope of the
## directive) with the specified extension(s) as FastCGI applications:

# AddHandler fastcgi-script fcg fcgi fpl

# Sample configuration for fcgi-bin directory

<IfModule mod_fastcgi.c>
    <IfModule mod_alias.c>
        Alias /fcgi-bin/ "%fastcgi_bindir"
    </IfModule>

    <Directory "%fastcgi_bindir">
	SetHandler fastcgi-script
	AllowOverride none
	Options ExecCGI
	Order allow,deny
	Allow from all
    </Directory>
</IfModule>
EOF

install -m644 mod_fastcgi.conf %buildroot%apache_modconfdir

%post
%post_apacheconf

%postun
%postun_apacheconf

%files
%apache_libdir/mod_fastcgi.so
%apache_moddocdir/*
%config(noreplace) %apache_modconfdir/mod_fastcgi.conf
%attr(2771,root,%apache_webmaster) %fastcgi_bindir
%doc CHANGES docs

%changelog
* Fri May 23 2008 Victor Forsyuk <force@altlinux.org> 2.4.6-alt2
- Include directives to load installed fastcgi module, fixes #15465.

* Mon Mar 31 2008 Victor Forsyuk <force@altlinux.org> 2.4.6-alt1
- 2.4.6
- More precise License: OpenMarket, not just simply "Free".
- We now rely on apache-devel macro definitions. Visible consequence:
  configuration for module will be placed in addon-modules.d instead of
  previous location, addon-modules.
- No more httpd.conf editing with apxs.

* Wed Nov 02 2005 Stanislav Ievlev <inger@altlinux.org> 2.2.12-alt2.1
- fixed default config

* Wed Nov 13 2002 Yuri N. Sedunov <aris@altlinux.ru> 2.2.12-alt2
- Rebuild.

* Sat Mar 9 2002 Yuri N. Sedunov <aris@altlinux.ru> 2.2.12-alt1
- First build for Sisyphus.
