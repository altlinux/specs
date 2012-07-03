%define _unpackaged_files_terminate_build 1

%define oname rabbitmq

Name: rabbitmq-server
Version: 1.6.0
Release: alt3
License: MPLv1.1
Group: System/Servers
Source: %name-%version.tar
Source1: rabbitmq-server.init
Source2: rabbitmq-script-wrapper
Source3: rabbitmq-server.logrotate
Source4: rabbitmq.conf
URL: http://www.rabbitmq.com/
Packager: Maxim Ivanov <redbaron@altlinux.org>

BuildRequires(pre): rpm-macros-erlang
BuildRequires: erlang-devel, python-module-simplejson, erlang-otp-devel
Requires: erlang
Summary: The RabbitMQ server

%description
RabbitMQ is an implementation of AMQP, the emerging standard for high
performance enterprise messaging. The RabbitMQ server is a robust and
scalable implementation of an AMQP broker.

%package -n %name-devel
Summary: %name header files
License: MPLv1.1
Group: Development/Erlang

%description -n %name-devel
Erlang header files for %name 

%prep
%setup -q

%build
sed -i 's|@libexecdir@|%_libexecdir|g' %SOURCE2
sed -i 's|@localstatedir@|%_localstatedir|g' %SOURCE2
%make_build

%install
%make_install TARGET_DIR=%buildroot%_erllibdir/%name \
        SBIN_DIR=%buildroot%_libexecdir/%oname \
        MAN_DIR=%buildroot%_mandir \
        install

mkdir -p %buildroot%_localstatedir/%oname/mnesia
mkdir -p %buildroot%_logdir/%oname

#Copy all necessary lib files etc.
install -p -D -m 0755 %SOURCE1 %{buildroot}%{_initrddir}/%oname
install -p -D -m 0755 %SOURCE2 %{buildroot}%{_sbindir}/rabbitmqctl
install -p -D -m 0755 %SOURCE2 %{buildroot}%{_sbindir}/rabbitmq-server
install -p -D -m 0755 %SOURCE2 %{buildroot}%{_sbindir}/rabbitmq-multi

install -p -D -m 0644 %SOURCE3 %buildroot%_logrotatedir/%name
install -p -D -m 0644 %SOURCE4 %buildroot%_sysconfdir/%oname/rabbitmq.conf

mkdir -p %buildroot%_sysconfdir/%oname/conf.d
rm %buildroot%_erllibdir/%name/{LICENSE,LICENSE-MPL-RabbitMQ,INSTALL}

%pre
%_sbindir/groupadd -r -f rabbitmq &>/dev/null
%_sbindir/useradd -r -g rabbitmq  -d %_localstatedir/rabbitmq -s /dev/null \
   -c 'RabbitMQ messaging server' -M -n rabbitmq &>/dev/null ||:

%post
%post_service %oname

%preun
%preun_service %oname

%files
%_sbindir/*
%_libexecdir/%oname
%_erlanglibdir/%name
%exclude %_erlanglibdir/%name/include
%attr(0750, rabbitmq, rabbitmq) %dir %_localstatedir/%oname
%attr(0750, rabbitmq, rabbitmq) %dir %_logdir/%oname
%config(noreplace) %_logrotatedir/*
%config(noreplace) %_sysconfdir/%oname
%_man1dir/*
%_man5dir/*
%_initrddir/%oname
%doc LICENSE LICENSE-MPL-RabbitMQ README INSTALL

%files -n %name-devel
%_erlanglibdir/%name/include

%changelog
* Sun Sep 20 2009 Maxim Ivanov <redbaron at altlinux.org> 1.6.0-alt3
- New conf.d dir for plugable addons configs
- fix condreload arg support in init script

* Mon Jul 20 2009 Maxim Ivanov <redbaron at altlinux.org> 1.6.0-alt2
- Header files packed separately now 
- Fix added condstop to init script

* Sun Jul 19 2009 Maxim Ivanov <redbaron at altlinux.org> 1.6.0-alt1
- Initial build for ALTLinux

