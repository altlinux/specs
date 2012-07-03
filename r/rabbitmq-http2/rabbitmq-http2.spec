%define _unpackaged_files_terminate_build 1
%define oname rabbitmq

Name: rabbitmq-http2
Version: 0.0.1
Release: alt1.hg.4b8597
License: MPLv1.1
Group: System/Servers
Source: %name-%version.tar
Source1: %oname-http2.conf
Source2: %oname-httpd.conf
URL: http://www.rabbitmq.com/
Packager: Maxim Ivanov <redbaron@altlinux.org>

BuildRequires(pre): rpm-macros-erlang
BuildRequires: erlang-devel, erlang-otp-devel
BuildRequires: rabbitmq-server-devel
Requires: rabbitmq-server >= 1.6.0-alt3 erlang-rfc4627
Summary: HTTP protocol adapter for RabbitMQ

%define server_root %_datadir/%name
%define rabbitmq_ebin %_erllibdir/rabbitmq-server/ebin

%package demo
Summary: %name demo site
License: MPLv1.1
Group: Development/Erlang
Requires: %name = %version-%release

%description
An AMQP-over-HTTP protocol binding for RabbitMQ and some Javascript
libraries for interacting with RabbitMQ over HTTP, as well as some
examples

%description demo
Demo site which shows realtime web applications build on
top of javascript and rabbitmq

%prep
%setup  

%build
sed -i 's|@sysconfdir@|%_sysconfdir|g' %SOURCE1
sed -i 's|@server_root@|%server_root|g' %SOURCE2
sed -i 's|@logdir@|%_logdir|g' %SOURCE2
%make_build RABBIT_SERVER_INCLUDE_DIR=%_erllibdir/rabbitmq-server/include

%install
mkdir -p %buildroot%rabbitmq_ebin
mkdir -p %buildroot%_logdir/%oname
mkdir -p %buildroot%server_root

install -D -m 664 ebin/*.beam %buildroot%rabbitmq_ebin
install -D -m 664 %SOURCE1 %buildroot%_sysconfdir/%oname/conf.d/http2.conf
install -D -m 664 %SOURCE2 %buildroot%_sysconfdir/%oname/httpd.conf
cp -r server_root/htdocs %buildroot%server_root/

#Copy all necessary lib files etc.
mkdir -p %buildroot%_sysconfdir/%oname

%post
%post_service %oname

%preun
%preun_service %oname

%files
%rabbitmq_ebin/*.beam
%config(noreplace) %_sysconfdir/%oname/conf.d/*.conf
%config(noreplace) %_sysconfdir/%oname/*.conf

%files demo
%attr(0750, rabbitmq, rabbitmq) %server_root

%changelog
* Sun Sep 20 2009 Maxim Ivanov <redbaron at altlinux.org> 0.0.1-alt1.hg.4b8597
- Initial build for ALT Linux


