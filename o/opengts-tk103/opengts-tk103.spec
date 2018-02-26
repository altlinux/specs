Name: opengts-tk103
Version: 0.0.2
Release: alt2

Summary: Tools for tk103 gps tracker
License: GPLv3
Group: Networking/Other

Source: %name-%version.tar

Source1: tk103-gprs.init
Source2: tk103-query.sh
Source3: tk103-query.init
Source4: tk103-sms.sh
Source5: tk103-sms.init
Source6: query.conf
Source7: sms.conf

BuildRequires: libmysqlclient-devel

%description
Tools for reading and decoding tk103 protocol

%prep
%setup

%build
autoreconf --install
%configure
%make_build

%install
%makeinstall_std
install -pD -m755 %SOURCE1 %buildroot%_initdir/tk103-gprs
cp -p %SOURCE2 %buildroot%_bindir/tk103-query
install -pD -m755 %SOURCE3 %buildroot%_initdir/tk103-query
cp -p %SOURCE4 %buildroot%_bindir/tk103-sms
install -pD -m755 %SOURCE5 %buildroot%_initdir/tk103-sms
install -pD -m644 %SOURCE6 %buildroot%_sysconfdir/opengts-tk103/query.conf
install -pD -m644 %SOURCE7 %buildroot%_sysconfdir/opengts-tk103/sms.conf

%files
%doc AUTHORS ChangeLog COPYING NEWS README*
%config(noreplace) %_initdir/tk103-gprs
%config(noreplace) %_initdir/tk103-query
%config(noreplace) %_initdir/tk103-sms
%config(noreplace) %_sysconfdir/opengts-tk103/gprs.conf
%config(noreplace) %_sysconfdir/opengts-tk103/sms.conf
%config(noreplace) %_sysconfdir/opengts-tk103/query.conf
%_bindir/*

%changelog
* Mon Jan 31 2011 Timur Aitov <timonbl4@altlinux.org> 0.0.2-alt2
- 0.0.2-alt2

* Fri Dec 10 2010 Timur Aitov <timonbl4@altlinux.org> 0.0.2-alt1
- 0.0.2-alt1

* Thu Dec 02 2010 Timur Aitov <timonbl4@altlinux.org> 0.0.1-alt1
- first release

