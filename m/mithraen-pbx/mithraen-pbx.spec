Name: mithraen-pbx
Summary: Asterisk fax support scripts
Version: 0.2
Release: alt3
License: GPL
Group: System/Servers
BuildArch: noarch
Packager: Denis Smirnov <mithraen@altlinux.ru>
Source: %name-%version.tar

%package fax
Summary: Asterisk fax support scripts
Group: System/Servers
BuildArch: noarch
Obsoletes: seiros-pbx-fax
Requires: tcllib
Requires: libtiff-utils
Requires: postfix

%description fax
Asterisk fax support scripts


%package systemtest
Summary: Autotest hardware configuration for using with Asterisk PBX
Group: System/Base
BuildArch: noarch
Obsoletes: seiros-pbx-systemtest
Requires: csed

%description systemtest
Autotest hardware configuration for using with Asterisk PBX

%description
Asterisk fax support scripts


%prep
%setup

%install
install -D -m755 fax-send 		%buildroot%_bindir/fax-send
mkdir -p %buildroot%_sbindir
mkdir -p %buildroot%_sysconfdir/cron.d
mkdir -p %buildroot%_datadir/mithraen-pbx-systemtest/
install -D -m755 mithraen-pbx-systemtest   %buildroot%_sbindir/mithraen-pbx-systemtest
install -D -m644 crontab %buildroot%_sysconfdir/cron.d/mithraen-pbx-systemtest
for s in sensors/*; do
    install -m755 $s %buildroot%_datadir/mithraen-pbx-systemtest/
done

%post systemtest
if [ -f %_initdir//crond ]; then
  service crond reload
fi
if [ -c /dev/tty11 ]; then
	%_sbindir/mithraen-pbx-systemtest > /dev/tty11 2> /dev/null ||:
fi

%files fax
%_bindir/fax-send

%files systemtest
%_sbindir/mithraen-pbx-systemtest
%_sysconfdir/cron.d/mithraen-pbx-systemtest
%dir %_datadir/mithraen-pbx-systemtest
%_datadir/mithraen-pbx-systemtest/*

%changelog
* Tue Sep 08 2009 Denis Smirnov <mithraen@altlinux.ru> 0.2-alt3
- add obsoletes to seiros-pbx-fax

* Sun Aug 30 2009 Denis Smirnov <mithraen@altlinux.ru> 0.2-alt2
- small fix

* Sat Aug 29 2009 Denis Smirnov <mithraen@altlinux.ru> 0.2-alt1
- add mithraen-pbx-systemtest

* Sat Aug 29 2009 Denis Smirnov <mithraen@altlinux.ru> 0.1-alt1
- first build for Sisyphus

