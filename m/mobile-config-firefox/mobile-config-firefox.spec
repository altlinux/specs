%define _unpackaged_files_terminate_build 1

Name: mobile-config-firefox
Version: 5.0.1
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
sed -i "s|/usr/lib/mobile-config-firefox|%firefox_datadir|" src/mobile-config-autoconfig.js
# fix "outdated UserAgent" in Google search
sed -i 's/wwww.)?google/www.)?google/' src/modules/UserAgentManager.sys.mjs

%build
%make_build

%install
%makeinstall \
		DESTDIR=%buildroot \
		FIREFOX_DIR=%firefox_prefix \
		FIREFOX_CONFIG_DIR=%firefox_datadir \


%files
%firefox_datadir
%firefox_prefix
%_datadir/metainfo/org.postmarketos.mobile_config_firefox.metainfo.xml

%changelog
* Wed Dec 17 2025 Andrew Savchenko <bircoph@altlinux.org> 5.0.1-alt1
- Update to 5.0.1.

* Sat Apr 26 2025 Egor Shestakov <ved@altlinux.org> 4.6.0-alt1
- New version.

* Tue Mar 11 2025 Egor Shestakov <ved@altlinux.org> 4.4.0-alt1
- Initial build.
