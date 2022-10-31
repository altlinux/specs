%define _unpackaged_files_terminate_build 1                                                                           
%def_without tests

Name:    dnf
Version: 4.13.0
Release: alt1

Summary: Package manager based on libdnf and libsolv. Replaces YUM.
License: GPL-2.0
Group:   System/Configuration/Packaging
Url:     https://github.com/rpm-software-management/dnf

Packager: Andrey Cherepanov <cas@altlinux.org>

Source: %name-%version.tar
Patch1: dnf-alt-pathes.patch

BuildArch: noarch

BuildRequires(pre): cmake
BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-sphinx
BuildRequires: libdnf-devel
%if_with tests
BuildRequires: ctest
%endif

%description
Dandified YUM (DNF) is the next upcoming major version of YUM. It does package
management using RPM, libsolv and hawkey libraries. For metadata handling and
package downloads it utilizes librepo. To process and effectively handle the
comps data it uses libcomps.

%package -n python3-module-dnf
Summary: Python 3 interface to DNF
Group: Development/Python3
%py3_requires rpm gpg

%description -n python3-module-dnf
Python 3 interface to DNF.

%package automatic
Summary: Automatic upgrades for DNF
Group: System/Configuration/Packaging

%description automatic
Automatic upgrades for DNF.

%prep
%setup
%patch1 -p1

%build
%cmake
%cmake_build
make -C "%_cmake__builddir" doc-man

%install
%cmake_install
ln -s dnf-3 %buildroot%_bindir/dnf
ln -s dnf-automatic-3 %buildroot%_bindir/dnf-automatic
mkdir -p %buildroot%_sysconfdir/dnf/vars
mkdir -p %buildroot%_sysconfdir/dnf/aliases.d
mkdir -p %buildroot%_sysconfdir/%name/modules.d
mkdir -p %buildroot%_sysconfdir/%name/modules.defaults.d
mkdir -p %buildroot%_localstatedir/log/
mkdir -p %buildroot%_var/cache/dnf/
%find_lang %name

%if_with tests
%check
cd "%_cmake__builddir"
ctest -VV
%endif

%files -f %name.lang
%doc AUTHORS README.rst
%config(noreplace) %_sysconfdir/dnf/%name.conf
%config(noreplace) %_sysconfdir/dnf/protected.d/%name.conf
%config(noreplace) %_sysconfdir/logrotate.d/%name
%_sysconfdir/bash_completion.d/dnf
%_sysconfdir/dnf/dnf-strict.conf
%_sysconfdir/dnf/protected.d/yum.conf
%_sysconfdir/dnf/aliases.d/zypper.conf
%dir %_sysconfdir/dnf
%dir %_sysconfdir/dnf/modules.d
%dir %_sysconfdir/dnf/modules.defaults.d
%dir %_sysconfdir/dnf/protected.d
%dir %_sysconfdir/dnf/vars
%dir %_sysconfdir/dnf/aliases.d
%_bindir/dnf
%_bindir/dnf-3
%_man1dir/*
%_man5dir/*
%_man7dir/*
%_man8dir/*
%_tmpfilesdir/%name.conf
%_var/cache/dnf/
%_sysconfdir/libreport/events.d/collect_dnf.conf

%files -n python3-module-dnf
%python3_sitelibdir/%name
%exclude %python3_sitelibdir/%name/automatic

%files automatic
%config(noreplace) %_sysconfdir/dnf/automatic.conf
%_bindir/dnf-automatic
%_bindir/dnf-automatic-3
%_unitdir/*
%python3_sitelibdir/%name/automatic

%changelog
* Wed Jun 15 2022 Andrey Cherepanov <cas@altlinux.org> 4.13.0-alt1
- Initial build for Sisyphus.
