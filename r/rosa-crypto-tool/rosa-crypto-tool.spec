Name:           rosa-crypto-tool
Version:        0.1.5
Release:        alt1
Summary:        Program for working with electronic digital signatures

Group:          Text tools
License:        BSD
URL:            https://abf.io/uxteam/rosa-crypto-tool-devel.git

Source0:        %name-%version.tar
Patch:		%name-%version-%release.patch

BuildArch:      noarch
BuildRequires(pre): rpm-build-python
BuildRequires:  python-devel
BuildRequires:  python-module-distribute

Requires: python-module-pyudev-pyqt5 >= 0.21.0

%description
Program for working with electronic digital signatures.

%prep
%setup -q
%patch -p1

%build
%python_build

%install
%python_install
%find_lang %name

%files -f %name.lang
%_bindir/%name
%doc %_defaultdocdir/%name/help.pdf
%python_sitelibdir/*
%_desktopdir/%name.desktop
%_iconsdir/hicolor/scalable/apps/%name.svg

%changelog
* Wed Nov 02 2016 Andrey Cherepanov <cas@altlinux.org> 0.1.5-alt1
- New version

* Tue Oct 04 2016 Andrey Cherepanov <cas@altlinux.org> 0.1.0-alt0.1.beta
- New beta version
- Added executable and desktop files

* Sun Aug 14 2016 Andrey Cherepanov <cas@altlinux.org> 0.0.8-alt1
- Initial build in Sisyphus

