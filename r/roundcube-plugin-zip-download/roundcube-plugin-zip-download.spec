%define oname zip-download
%define pluginsdir %_datadir/roundcube/plugins

Name: roundcube-plugin-%oname

Version: 1.3
Release: alt1

Summary: Roundcube plugin for download all attachments to a message in one zip file

License: GPL2
Group: Networking/Mail
Url: http://www.tehinterweb.co.uk/roundcube/

Packager: Vitaly Lipatov <lav@altlinux.ru>

# FIXME: manually downloaded
# Source: https://github.com/JohnDoh/Roundcube-Plugin-Zip-Download/zipball/master
Source: %oname.tar

BuildArch: noarch

Requires: php5-zip
Requires: roundcube >= 0.4

Provides: roundcube-%oname
Obsoletes: roundcube-%oname

%description
This plugin adds an option to download all attachments to a message in one zip
file, when a message has multiple attachments. The plugin also allows the
download of a selection of messages in 1 zip file and the download of entire
folders.

%prep
%setup -n %oname
find -type f -print0 | xargs -0 chmod a-x

%install
mkdir -p %buildroot%pluginsdir/%oname/
cp -a * %buildroot%pluginsdir/%oname/
rm -rf %buildroot%pluginsdir/%oname/lib
rm -rf %buildroot%pluginsdir/%oname/CHANGELOG

%files
%doc README
%pluginsdir/%oname/

%changelog
* Wed Dec 28 2011 Vitaly Lipatov <lav@altlinux.ru> 1.3-alt1
- initial build for ALT Linux Sisyphus

