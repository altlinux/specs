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
Release:        alt6
URL:            https://www.icinga.com/
Source:         https://github.com/Icinga/%name/archive/v%version/%name-%version.tar

Patch0:         icinga2-graphite.patch
Patch1:         icinga2-vim_syntax.patch
Patch2:         icinga2-fix-unitdir-alt.patch
Patch3:         icinga2-fix-plugin-loader-path.patch
Patch4:         icinga2-global-commands-zone.patch

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
BuildRequires:  boost-beast-devel >= 1.66
BuildRequires:  boost-signals-devel >= 1.66
BuildRequires:  boost-interprocess-devel >= 1.66

BuildRequires:  pkgconfig(libsystemd)
BuildRequires:  logrotate

BuildRequires:  libmariadb-devel
BuildRequires:  postgresql-devel

%description
Meta package for Icinga 2 Core and DB IDO.

%package common
Summary:        Common Icinga 2 configuration
Group:          Monitoring
BuildArch:      noarch

%description common
This subpackage provides common directories, and the UID and GUID definitions
among Icinga 2 related packages.

%package doc
Summary:        Documentation for Icinga 2
Group:          Documentation
BuildArch:      noarch

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

%package -n vim-%name
Summary:        Vim syntax highlighting for icinga2
Group:          Editors
BuildArch:      noarch

%description -n vim-%name
Provides Vim syntax highlighting for icinga2.

%package -n nano-%name
Summary:        Nano syntax highlighting for icinga2
Group:          Editors
BuildArch:      noarch

%description -n nano-%name
Provides Nano syntax highlighting for icinga2.

%prep
%setup
%patch0 -p1
%patch1 -p1
%patch2 -p2
%patch3 -p2
%patch4 -p1

%ifarch %e2k
# compiler bug workaround
sed -i '/Lazy(const Lazy/s/explicit//' lib/base/object.hpp
sed -i 's/operator Lazy<U>()/Lazy<U> edg_fix_dummy()/' lib/base/object.hpp
%endif

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

%install
%cmake_install

# install custom limits.conf for systemd
%if_enabled configure_systemd_limits
install -D -m 0644 etc/initsystem/icinga2.service.limits.conf %{buildroot}/%{_unitdir}/%{name}.service.d/limits.conf
%endif

# remove features-enabled symlinks
rm -f %buildroot%_sysconfdir/%name/features-enabled/*.conf

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
%_sysconfdir/bash_completion.d/%name
%attr(0750,%icinga_user,%icinga_group) %dir %_datadir/%name/include
%_datadir/%name/include/*

%files doc
%defattr(-,root,root,-)
%_datadir/doc/%name
%docdir %_datadir/doc/%name

%files ido-mysql
%defattr(-,root,root,-)
%config(noreplace) %attr(0640,%icinga_user,%icinga_group) %_sysconfdir/%name/features-available/ido-mysql.conf
%_libdir/%name/libmysql_shim*
%_datadir/icinga2-ido-mysql
%ghost %_sysconfdir/%name/features-enabled/ido-mysql.conf

%files ido-pgsql
%defattr(-,root,root,-)
%config(noreplace) %attr(0640,%icinga_user,%icinga_group) %_sysconfdir/%name/features-available/ido-pgsql.conf
%_libdir/%name/libpgsql_shim*
%_datadir/icinga2-ido-pgsql
%ghost %_sysconfdir/%name/features-enabled/ido-pgsql.conf

%files -n vim-%name
%defattr(-,root,root,-)
%_datadir/vim/vimfiles/syntax/%name.vim
%_datadir/vim/vimfiles/ftdetect/%name.vim

%files -n nano-%name
%defattr(-,root,root,-)
%_datadir/nano/%name.nanorc

%changelog
* Thu Jun 06 2024 Paul Wolneykien <manowar@altlinux.org> 2.14.0-alt6
- Fix: Package common doc files into the main package.
- Include files from icinga2-bin package into the main package.
- Pre-define the "global-commands" zone (patch).

* Thu Feb 08 2024 Ivan A. Melnikov <iv@altlinux.org> 2.14.0-alt5.1
- NMU: fix building with boost 1.84.0-alt1

* Thu Nov 23 2023 Paul Wolneykien <manowar@altlinux.org> 2.14.0-alt5
- Remove disabled 'selinux' subpackage from the spec.
- Fix: Make -common, -doc, vim- and nano- subpackages noarch.

* Thu Nov 23 2023 Paul Wolneykien <manowar@altlinux.org> 2.14.0-alt4
- Save git remotes.
- Fix: Load feature plugins by full path (patch).

* Tue Nov 21 2023 Ilya Kurdyukov <ilyakurdyukov@altlinux.org> 2.14.0-alt3.1
- Fixed build for Elbrus.

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
