Name: altcenter
Version: 1.0
Release: alt0.1
Summary: Application for show information and configure system

License: GPL-3.0+
Group: Graphical desktop/Other
URL: http://www.altlinux.org/altcenter

Source0: %name-%version.tar

ExcludeArch: ppc64le armh

BuildRequires(pre): rpm-build-python3

%add_python3_path %_datadir/%name

%description
This is the grapical plugin-based application for show information and
configure system.

Available plugins:
- about
- license
- documentation
- hardware
- settings
- useful

%prep
%setup

%install
%makeinstall_std

%files
%doc README.md TODO.md
%_bindir/%name
%_datadir/%name
%_desktopdir/%name.desktop

%changelog
* Wed Jan 22 2025 Andrey Cherepanov <cas@altlinux.org> 1.0-alt0.1
- Initail build for Sisyphus.
