%define        gemname gettext

Name:          gem-gettext
Version:       3.4.3
Release:       alt1
Summary:       Native Language Support Library for Ruby
License:       Ruby or LGPL-3.0+
Group:         Development/Ruby
Url:           https://ruby-gettext.github.io/
Vcs:           https://github.com/ruby-gettext/locale.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
%if_with check
BuildRequires: gem(kramdown) >= 0
BuildRequires: gem(racc) >= 0
BuildRequires: gem(rake) >= 0
BuildRequires: gem(red-datasets) >= 0
BuildRequires: gem(test-unit) >= 0
BuildRequires: gem(test-unit-rr) >= 0
BuildRequires: gem(yard) >= 0
BuildRequires: gem(erubi) >= 0
BuildRequires: gem(locale) >= 2.0.5
BuildRequires: gem(prime) >= 0
BuildRequires: gem(text) >= 1.3.0
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
Requires:      gem(erubi) >= 0
Requires:      gem(locale) >= 2.0.5
Requires:      gem(prime) >= 0
Requires:      gem(text) >= 1.3.0
Obsoletes:     gem-gettext-cgi < %EVR
Obsoletes:     gem-gettext-erb < %EVR
Obsoletes:     ruby-gettext < %EVR
Provides:      gem-gettext-cgi = %EVR
Provides:      gem-gettext-erb = %EVR
Provides:      ruby-gettext = %EVR
Provides:      gem(gettext) = 3.4.3


%description
Ruby GetText Package is Native Language Support Library and Tools which modeled
after GNU gettext package.

Features: * Simple APIs(similar GNU gettext) * rgettext creates po-files from
ruby scripts. The po-file is compatible to GNU gettext. * rmsgfmt creates a
mo-file from a po-file.

This library was called as "Ruby-Locale". Since 2.0.6, this library is called
just "locale". You can call this library as "locale gem" or "Ruby Locale" to
distinguish from other "locale"s.

This library aims to support all environments which Ruby works and all kind of
programs (GUI, WWW, library, etc), and becomes the hub of other i18n/l10n
libs/apps to handle major locale ID standards.


%package       -n rmsg
Version:       3.4.3
Release:       alt1
Summary:       Native Language Support Library for Ruby executable(s)
Summary(ru_RU.UTF-8): Исполнямка для самоцвета gettext
Group:         Other
BuildArch:     noarch

Requires:      gem(gettext) = 3.4.3
Obsoletes:     gettext-gemtools < %EVR
Provides:      gettext-gemtools = %EVR

%description   -n rmsg
Native Language Support Library for Ruby executable(s).

Ruby GetText Package is Native Language Support Library and Tools which modeled
after GNU gettext package.

Features: * Simple APIs(similar GNU gettext) * rgettext creates po-files from
ruby scripts. The po-file is compatible to GNU gettext. * rmsgfmt creates a
mo-file from a po-file.

This library was called as "Ruby-Locale". Since 2.0.6, this library is called
just "locale". You can call this library as "locale gem" or "Ruby Locale" to
distinguish from other "locale"s.

This library aims to support all environments which Ruby works and all kind of
programs (GUI, WWW, library, etc), and becomes the hub of other i18n/l10n
libs/apps to handle major locale ID standards.

%description   -n rmsg -l ru_RU.UTF-8
Исполнямка для самоцвета gettext.


%package       -n gem-gettext-doc
Version:       3.4.3
Release:       alt1
Summary:       Native Language Support Library for Ruby documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета gettext
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(gettext) = 3.4.3

%description   -n gem-gettext-doc
Native Language Support Library for Ruby documentation files.

Ruby GetText Package is Native Language Support Library and Tools which modeled
after GNU gettext package.

Features: * Simple APIs(similar GNU gettext) * rgettext creates po-files from
ruby scripts. The po-file is compatible to GNU gettext. * rmsgfmt creates a
mo-file from a po-file.

This library was called as "Ruby-Locale". Since 2.0.6, this library is called
just "locale". You can call this library as "locale gem" or "Ruby Locale" to
distinguish from other "locale"s.

This library aims to support all environments which Ruby works and all kind of
programs (GUI, WWW, library, etc), and becomes the hub of other i18n/l10n
libs/apps to handle major locale ID standards.

%description   -n gem-gettext-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета gettext.


%package       -n gem-gettext-devel
Version:       3.4.3
Release:       alt1
Summary:       Native Language Support Library for Ruby development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета gettext
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(gettext) = 3.4.3
Requires:      gem(kramdown) >= 0
Requires:      gem(racc) >= 0
Requires:      gem(rake) >= 0
Requires:      gem(red-datasets) >= 0
Requires:      gem(test-unit) >= 0
Requires:      gem(test-unit-rr) >= 0
Requires:      gem(yard) >= 0

%description   -n gem-gettext-devel
Native Language Support Library for Ruby development package.

Ruby GetText Package is Native Language Support Library and Tools which modeled
after GNU gettext package.

Features: * Simple APIs(similar GNU gettext) * rgettext creates po-files from
ruby scripts. The po-file is compatible to GNU gettext. * rmsgfmt creates a
mo-file from a po-file.

This library was called as "Ruby-Locale". Since 2.0.6, this library is called
just "locale". You can call this library as "locale gem" or "Ruby Locale" to
distinguish from other "locale"s.

This library aims to support all environments which Ruby works and all kind of
programs (GUI, WWW, library, etc), and becomes the hub of other i18n/l10n
libs/apps to handle major locale ID standards.

%description   -n gem-gettext-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета gettext.


%prep
%setup

%build
%ruby_build

%install
%ruby_install

%check
%ruby_test

%files
%doc README.md
%ruby_gemspec
%ruby_gemlibdir

%files         -n rmsg
%doc README.md
%_bindir/rmsgcat
%_bindir/rmsgfmt
%_bindir/rmsginit
%_bindir/rmsgmerge
%_bindir/rxgettext

%files         -n gem-gettext-doc
%doc README.md
%ruby_gemdocdir

%files         -n gem-gettext-devel
%doc README.md


%changelog
* Fri Apr 14 2023 Pavel Skrylev <majioa@altlinux.org> 3.4.3-alt1
- ^ 3.3.5 -> 3.4.3

* Wed May 06 2020 Pavel Skrylev <majioa@altlinux.org> 3.3.5-alt1
- ^ 3.2.9 -> 3.3.5
- * renamed tools -> gemtools
- ! spec tags

* Mon Feb 18 2019 Pavel Skrylev <majioa@altlinux.org> 3.2.9-alt2
- > Ruby Policy 2.0

* Sun Jan 20 2019 Andrey Cherepanov <cas@altlinux.org> 3.2.9-alt1.6
- Drop deprecated macro (ALT #35937).

* Wed Jul 11 2018 Andrey Cherepanov <cas@altlinux.org> 3.2.9-alt1.5
- Rebuild with new Ruby autorequirements.

* Fri Jul 06 2018 Andrey Cherepanov <cas@altlinux.org> 3.2.9-alt1.4
- Rebuild for correct gemspec file name.

* Tue Jun 26 2018 Andrey Cherepanov <cas@altlinux.org> 3.2.9-alt1.3
- Use new macro and automatic gemspec installation.

* Fri Mar 30 2018 Andrey Cherepanov <cas@altlinux.org> 3.2.9-alt1.2
- Rebuild with Ruby 2.5.1

* Tue Mar 13 2018 Andrey Cherepanov <cas@altlinux.org> 3.2.9-alt1.1
- Rebuild with Ruby 2.5.0

* Mon Mar 05 2018 Andrey Cherepanov <cas@altlinux.org> 3.2.9-alt1
- New version.

* Tue Dec 19 2017 Andrey Cherepanov <cas@altlinux.org> 3.2.6-alt1
- New version.

* Fri Dec 15 2017 Andrey Cherepanov <cas@altlinux.org> 3.2.5-alt1
- New version.

* Tue Sep 26 2017 Andrey Cherepanov <cas@altlinux.org> 3.2.4-alt2
- Rebuild with Ruby 2.4.2

* Mon Aug 14 2017 Andrey Cherepanov <cas@altlinux.org> 3.2.4-alt1
- New version

* Sat Jun 24 2017 Andrey Cherepanov <cas@altlinux.org> 3.2.3-alt1
- New version

* Fri May 19 2017 Andrey Cherepanov <cas@altlinux.org> 3.2.2-alt1
- New version
- Fix project homepage, license and cleanup spec
- Package as gem

* Fri Mar 14 2014 Led <led@altlinux.ru> 2.1.0-alt2.qa1.2
- fixed build without system iconv module
- remove using deprecated 'all_load_paths'
- disable %%ruby_test for ruby >= 2.0
- iconv.rb: set encoding UTF-8

* Sun Dec 09 2012 Led <led@altlinux.ru> 2.1.0-alt2.qa1.1
- Rebuilt with ruby-1.9.3-alt1
- fixed BuildRequires

* Mon Aug 27 2012 Repocop Q. A. Robot <repocop@altlinux.org> 2.1.0-alt2.qa1
- NMU (by repocop). See http://www.altlinux.org/Tools/Repocop
- applied repocop fixes:
  * backup-file-in-package for ruby-gettext-doc

* Mon Mar 21 2011 Andriy Stepanov <stanv@altlinux.ru> 2.1.0-alt2
- Rebuild with new version.

* Sun Apr 11 2010 Alexey I. Froloff <raorn@altlinux.org> 2.1.0-alt1
- [2.1.0]

* Tue Oct 13 2009 Alexey I. Froloff <raorn@altlinux.org> 2.0.4-alt1
- [2.0.4]

* Wed May 06 2009 Alexey I. Froloff <raorn@altlinux.org> 2.0.1-alt1
- [2.0.1]

* Sun Aug 31 2008 Sir Raorn <raorn@altlinux.ru> 1.92.0-alt2
- Rebuilt wth new rpm-build-ruby

* Wed Aug 13 2008 Sir Raorn <raorn@altlinux.ru> 1.92.0-alt1
- [1.92.0]

* Sun Jul 13 2008 Sir Raorn <raorn@altlinux.ru> 1.91.0-alt1
- [1.91.0]

* Mon Mar 31 2008 Sir Raorn <raorn@altlinux.ru> 1.90.0-alt1
- [1.90.0]
- Package made noarch

* Wed Jan 23 2008 Sir Raorn <raorn@altlinux.ru> 1.10.0-alt3
- Added doc subpackage

* Sun Jan 13 2008 Sir Raorn <raorn@altlinux.ru> 1.10.0-alt2
- Split package to pieces:
 + ruby-gettext - common modules
 + utils - development utilites
 + rails - Ruby on Rails gettext support
 + cgi - CGI gettext support
 + erb - eRuby gettext support
- Removed obsolete be rmsgfmt translation
- Removed 'gettext/iconv', use 'iconv' module
- Removed win32 support

* Wed Aug 22 2007 Pavlov Konstantin <thresh@altlinux.ru> 1.10.0-alt1
- 1.10.0 source tree.

* Tue May 08 2007 Pavlov Konstantin <thresh@altlinux.ru> 1.9.0-alt1
- 1.9.0.

* Fri Apr 21 2006 Vital Khilko <vk@altlinux.ru> 1.4.0-alt1
- 1.4.0

* Tue Nov 15 2005 Vital Khilko <vk@altlinux.ru> 1.0.0-alt1
- 1.0.0

* Thu Sep 08 2005 Vital Khilko <vk@altlinux.ru> 0.6.1-alt2
- fixed locale dir

* Tue Sep 28 2004 Vital Khilko <vk@altlinux.ru> 0.5.3-alt3
- fixed locale.rb for new global variable RUBY_PLATFORM

* Mon Sep 27 2004 Vital Khilko <vk@altlinux.ru> 0.5.3-alt2
- rebuilded with new ruby

* Wed Mar 31 2004 Vital Khilko <vk@altlinux.ru> 0.5.3-alt1
- initial build for altlinux sisyphus.
- added belarusian translation
