%define oname FileSync

Name: mediawiki-extensions-%oname
Version: 0.0.2
Release: alt1

BuildArch: noarch

Group: Networking/WWW
Summary: A template which can be added to an article to make it synchronise with a file
Url: http://www.mediawiki.org/wiki/Extension:%oname

Packager: Vitaly Lipatov <lav@altlinux.ru>

License: LGPL

BuildPreReq: rpm-build-mediawiki >= 0.2
Requires: mediawiki-common >= 1.15.1-alt4

# It is new feature etersoft-build-utils since 1.7.6: supports commented real url
# Source-url: http://www.organicdesign.co.nz/Extension:FileSync.php
Source: %oname-%version.tar

%description
This extension allows wiki sysops to set up relationships between wiki
articles and files in the local file-system so that when the article
is modified the file's content is also updated. Also if the file in
the file-system is modified, then when the article is next viewed, it's
content will be updated and the revision added to the history as if it
were edited in the wiki. Whenever the article is updated from the file, or
if the file doesn't exist, the user viewing the article is notified with
a warning message. If the article is deleted, then the corresponding file
in the file-system is also deleted, and if a synchronised file doesn't
exist when its article is saved the wiki will attempt to create it.

%prep
%setup -n %oname-%version

%install
%mediawiki_ext_install 50 %oname

%files -f %oname.files

%changelog
* Tue Feb 02 2010 Vitaly Lipatov <lav@altlinux.ru> 0.0.2-alt1
- initial build for ALT Linux Sisyphus
