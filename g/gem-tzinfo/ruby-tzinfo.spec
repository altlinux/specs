%define        gemname tzinfo

Name:          gem-tzinfo
Version:       2.0.4
Release:       alt1
Summary:       Daylight-savings aware timezone support for Ruby
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/tzinfo/tzinfo
Vcs:           https://github.com/tzinfo/tzinfo.git
Packager:      Pavel Skrylev <majioa@altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
BuildRequires: gem(concurrent-ruby) >= 1.0 gem(concurrent-ruby) < 2

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
Requires:      gem(concurrent-ruby) >= 1.0 gem(concurrent-ruby) < 2
Obsoletes:     ruby-tzinfo < %EVR
Provides:      ruby-tzinfo = %EVR
Provides:      gem(tzinfo) = 2.0.4


%description
TZInfo uses the tz database (http://www.twinsun.com/tz/tz-link.htm) to provide
daylight-savings aware transformations between times in different
timezones.

This is the same database as used for zoneinfo on Unix machines.


%package       -n gem-tzinfo-doc
Version:       2.0.4
Release:       alt1
Summary:       Daylight-savings aware timezone support for Ruby documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета tzinfo
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(tzinfo) = 2.0.4

%description   -n gem-tzinfo-doc
Daylight-savings aware timezone support for Ruby documentation files.

TZInfo uses the tz database (http://www.twinsun.com/tz/tz-link.htm) to provide
daylight-savings aware transformations between times in different
timezones.

This is the same database as used for zoneinfo on Unix machines.

%description   -n gem-tzinfo-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета tzinfo.


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

%files         -n gem-tzinfo-doc
%doc README.md
%ruby_gemdocdir


%changelog
* Tue Jun 15 2021 Pavel Skrylev <majioa@altlinux.org> 2.0.4-alt1
- > Ruby Policy 2.0
- ^ 1.2.5 -> 2.0.4

* Fri Aug 31 2018 Andrey Cherepanov <cas@altlinux.org> 1.2.5-alt1
- New version.

* Wed Jul 11 2018 Andrey Cherepanov <cas@altlinux.org> 0.3.25-alt1.2
- Rebuild with new Ruby autorequirements.

* Thu Dec 06 2012 Led <led@altlinux.ru> 0.3.25-alt1.1
- Rebuilt with ruby-1.9.3-alt1
- disabled check

* Mon Mar 21 2011 Andriy Stepanov <stanv@altlinux.ru> 0.3.25-alt1
- [0.3.25]

* Fri Jul 16 2010 Alexey I. Froloff <raorn@altlinux.org> 0.3.22-alt1
- [0.3.22]

* Sat Jun 27 2009 Alexey I. Froloff <raorn@altlinux.org> 0.3.13-alt1
- [0.3.13]

* Tue Feb 03 2009 Sir Raorn <raorn@altlinux.ru> 0.3.12-alt1
- [0.3.12]

* Mon Nov 10 2008 Sir Raorn <raorn@altlinux.ru> 0.3.11-alt1
- [0.3.11]

* Tue Jul 08 2008 Sir Raorn <raorn@altlinux.ru> 0.3.9-alt1
- Built for Sisyphus
