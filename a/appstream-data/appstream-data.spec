Name:      appstream-data
Summary:   ALT Linux AppStream metadata
Version:   20150308
Release:   alt1
Group:     System/Configuration/Packaging
BuildArch: noarch
License:   CC0 and CC-BY and CC-BY-SA and GFDL
URL:       http://www.altlinux.org/SoftwareCenter/Applications
Source:    %name-%version.tar

BuildRequires: libappstream-glib

%description
This package provides the distribution specific AppStream metadata
required for ALT Linux Software Center.

%prep
%setup -q

%install
DESTDIR=%buildroot appstream-util install altlinux.xml

%files
%_datadir/app-info/xmls/*

%changelog
* Sun Mar 08 2015 Andrey Cherepanov <cas@altlinux.org> 20150308-alt1
- Initial build in Sisyphus
