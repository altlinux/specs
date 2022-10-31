Name: dnf-plugins-core
Version: 4.3.1
Release: alt1

Summary: Core DNF Plugins
License: GPL-2.0
Group: System/Configuration/Packaging
Url: https://github.com/rpm-software-management/dnf-plugins-core

Packager: Andrey Cherepanov <cas@altlinux.org>

Source: %name-%version.tar

BuildArch: noarch

BuildRequires(pre): cmake
BuildRequires(pre): rpm-build-ninja
BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-sphinx

Provides: dnf-command(builddep)
Provides: dnf-command(changelog)
Provides: dnf-command(config-manager)
Provides: dnf-command(copr)
Provides: dnf-command(debug-dump)
Provides: dnf-command(debug-restore)
Provides: dnf-command(debuginfo-install)
Provides: dnf-command(download)
Provides: dnf-command(groups-manager)
Provides: dnf-command(repoclosure)
Provides: dnf-command(repograph)
Provides: dnf-command(repomanage)
Provides: dnf-command(reposync)
Provides: dnf-command(repodiff)
Provides: dnf-plugins-extras-debug = %EVR
Provides: dnf-plugins-extras-repoclosure = %EVR
Provides: dnf-plugins-extras-repograph = %EVR
Provides: dnf-plugins-extras-repomanage = %EVR
Provides: dnf-plugin-builddep = %EVR
Provides: dnf-plugin-config-manager = %EVR
Provides: dnf-plugin-debuginfo-install = %EVR
Provides: dnf-plugin-download = %EVR
Provides: dnf-plugin-generate_completion_cache = %EVR
Provides: dnf-plugin-needs_restarting = %EVR
Provides: dnf-plugin-groups-manager = %EVR
Provides: dnf-plugin-repoclosure = %EVR
Provides: dnf-plugin-repodiff = %EVR
Provides: dnf-plugin-repograph = %EVR
Provides: dnf-plugin-repomanage = %EVR
Provides: dnf-plugin-reposync = %EVR

%description
Core Plugins for DNF. This package enhances DNF with builddep, config-manager,
copr, debug, debuginfo-install, download, needs-restarting, groups-manager,
repoclosure, repograph, repomanage, reposync, changelog and repodiff commands.
Additionally provides generate_completion_cache passive plugin.

%prep
%setup

%build
%cmake -GNinja
%ninja_build -C "%_cmake__builddir"
%ninja_build -C "%_cmake__builddir" doc-man

%install
%ninja_install -C "%_cmake__builddir"
%find_lang %name

%files -f %name.lang
%doc AUTHORS README.rst
%config(noreplace) %_sysconfdir/dnf/plugins/*.conf
%_sysconfdir/dnf/plugins/*.list
%_prefix/libexec/dnf-utils-3
%python3_sitelibdir/dnf-plugins
%python3_sitelibdir/dnfpluginscore
%_man1dir/*.1*
%_man5dir/*.5*
%_man8dir/*.8*

%changelog
* Mon Oct 31 2022 Andrey Cherepanov <cas@altlinux.org> 4.3.1-alt1
- Initial build for Sisyphus
