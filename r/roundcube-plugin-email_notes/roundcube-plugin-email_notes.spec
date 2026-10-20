%define oname email_notes
%define pluginsdir %_datadir/roundcube/plugins

Name: roundcube-plugin-%oname
Version: 1.0.1
Release: alt1

Summary: Roundcube plugin to add notes to emails

License: MIT
Group: Networking/Mail
Url: https://github.com/prefo-pl/roundcube-plugin-email-notes

Packager: Vitaly Lipatov <lav@altlinux.ru>

# Source-url: https://github.com/prefo-pl/roundcube-plugin-email-notes/archive/refs/tags/%version.tar.gz
Source: %name-%version.tar
Patch: email_notes-no-config-warning.patch

BuildArch: noarch

Requires: roundcube >= 1.7

%description
Roundcube plugin which allows to add personal notes to email messages.

%prep
%setup
find -type f -print0 | xargs -0 chmod a-x
%patch -p1

%install
mkdir -p %buildroot%pluginsdir/%oname/
cp -a * %buildroot%pluginsdir/%oname/

%files
%pluginsdir/%oname/

%changelog
* Tue Oct 20 2026 Vitaly Lipatov <lav@altlinux.ru> 1.0.1-alt1
- initial build for Sisyphus
