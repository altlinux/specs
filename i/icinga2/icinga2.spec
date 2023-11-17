# Copyright (c) 2021 SUSE LLC
# Copyright (c) 2023 BaseALT Ltd
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

%define _unpackaged_files_terminate_build 1

%define plugindir %_libexecdir/nagios/plugins
%define _rundir /run

#%if %(uname -m) != "x86_64"
#%define march_flag -march=i686
#%endif

%def_disable configure_systemd_limits
%def_without selinux

%define icinga_user icinga
%define icinga_group icinga
%define icingacmd_group icingacmd

# enable unity builds by default for all architectures except arm32
%ifnarch armh
%def_with unity_build
%else
%def_without unity_build
%endif

Summary:        Network monitoring application
License:        GPL-2.0-or-later
Group:          Monitoring

Name:           icinga2
Version:        2.14.0
Release:        alt3
URL:            https://www.icinga.com/
Source:         https://github.com/Icinga/%name/archive/v%version/%name-%version.tar

Patch0:         icinga2-graphite.patch
Patch1:         icinga2-vim_syntax.patch
Patch2:         icinga2-fix-unitdir-alt.patch

Requires:       %name-bin = %version-%release
Requires:       %name-common = %version-%release
Requires:       vim-%name = %version-%release
Requires:       nano-%name = %version-%release
Requires:       nagios-plugins nagios-plugins-local nagios-plugins-network

BuildRequires:  libyajl-devel
BuildRequires:  libedit-devel
BuildRequires:  ncurses-devel
BuildRequires:  gcc-c++
BuildRequires:  libssl-devel
BuildRequires:  libstdc++-devel

BuildRequires(pre):  cmake rpm-macros-cmake

BuildRequires:  flex >= 2.5.35

BuildRequires:  boost-context-devel >= 1.66
BuildRequires:  boost-coroutine-devel >= 1.66
BuildRequires:  boost-filesystem-devel >= 1.66
BuildRequires:  boost-iostreams-devel >= 1.66
BuildRequires:  boost-program_options-devel >= 1.66
BuildRequires:  boost-regex-devel >= 1.66
BuildRequires:  boost-system-devel >= 1.66
BuildRequires:  boost-test-devel >= 1.66
BuildRequires:  boost-thread-devel >= 1.66
BuildRequires:  boost-asio-devel >= 1.66
BuildRequires:  boost-signals-devel >= 1.66
BuildRequires:  boost-interprocess-devel >= 1.66

BuildRequires:  pkgconfig(libsystemd)
BuildRequires:  logrotate

BuildRequires:  libmariadb-devel
BuildRequires:  postgresql-devel

%if_with selinux
BuildRequires:  checkpolicy selinux-policy-alt
%endif

%description
Meta package for Icinga 2 Core and DB IDO.

%package bin
Summary:        Icinga 2 binaries and libraries
Group:          Monitoring

%description bin
Icinga 2 is a general-purpose network monitoring application.
This subpackage provides the binaries for Icinga 2 Core.

%package common
Summary:        Common Icinga 2 configuration
Group:          Monitoring

%description common
This subpackage provides common directories, and the UID and GUID definitions
among Icinga 2 related packages.

%package doc
Summary:        Documentation for Icinga 2
Group:          Documentation

%description doc
This subpackage provides documentation for Icinga 2.

%package ido-mysql
Summary:        IDO MySQL database backend for Icinga 2
Group:          Monitoring

%description ido-mysql
Icinga 2 IDO mysql database backend. Compatible with Icinga 1.x
IDOUtils schema >= 1.12.

%package ido-pgsql
Summary:        IDO PostgreSQL database backend for Icinga 2
Group:          Monitoring

%description ido-pgsql
Icinga 2 IDO PostgreSQL database backend. Compatible with Icinga 1.x
IDOUtils schema >= 1.12.

%global selinux_variants mls targeted
%global selinux_modulename %name

%package selinux
Summary:        SELinux policy module supporting icinga2
Group:          System/Base

%description selinux
SELinux policy module supporting icinga2.

%package -n vim-%name
Summary:        Vim syntax highlighting for icinga2
Group:          Editors

%description -n vim-%name
Provides Vim syntax highlighting for icinga2.

%package -n nano-%name
Summary:        Nano syntax highlighting for icinga2
Group:          Editors

%description -n nano-%name
Provides Nano syntax highlighting for icinga2.

%prep
%setup
%patch0 -p1
%patch1 -p1
%patch2 -p2

%build
CMAKE_OPTS="
	-DCMAKE_INSTALL_SYSCONFDIR=%_sysconfdir \
	-DCMAKE_INSTALL_LOCALSTATEDIR=%_var \
	-DICINGA2_LTO_BUILD=ON \
        -DBoost_NO_BOOST_CMAKE=ON \
        -DICINGA2_PLUGINDIR=%plugindir \
        -DICINGA2_RUNDIR=%_rundir \
        -DICINGA2_SYSCONFIGFILE=%_sysconfdir/sysconfig/%name \
        -DICINGA2_USER=%icinga_user \
        -DICINGA2_GROUP=%icinga_group \
        -DICINGA2_COMMAND_GROUP=%icingacmd_group"

CMAKE_OPTS="$CMAKE_OPTS -DICINGA2_WITH_STUDIO=true"

%if_with unity_build
CMAKE_OPTS="$CMAKE_OPTS -DICINGA2_UNITY_BUILD=ON"
%else
CMAKE_OPTS="$CMAKE_OPTS -DICINGA2_UNITY_BUILD=OFF"
%endif

CMAKE_OPTS="$CMAKE_OPTS -DUSE_SYSTEMD=ON"

%cmake $CMAKE_OPTS
%cmake_build

%if_with selinux
pushd tools/selinux
for selinuxvariant in %selinux_variants
do
  make NAME=$selinuxvariant -f %_datadir/selinux/alt/Makefile
  mv %selinux_modulename.pp %selinux_modulename.pp.$selinuxvariant
  make NAME=$selinuxvariant -f %_datadir/selinux/alt/Makefile clean
done
popd
%endif

%install
%cmake_install

# install custom limits.conf for systemd
%if_enabled configure_systemd_limits
install -D -m 0644 etc/initsystem/icinga2.service.limits.conf %{buildroot}/%{_unitdir}/%{name}.service.d/limits.conf
%endif

# remove features-enabled symlinks
rm -f %buildroot%_sysconfdir/%name/features-enabled/*.conf

%if_with selinux
pushd tools/selinux
for selinuxvariant in %selinux_variants
do
  install -d %buildroot%_datadir/selinux/$selinuxvariant
  install -p -m 644 %selinux_modulename.pp.$selinuxvariant \
    %buildroot%_datadir/selinux/$selinuxvariant/%selinux_modulename.pp
done
popd
%endif

install -D -m 0644 tools/syntax/vim/syntax/%name.vim %buildroot%_datadir/vim/vimfiles/syntax/%name.vim
install -D -m 0644 tools/syntax/vim/ftdetect/%name.vim %buildroot%_datadir/vim/vimfiles/ftdetect/%name.vim

install -D -m 0644 tools/syntax/nano/%name.nanorc %buildroot%_datadir/nano/%name.nanorc

mkdir -p %buildroot%_localstatedir/%name

# Create %%ghost dirs:
mkdir -p %buildroot%_var/cache/%name
mkdir -p %buildroot%_var/log/%name
mkdir -p %buildroot%_var/log/%name/crash
mkdir -p %buildroot%_var/log/%name/compat
mkdir -p %buildroot%_var/log/%name/compat/archives
mkdir -p %buildroot%_rundir/%name
mkdir -p %buildroot%_rundir/%name/cmd
mkdir -p %buildroot%_var/spool/%name
mkdir -p %buildroot%_var/spool/%name/perfdata
mkdir -p %buildroot%_var/spool/%name/tmp

# Create %%ghost symlinks:
ln -srf %buildroot%_sysconfdir/%name/features-available/*.conf \
        %buildroot%_sysconfdir/%name/features-enabled/

%post
%post_service %name

if [ $1 -eq 1 ]
then
  # initial installation, enable default features
  for feature in checker notification mainlog; do
    ln -sf ../features-available/$feature.conf %_sysconfdir/%name/features-enabled/$feature.conf
  done
fi

%preun
%preun_service %name

if [ $1 -eq 0 ]; then
  # deinstallation of the package -- remove all enabled features
  rm -rf %_sysconfdir/%name/features-enabled
fi

%pre common
getent group %icinga_group >/dev/null || %_sbindir/groupadd -r %icinga_group
getent group %icingacmd_group >/dev/null || %_sbindir/groupadd -r %icingacmd_group
getent passwd %icinga_user >/dev/null || %_sbindir/useradd -c "icinga" -s /sbin/nologin -r -d %_var/spool/%name -G %icingacmd_group -g %icinga_group %icinga_user

%post ido-mysql
if [ $1 -eq 1 ]
then
  # initial installation, enable ido-mysql feature
  ln -sf ../features-available/ido-mysql.conf %_sysconfdir/%name/features-enabled/ido-mysql.conf
fi

%preun ido-mysql
if [ $1 -eq 0 ]; then
  # deinstallation of the package -- remove ido-mysql feature
  rm -f %_sysconfdir/%name/features-enabled/ido-mysql.conf
fi

%post ido-pgsql
if [ $1 -eq 1 ]
then
  # initial installation, enable ido-pgsql feature
  ln -sf ../features-available/ido-pgsql.conf %_sysconfdir/%name/features-enabled/ido-pgsql.conf
fi

%preun ido-pgsql
if [ $1 -eq 0 ]; then
  # deinstallation of the package -- remove ido-pgsql feature
  rm -f %_sysconfdir/%name/features-enabled/ido-pgsql.conf
fi

%post selinux
for selinuxvariant in %selinux_variants
do
  /usr/sbin/semodule -s $selinuxvariant -i \
    %_datadir/selinux/$selinuxvariant/%selinux_modulename.pp &> /dev/null || :
done
/sbin/fixfiles -R %name-bin restore &> /dev/null || :
/sbin/fixfiles -R %name-common restore &> /dev/null || :
/sbin/semanage port -a -t %{name}_port_t -p tcp 5665 &> /dev/null || :

%postun selinux
if [ $1 -eq 0 ] ; then
  /sbin/semanage port -d -t icinga2_port_t -p tcp 5665 &> /dev/null || :
  for selinuxvariant in %selinux_variants
  do
     /usr/sbin/semodule -s $selinuxvariant -r %selinux_modulename &> /dev/null || :
  done
  /sbin/fixfiles -R icinga2-bin restore &> /dev/null || :
  /sbin/fixfiles -R icinga2-common restore &> /dev/null || :
fi

%files
%defattr(-,root,root,-)
%config(noreplace) %_sysconfdir/logrotate.d/%name
%attr(644,root,root) %_unitdir/%name.service

%if_enabled configure_systemd_limits
%dir %_unitdir/%name.service.d
%_unitdir/%name.service.d/limits.conf
%endif

%config(noreplace) %_sysconfdir/sysconfig/%name
%_sbindir/%name
%dir %_libexecdir/%name
%_libexecdir/%name/prepare-dirs
%_libexecdir/%name/safe-reload

%attr(0750,%icinga_user,%icinga_group) %dir %_sysconfdir/%name
%attr(0750,%icinga_user,%icinga_group) %dir %_sysconfdir/%name/conf.d
%attr(0750,%icinga_user,%icinga_group) %dir %_sysconfdir/%name/features-available
%exclude %_sysconfdir/%name/features-available/ido-*.conf
%attr(0750,%icinga_user,%icinga_group) %dir %_sysconfdir/%name/features-enabled
%attr(0750,%icinga_user,%icinga_group) %dir %_sysconfdir/%name/scripts
%attr(0750,%icinga_user,%icinga_group) %dir %_sysconfdir/%name/zones.d
%config(noreplace) %attr(0640,%icinga_user,%icinga_group) %_sysconfdir/%name/%name.conf
%config(noreplace) %attr(0640,%icinga_user,%icinga_group) %_sysconfdir/%name/constants.conf
%config(noreplace) %attr(0640,%icinga_user,%icinga_group) %_sysconfdir/%name/zones.conf
%config(noreplace) %attr(0640,%icinga_user,%icinga_group) %_sysconfdir/%name/conf.d/*.conf
%config(noreplace) %attr(0640,%icinga_user,%icinga_group) %_sysconfdir/%name/features-available/*.conf
%config(noreplace) %attr(0640,%icinga_user,%icinga_group) %_sysconfdir/%name/zones.d/*
%config(noreplace) %_sysconfdir/%name/scripts/*

%attr(0750,%icinga_user,%icinga_group) %dir %_localstatedir/%name

%ghost %attr(0750,%icinga_user,%icingacmd_group) %dir %_var/cache/%name
%ghost %attr(0750,%icinga_user,%icingacmd_group) %dir %_var/log/%name
%ghost %attr(0750,%icinga_user,%icinga_group) %dir %_var/log/%name/crash
%ghost %attr(0750,%icinga_user,%icingacmd_group) %dir %_var/log/%name/compat
%ghost %attr(0750,%icinga_user,%icingacmd_group) %dir %_var/log/%name/compat/archives
%ghost %attr(0750,%icinga_user,%icingacmd_group) %dir %_rundir/%name
%ghost %attr(2750,%icinga_user,%icingacmd_group) %dir %_rundir/%name/cmd
%ghost %attr(0750,%icinga_user,%icinga_group) %dir %_var/spool/%name
%ghost %attr(0770,%icinga_user,%icinga_group) %dir %_var/spool/%name/perfdata
%ghost %attr(0750,%icinga_user,%icinga_group) %dir %_var/spool/%name/tmp
%ghost %_sysconfdir/%name/features-enabled/*.conf
%exclude %_sysconfdir/%name/features-enabled/ido-mysql.conf
%exclude %_sysconfdir/%name/features-enabled/ido-pgsql.conf

%files bin
%defattr(-,root,root,-)
%doc README.md NEWS AUTHORS CHANGELOG.md
%dir %_libdir/%name
%dir %_libdir/%name/sbin
%_libdir/%name/sbin/%name
%plugindir/check_nscp_api
%_datadir/%name
%exclude %_datadir/%name/include
%_mandir/man8/%name.8.*

%files common
%defattr(-,root,root,-)
%doc README.md NEWS AUTHORS CHANGELOG.md tools/syntax
%_sysconfdir/bash_completion.d/%name
%attr(0750,%icinga_user,%icinga_group) %dir %_datadir/%name/include
%_datadir/%name/include/*

%files doc
%defattr(-,root,root,-)
%_datadir/doc/%name
%docdir %_datadir/doc/%name

%files ido-mysql
%defattr(-,root,root,-)
%doc README.md NEWS AUTHORS CHANGELOG.md
%config(noreplace) %attr(0640,%icinga_user,%icinga_group) %_sysconfdir/%name/features-available/ido-mysql.conf
%_libdir/%name/libmysql_shim*
%_datadir/icinga2-ido-mysql
%ghost %_sysconfdir/%name/features-enabled/ido-mysql.conf

%files ido-pgsql
%defattr(-,root,root,-)
%doc README.md NEWS AUTHORS CHANGELOG.md
%config(noreplace) %attr(0640,%icinga_user,%icinga_group) %_sysconfdir/%name/features-available/ido-pgsql.conf
%_libdir/%name/libpgsql_shim*
%_datadir/icinga2-ido-pgsql
%ghost %_sysconfdir/%name/features-enabled/ido-pgsql.conf

%if_with selinux
%files selinux
%defattr(-,root,root,0755)
%doc tools/selinux/*
%_datadir/selinux/*/%selinux_modulename.pp
%endif

%files -n vim-%name
%defattr(-,root,root,-)
%_datadir/vim/vimfiles/syntax/%name.vim
%_datadir/vim/vimfiles/ftdetect/%name.vim

%files -n nano-%name
%defattr(-,root,root,-)
%_datadir/nano/%name.nanorc

%changelog
* Mon Nov 13 2023 Paul Wolneykien <manowar@altlinux.org> 2.14.0-alt3
- Require nagios-plugins, nagios-plugins-local and
  nagios-plugins-network.

* Sat Nov 11 2023 Paul Wolneykien <manowar@altlinux.org> 2.14.0-alt2
- Delete enabled features on package removal.
- Add all known features to %%ghost files.
- Fix: Make /var/lib/icinga2 an ordinary (i. e. not %%ghost) directory.
- Fixed path to /var in build configuration.

* Wed Nov 08 2023 Paul Wolneykien <manowar@altlinux.org> 2.14.0-alt1
- Initial build for Sisyphus.
