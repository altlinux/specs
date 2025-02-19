%define _unpackaged_files_terminate_build 1

Name: magnus
Version: 1.0.3
Release: alt2

Summary: Very simple screen magnifier
License: MIT
Group: Accessibility
URL: https://github.com/stuartlangridge/magnus

BuildArch: noarch

BuildRequires(pre): rpm-build-python3

BuildRequires: python3-module-setuptools
BuildRequires: python3-module-distutils-extra

Requires: libkeybinder3-gir

Source: %name-%version.tar

Patch: %name-%version-%release.patch

%description
Magnus is a simple screen magnifying glass. It nicely integrates with X11
desktops like MATE or Xfce (probably with others not named here, too).

Visually impaired users may find this tool helpful for zooming into
certain screen areas in order to improve readability/visibilty of fonts,
icons and other data.

%prep
%setup

%build
%python3_build

%install
%python3_install

rm -v %buildroot%python3_sitelibdir/setup.py
rm -vrf %buildroot%python3_sitelibdir/__pycache__

%files
%doc LICENSE README.md
%_bindir/%name
%python3_sitelibdir/Magnus-%{version}*-info
%config %_sysconfdir/xdg/autostart/%name-autostart.desktop
%_desktopdir/%name.desktop
%_man1dir/%name.1*

%changelog
* Wed Feb 19 2025 Nikolay Strelkov <snk@altlinux.org> 1.0.3-alt2
- Moved to correct category - Accessibility (closes: #52616)

* Sun Jan 19 2025 Nikolay Strelkov <snk@altlinux.org> 1.0.3-alt1
- Initial build for Sisyphus
