Name:		yandex-disk-indicator
Version:	1.9.8
Release:	alt2
Summary:	Panel indicator for YandexDisk CLI client for Linux
Group:		Communications
License:	Creative Commons Attribution-ShareAlike
URL:		https://github.com/slytomcat/yandex-disk-indicator/wiki
Source0:	%name-%version.tar
BuildArch:	noarch

BuildRequires(pre): rpm-build-python3 rpm-build-gir
#Requires: typelib(AppIndicator3)
#Requires: python3-module-pyinotify
#Requires: python3-module-pygobject3
#Requires: libnotify-gir
%add_python3_req_skip gi.repository.GLib
%add_python3_req_skip gi.repository.GdkPixbuf

%description
Panel indicator for YandexDisk CLI client for Linux

%prep
%setup -q

%build
pushd build
./prepare.sh
popd

%install
mkdir -p %buildroot
cp -r build/yd-tools/usr %buildroot
chmod 644 %buildroot%_desktopdir/*

%find_lang %name

%files -f %name.lang
%_bindir/*
%_desktopdir/*
%_datadir/yd-tools

%changelog
* Wed Mar 15 2017 Andrey Cherepanov <cas@altlinux.org> 1.9.8-alt2
- Added missing buildrequires: rpm-build-python3 rpm-build-gir (thanks antohami@)

* Sun Mar 05 2017 Andrey Cherepanov <cas@altlinux.org> 1.9.8-alt1
- New version

* Fri Feb 17 2017 Andrey Cherepanov <cas@altlinux.org> 1.9.7-alt1
- new version 1.9.7

* Mon Jan 23 2017 Andrey Cherepanov <cas@altlinux.org> 1.9.6-alt1
- new version 1.9.6
- require python3-module-pygobject3 and libnotify-gir (ALT #33023)

* Mon Aug 01 2016 Andrey Cherepanov <cas@altlinux.org> 1.9.0-alt1
- new version 1.9.0

* Mon Jul 25 2016 Andrey Cherepanov <cas@altlinux.org> 1.8.16-alt1
- Initial build in Sisyphus (thanks ROSA for the spec)
