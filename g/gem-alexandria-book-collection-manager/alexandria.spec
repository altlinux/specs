%define        pkgname alexandria-book-collection-manager

Name:          gem-%pkgname
Version:       0.7.7
Release:       alt1
Summary:       Alexandria is a GNOME application to help you manage your book collection
License:       GPLv2
Group:         Development/Ruby
Url:           https://github.com/mvz/alexandria-book-collection-manager
Vcs:           https://github.com/mvz/alexandria-book-collection-manager.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
BuildRequires(pre): rpm-build-gnome
BuildRequires: gem(rake)
BuildRequires: gem(rspec)
BuildRequires: GConf
BuildRequires: intltool
BuildRequires: libGConf2-devel

Requires(preun,post): GConf
Requires:      alexandria
%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*

%description
Alexandria is a GNOME application to help you manage your book collection.

Alexandria:
 * retrieves book information from Amazon (including cover pictures) ;
 * saves data using the YAML format ;
 * features an HIG-compliant user interface ;
 * shows books in different views (standard list or icons list).


%package       -n alexandria
Summary:       HTML, XML, SAX, and Reader parser
Summary(ru_RU.UTF-8): Исполнямка для самоцвета %gemname
Group:         Books/Other
BuildArch:     noarch

Requires:      /usr/bin/update-desktop-database
Requires:      /usr/sbin/update-menus

%description   -n alexandria
Alexandria is a GNOME application to help you manage your book collection.


%package       -n gem-%pkgname-doc
Summary:       Documentation files for %gemname gem
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета %gemname
Group:         Development/Documentation
BuildArch:     noarch

%description   -n gem-%pkgname-doc
Documentation files for %gemname gem.

%description   -n gem-%pkgname-doc -l ru_RU.UTF8
Файлы сведений для самоцвета %gemname.


%prep
%setup

%build
%ruby_build --pre=pre_install --use=alexandria-book-collection-manager --alias=alexandria

%install
%ruby_install

mkdir -p %buildroot%_desktopdir/ %buildroot%_datadir/sounds/alexandria/
install -D -m 0644 schemas/alexandria.schemas %buildroot/%_sysconfdir/gconf/schemas/alexandria.schemas
install -D -m 0644 alexandria.desktop %buildroot%_desktopdir/alexandria.desktop
install -D -m 0644 misc/sounds/* %buildroot%_datadir/sounds/alexandria/

%find_lang alexandria --with-gnome

%check
%ruby_test

%post          -n alexandria
%gconf2_install alexandria

%preun         -n alexandria
if [ $1 = 0 ]; then
%gconf2_uninstall alexandria
fi

%files
%doc README*
%ruby_gemspecdir/alexandria-book-collection-manager-%version.gemspec
%ruby_gemslibdir/alexandria-book-collection-manager-%version/

%files      -n gem-%pkgname-doc
%ruby_gemsdocdir/alexandria-book-collection-manager-%version/

%files      -n alexandria
%_bindir/alexandria
%_mandir/*
%_desktopdir/alexandria.desktop
%config %gconf_schemasdir/*
%_datadir/sounds/alexandria/


%changelog
* Sun Nov 22 2020 Pavel Skrylev <majioa@altlinux.org> 0.7.7-alt1
- ^ 0.7.5 -> 0.7.7

* Mon May 25 2020 Pavel Skrylev <majioa@altlinux.org> 0.7.5-alt1
- ^ 0.7.4 -> 0.7.5
- ! spec syntax
- lost require deps to post script executables

* Wed Mar 04 2020 Pavel Skrylev <majioa@altlinux.org> 0.7.4-alt1
- updated (^) 0.7.3 -> 0.7.4
- fixed (!) spec

* Tue Sep 10 2019 Pavel Skrylev <majioa@altlinux.org> 0.7.3-alt4.1
- fixed (!) spec according to changelog rules, plus some others

* Mon Sep 02 2019 Pavel Skrylev <majioa@altlinux.org> 0.7.3-alt4
- fixed (!) spec

* Wed Apr 03 2019 Pavel Skrylev <majioa@altlinux.org> 0.7.3-alt3
- cleanup spec

* Fri Mar 22 2019 Pavel Skrylev <majioa@altlinux.org> 0.7.3-alt2
- Use setup's dependency detection

* Thu Feb 28 2019 Pavel Skrylev <majioa@altlinux.org> 0.7.3-alt1
- Bump to 0.7.3;
- Use Ruby Policy 2.0.

* Mon May 11 2009 Alexey I. Froloff <raorn@altlinux.org> 0.6.4.1-alt1
- [0.6.4.1]
- Removed all web-based providers (due to missing hpricot)
- Enabled Z39.50 provider (zoom and marc are now available)

* Thu May 29 2008 Vitaly Lipatov <lav@altlinux.ru> 0.6.3-alt2
- fix build, use rake_install macros
- remove unsupported providers (due missed hpricot, marc, zoom modules)

* Thu May 29 2008 Vitaly Lipatov <lav@altlinux.ru> 0.6.3-alt1
- new version 0.6.3 (with rpmrb script)
- note: rake_build/rake_install macroses is broken now

* Wed Jan 16 2008 Vitaly Lipatov <lav@altlinux.ru> 0.6.2-alt2
- remove rubygems requires
- use new rpm-build-ruby

* Tue Jan 08 2008 Vitaly Lipatov <lav@altlinux.ru> 0.6.2-alt1
- new version 0.6.2 (with rpmrb script)

* Sun Sep 10 2006 Vitaly Lipatov <lav@altlinux.ru> 0.6.1-alt0.3
- fix requires
- remove debian menu

* Tue May 23 2006 Vitaly Lipatov <lav@altlinux.ru> 0.6.1-alt0.2
- spec cleanup
- fix requires (bug #9601)

* Sun Oct 16 2005 Vitaly Lipatov <lav@altlinux.ru> 0.6.1-alt0.1
- new version
- add require for ruby-gettext
- still some broken code

* Tue Sep 13 2005 Vitaly Lipatov <lav@altlinux.ru> 0.6.0-alt0.2
- fix scrollkeeper install

* Sat Sep 10 2005 Vitaly Lipatov <lav@altlinux.ru> 0.6.0-alt0.1
- new version

* Wed Aug 24 2005 Vitaly Lipatov <lav@altlinux.ru> 0.5.1-alt0.1
- new version. Ruby hackers, please check this app

* Sat Dec 18 2004 Vitaly Lipatov <lav@altlinux.ru> 0.4.0-alt1
- first build for ALT Linux Sisyphus
