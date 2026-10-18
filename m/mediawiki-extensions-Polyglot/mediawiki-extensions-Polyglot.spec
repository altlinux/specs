%define oname Polyglot
%define mwversion 1.46
%define commit c9bce09
%setup_mediawiki_ext %mwversion %oname

Name: mediawiki-extensions-%oname
Version: 1.46
Release: alt1

Summary: MediaWiki extension for automatic redirects based on user language

License: GPL-2.0-or-later
Group: Networking/WWW
Url: https://www.mediawiki.org/wiki/Extension:%oname

Packager: Vitaly Lipatov <lav@altlinux.ru>

BuildArch: noarch

BuildRequires(pre): rpm-macros-mediawiki >= 0.7

# Source-url: https://extdist.wmflabs.org/dist/extensions/%oname-%MWREL-%commit.tar.gz
Source: %oname-%version.tar
Patch: %oname-mediawiki-1.46-hooks.patch
Patch1: %oname-mediawiki-1.46-language-links-order.patch

%description
The Polyglot extension provides automatic redirects based on user language:
when visiting the page Foo with the user language set to de, the user is
redirected to Foo/de, if it exists (Foo/ always shows Foo itself).
Polyglot also shows the existing localized versions of each page
(subpages Foo/<lang>) as interlanguage links in the sidebar.

%prep
%setup -n %oname-%version
%patch -p1
%patch1 -p1

%install
%mediawiki_ext_install 50 %oname
# remove development files
rm -rv %buildroot%mediawiki_ext_dir/{Gruntfile.js,package.json,package-lock.json,composer.json}

%files -f %oname.files

%changelog
* Sat Oct 17 2026 Vitaly Lipatov <lav@altlinux.ru> 1.46-alt1
- initial build for Sisyphus
- added patch: port the hooks removed in MediaWiki 1.46: LinkBegin to
  HtmlPageLinkRendererBegin, SkinTemplateOutputPageBeforeExec to
  SkinTemplateGetLanguageLink
- added patch: keep the order of the language links (the LanguageLinks hook
  restores the order of $wgPolyglotLanguages after the sorting by MediaWiki)
