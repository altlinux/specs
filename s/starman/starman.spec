Name: starman
Version: 0.29_90
Release: alt2
Serial: 1
Summary: High-performance preforking PSGI/Plack web server

Group: Networking/WWW
License: Perl
Url: %CPAN Starman

BuildArch: noarch
Source0: %name-%version.tar
Source1: %name.init
Source2: %name.sysconfig
Source3: %name.logrotate

BuildRequires: perl-Plack perl-HTTP-Parser-XS perl-Net-Server perl-Module-Install perl-Module-Install-Repository perl-Module-Install-ReadmeFromPod perl-Module-Install-AuthorTests perl-Test-Requires perl-Data-Dump 

%add_findreq_skiplist */Plack/Handler/Starman.pm

%description
Starman is a PSGI perl web server that has unique features such as:

* High Performance
    Uses the fast XS/C HTTP header parser
* Preforking
    Spawns workers preforked like most high performance UNIX servers do.
    Starman also reaps dead children and automatically restarts the
    worker pool.
* Signals
    Supports "HUP" for graceful restarts, and "TTIN"/"TTOU" to
    dynamically increase or decrease the number of worker processes.
* Superdaemon aware
    Supports Server::Starter for hot deploy and graceful restarts.
* Multiple interfaces and UNIX Domain Socket support
    Able to listen on multiple intefaces including UNIX sockets.
* Small memory footprint
    Preloading the applications with "--preload-app" command line option
    enables copy-on-write friendly memory management. Also, the minimum
    memory usage Starman requires for the master process is 7MB and
    children (workers) is less than 3.0MB.
* PSGI compatible
    Can run any PSGI applications and frameworks
* HTTP/1.1 support
    Supports chunked requests and responses, keep-alive and pipeline
    requests.
* UNIX only
    This server does not support Win32.

%prep
%setup -q

%build
%perl_vendor_build INSTALLMAN1DIR=%_man1dir

%install
%perl_vendor_install
mkdir -p %buildroot/%_initdir
install -m 755 %SOURCE1 %buildroot/%_initdir/%name
mkdir -p %buildroot/%_sysconfdir/sysconfig/
install -m 644 %SOURCE2 %buildroot/%_sysconfdir/sysconfig/%name
mkdir -p %buildroot/%_sysconfdir/logrotate.d/
install -m 644 %SOURCE3  %buildroot/%_sysconfdir/logrotate.d/%name
mkdir -p %buildroot/var/log/%name

%pre
%_sbindir/groupadd -r -f _starman
%_sbindir/useradd -r -g _starman -r -c "starman web server" -s /dev/null -d /dev/null -n _starman > /dev/null 2>&1 ||:

%post
%post_service %name

%preun
%preun_service %name

%files
%_bindir/%name
%_man1dir/%name.1*
%perl_vendor_privlib/Starman*
%perl_vendor_privlib/HTTP/Server/PSGI/Net/Server/PreFork.pm
%perl_vendor_privlib/Plack/Handler/Starman.pm
%config(noreplace) %_sysconfdir/sysconfig/%name
%_initdir/%name
%_sysconfdir/logrotate.d/%name
%attr(3770,root,_starman) /var/log/%name
%doc Changes README

%changelog
* Fri Feb 17 2012 Eugene Prokopiev <enp@altlinux.ru> 1:0.29_90-alt2
- add serial
- add initscript and logrotate configuration

* Fri Feb 17 2012 Eugene Prokopiev <enp@altlinux.ru> 0.29_90-alt1
- New version 0.29_90

* Thu Feb 16 2012 Eugene Prokopiev <enp@altlinux.ru> 0.2014-alt1
- New version 0.2014

* Thu Mar 03 2011 Vladimir Lettiev <crux@altlinux.ru> 0.2008-alt1
- New version 0.2008

* Thu Feb 10 2011 Vladimir Lettiev <crux@altlinux.ru> 0.2007-alt1
- initial build

