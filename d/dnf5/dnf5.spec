%define libdnf5_soname 2
%define libdnf5_cli_soname 3
%define libdnf5_dir %_sharedstatedir/libdnf5

Name: dnf5
Version: 5.4.2.1
Release: alt1

Summary: Command-line package manager

License: GPL-2.0-or-later AND LGPL-2.1-or-later
Group: System/Configuration/Packaging
URL: https://github.com/rpm-software-management/dnf5

# 32-bit time_t narrowing in libdnf5/base/transaction.cpp
ExcludeArch: %ix86
# Source-url: https://github.com/rpm-software-management/dnf5/archive/refs/tags/%version.tar.gz
Source: %name-%version.tar

Patch1: %name-5.4.0.0-rpm-4.13-compat.patch
Patch2: %name-cstring.patch

BuildRequires(pre): rpm-macros-cmake
BuildRequires: cmake >= 3.21
BuildRequires: gcc-c++ >= 10.1
BuildRequires: gettext-tools
BuildRequires: librpm-devel
BuildRequires: libsolv-devel >= 0.7.35
BuildRequires: librepo-devel >= 1.20.0
BuildRequires: libfmt-devel
BuildRequires: libjson-c-devel
BuildRequires: libsqlite3-devel >= 3.35.0
BuildRequires: libtoml11-devel
BuildRequires: zlib-devel
BuildRequires: libsmartcols-devel
BuildRequires: libcurl-devel
BuildRequires: libxml2-devel
BuildRequires: libacl-devel
BuildRequires: libmodulemd-devel >= 2.5.0
BuildRequires: libcomps-devel
BuildRequires: libsdbus-cpp-devel >= 0.8.1
BuildRequires: systemd-devel
BuildRequires: swig >= 4
BuildRequires: python3-devel
BuildRequires: rpm-build-python3
BuildRequires: bash-completion

Conflicts: dnf < 5

%description
DNF5 is a command-line package manager that automates the process of installing,
upgrading, configuring, and removing computer programs in a consistent manner.
It supports RPM packages, modulemd modules, and comps groups & environments.

%package -n libdnf5
Summary: Package management library
Group: System/Libraries
License: LGPL-2.1-or-later
Conflicts: dnf < 5

%description -n libdnf5
Package management library.

%package -n libdnf5-devel
Summary: Development files for libdnf5
Group: Development/C++
License: LGPL-2.1-or-later
Requires: libdnf5 = %EVR
Requires: libsolv-devel >= 0.7.35

%description -n libdnf5-devel
Development files for libdnf5.

%package -n libdnf5-cli
Summary: Library for working with a terminal in a command-line package manager
Group: System/Libraries
License: LGPL-2.1-or-later

%description -n libdnf5-cli
Library for working with a terminal in a command-line package manager.

%package -n libdnf5-cli-devel
Summary: Development files for libdnf5-cli
Group: Development/C++
License: LGPL-2.1-or-later
Requires: libdnf5-cli = %EVR

%description -n libdnf5-cli-devel
Development files for libdnf5-cli.

%package -n dnf5-devel
Summary: Development files for dnf5
Group: Development/C++
License: LGPL-2.1-or-later
Requires: dnf5 = %EVR
Requires: libdnf5-devel = %EVR
Requires: libdnf5-cli-devel = %EVR

%description -n dnf5-devel
Development files for dnf5.

%package -n python3-module-libdnf5
Summary: Python 3 bindings for the libdnf5 library
Group: Development/Python3
License: LGPL-2.1-or-later

%description -n python3-module-libdnf5
Python 3 bindings for the libdnf5 library.

%package -n python3-module-libdnf5-cli
Summary: Python 3 bindings for the libdnf5-cli library
Group: Development/Python3
License: LGPL-2.1-or-later

%description -n python3-module-libdnf5-cli
Python 3 bindings for the libdnf5-cli library.

%package plugins
Summary: Plugins for dnf5
Group: System/Configuration/Packaging

%description plugins
Core DNF5 plugins that enhance dnf5 with builddep, changelog, config-manager,
copr, needs-restarting, repoclosure, repomanage, and reposync commands.

%package plugin-automatic
Summary: Package manager - automated upgrades
Group: System/Configuration/Packaging
Conflicts: dnf-automatic

%description plugin-automatic
Alternative command-line interface "dnf upgrade" suitable to be executed
automatically and regularly from systemd timers, cron jobs or similar.

%package -n libdnf5-plugin-actions
Summary: Libdnf5 plugin that allows to run actions on hooks
Group: System/Libraries
License: LGPL-2.1-or-later

%description -n libdnf5-plugin-actions
Libdnf5 plugin that allows to run actions (external executables) on hooks.

%package -n libdnf5-plugin-local
Summary: Libdnf5 plugin for local RPM repository
Group: System/Libraries
License: LGPL-2.1-or-later

%description -n libdnf5-plugin-local
Libdnf5 plugin that maintains a local RPM repository. Packages can be
dropped into the local repository directory and they will be available
for installation via dnf5.

%package -n python3-libdnf5-python-plugins-loader
Summary: Libdnf5 plugin that allows loading Python plugins
Group: System/Libraries
License: LGPL-2.1-or-later

%description -n python3-libdnf5-python-plugins-loader
Libdnf5 plugin that allows loading Python plugins.

%prep
%setup
%patch1 -p1
%patch2 -p1

%build
%cmake \
    -DPACKAGE_VERSION=%version \
    \
    -DWITH_DNF5DAEMON_CLIENT=OFF \
    -DWITH_DNF5DAEMON_SERVER=OFF \
    -DWITH_LIBDNF5_CLI=ON \
    -DWITH_DNF5=ON \
    -DWITH_DNF5_OBSOLETES_DNF=OFF \
    -DWITH_DNF5_PLUGINS=ON \
    -DWITH_PLUGIN_ACTIONS=ON \
    -DWITH_PLUGIN_APPSTREAM=OFF \
    -DWITH_PLUGIN_EXPIRED_PGP_KEYS=OFF \
    -DWITH_PLUGIN_LOCAL=ON \
    -DWITH_PLUGIN_RHSM=OFF \
    -DWITH_PLUGIN_MANIFEST=OFF \
    -DWITH_PYTHON_PLUGINS_LOADER=ON \
    \
    -DWITH_ACL=ON \
    -DWITH_COMPS=ON \
    -DWITH_MODULEMD=ON \
    -DWITH_SYSTEMD=ON \
    \
    -DWITH_HTML=OFF \
    -DWITH_MAN=OFF \
    \
    -DWITH_GO=OFF \
    -DWITH_PERL5=OFF \
    -DWITH_PYTHON3=ON \
    -DWITH_RUBY=OFF \
    \
    -DWITH_TESTS=OFF \
    -DWITH_PERFORMANCE_TESTS=OFF \
    -DWITH_DNF5DAEMON_TESTS=OFF \
    \
    -DENABLE_SOLV_FOCUSNEW=ON

%cmake_build

%install
%cmake_install

# dnf5 replaces dnf
ln -sr %buildroot%_bindir/dnf5 %buildroot%_bindir/dnf
ln -sr %buildroot%_datadir/bash-completion/completions/dnf5 %buildroot%_datadir/bash-completion/completions/dnf

# Fix paths for ALT Linux (/usr/bin/rm -> /bin/rm, /usr/bin/sh -> /bin/sh)
sed -i 's|/usr/bin/rm |/bin/rm |g' %buildroot%_unitdir/dnf5-offline-transaction-cleanup.service
sed -i 's|#!/usr/bin/sh|#!/bin/sh|' %buildroot%_bindir/dnf-automatic

mkdir -p %buildroot%libdnf5_dir
for file in \
    environments.toml groups.toml modules.toml nevras.toml packages.toml \
    system.toml \
    transaction_history.sqlite transaction_history.sqlite-shm \
    transaction_history.sqlite-wal \
    system-repo.lock
do
    touch %buildroot%libdnf5_dir/$file
done
mkdir -p %buildroot%libdnf5_dir/comps_groups
mkdir -p %buildroot%libdnf5_dir/offline

touch %buildroot%_sysconfdir/dnf/versionlock.toml

mkdir -p %buildroot%_libdir/libdnf5/plugins
mkdir -p %buildroot%_sharedstatedir/dnf/plugins/local
mkdir -p %buildroot%_var/cache/libdnf5
mkdir -p %buildroot%_sharedstatedir/dnf

# Move python plugins directory to arch-specific path for sisyphus_check
if [ -d %buildroot%python3_sitelibdir_noarch/libdnf_plugins ] && [ "%python3_sitelibdir_noarch" != "%python3_sitelibdir" ]; then
    mkdir -p %buildroot%python3_sitelibdir
    mv %buildroot%python3_sitelibdir_noarch/libdnf_plugins %buildroot%python3_sitelibdir/
fi

%find_lang dnf5
%find_lang libdnf5
%find_lang libdnf5-cli
%find_lang dnf5-plugin-builddep
%find_lang dnf5-plugin-changelog
%find_lang dnf5-plugin-config-manager
%find_lang dnf5-plugin-copr
%find_lang dnf5-plugin-needs-restarting
%find_lang dnf5-plugin-repoclosure
%find_lang dnf5-plugin-reposync
cat dnf5-plugin-builddep.lang dnf5-plugin-changelog.lang dnf5-plugin-config-manager.lang dnf5-plugin-copr.lang dnf5-plugin-needs-restarting.lang dnf5-plugin-repoclosure.lang dnf5-plugin-reposync.lang | sort -u > dnf5-plugins.lang

# Remove zh_Hans and zh_Hant locales not supported by %find_lang
rm -rf %buildroot%_datadir/locale/zh_Hans
rm -rf %buildroot%_datadir/locale/zh_Hant
%find_lang dnf5-plugin-automatic
%find_lang libdnf5-plugin-actions

%files -f dnf5.lang
%_bindir/dnf5
%_bindir/dnf
%_unitdir/dnf5-makecache.service
%_unitdir/dnf5-makecache.timer
%dir %_sysconfdir/dnf/dnf5-aliases.d
%doc %_sysconfdir/dnf/dnf5-aliases.d/README
%dir %_datadir/dnf5
%dir %_datadir/dnf5/aliases.d
%_datadir/dnf5/aliases.d/compatibility.conf
%_datadir/dnf5/aliases.d/compatibility-plugins.conf
%_datadir/dnf5/aliases.d/compatibility-reposync.conf
%dir %_libdir/dnf5
%dir %_libdir/dnf5/plugins
%dir %_datadir/dnf5/dnf5-plugins
%dir %_sysconfdir/dnf/dnf5-plugins
%doc %_libdir/dnf5/plugins/README
%dir %_libdir/libdnf5/plugins
%_datadir/bash-completion/completions/dnf5
%_datadir/bash-completion/completions/dnf
%_datadir/zsh/site-functions/_dnf5
%_unitdir/dnf5-offline-transaction.service
%_unitdir/dnf5-offline-transaction-cleanup.service

%files -n libdnf5 -f libdnf5.lang
%_sysconfdir/dnf/dnf.conf
%ghost %attr(0644,root,root) %_sysconfdir/dnf/versionlock.toml
%dir %_datadir/dnf5/libdnf.conf.d
%dir %_sysconfdir/dnf/libdnf5.conf.d
%dir %_datadir/dnf5/repos.override.d
%dir %_sysconfdir/dnf/repos.override.d
%dir %_sysconfdir/dnf/libdnf5-plugins
%dir %_datadir/dnf5/repos.d
%dir %_datadir/dnf5/vars.d
%dir %_datadir/dnf5/vendors.d
%dir %_datadir/dnf5/libdnf.plugins.conf.d
%dir %_sysconfdir/dnf/vendors.d
%dir %_libdir/libdnf5
%_libdir/libdnf5.so.%{libdnf5_soname}*
%dir %libdnf5_dir
%ghost %dir %libdnf5_dir/comps_groups
%ghost %dir %libdnf5_dir/offline
%ghost %libdnf5_dir/environments.toml
%ghost %libdnf5_dir/groups.toml
%ghost %libdnf5_dir/modules.toml
%ghost %libdnf5_dir/nevras.toml
%ghost %libdnf5_dir/packages.toml
%ghost %libdnf5_dir/system.toml
%ghost %libdnf5_dir/transaction_history.sqlite
%ghost %libdnf5_dir/transaction_history.sqlite-shm
%ghost %libdnf5_dir/transaction_history.sqlite-wal
%ghost %libdnf5_dir/system-repo.lock
%ghost %dir %_var/cache/libdnf5
%ghost %dir %_sharedstatedir/dnf

%files -n libdnf5-devel
%_includedir/libdnf5/
%_libdir/libdnf5.so
%_libdir/pkgconfig/libdnf5.pc

%files -n libdnf5-cli -f libdnf5-cli.lang
%_libdir/libdnf5-cli.so.%{libdnf5_cli_soname}*

%files -n libdnf5-cli-devel
%_includedir/libdnf5-cli/
%_libdir/libdnf5-cli.so
%_libdir/pkgconfig/libdnf5-cli.pc

%files -n dnf5-devel
%_includedir/dnf5/

%files -n python3-module-libdnf5
%python3_sitelibdir/libdnf5/
%python3_sitelibdir/libdnf5-*.dist-info/

%files -n python3-module-libdnf5-cli
%python3_sitelibdir/libdnf5_cli/
%python3_sitelibdir/libdnf5_cli-*.dist-info/

%files plugins -f dnf5-plugins.lang
%_libdir/dnf5/plugins/builddep_cmd_plugin.so
%_libdir/dnf5/plugins/changelog_cmd_plugin.so
%_libdir/dnf5/plugins/config-manager_cmd_plugin.so
%_libdir/dnf5/plugins/copr_cmd_plugin.so
%_libdir/dnf5/plugins/needs_restarting_cmd_plugin.so
%_libdir/dnf5/plugins/repoclosure_cmd_plugin.so
%_libdir/dnf5/plugins/reposync_cmd_plugin.so
%_libdir/dnf5/plugins/repomanage_cmd_plugin.so

%files plugin-automatic -f dnf5-plugin-automatic.lang
%_bindir/dnf-automatic
%_libdir/dnf5/plugins/automatic_cmd_plugin.so
%_datadir/dnf5/dnf5-plugins/automatic.conf
%_unitdir/dnf5-automatic.service
%_unitdir/dnf5-automatic.timer
%_unitdir/dnf-automatic.service
%_unitdir/dnf-automatic.timer

%files -n libdnf5-plugin-actions -f libdnf5-plugin-actions.lang
%_libdir/libdnf5/plugins/actions.*
%config %_sysconfdir/dnf/libdnf5-plugins/actions.conf
%dir %_sysconfdir/dnf/libdnf5-plugins/actions.d

%files -n libdnf5-plugin-local
%_libdir/libdnf5/plugins/local.*
%config %_sysconfdir/dnf/libdnf5-plugins/local.conf
%dir %_sharedstatedir/dnf/plugins/local

%files -n python3-libdnf5-python-plugins-loader
%_libdir/libdnf5/plugins/python_plugins_loader.*
%config %_sysconfdir/dnf/libdnf5-plugins/python_plugins_loader.conf
%dir %_sysconfdir/dnf/libdnf5-plugins/python_plugins_loader.d
%dir %python3_sitelibdir/libdnf_plugins/
%doc %python3_sitelibdir/libdnf_plugins/README

%changelog
* Sun Jun 28 2026 Vitaly Lipatov <lav@altlinux.ru> 5.4.2.1-alt1
- new version 5.4.2.1
- fixed FTBFS: include <cstring> for std::strcmp etc. (new libstdc++)

* Tue May 05 2026 Vitaly Lipatov <lav@altlinux.ru> 5.4.2.0-alt1
- new version 5.4.2.0
- pack zsh completion

* Wed Mar 11 2026 Vitaly Lipatov <lav@altlinux.ru> 5.4.0.0-alt1
- initial build for ALT Sisyphus
- add Conflicts: dnf < 5 for libdnf5 (dnf.conf), dnf-automatic for plugin-automatic
- fix /usr/bin/rm and /usr/bin/sh paths for ALT Linux
- move system state dir from /usr/lib/sysimage/libdnf5 to /var/lib/libdnf5
- add Conflicts: dnf < 5, symlinks /usr/bin/dnf -> dnf5

