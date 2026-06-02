Name: icon-themes-mint-l
Version: 1.8.1
Release: alt1

Summary: Mint-L Icon Theme

License: GPLv3 and CC-BY-SA-4.0
Group: Graphical desktop/MATE
URL: https://github.com/linuxmint/mint-l-icons
VCS: https://github.com/linuxmint/mint-l-icons.git

Source: %name-%version.tar

BuildArch: noarch

AutoReqProv: no

%description
Mint-L icon theme contains the application and category, folder,
device, mimetype, action and panel icons originate from the
Moka, Arc, Paper, Elementary, ePapirus themes.

%package -n folder-color-switcher-mint-l
Summary: Mint-L style for Folder Color Switcher
Group: Graphical desktop/Other
Requires: %name = %EVR
%description -n folder-color-switcher-mint-l
This package contains the style for Folder Color Switcher.

%prep
%setup

%build
# Remove broken links
find usr/share/icons -xtype l -delete

%install
mkdir -p %buildroot
cp -a usr %buildroot/

%files
%doc debian/copyright README.md
%_datadir/icons/Mint-L*

%files -n folder-color-switcher-mint-l
%_datadir/folder-color-switcher/colors.d/Mint-L.json

%changelog
* Tue Jun 02 2026 Alexander Kovalev <alexvk@altlinux.org> 1.8.1-alt1
- New version 1.8.1.

* Sat Jan 17 2026 Alexander Kovalev <alexvk@altlinux.org> 1.8.0-alt1
- New version 1.8.0.

* Wed Sep 03 2025 Alexander Kovalev <alexvk@altlinux.org> 1.7.6-alt1
- New version 1.7.6.

* Sun May 18 2025 Alexander Kovalev <alexvk@altlinux.org> 1.7.4-alt1
- Initial build for ALT.
