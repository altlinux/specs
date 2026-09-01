%define _unpackaged_files_terminate_build 1

Name: python3-module-iwdgui
Version: 0.3.0
Release: alt2

Summary: Graphical frontend for iwd
License: MPL-2.0
Group: Networking/WWW
Url: https://pypi.org/project/iwdgui/
Vcs: https://gitlab.com/hfernh/iwdgui
BuildArch: noarch

Source: %name-%version.tar
Source1: %pyproject_deps_config_name

BuildRequires(pre): rpm-build-pyproject
BuildRequires: python3-dev

%pyproject_runtimedeps_metadata
%pyproject_builddeps_build
%pyproject_builddeps_metadata
Provides: iwdgui = %EVR
Obsoletes: iwdgui < %EVR

%description
A graphical frontend for iwd, Intel's iNet Wireless Daemon, written in python.
Graphical user interface for iwd, focusing on practical use, making it easy
to connect a laptop or desktop to a wifi network.
Supporting multiple wireless adapters, in different tabs.
Can provide detailed information: vendor/model of the wireless interface,
IP address information, radio standard (802.??), channel, signal strength,
etc.
Iwdgui supports station mode, access point mode, and ad-hoc mode.
(The latter two depend on the wireless network interface capabilities)
Able to manage previously connected networks.

%prep
%setup
%autopatch -p1
%pyproject_deps_resync_build
%pyproject_deps_resync_metadata

%build
%pyproject_build

%install
%pyproject_install

%files
%_bindir/iwdgui
%python3_sitelibdir/iwdgui
%python3_sitelibdir/%pyproject_distinfo iwdgui
%_desktopdir/iwdgui.desktop
%_liconsdir/iwdgui.png
%_iconsdir/hicolor/96x96/apps/iwdgui.png

%changelog
* Fri Aug 28 2026 Pavel Petrykin <silverducks@altlinux.org> 0.3.0-alt2
- Rename package according to Alt Linux conventions.
- Minor spec cleanup.

* Fri Apr 10 2026 Pavel Petrykin <silverducks@altlinux.org> 0.3.0-alt1
- Initial build for Alt Linux.
