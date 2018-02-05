%define i2pduser _i2pd
%define _i2pd_root %_sharedstatedir/%name

Name: i2pd
Version: 2.18.0
Release: alt1

Summary: Full C++ implementation of I2P router

License: BSD-3-Clause
Group: System/Servers
Url: https://github.com/PurpleI2P/i2pd

# Source0-git: https://github.com/PurpleI2P/i2pd.git
Source0: %name-%version.tar
Patch: %name-%version-upstream.patch
Source1: %name.service
Source2: %name.logrotate
Source3: i2p.conf
Source4: tunnels.conf
Source5: %name.sysconfig

BuildRequires: rpm-build-intro rpm-macros-cmake

BuildRequires: gcc-c++ cmake libssl-devel boost-devel boost-filesystem-devel boost-program_options-devel boost-asio-devel libminiupnpc-devel zlib-devel

BuildRequires: /proc

%description
I2P router written in C++.

See documentation at https://i2pd.readthedocs.io/en/latest/

%prep
%setup
%patch -p1

%build
export CXXFLAGS="%optflags"
pushd build
#cmake_insource
cmake \
      -DCMAKE_BUILD_TYPE=Debug \
      -DWITH_BINARY=ON \
      -DWITH_LIBRARY=OFF \
      -DWITH_STATIC=OFF \
      -DWITH_UPNP=ON \
      -DWITH_AESNI=OFF \
      -DWITH_HARDENING=ON \
      -DWITH_PCH=OFF \
      -DCMAKE_INSTALL_PREFIX=%prefix \
      .

%make_build
popd

%install
pushd build
%makeinstall_std
popd

# fix strange install
rm -rf %buildroot/%prefix/{LICENSE,lib/lib*.a,src/}

install -pDm 644 contrib/subscriptions.txt %buildroot%_sysconfdir/%name/subscriptions.txt
install -pDm 644 debian/%name.1 %buildroot%_man1dir/%name.1
install -pDm 644 %SOURCE1 %buildroot%_unitdir/%name.service
install -pDm 644 %SOURCE2 %buildroot%_sysconfdir/logrotate.d/%name
install -pDm 644 %SOURCE3 %buildroot%_sysconfdir/%name/i2p.conf
install -pDm 644 %SOURCE4 %buildroot%_sysconfdir/%name/tunnels.conf
install -pDm 644 %SOURCE5 %buildroot%_sysconfigdir/%name

mkdir -p %buildroot%_i2pd_root %buildroot%_datadir/%name/
cp -rav contrib/certificates %buildroot%_datadir/%name/

pushd %buildroot%_i2pd_root
ln -s $(relative %_sysconfdir/%name/i2p.conf %_i2pd_root/i2p.conf) i2p.conf
ln -s $(relative %_sysconfdir/%name/tunnels.conf %_i2pd_root/tunnels.conf) tunnels.conf
ln -s $(relative %_sysconfdir/%name/subscriptions.txt %_i2pd_root/subscriptions.txt) subscriptions.txt
popd

mkdir -p %buildroot%_logdir/%name
touch %buildroot%_logdir/%name/%name.log

%pre
/usr/sbin/groupadd -r -f %i2pduser
/usr/sbin/useradd -r -g %i2pduser -d %_i2pd_root -s /dev/null -c 'I2pd user' %i2pduser >/dev/null 2>&1 ||:

%post
%post_service %name

%preun
%preun_service %name

%files
%doc LICENSE README.md
%_bindir/%name
%_datadir/%name/
%_unitdir/%name.service
%_man1dir/%name.1.*
%ghost %attr(640,%i2pduser,adm) %_logdir/%name/%name.log
%config(noreplace) %_sysconfdir/logrotate.d/%name

# configs:
%defattr(640,root,%i2pduser,710)
%dir %_sysconfdir/%name/
%config(noreplace) %_sysconfigdir/%name
%config(noreplace) %_sysconfdir/%name/i2p.conf
%config(noreplace) %_sysconfdir/%name/tunnels.conf
%config(noreplace) %_sysconfdir/%name/subscriptions.txt

%defattr(640,root,%i2pduser,3770)
# root dir:
%_i2pd_root/
# log dir:
%dir %_logdir/%name/

%changelog
* Mon Feb 05 2018 Vitaly Lipatov <lav@altlinux.ru> 2.18.0-alt1
- new version 2.18.0 (with rpmrb script)

* Mon Oct 23 2017 Vitaly Lipatov <lav@altlinux.ru> 2.15.0-alt1
- new version 2.15.0 (with rpmrb script)
- fix daemon args

* Mon Oct 23 2017 Vitaly Lipatov <lav@altlinux.ru> 2.14.0-alt2
- add /etc/sysconfig/i2pd support

* Mon Jun 05 2017 Vitaly Lipatov <lav@altlinux.ru> 2.14.0-alt1
- new version 2.14.0 (with rpmrb script)

* Sun May 28 2017 Vitaly Lipatov <lav@altlinux.ru> 2.13.0-alt1
- new version (2.13.0) with rpmgs script

* Thu Jan 28 2016 Terechkov Evgenii <evg@altlinux.org> 2.3.0-alt4
- git-20160128

* Tue Jan 26 2016 Terechkov Evgenii <evg@altlinux.org> 2.3.0-alt3
- Fix daemon logging (with patch)

* Sun Jan 24 2016 Terechkov Evgenii <evg@altlinux.org> 2.3.0-alt2
- Pack as system-wide service

* Fri Jan 22 2016 Terechkov Evgenii <evg@altlinux.org> 2.3.0-alt1
- Initial build for ALT Linux Sisyphus
