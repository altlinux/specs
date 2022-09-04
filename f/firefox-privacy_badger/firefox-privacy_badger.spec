%define rname privacy_badger17
%define cid jid1-MnnxcxisBPnSXQ@jetpack

Name: firefox-privacy_badger
Version: 2021.11.23.1
Release: alt1

Summary: a browser extension that automatically learns to block invisible trackers

License: GPL-3.0-or-later
Group: Networking/WWW
Url: https://privacybadger.org/
BuildArch: noarch

# repacked https://addons.mozilla.org/firefox/downloads/file/3872283/privacy_badger17-%version.xpi
Source: %rname.xpi

BuildRequires(pre): rpm-build-firefox
BuildRequires: unzip

%description
Privacy Badger is a browser extension that automatically learns to block
invisible trackers. Instead of keeping lists of what to block, Privacy Badger
automatically discovers trackers based on their behavior.

Privacy Badger sends the Global Privacy Control signal to opt you out of data
sharing and selling, and the Do Not Track signal to tell companies not to track
you. If trackers ignore your wishes, Privacy Badger will learn to block them.

Besides automatic tracker blocking, Privacy Badger comes with privacy features
like click-to-activate replacements for potentially useful trackers (video
players, comments widgets, etc.), and link cleaning on Facebook and Google.

%install
install -pD -m 644 %SOURCE0 %buildroot%firefox_noarch_extensionsdir/%{cid}.xpi

%files
%firefox_noarch_extensionsdir/%{cid}.xpi

%changelog
* Sun Sep 04 2022 Vladimir D. Seleznev <vseleznv@altlinux.org> 2021.11.23.1-alt1
- Initial build for ALT Sisyphus.
