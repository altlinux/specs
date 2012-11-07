%define _unpackaged_files_terminate_build 1
%add_erlang_req_modules_skiplist bad

%define oname rabbitmq

Name: rabbitmq-server
Version: 2.8.7
Release: alt1
License: MPLv1.1
BuildArch: noarch
Group: System/Servers
Source: %name-%version.tar
Source1: rabbitmq-server.service
Source2: rabbitmq-script-wrapper
Source3: rabbitmq-server.logrotate
Source4: rabbitmq.conf
Source5: include.mk
URL: http://www.rabbitmq.com/
Packager: Maxim Ivanov <redbaron@altlinux.org>


BuildRequires(pre): rpm-build-erlang
BuildRequires: erlang-devel
BuildRequires: python-module-simplejson
BuildRequires: erlang-otp-devel
BuildRequires: xmlto
BuildRequires: zip
BuildRequires: unzip
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
sed -i 's|@RABBITMQ_DIR@|%_erllibdir/%name|g' %SOURCE5
%make_build

%install
%make_install TARGET_DIR=%buildroot%_erllibdir/%name \
        SBIN_DIR=%buildroot%_libexecdir/%oname \
        MAN_DIR=%buildroot%_mandir \
        install

mkdir -p %buildroot%_localstatedir/%oname/mnesia
mkdir -p %buildroot%_logdir/%oname

#Copy all necessary lib files etc.
install -p -D -m 0755 %SOURCE1 %buildroot%_unitdir/%oname.service
install -p -D -m 0755 %SOURCE2 %buildroot%_sbindir/rabbitmqctl
install -p -D -m 0755 %SOURCE2 %buildroot%_sbindir/%name

install -p -D -m 0644 %SOURCE3 %buildroot%_logrotatedir/%name
install -p -D -m 0644 %SOURCE4 %buildroot%_sysconfdir/%oname/%oname.conf

install -p -D -m 0644 %SOURCE5 %buildroot%_datadir/%name/include.mk

mkdir -p %buildroot%_sysconfdir/%oname/conf.d
rm %buildroot%_erllibdir/%name/{LICENSE,LICENSE-MPL-RabbitMQ,INSTALL}

mkdir -p %buildroot/%_erlanglibdir/%name/priv

%pre
%_sbindir/groupadd -r -f rabbitmq &>/dev/null
%_sbindir/useradd -r -g rabbitmq  -d %_localstatedir/rabbitmq -s /dev/null \
   -c 'RabbitMQ messaging server' -M -n rabbitmq &>/dev/null ||:

%post
if [ $1 -eq 1 ] ; then
    # Initial installation
    /bin/systemctl daemon-reload >/dev/null 2>&1 || :
fi


%preun
if [ $1 -eq 0 ] ; then
    # Package removal, not upgrade
    /bin/systemctl --no-reload disable rabbitmq.service > /dev/null 2>&1 || :
    /bin/systemctl stop rabbitmq.service > /dev/null 2>&1 || :
fi

%postun
/bin/systemctl daemon-reload >/dev/null 2>&1 || :
if [ $1 -ge 1 ] ; then
    # Package upgrade, not uninstall
    /bin/systemctl try-restart rabbitmq.service >/dev/null 2>&1 || :
fi

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
%_unitdir/%oname.service
%doc LICENSE LICENSE-MPL-RabbitMQ README INSTALL

%files -n %name-devel
%_erlanglibdir/%name/include
%_datadir/%name

%changelog
* Thu Oct 04 2012 Pavel Shilovsky <piastry@altlinux.org> 2.8.7-alt1
- New version 2.8.7

* Sat Oct 31 2009 Maxim Ivanov <redbaron at altlinux.org> 1.7.0-alt1
- New version
- New plugin architecture introduced

* Sun Sep 20 2009 Maxim Ivanov <redbaron at altlinux.org> 1.6.0-alt3
- New conf.d dir for plugable addons configs
- fix condreload arg support in init script

* Mon Jul 20 2009 Maxim Ivanov <redbaron at altlinux.org> 1.6.0-alt2
- Header files packed separately now
- Fix added condstop to init script

* Sun Jul 19 2009 Maxim Ivanov <redbaron at altlinux.org> 1.6.0-alt1
- Initial build for ALTLinux

