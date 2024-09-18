%define rname mint-y-icons

Name: icon-themes-mint-y
Version: 1.7.7
Release: alt1

Summary: The Mint-Y icon theme
License: CC-BY-SA-4.0
Group: Graphical desktop/MATE
Url: https://github.com/linuxmint/mint-y-icons
BuildArch: noarch

AutoReqProv: no

Source: %rname-%version.tar

%description
%summary.

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
%exclude %_datadir/folder-color-switcher/

%changelog
* Wed Sep 18 2024 Anton Kurachenko <srebrov@altlinux.org> 1.7.7-alt1
- Initial build for Sisyphus.
