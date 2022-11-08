Name:    xdg-prefs
Version: 0.2
Release: alt1

Summary: A GUI program to view and change your default programs' preferences (which program should open which type of file) using the XDG Specifications
License: Apache-2.0
Group:   Other
URL:     https://github.com/rchaput/xdg-prefs

Packager: Andrey Cherepanov <cas@altlinux.org>

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-dev python3-module-setuptools

BuildArch: noarch

Source:  %name-%version.tar

%description
%summary

%prep
%setup -n %name-%version

%build
%python3_build

%install
%python3_install

%files
%doc *.md
%_bindir/%name
%python3_sitelibdir/xdgprefs
%python3_sitelibdir/*.egg-info

%changelog
* Tue Nov 08 2022 Andrey Cherepanov <cas@altlinux.org> 0.2-alt1
- Initial build for Sisyphus
