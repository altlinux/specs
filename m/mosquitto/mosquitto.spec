%define mosquitto_user      mosquitto
%define mosquitto_group     mosquitto
%define mosquitto_dir      /var/lib/%mosquitto_user

Name: mosquitto
Version: 1.4.7
Release: alt1

Summary: Mosquitto is an open source implementation of a server for version 3.1 and 3.1.1 of the MQTT protocol

License: This project is dual licensed under the Eclipse Public License 1.0 and the Eclipse Distribution License 1.0 as described in the epl-v10 and edl-v10 files
Group: Development/C++
Url: https://github.com/philsquared/Catch

Packager: Pavel Vainerman <pv@altlinux.ru>

# http://mosquitto.org/
Source: %name-%version.tar

# Automatically added by buildreq on Mon Feb 01 2016
# optimized out: libcom_err-devel libkrb5-devel libstdc++-devel
BuildRequires: gcc-c++ libcares-devel libssl-devel libuuid-devel

%description
The Mosquitto project has been created to provide a light weight, open-source
implementation, of an MQTT broker to allow new, existing, and emerging
applications for Machine-to-Machine (M2M) and Internet of Things (IoT).

%package devel
Group: Development/C
Summary: Libraries needed to develop for mosquitto
Requires: %name = %version-%release

%description devel
Libraries needed to develop for mosquitto

%prep
%setup 

%build
subst 's|prefix=/usr/local|prefix=/usr|g' config.mk
%make_build

%install
%makeinstall_std
%ifarch x86_64
mkdir -p %buildroot%_libdir
mv -f %buildroot/usr/lib/* %buildroot%_libdir/
%endif

chmod a-x %buildroot%_includedir/*.h

mkdir -p %buildroot/%mosquitto_dir

mkdir -p %buildroot/%_initdir
mv .gear/%name %buildroot%_initdir/

mkdir -p %buildroot/%_sysconfdir/sysconfig
mv .gear/%name.sysconf %buildroot%_sysconfdir/sysconfig/%name

mkdir -p %buildroot/%_sysconfdir/%name
mv .gear/%name.conf %buildroot%_sysconfdir/%name

%pre
%_sbindir/groupadd -r -f %mosquitto_group 2>/dev/null ||:
%_sbindir/useradd -M -r -g %mosquitto_group -c 'Mosquitto daemon' -s /dev/null -d %mosquitto_dir %mosquitto_user 2>/dev/null ||:

%post
%post_service %name

%preun
%preun_service %name
        
%files
%dir %_sysconfdir/%name
%config %dir %_sysconfdir/%name/*
%config %_sysconfdir/sysconfig/%name
%_libdir/*.so.*
%_bindir/*
%_sbindir/*
%_man1dir/*
%_man3dir/*
%_man5dir/*
%_man7dir/*
%_man8dir/*
%attr(750,%mosquitto_user,%mosquitto_group) %dir %mosquitto_dir/
%_initdir/*

%files devel
%_includedir/*.h
%_libdir/*.so

%changelog
* Sun Feb 07 2016 Pavel Vainerman <pv@altlinux.ru> 1.4.7-alt1
- fixed header files attributes
- add service file for init.d
- create mosquitto_user and group 
- add sysconfig/mosquitto

* Mon Feb 01 2016 Pavel Vainerman <pv@altlinux.ru> 1.4.7-alt0.4
- test build for x86_64

* Mon Feb 01 2016 Pavel Vainerman <pv@altlinux.ru> 1.4.7-alt0.3
- test build

* Mon Feb 01 2016 Pavel Vainerman <pv@altlinux.ru> 1.4.7-alt0.2
- initial build
