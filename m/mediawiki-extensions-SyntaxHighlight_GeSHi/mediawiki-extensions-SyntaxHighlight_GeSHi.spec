%define ShortName SyntaxHighlight_GeSHi

%define mwversion 1.31
%setup_mediawiki_ext %mwversion %ShortName

Name: mediawiki-extensions-%ShortName
Version: 2.0
Release: alt1

Summary: Extension for mediawiki to highlight source code with GeSHi.
Summary(ru_RU.UTF-8): Расширение mediawiki для раскраски синтаксиса исходников с помощью GeSHi.

Group: Networking/WWW
Url: http://www.mediawiki.org/wiki/Extension:SyntaxHighlight_GeSHi
License: GPLv2

Packager: Michael A. Kangin <prividen@altlinux.org>

BuildArch: noarch

BuildRequires(pre): rpm-build-mediawiki >= 0.6

Requires: python3-module-Pygments >= 2.2.0

Requires: mediawiki-common >= %mwversion

# Source-url: https://github.com/wikimedia/mediawiki-extensions-SyntaxHighlight_GeSHi/archive/%MWREL.zip
Source: %ShortName-%version.tar

%description
The <source> tags allow the display of preformatted code modules but in addition
they add coloring according to the code language settings. Like the <pre> tags
and the <poem> tags, they preserve white space, that is, they depict the code
module exactly as it was typed.

%prep
%setup -n %ShortName-%version

%build

%install
%mediawiki_ext_install 50 %ShortName
rm -f %buildroot%_datadir/mediawiki/extensions/%ShortName/pygments/pygmentize
ln -s %_bindir/pygmentize3 %buildroot%_datadir/mediawiki/extensions/%ShortName/pygments/pygmentize

%files -f %ShortName.files
%add_findreq_skiplist %_datadir/mediawiki/extensions/%ShortName/pygments
%doc README

%changelog
* Sat Oct 06 2018 Vitaly Lipatov <lav@altlinux.ru> 2.0-alt1
- new version (2.0) with rpmgs script, build for MW >= 1.31
- use pygmentize instead geshi

* Wed Mar 26 2014 Vitaly Lipatov <lav@altlinux.ru> 1.22.4-alt1
- new version 1.22.4

* Wed Dec 30 2009 Michael A. Kangin <prividen@altlinux.org> 0.r60508-alt1
- New version
- Adopt for new Mediawiki config layout

* Sun Jul 19 2009 Michael A. Kangin <prividen@altlinux.org> 0.r53473-alt1
- Initial release

