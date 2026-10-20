%define oname image_paster
%define pluginsdir %_datadir/roundcube/plugins

Name: roundcube-plugin-%oname
Version: 1.0
Release: alt1

Summary: Roundcube plugin to paste images from the clipboard

License: GPL-3.0-or-later
Group: Networking/Mail
Url: https://github.com/mkrauser/roundcube_image_paster

Packager: Vitaly Lipatov <lav@altlinux.ru>

# Source-url: https://github.com/mkrauser/roundcube_image_paster/archive/refs/tags/v%version.tar.gz
Source: %name-%version.tar

BuildArch: noarch

Requires: roundcube >= 1.7

%description
Roundcube plugin which allows to paste images from the clipboard directly
into the body of a new email in the compose window.

%prep
%setup
find -type f -print0 | xargs -0 chmod a-x

%install
mkdir -p %buildroot%pluginsdir/%oname/
cp -a * %buildroot%pluginsdir/%oname/

%files
%pluginsdir/%oname/

%changelog
* Tue Oct 20 2026 Vitaly Lipatov <lav@altlinux.ru> 1.0-alt1
- initial build for Sisyphus
