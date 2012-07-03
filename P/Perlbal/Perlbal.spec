Name: Perlbal
Version: 1.80
Release: alt1

Summary: Reverse-proxy load balancer and webserver
License: Perl
Group: System/Servers

URL: http://www.danga.com/perlbal/
Source: http://search.cpan.org/CPAN/authors/id/D/DO/DORMANDO/%name-%version.tar.gz
Source1: perlbal.init
Patch1: perlbal-1.79-pidfile.patch

# Automatically added by buildreq on Mon Jul 18 2011
BuildRequires: perl-BSD-Resource perl-Danga-Socket perl-IO-AIO perl-devel perl-libwww

BuildArch: noarch

%description
Perlbal is a single-threaded event-based server supporting HTTP load
balancing, web serving, and a mix of the two. Perlbal can act as either
a web server or a reverse proxy.

One of the defining things about Perlbal is that almost everything can be
configured or reconfigured on the fly without needing to restart the software.
A basic configuration file containing a management port enables you to easily
perform operations on a running instance of Perlbal.

Perlbal can also be extended by means of per-service (and global) plugins that
can override many parts of request handling and behavior.

%prep
%setup
%patch1 -p1

%build
%perl_vendor_build

%install
%perl_vendor_install

install -D -p -m 0644 conf/webserver.conf %buildroot%_sysconfdir/perlbal/perlbal.conf
install -D -p -m 0755 %SOURCE1 %buildroot%_initddir/perlbal

%set_perl_req_method relaxed

%post
%post_service perlbal

%preun
%preun_service perlbal

%files
%dir %_sysconfdir/perlbal
%config(noreplace) %_sysconfdir/perlbal/perlbal.conf
%_initdir/perlbal
%_bindir/*
%perl_vendor_privlib/Perlbal*
%doc doc/* conf

%changelog
* Tue Feb 28 2012 Victor Forsiuk <force@altlinux.org> 1.80-alt1
- 1.80

* Mon Jul 18 2011 Victor Forsiuk <force@altlinux.org> 1.79-alt2
- Fix install/uninstall service management.

* Mon Jul 18 2011 Victor Forsiuk <force@altlinux.org> 1.79-alt1
- Initial build.
