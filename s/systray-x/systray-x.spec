%def_without kde5

Name:    systray-x
Version: 0.9.9
Release: alt1

Summary: A system tray extension for Thunderbird 68+
License: MPL-2.0
Group:   Other
Url:     https://github.com/Ximi1970/systray-x

Packager: Andrey Cherepanov <cas@altlinux.org>

Source: %name-%version.tar
Patch0: %name-version.patch

BuildRequires(pre): rpm-build-thunderbird
BuildRequires: qt5-base-devel
BuildRequires: qt5-x11extras-devel
BuildRequires: zip
BuildRequires: unzip
%if_with kde5
BuildRequires: kf5-knotifications-devel
%endif

Requires: thunderbird

%description
SysTray-X is a system tray extension for Thunderbird 68+. The addon uses the
WebExtension API's to control an external system dependent system tray
application.

The addon and system tray application can do:
* custom new mail icon
* display number of unread / new mails
* show / hide Thunderbird (minimize)
* minimizing hides to tray
* minimize on startup
* minimize on close

%prep
%setup
%patch0 -p1

%build
export PATH=$PATH:%_qt5_bindir
%make_build \
%if_without kde5
	OPTIONS="DEFINES+=NO_KDE_INTEGRATION"
%endif
sed < app/config/linux/SysTray_X.json.template -e 's|SYSTRAY_X_PATH|%{_bindir}/SysTray-X|' > SysTray_X.json

%install
install -Dm0755 SysTray-X %buildroot/%_bindir/SysTray-X
install -Dm0644 SysTray_X.json %buildroot%_libdir/mozilla/native-messaging-hosts/SysTray_X.json
mkdir -p %buildroot%tbird_arch_extensionsdir/systray-x@Ximi1970
unzip -d %buildroot%tbird_arch_extensionsdir/systray-x@Ximi1970 systray-x@Ximi1970.xpi

%files
%doc README.md FAQ.txt README.preferences.md
%_bindir/SysTray-X
%_libdir/mozilla/native-messaging-hosts/SysTray_X.json
%tbird_arch_extensionsdir/systray-x@Ximi1970

%changelog
* Sat Apr 27 2024 Andrey Cherepanov <cas@altlinux.org> 0.9.9-alt1
- New version.

* Fri Dec 15 2023 Andrey Cherepanov <cas@altlinux.org> 0.9.8-alt1
- New version.

* Sat Nov 11 2023 Andrey Cherepanov <cas@altlinux.org> 0.9.7-alt1
- New version.

* Sat Oct 28 2023 Andrey Cherepanov <cas@altlinux.org> 0.9.6-alt1
- New version.

* Mon Aug 07 2023 Andrey Cherepanov <cas@altlinux.org> 0.9.5-alt1
- New version.

* Mon Jul 24 2023 Andrey Cherepanov <cas@altlinux.org> 0.9.4-alt1
- New version.

* Sun Jul 16 2023 Andrey Cherepanov <cas@altlinux.org> 0.9.3-alt1
- New version.

* Tue Apr 25 2023 Andrey Cherepanov <cas@altlinux.org> 0.9.2-alt1
- Initial build for Sisyphus
