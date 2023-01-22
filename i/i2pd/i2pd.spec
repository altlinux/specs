%define i2pduser _i2pd
%define _i2pd_root %_sharedstatedir/%name

Name: i2pd
Version: 2.45.1
Release: alt1

Summary: Full C++ implementation of I2P router

License: BSD-3-Clause
Group: System/Servers
Url: https://github.com/PurpleI2P/i2pd

# Source0-git: https://github.com/PurpleI2P/i2pd.git
Source0: %name-%version.tar
Patch: %name-%version-upstream.patch

ExcludeArch: %ix86

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
%ifarch %e2k
%add_optflags -mno-aes
%endif
export CXXFLAGS="%optflags"
pushd build
%cmake_insource \
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
* Sun Jan 22 2023 Vitaly Lipatov <lav@altlinux.ru> 2.45.1-alt1
- new version 2.45.1 (with rpmrb script)

* Mon Dec 19 2022 Vitaly Lipatov <lav@altlinux.ru> 2.44.0-alt1
- new version 2.44.0 (with rpmrb script)

* Thu Aug 25 2022 Vitaly Lipatov <lav@altlinux.ru> 2.43.0-alt1
- new version 2.43.0 (with rpmrb script)

* Tue Jun 07 2022 Vitaly Lipatov <lav@altlinux.ru> 2.42.1-alt1
- new version 2.42.1 (with rpmrb script)

* Wed Feb 23 2022 Vitaly Lipatov <lav@altlinux.ru> 2.41.0-alt1
- new version 2.41.0 (with rpmrb script)

* Sun Dec 19 2021 Vitaly Lipatov <lav@altlinux.ru> 2.40.0-alt1
- new version 2.40.0 (with rpmrb script)

* Tue Jul 27 2021 Ilya Kurdyukov <ilyakurdyukov@altlinux.org> 2.38.0-alt2
- fixed build for Elbrus

* Mon Jun 07 2021 Vitaly Lipatov <lav@altlinux.ru> 2.38.0-alt1
- new version 2.38.0 (with rpmrb script)

* Fri Feb 05 2021 Vitaly Lipatov <lav@altlinux.ru> 2.35.0-alt1
- new version 2.35.0 (with rpmrb script)

* Wed Sep 02 2020 Vitaly Lipatov <lav@altlinux.ru> 2.33.0-alt1
- new version 2.33.0 (with rpmrb script)

* Fri Aug 21 2020 Vitaly Lipatov <lav@altlinux.ru> 2.32.1-alt1
- new version 2.32.1 (with rpmrb script)

* Fri May 29 2020 Vitaly Lipatov <lav@altlinux.ru> 2.31.0-alt1
- new version 2.31.0 (with rpmrb script)

* Sun Mar 01 2020 Vitaly Lipatov <lav@altlinux.ru> 2.30.0-alt1
- new version 2.30.0 (with rpmrb script)

* Sun Jan 26 2020 Vitaly Lipatov <lav@altlinux.ru> 2.29.0-alt1
- new version 2.29.0 (with rpmrb script)

* Sat Sep 07 2019 Vitaly Lipatov <lav@altlinux.ru> 2.28.0-alt1
- new version 2.28.0 (with rpmrb script)

* Fri Aug 16 2019 Vitaly Lipatov <lav@altlinux.ru> 2.27.0-alt1
- new version 2.27.0 (with rpmrb script)

* Tue Jun 18 2019 Vitaly Lipatov <lav@altlinux.ru> 2.26.0-alt1
- new version 2.26.0 (with rpmrb script)

* Thu May 30 2019 Vitaly Lipatov <lav@altlinux.ru> 2.25.0-alt1
- new version 2.25.0 (with rpmrb script)

* Thu Apr 11 2019 Vitaly Lipatov <lav@altlinux.ru> 2.24.0-alt1
- new version 2.24.0 (with rpmrb script)

* Mon Dec 17 2018 Vitaly Lipatov <lav@altlinux.ru> 2.22.0-alt1
- new version 2.22.0 (with rpmrb script)

* Wed Aug 29 2018 Grigory Ustinov <grenka@altlinux.org> 2.18.0-alt1.2
- NMU: Rebuild with new openssl 1.1.0.

* Thu May 31 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 2.18.0-alt1.1
- NMU: rebuilt with boost-1.67.0

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
