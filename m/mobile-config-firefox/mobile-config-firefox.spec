%define _unpackaged_files_terminate_build 1

Name: mobile-config-firefox
Version: 5.4.0
Release: alt1

Summary: Mobile and privacy friendly firefox configuration

License: MPL-2.0
Group: System/Configuration/Networking
URL: https://gitlab.postmarketos.org/postmarketOS/mobile-config-firefox

Source: %name-%version.tar

Requires: mozilla-common

BuildRequires(pre): rpm-build-firefox

%description
Mobile and privacy friendly configuration for current standard and
extended support releases of Firefox.

%prep
%setup
# fix hardcoded autoconfig path
sed -i "s|/usr/lib/mobile-config-firefox|%firefox_datadir|" \
                            src/mobile-config-autoconfig.js
%build
%make_build

%install
%makeinstall \
        DESTDIR=%buildroot \
        FIREFOX_DIR=%firefox_prefix \
        MCF_DIR=%firefox_datadir \
        %nil

%files
%firefox_datadir
%firefox_prefix
%_datadir/metainfo/org.postmarketos.mobile_config_firefox.metainfo.xml

%changelog
* Mon Jul 06 2026 Egor Shestakov <ved@altlinux.org> 5.4.0-alt1
- Update to 5.4.0.

* Mon May 25 2026 Egor Shestakov <ved@altlinux.org> 5.2.0-alt1
- Update to 5.2.0.

* Wed Dec 24 2025 Egor Shestakov <ved@altlinux.org> 5.1.0-alt1
- Update to 5.1.0:
  + Change FIREFOX_CONFIG_DIR to MCF_DIR.
- Minor spec cleanup.

* Wed Dec 17 2025 Andrew Savchenko <bircoph@altlinux.org> 5.0.1-alt1
- Update to 5.0.1.

* Sat Apr 26 2025 Egor Shestakov <ved@altlinux.org> 4.6.0-alt1
- New version.

* Tue Mar 11 2025 Egor Shestakov <ved@altlinux.org> 4.4.0-alt1
- Initial build.
