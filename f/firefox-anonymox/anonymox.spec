%define cid client@anonymox.net
%define ciddir 	%firefox_noarch_extensionsdir/%cid

Name: firefox-anonymox
Version: 2.1.1
Release: alt1
Summary: Easy anonymous web browsing
Group: Networking/WWW
License: CCPL
URL: https://addons.mozilla.org/ru/firefox/addon/anonymox/
Source: %name-%version.tar
Requires: %firefox_name
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>
BuildArch: noarch
BuildRequires(pre): rpm-build-firefox

%description 
AnonymoX is an initiative for anonymization in the internet. The aim is
to restore the users right of anonymity in the web. Most websites
monitor the behaviour of their users, giving the websites hosts the
ability to analyze the general users behaviour and create detailed user
profiles, which often times are sold to third parties.
A thread for the freedom of speech of the internet manifests in the
repression through federal or private organizations. More and more
governments censor websites with the excuse of child safety, copyright
infringement or the fight against terrorism and thereby limit the
freedom of speech.
Also blocking users by based on their origin with GeoIP-Blocks is
applied often, for example at media platforms like YouTube.

anonymoX enables you to...
* Browse the web anonymously
* Change your IP-Address (to one provided by us)
* Visit blocked/censored websites
* Appear to originate from another country
* Delete cookies, show your public ip, change browser id, ....

%prep
%setup
rm -fR .gear

%install
install -d %buildroot/%ciddir
cp -fR * %buildroot/%ciddir

%files
%ciddir

%changelog
* Mon Nov 04 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.1.1-alt1
- Initial build for Sisyphus

