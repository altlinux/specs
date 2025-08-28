%define mozilla_arch_extdir %_libdir/mozilla/extensions
%define tbird_cid \{3550f703-e582-4d05-9a08-453d09bdfdc6\}
%define tbird_arch_extensionsdir %mozilla_arch_extdir/%tbird_cid

# Disable because binary with same name
%def_without kde

Name:    systray-x
Version: 0.9.11
Release: alt5

Summary: A system tray extension for Thunderbird
License: MPL-2.0
Group:   Other
Url:     https://github.com/Ximi1970/systray-x

Packager: Andrey Cherepanov <cas@altlinux.org>

Source: %name-%version.tar
Patch0: %name-version.patch

ExclusiveArch: %thunderbird_arches

BuildRequires(pre): rpm-macros-thunderbird
BuildRequires: thunderbird
BuildRequires: qt6-base-devel
BuildRequires: zip
BuildRequires: unzip
%if_with kde
BuildRequires: kf6-knotifications-devel
BuildRequires: kf6-kstatusnotifieritem-devel
%endif

Requires: thunderbird

%description
SysTray-X is a system tray extension for Thunderbird. The addon uses the
WebExtension API's to control an external system dependent system tray
application.

The addon and system tray application can do:
* custom new mail icon
* display number of unread / new mails
* show / hide Thunderbird (minimize)
* minimizing hides to tray
* minimize on startup
* minimize on close

%if_with kde
%package kde
Summary: System tray extension for Thunderbird for KDE
Group: Other
Requires: %name = %EVR

%description kde
%summary
%endif

%prep
%setup
%autopatch -p1
max_ver="$((`sed -n 's/^Version=\([0-9]\+\)\..*$/\1/p' %_libdir/thunderbird/application.ini`+1))"
# Use real current Thunderbird version + 1
# Set maximum supported version
max_ver="200"
subst "s|136|$max_ver|" webext/manifest.json

%build
export PATH=$PATH:%_qt6_bindir
%if_with kde
%add_optflags -L%_libdir/kf6/devel
%endif
%make_build \
%if_without kde
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
* Thu Aug 28 2025 Andrey Cherepanov <cas@altlinux.org> 0.9.11-alt5
- Set maximum supported version to 200 (ALT #55745).

* Wed Jun 04 2025 Ajrat Makhmutov <rauty@altlinux.org> 0.9.11-alt4
- Use %%thunderbird_arch to specify supported architectures.

* Fri Apr 25 2025 Andrey Cherepanov <cas@altlinux.org> 0.9.11-alt3
- FTBFS: fixed build with new thunderbird.

* Fri Apr 18 2025 Andrey Cherepanov <cas@altlinux.org> 0.9.11-alt2
- Adapted to Thunderbird 137.x (ALT #53895).
- Built with Qt6.

* Thu Mar 13 2025 Andrey Cherepanov <cas@altlinux.org> 0.9.11-alt1
- New version.

* Tue Nov 19 2024 Andrey Cherepanov <cas@altlinux.org> 0.9.10-alt2
- ExcludeArch: armh ppc64le.

* Sun Aug 11 2024 Andrey Cherepanov <cas@altlinux.org> 0.9.10-alt1
- New version.

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
