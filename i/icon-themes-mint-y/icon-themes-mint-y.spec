%define rname mint-y-icons

Name: icon-themes-mint-y
Version: 1.8.8
Release: alt1

Summary: The Mint-Y icon theme
License: CC-BY-SA-4.0
Group: Graphical desktop/MATE
Url: https://github.com/linuxmint/mint-y-icons
Vcs: https://github.com/linuxmint/mint-y-icons.git
BuildArch: noarch

AutoReqProv: no

Source: %rname-%version.tar

%description
%summary.

%package -n folder-color-switcher-mint-y
Summary: Mint-Y style for Folder Color Switcher
Group: Graphical desktop/Other
Requires: %name = %EVR
%description -n folder-color-switcher-mint-y
This package contains the style for Folder Color Switcher.

%prep
%setup -q -n %rname-%version

#Remove broken symlinks
find usr/share/icons -xtype l -delete

%build
#nope

%install
mkdir -p %buildroot
cp -a usr %buildroot/

%files
%doc debian/copyright README.md
%_datadir/icons/Mint-*/

%files -n folder-color-switcher-mint-y
%_datadir/folder-color-switcher/colors.d/Mint-Y.json

%changelog
* Fri Oct 17 2025 Anton Kurachenko <srebrov@altlinux.org> 1.8.8-alt1
- New version 1.8.8.

* Mon Sep 08 2025 Anton Kurachenko <srebrov@altlinux.org> 1.8.6-alt1
- New version 1.8.6.

* Sat Aug 23 2025 Anton Kurachenko <srebrov@altlinux.org> 1.8.5-alt1
- New version 1.8.5.

* Sun Jun 01 2025 Alexander Kovalev <alexvk@altlinux.org> 1.8.3-alt2
- Add package with style for Folder Color Switcher.

* Sun Jan 19 2025 Anton Kurachenko <srebrov@altlinux.org> 1.8.3-alt1
- New version 1.8.3.

* Mon Dec 23 2024 Anton Kurachenko <srebrov@altlinux.org> 1.8.0-alt1
- New version 1.8.0.

* Wed Sep 18 2024 Anton Kurachenko <srebrov@altlinux.org> 1.7.7-alt1
- Initial build for Sisyphus.
