Name: ike
Version: 2.2.1
Release: alt1
Summary: Shrew Soft VPN Client For Linux
Group: Communications
License: Sleepycat
Url: http://www.shrew.net/
Source0: %name-%version.tar
Source1: iked.service
Source2: ike.desktop
Source3: ike.logrotate
Source4: iked.init

Patch1: ike-2.2.1-paths.patch
Patch2: ike-2.2.1-spelling.patch

BuildRequires: cmake flex bison openldap-devel libqt4-devel openssl-devel libedit-devel gcc-c++ desktop-file-utils
#BuildRequires:  systemd

#Requires(post): systemd
#Requires(preun): systemd
#Requires(postun): systemd

%description
This free IPSEC VPN client can be used to communicate with
Open Source IPSEC VPN servers as well as some commercial
IPSEC VPN servers.

%prep
%setup
%patch1 -p1
%patch2 -p1

#sed -i 's:/var/log/:/var/log/iked/:' source/iked/iked.conf.sample
sed -i 's/\r//' TODO.TXT

%build
#%%cmake -DQTGUI=YES -DNATT=YES -DCMAKE_INSTALL_PREFIX:PATH=%prefix -DETCDIR:PATH=%_sysconfdir \
#      -DMANDIR:PATH=%_mandir -DLDAP=YES -DLIBDIR=%_libdir
#%%cmake_insource

cmake . \
	-DCMAKE_SKIP_RPATH:BOOL=ON \
	-DCMAKE_SKIP_INSTALL_RPATH:BOOL=yes \
	-DCMAKE_C_FLAGS:STRING='-pipe -Wall -g -O2' \
	-DCMAKE_CXX_FLAGS:STRING='-pipe -Wall -g -O2' \
	-DCMAKE_Fortran_FLAGS:STRING='-pipe -Wall -g -O2' \
	-DCMAKE_INSTALL_PREFIX=/usr \
	-DINCLUDE_INSTALL_DIR:PATH=/usr/include \
	-DLIB_INSTALL_DIR:PATH=/usr/lib64 \
	-DSYSCONF_INSTALL_DIR:PATH=/etc \
	-DSHARE_INSTALL_PREFIX:PATH=/usr/share \
	%if "lib64" == "lib64"
	-DLIB_SUFFIX="64" \
	%else
	-DLIB_SUFFIX="" \
	%endif
	-DLIB_DESTINATION=lib64 \
	-DQTGUI=YES -DNATT=YES -DCMAKE_INSTALL_PREFIX:PATH=%prefix -DETCDIR:PATH=%_sysconfdir \
	-DMANDIR:PATH=%_mandir -DLDAP=YES -DLIBDIR=%_libdir

%install
%makeinstall_std

install -d -p $RPM_BUILD_ROOT%_initdir
install -d -p $RPM_BUILD_ROOT%_unitdir
install -d -p $RPM_BUILD_ROOT%_runtimedir/%{name}d
#install -d -p $RPM_BUILD_ROOT%_logdir/%{name}d
install -d -p $RPM_BUILD_ROOT%_datadir/pixmaps
#install -D -p -m0755 %SOURCE1 $RPM_BUILD_ROOT%_unitdir/%{name}d.service
install -D -p -m0755 %SOURCE4 $RPM_BUILD_ROOT%_initdir/%{name}d
mv $RPM_BUILD_ROOT%_sysconfdir/iked.conf.sample $RPM_BUILD_ROOT%_sysconfdir/iked.conf

# Create desktop file
install -p source/qikea/png/ikea.png $RPM_BUILD_ROOT%_datadir/pixmaps/%{name}a.png
desktop-file-install --dir $RPM_BUILD_ROOT/%_datadir/applications \
    %SOURCE2

# Create /etc/logrotate.d/ike
mkdir -p $RPM_BUILD_ROOT%_sysconfdir/logrotate.d
install -m 0644 -p %SOURCE3 $RPM_BUILD_ROOT%_sysconfdir/logrotate.d/%name

%post
%post_service iked

%preun
%preun_service iked
%files
%doc LICENSE.TXT TODO.TXT
%config(noreplace) %_sysconfdir/iked.conf
%config(noreplace) %_sysconfdir/logrotate.d/ike
%_libdir/*.so.*
%_libdir/*.so
#%_unitdir/%{name}d.service
%_initdir/%{name}d
%_bindir/*
%_sbindir/*
%_mandir/man*/*
%_datadir/pixmaps/*
%_datadir/applications/*
%dir %_runtimedir/%{name}d
#%dir %_logdir/%{name}d

%changelog
* Mon Feb 05 2018 Lenar Shakirov <snejok@altlinux.ru> 2.2.1-alt1
- Initial build for ALT (based on 2.2.1-7.fc24.src)

