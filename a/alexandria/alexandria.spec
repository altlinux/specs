%define        gemname alexandria-book-collection-manager

Name:          alexandria
Version:       0.7.3
Release:       alt4
Summary:       Alexandria is a GNOME application to help you manage your book collection
License:       GPLv2
Group:         Development/Ruby
Url:           https://github.com/mvz/alexandria-book-collection-manager
%vcs           https://github.com/mvz/alexandria-book-collection-manager.git
BuildArch:     noarch
Packager:      Vitaly Lipatov <lav@altlinux.ru>

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
BuildRequires: gem(rake)
BuildRequires: gem(rspec)
BuildRequires: GConf
BuildRequires: intltool
BuildRequires: libGConf2-devel

%gem_replace_version image_size ~> 2.0.0
%gem_replace_version gtk3 ~> 3.3.2
%gem_replace_version gstreamer ~> 3.3.2
%add_findreq_skiplist %ruby_gemslibdir/**/*

%description
Alexandria is a GNOME application to help you manage your book collection.

Alexandria:
 * retrieves book information from Amazon (including cover pictures) ;
 * saves data using the YAML format ;
 * features an HIG-compliant user interface ;
 * shows books in different views (standard list or icons list).


%package       -n gem-alexandria-book-collection-manager
Summary:       HTML, XML, SAX, and Reader parser
Summary(ru_RU.UTF-8): Библиотека для самоцвета %gemname
Group:         Development/Other
BuildArch:     noarch

%description   -n gem-alexandria-book-collection-manager
Nokogiri parses and searches XML/HTML very quickly, and also has correctly
implemented CSS3 selector support as well as XPath support.
This package contanis Ruby libraries for Nokogiri.


%package       -n gem-alexandria-book-collection-manager-doc
Summary:       Documentation files for %gemname gem
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета %gemname
Group:         Development/Documentation
BuildArch:     noarch

%description   -n gem-alexandria-book-collection-manager-doc
Documentation files for %gemname gem.

%description   -n gem-alexandria-book-collection-manager-doc -l ru_RU.UTF8
Файлы сведений для самоцвета %gemname.


%prep
%setup

%build
%ruby_build --pre=pre_install --use=alexandria-book-collection-manager --alias=alexandria

%install
%ruby_install

mkdir -p %buildroot%_desktopdir/ %buildroot%_datadir/sounds/%name/
install -D -m 0644 schemas/%name.schemas %buildroot/%_sysconfdir/gconf/schemas/%name.schemas
install -D -m 0644 %name.desktop %buildroot%_desktopdir/%name.desktop
install -D -m 0644 misc/sounds/* %buildroot%_datadir/sounds/%name/

%find_lang %name --with-gnome

%check
%ruby_test

%post
%gconf2_install %name

%preun
if [ $1 = 0 ]; then
%gconf2_uninstall %name
fi

%files
%_bindir/%name
%_mandir/*
%_desktopdir/%name.desktop
%config %_sysconfdir/gconf/schemas/*
%_datadir/sounds/%name/


%files      -n gem-alexandria-book-collection-manager
%ruby_gemspecdir/alexandria-book-collection-manager-%version.gemspec
%ruby_gemslibdir/alexandria-book-collection-manager-%version/

%files      -n gem-alexandria-book-collection-manager-doc
%ruby_gemsdocdir/alexandria-book-collection-manager-%version/


%changelog
* Mon Sep 02 2019 Pavel Skrylev <majioa@altlinux.org> 0.7.3-alt4
! spec

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

