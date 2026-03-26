%define        _unpackaged_files_terminate_build 1
%def_enable    check
%def_enable    doc
%def_enable    devel
%define        gemname alexandria-book-collection-manager

Name:          gem-alexandria-book-collection-manager
Version:       0.7.11
Release:       alt1
Summary:       Alexandria is a GNOME application to help you manage your book collection
License:       GPL-2.0-or-later
Group:         Development/Ruby
Url:           https://github.com/mvz/alexandria-book-collection-manager
Vcs:           https://github.com/mvz/alexandria-book-collection-manager.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
Autoprov:      yes,noruby
Autoreq:       yes,noruby
BuildRequires(pre): rpm-build-ruby
BuildRequires(pre): rpm-build-gnome
%if_enabled check
BuildRequires: gem(alexandria-zoom) >= 0.6.0
BuildRequires: gem(csv) >= 3.2
BuildRequires: gem(gettext) >= 3.1
BuildRequires: gem(gnome_app_driver) >= 0.3.2
BuildRequires: gem(gstreamer) >= 4.3.0
BuildRequires: gem(gtk3) >= 4.3.0
BuildRequires: gem(htmlentities) >= 4.3
BuildRequires: gem(image_size) >= 3.0
BuildRequires: gem(irb) >= 1.16
BuildRequires: gem(logger) >= 1.7
BuildRequires: gem(marc) >= 1.3
BuildRequires: gem(nokogiri) >= 1.11
BuildRequires: gem(observer) >= 0.1.2
BuildRequires: gem(rake) >= 13.0
BuildRequires: gem(rspec) >= 3.0
BuildRequires: gem(rubocop) >= 1.15.0
BuildRequires: gem(rubocop-i18n) >= 3.0.0
BuildRequires: gem(rubocop-performance) >= 1.11.3
BuildRequires: gem(rubocop-rake) >= 0.6.0
BuildRequires: gem(rubocop-rspec) >= 3.6
BuildRequires: gem(simplecov) >= 0.17
BuildRequires: gem(webmock) >= 3.9
BuildConflicts: gem(alexandria-zoom) >= 0.7
BuildConflicts: gem(csv) >= 4
BuildConflicts: gem(gettext) >= 4
BuildConflicts: gem(gnome_app_driver) >= 0.4
BuildConflicts: gem(gstreamer) >= 4.4
BuildConflicts: gem(gtk3) >= 4.4
BuildConflicts: gem(htmlentities) >= 5
BuildConflicts: gem(image_size) >= 4
BuildConflicts: gem(irb) >= 2
BuildConflicts: gem(logger) >= 2
BuildConflicts: gem(marc) >= 2
BuildConflicts: gem(nokogiri) >= 2
BuildConflicts: gem(observer) >= 0.2
BuildConflicts: gem(rake) >= 14
BuildConflicts: gem(rspec) >= 4
BuildConflicts: gem(rubocop) >= 2
BuildConflicts: gem(rubocop-i18n) >= 4
BuildConflicts: gem(rubocop-performance) >= 2
BuildConflicts: gem(rubocop-rake) >= 1
BuildConflicts: gem(rubocop-rspec) >= 4
BuildConflicts: gem(simplecov) >= 1
BuildConflicts: gem(webmock) >= 4
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_use_gem_dependency rubocop-i18n >= 3.0.0,rubocop-i18n < 4
%ruby_use_gem_dependency rubocop >= 1.15.0,rubocop < 2
%ruby_use_gem_dependency simplecov >= 0.17,simplecov < 1
%ruby_use_gem_dependency rubocop-performance >= 1.11.3,rubocop-performance < 2
%ruby_use_gem_dependency rubocop-rake >= 0.6.0,rubocop-rake < 1
Requires:      alexandria
Requires:      ruby >= 3.2.0
Requires:      gem(alexandria-zoom) >= 0.6.0
Requires:      gem(csv) >= 3.2
Requires:      gem(gettext) >= 3.1
Requires:      gem(gstreamer) >= 4.3.0
Requires:      gem(gtk3) >= 4.3.0
Requires:      gem(htmlentities) >= 4.3
Requires:      gem(image_size) >= 3.0
Requires:      gem(logger) >= 1.7
Requires:      gem(marc) >= 1.3
Requires:      gem(nokogiri) >= 1.11
Requires:      gem(observer) >= 0.1.2
Conflicts:     gem(alexandria-zoom) >= 0.7
Conflicts:     gem(csv) >= 4
Conflicts:     gem(gettext) >= 4
Conflicts:     gem(gstreamer) >= 4.4
Conflicts:     gem(gtk3) >= 4.4
Conflicts:     gem(htmlentities) >= 5
Conflicts:     gem(image_size) >= 4
Conflicts:     gem(logger) >= 2
Conflicts:     gem(marc) >= 2
Conflicts:     gem(nokogiri) >= 2
Conflicts:     gem(observer) >= 0.2
Provides:      alexandria-book-collection-manager = %EVR
Provides:      gem(alexandria-book-collection-manager) = 0.7.11

%description
Alexandria is a GNOME application to help you manage your book
collection.

Alexandria:
* retrieves book information from Amazon (including cover pictures)
* saves data using the YAML format
* features an HIG-compliant user interface
* shows books in different views (standard list or icons list).


%package       -n alexandria
Version:       0.7.11
Release:       alt1
Summary:       Alexandria is a GNOME application to help you manage your book collection executable(s)
Summary(ru_RU.UTF-8): Исполнямка для самоцвета alexandria-book-collection-manager
Group:         Other
BuildArch:     noarch

Autoprov:      yes,noruby
Autoreq:       yes,noruby
Requires:      gem(alexandria-book-collection-manager) = 0.7.11

%description   -n alexandria
Alexandria is a GNOME application to help you manage your book collection
executable(s).

%description   -n alexandria -l ru_RU.UTF-8
Исполнямка для самоцвета alexandria-book-collection-manager.


%if_enabled    doc
%package       -n gem-alexandria-book-collection-manager-doc
Version:       0.7.11
Release:       alt1
Summary:       Alexandria is a GNOME application to help you manage your book collection documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета alexandria-book-collection-manager
Group:         Development/Documentation
BuildArch:     noarch

Autoprov:      yes,noruby
Autoreq:       yes,noruby
Requires:      gem(alexandria-book-collection-manager) = 0.7.11

%description   -n gem-alexandria-book-collection-manager-doc
Alexandria is a GNOME application to help you manage your book collection
documentation files.

%description   -n gem-alexandria-book-collection-manager-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета alexandria-book-collection-manager.
%endif


%if_enabled    devel
%package       -n gem-alexandria-book-collection-manager-devel
Version:       0.7.11
Release:       alt1
Summary:       Alexandria is a GNOME application to help you manage your book collection development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета alexandria-book-collection-manager
Group:         Development/Ruby
BuildArch:     noarch

Autoprov:      yes,noruby
Autoreq:       yes,noruby
Requires:      gem(alexandria-book-collection-manager) = 0.7.11
Requires:      gem(irb) >= 1.16
Conflicts:     gem(irb) >= 2

%description   -n gem-alexandria-book-collection-manager-devel
Alexandria is a GNOME application to help you manage your book collection
development package.

%description   -n gem-alexandria-book-collection-manager-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета alexandria-book-collection-manager.
%endif


%prep
%setup

%build
%ruby_build

%install
%ruby_install

%check
%ruby_test

%files
%doc CHANGELOG.md COPYING ChangeLog.0 README.md
%ruby_gemspec
%ruby_gemlibdir

%files         -n alexandria
%doc CHANGELOG.md COPYING ChangeLog.0 README.md
%_bindir/alexandria
%_mandir/alexandria.1.xz

%if_enabled    doc
%files         -n gem-alexandria-book-collection-manager-doc
%doc CHANGELOG.md COPYING ChangeLog.0 README.md
%ruby_gemdocdir
%endif

%if_enabled    devel
%files         -n gem-alexandria-book-collection-manager-devel
%doc CHANGELOG.md COPYING ChangeLog.0 README.md
%endif


%changelog
* Wed Mar 25 2026 Pavel Skrylev <majioa@altlinux.org> 0.7.11-alt1
- ^ 0.7.10 -> 0.7.11

* Wed Jul 31 2024 Pavel Skrylev <majioa@altlinux.org> 0.7.10-alt1.3
- ! upper dep limit to psych to 6.0

* Tue May 14 2024 Pavel Skrylev <majioa@altlinux.org> 0.7.10-alt1.2
- ! rollback bindir to %%_bindir

* Wed Nov 29 2023 Pavel Skrylev <majioa@altlinux.org> 0.7.10-alt1.1
- ! fixed bindir in spec

* Fri Jun 23 2023 Pavel Skrylev <majioa@altlinux.org> 0.7.10-alt1
- ^ 0.7.9 -> 0.7.10

* Fri Mar 11 2022 Pavel Skrylev <majioa@altlinux.org> 0.7.9-alt1
- ^ 0.7.8 -> 0.7.9

* Thu Jul 01 2021 Pavel Skrylev <majioa@altlinux.org> 0.7.8-alt1
- ^ 0.7.7 -> 0.7.8

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
