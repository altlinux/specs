%define _unpackaged_files_terminate_build 1
%define ext_id firefoxpwa@filips.si

Name: firefoxpwa
Version: 2.20.1
Release: alt1

Summary: A tool to install, manage and use Progressive Web Apps (PWAs) in Mozilla Firefox
License: MPL-2.0
Group: Networking/WWW
VCS: https://github.com/filips123/PWAsForFirefox
URL: https://pwasforfirefox.filips.si/
# Extention URL: https://addons.mozilla.org/en-US/firefox/addon/pwas-for-firefox/

ExcludeArch: i586

Source0: %name-%version.tar
Source1: vendor.tar
Source2: pwas_for_firefox-%version.xpi

BuildRequires(pre): rpm-build-firefox
BuildRequires(pre): rpm-macros-rust
BuildRequires: rpm-build-rust
BuildRequires: libssl-devel

%description
Progressive Web Apps (PWAs) are web apps that use web APIs and features along with progressive enhancement strategy to bring a native app-like user experience to cross-platform web applications.

This project creates a custom modified Firefox runtime to allow websites to be installed as standalone apps and provides a console tool and browser extension to install, manage and use them.


%package -n %firefox_name-%name
Summary: Browser extension for FirefoxPWA
License: MPL-2.0
Group: Networking/WWW
ExcludeArch: i586
Requires: %name = %EVR
Requires: firefox

%description -n %firefox_name-%name
Progressive Web Apps (PWAs) are web apps that use web APIs and features along with progressive enhancement strategy to bring a native app-like user experience to cross-platform web applications.

Browser extension for Progressive Web Apps for Firefox (FirefoxPWA).


%package doc
Summary: Documentation for firefoxpwa
License: MPL-2.0
Group: Documentation
BuildArch: noarch

%description doc
Progressive Web Apps (PWAs) are web apps that use web APIs and features along with progressive enhancement strategy to bring a native app-like user experience to cross-platform web applications.

FirefoxPWA's documentation files.


%prep
%setup
pushd native

# Set the correct version in source files
sed -i "s/version = \"0.0.0\"/version = \"%version\"/g" Cargo.toml
sed -i "s/DISTRIBUTION_VERSION = '0.0.0'/DISTRIBUTION_VERSION = '%version'/g" userchrome/profile/chrome/pwa/chrome.sys.mjs
sed -i 's|/usr/libexec|%_libexecdir|' manifests/linux.json

# Prepare vendor
tar -xf %SOURCE1
%rust_prep
cat >> .cargo/config.toml <<EOF
[source."git+https://github.com/filips123/WebAppManifestRS?branch=main"]
git = "https://github.com/filips123/WebAppManifestRS"
branch = "main"
replace-with = "vendored-sources"

[source."git+https://github.com/filips123/mime?branch=fix-compile-warnings"]
git = "https://github.com/filips123/mime"
branch = "fix-compile-warnings"
replace-with = "vendored-sources"
EOF

popd

%build
pushd native
%rust_build
popd

%check
pushd native
%rust_test
popd

%install
pushd native
# Executables
install -Dm 755 "target/release/%name" "%buildroot/%_bindir/%name"
install -Dm 755 "target/release/%name-connector" "%buildroot/%_libexecdir/%name-connector"

# Manifest
install -Dm 644 manifests/linux.json "%buildroot/%_libdir/mozilla/native-messaging-hosts/%name.json"

# Completions
install -Dm 644 "target/release/completions/%name.bash" "%buildroot/%_datadir/bash-completion/completions/%name"
install -Dm 644 "target/release/completions/%name.fish" "%buildroot/%_datadir/fish/vendor_completions.d/%name.fish"
install -Dm 644 "target/release/completions/_%name" "%buildroot/%_datadir/zsh/site-functions/_%name"

# UserChrome
install -dm 755 "%buildroot/%_datadir/%name/userchrome/"
cp -r userchrome/* "%buildroot/%_datadir/%name/userchrome/"

# Metadata
install -Dm 644 packages/appstream/si.filips.FirefoxPWA.metainfo.xml "%buildroot/%_datadir/metainfo/si.filips.FirefoxPWA.metainfo.xml"
install -Dm 644 packages/appstream/si.filips.FirefoxPWA.svg "%buildroot/%_datadir/icons/hicolor/scalable/apps/si.filips.FirefoxPWA.svg"
popd

# Extenstion
install -Dm 644 %SOURCE2 "%buildroot%firefox_arch_extensionsdir/%ext_id.xpi"

%files
%doc README.md LICENSE
# Executables
%_bindir/%name
%_libexecdir/%name-connector

# Manifest
%_libdir/mozilla/native-messaging-hosts/%name.json

# Completions
%_datadir/bash-completion/completions/%name
%_datadir/fish/vendor_completions.d/%name.fish
%_datadir/zsh/site-functions/_%name

# UserChrome
%_datadir/%name/userchrome/

# Metadata
%_datadir/metainfo/si.filips.FirefoxPWA.metainfo.xml
%_datadir/icons/hicolor/scalable/apps/si.filips.FirefoxPWA.svg

%files -n %firefox_name-%name
%firefox_arch_extensionsdir/%ext_id.xpi

%files doc
%doc docs

%changelog
* Tue Nov 10 2026 Aleksandr Dovydenkov <asd@altlinux.org> 2.20.1-alt1
- Initial build for ALT Linux.

