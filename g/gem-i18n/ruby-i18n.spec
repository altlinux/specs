%define        gemname i18n

Name:          gem-i18n
Version:       1.10.0
Release:       alt1
Summary:       I18n and localization solution for Ruby
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/svenfuchs/i18n
Vcs:           https://github.com/svenfuchs/i18n.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
BuildRequires: tzdata
BuildRequires: gem(concurrent-ruby) >= 1.0 gem(concurrent-ruby) < 2

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
Requires:      gem(concurrent-ruby) >= 1.0 gem(concurrent-ruby) < 2
Obsoletes:     ruby-i18n < %EVR
Provides:      ruby-i18n = %EVR
Provides:      gem(i18n) = 1.10.0


%description
Ruby internationalization and localization (i18n) solution.


%package       -n gem-i18n-doc
Version:       1.10.0
Release:       alt1
Summary:       I18n and localization solution for Ruby documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета i18n
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(i18n) = 1.10.0

%description   -n gem-i18n-doc
I18n and localization solution for Ruby documentation files.

Ruby internationalization and localization (i18n) solution.

%description   -n gem-i18n-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета i18n.


%package       -n gem-i18n-devel
Version:       1.10.0
Release:       alt1
Summary:       I18n and localization solution for Ruby development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета i18n
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(i18n) = 1.10.0

%description   -n gem-i18n-devel
I18n and localization solution for Ruby development package.

Ruby internationalization and localization (i18n) solution.

%description   -n gem-i18n-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета i18n.


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

%files         -n gem-i18n-doc
%doc README.md
%ruby_gemdocdir

%files         -n gem-i18n-devel
%doc README.md


%changelog
* Wed May 18 2022 Pavel Skrylev <majioa@altlinux.org> 1.10.0-alt1
- ^ 1.8.3 -> 1.10.0

* Wed Jun 10 2020 Pavel Skrylev <majioa@altlinux.org> 1.8.3-alt1
- ^ 1.1.1 -> 1.8.3
- ! spec name

* Sun Oct 14 2018 Andrey Cherepanov <cas@altlinux.org> 1.1.1-alt1
- New version.

* Fri Aug 31 2018 Andrey Cherepanov <cas@altlinux.org> 1.1.0-alt1
- New version.

* Wed Jul 11 2018 Andrey Cherepanov <cas@altlinux.org> 0.3.7-alt2.3
- Rebuild with new Ruby autorequirements.
- Disable tests.

* Sat Mar 22 2014 Led <led@altlinux.ru> 0.3.7-alt2.2
- add true to respond_to? for 1.9.3 compatibility
- enabled %%ruby_test

* Wed Dec 05 2012 Led <led@altlinux.ru> 0.3.7-alt2.1
- Rebuilt with ruby-1.9.3-alt1
- disabled check

* Sat May 29 2010 Alexey I. Froloff <raorn@altlinux.org> 0.3.7-alt2
- Mask ActiveRecord dependency

* Sun Apr 25 2010 Alexey I. Froloff <raorn@altlinux.org> 0.3.7-alt1
- [0.3.7]

* Sun Apr 11 2010 Alexey I. Froloff <raorn@altlinux.org> 0.3.6-alt1
- [0.3.6]

* Fri Jun 26 2009 Alexey I. Froloff <raorn@altlinux.org> 0.1.3-alt1
- [0.1.3]

* Tue Feb 03 2009 Sir Raorn <raorn@altlinux.ru> 0.1.2-alt1
- [0.1.2]

* Wed Nov 19 2008 Sir Raorn <raorn@altlinux.ru> 0.1.0-alt3
- Updated to [g3696c92] from git://github.com/svenfuchs/i18n

* Tue Nov 18 2008 Sir Raorn <raorn@altlinux.ru> 0.1.0-alt2
- Updated to [g0bafcb3] from git://github.com/mattetti/i18n.git

* Mon Nov 10 2008 Sir Raorn <raorn@altlinux.ru> 0.1.0-alt1
- Built for Sisyphus
