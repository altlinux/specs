Name: kde-styles-splash-children
Version: 1.0
Release: alt3
BuildArch: noarch

Summary: KDE splash for Children 4.0.x

License: GPL
Group: Graphical desktop/KDE

Packager: Alexandra Panyukova <mex3@altlinux.ru>

Source: %name-%version.tar

BuildRequires: fontconfig freetype2 kde-settings kdelibs

%description
KDE splash for Children 4.0.x

%prep
%setup -q 

%install
mkdir -p %buildroot/%_datadir/apps/ksplash/Themes/ALTLinuxChildren
install -m 644 *png %buildroot/%_datadir/apps/ksplash/Themes/ALTLinuxChildren/
install -m 644 *rc %buildroot/%_datadir/apps/ksplash/Themes/ALTLinuxChildren/

%files
%_datadir/apps/ksplash/Themes/*

%changelog
* Thu Jul 10 2008 Alexandra Panyukova <mex3@altlinux.ru> 1.0-alt3
- build for children

* Thu Oct 18 2007 Anton V. Boyarshinov <boyarsh@altlinux.ru> 1.0-alt2
- text on top fixed 

* Thu Oct 18 2007 Anton V. Boyarshinov <boyarsh@altlinux.ru> 1.0-alt1
- initial build 

