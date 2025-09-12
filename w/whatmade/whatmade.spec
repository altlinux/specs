%define _unpackaged_files_terminate_build 1
%define _stripped_files_terminate_build 1

Name: whatmade
Version: 0.2.0
Release: alt1

Summary: Linux daemon that monitors user-specified directories and records which process created each file
License: GPL-3.0
Group: Monitoring
Url: https://github.com/ANGulchenko/whatmade

Source: %name-%version.tar

BuildRequires(pre): rpm-macros-cmake
BuildRequires(pre): rpm-macros-systemd

BuildRequires: cmake
BuildRequires: gcc-c++
BuildRequires: pkgconfig(libconfig++)

Provides: whomade = %version
Obsoletes: whomade

%description
Whatmade is a Linux daemon that monitors user-specified directories and
records which process created each file. This makes it easy to later
identify the origin of files with suspicious or unexpected names.

The main idea was to monitor and identify files in the dot directories
in the /home.

%package caja
Summary: Whatmade GUI plug-in to the Caja file manager
Group: Graphical desktop/Other
Requires: %name = %version-%release
Requires: python3-module-caja
Requires: /usr/bin/caja

Provides: whomade-caja = %version
Obsoletes: whomade-caja

BuildArch: noarch

%description caja
Whatmade extension for the Caja FM (from MATE DE, fork of Gnome 2) where
you can just right-click on file and ask "What made this?" from a menu.

%prep
%setup

# correct path to image
sed -i "s|./FM_Extensions/MATE-CAJA/||" README.md

%build
%cmake
%cmake_build

%install
#%%cmake_install

# copy binary
mkdir -p %buildroot/%_bindir
cp -v %_cmake__builddir/whatmade %buildroot/%_bindir/

# create config folder with default config file
mkdir -p %buildroot/%_sysconfdir/whatmade
cat <<EOF > %buildroot/%_sysconfdir/whatmade/config.cfg

monitor = (
	"/home/user/.config",
	"/home/user/.cache"
);

ignore = (
	"/home/user/.cache/mozilla"
);

EOF

# copy systemd unit
mkdir -p %buildroot%_unitdir
sed -i "s|^ExecStart=/bin/whatmade|ExecStart=/usr/bin/whatmade|" systemd/whatmade.service
install -m 644 systemd/whatmade.service %buildroot%_unitdir/whatmade.service

# package Caja plugin
mkdir -p %buildroot%_datadir/caja-python/extensions/
cp -v FM_Extensions/MATE-CAJA/whatmade-extension.py %buildroot%_datadir/caja-python/extensions/

%post
%post_service %name

echo "NOTE: this package ships daemon, to enable it use command like"
echo "      systemctl enable --now whatmade.service"

%preun
%preun_service %name

%postun
%systemd_postun %name.service

%files
%doc CHANGELOG.md LICENSE README.md FM_Extensions/MATE-CAJA/whatmade_win.png
%_bindir/whatmade
%_unitdir/whatmade.service
%dir %_sysconfdir/whatmade
%config(noreplace) %_sysconfdir/whatmade/config.cfg

%files caja
%_datadir/caja-python/extensions/whatmade-extension.py*

%changelog
* Fri Sep 12 2025 Nikolay Strelkov <snk@altlinux.org> 0.2.0-alt1
- New version 0.2.0.

* Tue Aug 26 2025 Nikolay Strelkov <snk@altlinux.org> 0.1.1_git20250826.b85e285-alt1
- Following upstream decision - renaming source package from whomade to whatmade

* Sat Aug 23 2025 Nikolay Strelkov <snk@altlinux.org> 0.0.0_git20250822.3cb8166-alt1
- Initial build for Sisyphus
