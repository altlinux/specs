%define oname PoemChords
%define mwversion 1.46
%setup_mediawiki_ext %mwversion %oname

Name: mediawiki-extensions-%oname
Version: 1.0
Release: alt1

Summary: MediaWiki extension for poems and songs with guitar chords and transposition

License: CC0-1.0
Group: Networking/WWW
Url: https://github.com/vitlav/mediawiki-extensions-PoemChords

Packager: Vitaly Lipatov <lav@altlinux.ru>

BuildArch: noarch

BuildRequires(pre): rpm-macros-mediawiki >= 0.7

# Source-url: https://github.com/vitlav/mediawiki-extensions-PoemChords/archive/refs/tags/%version.tar.gz
Source: %oname-%version.tar

%description
The PoemChords extension adds the <poemchords> tag, based on the Poem
extension. It formats verses with line breaks and indents, highlights guitar
chords written in the text and lets a reader transpose them by halftones
in the browser.

%prep
%setup -n %oname-%version

%install
%mediawiki_ext_install 50 %oname

%files -f %oname.files

%changelog
* Fri Oct 16 2026 Vitaly Lipatov <lav@altlinux.ru> 1.0-alt1
- initial build for Sisyphus
