Name:  yandex-disk-indicator
Version: 1.11.0
Release: alt2.git561c25c
Summary: Panel indicator for YandexDisk CLI client for Linux
Group: Communications
License: GPL-3.0
URL: https://github.com/slytomcat/yandex-disk-indicator

Source0: %name-%version.tar
BuildArch: noarch

BuildRequires(pre): rpm-build-python3 rpm-build-gir
%add_python3_req_skip gi.repository.GLib
%add_python3_req_skip gi.repository.GdkPixbuf

%description
Panel indicator for YandexDisk CLI client for Linux

%prep
%setup -q

%build

%install
pushd build
TARGET=%buildroot%_prefix ./prepare.sh
popd
chmod 0644 %buildroot%_desktopdir/*.desktop
%find_lang %name

%files -f %name.lang
%_bindir/*
%_desktopdir/*
%_datadir/yd-tools

%changelog
* Mon Oct 31 2022 Andrey Cherepanov <cas@altlinux.org> 1.11.0-alt2.git561c25c
- New snapshot from upstream (ALT #44129).

* Fri Aug 13 2021 Andrey Cherepanov <cas@altlinux.org> 1.11.0-alt2
- Fix URL and License tags.

* Fri Jun 21 2019 Andrey Cherepanov <cas@altlinux.org> 1.11.0-alt1
- New version.

* Mon Apr 29 2019 Andrey Cherepanov <cas@altlinux.org> 1.10.9-alt1
- New version.

* Fri Apr 26 2019 Andrey Cherepanov <cas@altlinux.org> 1.10.7-alt1
- New version.

* Wed Oct 31 2018 Andrey Cherepanov <cas@altlinux.org> 1.10.6-alt1
- New version.

* Tue Oct 16 2018 Andrey Cherepanov <cas@altlinux.org> 1.10.5-alt1
- New version.

* Sun May 20 2018 Andrey Cherepanov <cas@altlinux.org> 1.10.4-alt1
- New version.

* Mon Apr 23 2018 Andrey Cherepanov <cas@altlinux.org> 1.10.3-alt1
- New version.

* Sat Mar 24 2018 Andrey Cherepanov <cas@altlinux.org> 1.10.2-alt1
- New version.

* Thu Mar 22 2018 Andrey Cherepanov <cas@altlinux.org> 1.10.1-alt1
- New version.

* Wed Mar 21 2018 Andrey Cherepanov <cas@altlinux.org> 1.10.0-alt1
- New version.

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
