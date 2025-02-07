%define _unpackaged_files_terminate_build 1

Name: caja-mediainfo
Version: 1.0.4
Release: alt1

Summary: View media information from the properties tab
License: GPLv3
Group: Graphical desktop/MATE
URL: https://github.com/linux-man/caja-mediainfo-tab

BuildArch: noarch

Source: %name-%version.tar

Patch: %name-%version-%release.patch

AutoProv: yes,nopython
AutoReq: yes,nopython

Requires: python3-module-caja
Requires: /usr/bin/caja

# FIXME, waiting for dependency (see bug 52975)
#Requires: python3-module-mediainfodll

%description
Caja is the official file manager for the MATE desktop. It allows one
to browse directories, preview files and launch applications associated
with them. It is also responsible for handling the icons on the MATE
desktop. It works on local and remote filesystems.

With this extension, you can view media information from the Caja file
properties tab.

%prep
%setup

%build
# nothing to build here

%install
mkdir -p %buildroot%_datadir/caja-python/extensions
cp -var caja-extension/* %buildroot%_datadir/caja-python/extensions/

%files
%doc README.md LICENSE
%dir %_datadir/caja-python/extensions/caja-mediainfo-tab/
%_datadir/caja-python/extensions/caja-mediainfo-tab/*
%_datadir/caja-python/extensions/caja-mediainfo-tab.py

%changelog
* Fri Feb 07 2025 Nikolay Strelkov <snk@altlinux.org> 1.0.4-alt1
- Initial build for Sisyphus
