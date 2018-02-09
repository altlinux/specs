Name:		yandex-disk-indicator
Version:	1.9.18
Release:	alt1
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
* Fri Feb 09 2018 Andrey Cherepanov <cas@altlinux.org> 1.9.18-alt1
- New version.

* Mon Jan 29 2018 Andrey Cherepanov <cas@altlinux.org> 1.9.16-alt1
- New version.

* Tue Jan 09 2018 Andrey Cherepanov <cas@altlinux.org> 1.9.15-alt1
- New version.

* Tue Dec 19 2017 Andrey Cherepanov <cas@altlinux.org> 1.9.14-alt1
- New version.

* Tue Nov 07 2017 Andrey Cherepanov <cas@altlinux.org> 1.9.12-alt1
- New version

* Tue May 09 2017 Andrey Cherepanov <cas@altlinux.org> 1.9.11-alt1
- New version

* Sat Apr 22 2017 Andrey Cherepanov <cas@altlinux.org> 1.9.10-alt1
- New version

* Mon Apr 10 2017 Andrey Cherepanov <cas@altlinux.org> 1.9.9-alt1
- New version

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
