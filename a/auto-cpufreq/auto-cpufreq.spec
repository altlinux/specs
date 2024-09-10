%define _unpackaged_files_terminate_build 1

Name: auto-cpufreq
Version: 2.4.0
Release: alt1

Summary: Automatic CPU speed & power optimizer
License: GPL-3.0-or-later
Group: System/Kernel and hardware
URL: https://github.com/AdnanHodzic/auto-cpufreq
BuildArch: noarch

Source: %name-%version.tar
Patch: %name-%version-alt-poetry-versioning-bypass.patch
Patch1: %name-%version-alt-systemd-service-fix.patch
Patch2: %name-%version-alt-policykit-rule-fix.patch
Patch3: %name-%version-alt-use-datadir-instead-local.patch
Patch4: %name-%version-alt-fix-icons-location.patch
Patch5: %name-%version-alt-pickle-change-dir.patch
Patch6: %name-%version-alt-fix-package-update.patch

BuildRequires(pre): rpm-macros-python3
BuildRequires: python3-module-certifi
BuildRequires: python3-module-setuptools
BuildRequires: python3-module-wheel
BuildRequires: python3-module-poetry-dynamic-versioning

%description
Automatic CPU speed & power optimizer for Linux based on active
monitoring of laptop's battery state, CPU usage, CPU temperature and system load.

%prep
%setup
%autopatch -p1

%build
%pyproject_build

%install
%pyproject_install

mkdir -p %buildroot%_datadir/%name
cp -rv scripts/ %buildroot%_datadir/%name
install -D -m 0644 scripts/org.%name.pkexec.policy -t %buildroot%_datadir/polkit-1/actions
install -D -m 0755 scripts/%name-gtk.desktop -t %buildroot%_datadir/applications
install -D -m 0755 images/icon.png %buildroot%_datadir/pixmaps/%name.png

%files
%_bindir/%name
%_bindir/%name-gtk
%dir %_datadir/%name
%dir %_datadir/%name/scripts
%_datadir/%name/scripts/%{name}*
%_datadir/%name/scripts/cpufreqctl.sh
%_datadir/%name/scripts/style.css
%exclude %_datadir/%name/scripts/org.%name.pkexec.policy
%exclude %_datadir/%name/scripts/%name-gtk.desktop
%exclude %_datadir/%name/scripts/snapdaemon.sh
%exclude %_datadir/%name/scripts/start_app
%exclude %_datadir/%name/scripts/auto-cpufreq-venv-wrapper
%_datadir/polkit-1/actions/org.%name.pkexec.policy
%_datadir/applications/*.desktop
%_datadir/pixmaps/*.png
%python3_sitelibdir/auto_cpufreq
%python3_sitelibdir/%{pyproject_distinfo auto_cpufreq}

%changelog
* Sun Sep 08 2024 Anton Kurachenko <srebrov@altlinux.org> 2.4.0-alt1
- New version 2.4.0.

* Sat May 11 2024 Anton Kurachenko <srebrov@altlinux.org> 2.3.0-alt1
- New version 2.3.0.

* Fri Mar 15 2024 Anton Kurachenko <srebrov@altlinux.org> 2.2.0-alt1
- Initial build for Sisyphus.
