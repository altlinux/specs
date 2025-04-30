Name: mobile-config-firefox
Version: 4.6.0
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

%build
%make_build

%install
%makeinstall \
		DESTDIR=%buildroot \
		FIREFOX_DIR=%firefox_prefix \
		FIREFOX_CONFIG_DIR=%firefox_datadir \


%files
%config(noreplace) %firefox_datadir/policies/policies.json
%_sysconfdir/mobile-config-firefox/
%firefox_prefix/mobile-config-autoconfig.js
%firefox_prefix/defaults/pref/mobile-config-prefs.js
%_datadir/metainfo/org.postmarketos.mobile_config_firefox.metainfo.xml

%changelog
* Sat Apr 26 2025 Egor Shestakov <ved@altlinux.org> 4.6.0-alt1
- New version.

* Tue Mar 11 2025 Egor Shestakov <ved@altlinux.org> 4.4.0-alt1
- Initial build.
