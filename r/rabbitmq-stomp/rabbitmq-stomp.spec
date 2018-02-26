%define _unpackaged_files_terminate_build 1
%define oname rabbitmq

Name: rabbitmq-stomp
Version: 0.0.1
Release: alt1.hg.9003ff
License: MPLv1.1
Group: System/Servers
Source: %name-%version.tar
Source1: %oname-stomp.conf
URL: http://www.rabbitmq.com/
Packager: Maxim Ivanov <redbaron@altlinux.org>

BuildRequires(pre): rpm-macros-erlang
BuildRequires: erlang-devel, erlang-otp-devel
BuildRequires: rabbitmq-server-devel
Requires: rabbitmq-server >= 1.6.0-alt3 
Summary: STOMP protocol adapter for RabbitMQ

%define rabbitmq_ebin %_erllibdir/rabbitmq-server/ebin

%description
A gateway for exposing AMQP functionality via the STOMP protocol, as
implemented by many clients for various programming languages, and a
few other servers besides RabbitMQ.

%prep
%setup  

%build
%make_build RABBIT_SERVER_INCLUDE_DIR=%_erllibdir/rabbitmq-server/include

%install
mkdir -p %buildroot%rabbitmq_ebin

install -D -m 664 ebin/*.beam %buildroot%rabbitmq_ebin
install -D -m 664 %SOURCE1 %buildroot%_sysconfdir/%oname/conf.d/stomp.conf

%post
%post_service %oname

%preun
%preun_service %oname

%files
%rabbitmq_ebin/*.beam
%config(noreplace) %_sysconfdir/%oname/conf.d/*.conf

%changelog
* Sun Sep 20 2009 Maxim Ivanov <redbaron at altlinux.org> 0.0.1-alt1.hg.9003ff
- Initial build for ALT Linux

