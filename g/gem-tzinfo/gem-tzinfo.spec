%define        _unpackaged_files_terminate_build 1
%def_enable    check
%def_enable    doc
%def_enable    devel
%define        gemname tzinfo

Name:          gem-tzinfo
Version:       2.0.6
Release:       alt1
Summary:       Daylight-savings aware timezone support for Ruby
License:       MIT
Group:         Development/Ruby
Url:           http://rubyforge.org/projects/tzinfo/
Vcs:           https://github.com/tzinfo/tzinfo.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
BuildRequires: gem(rake) >= 12.2.1
BuildConflicts: gem(rake) >= 14
%if_enabled check
BuildRequires: gem(concurrent-ruby) >= 1.0
BuildRequires: gem(minitest) >= 5.0
BuildRequires: gem(simplecov) >= 0.15.1
BuildConflicts: gem(concurrent-ruby) >= 2
BuildConflicts: gem(minitest) >= 6
BuildConflicts: gem(simplecov) >= 1
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_use_gem_dependency simplecov >= 0.17,simplecov < 1
Requires:      ruby >= 1.9.3
Requires:      gem(concurrent-ruby) >= 1.0
Conflicts:     gem(concurrent-ruby) >= 2
Obsoletes:     ruby-tzinfo < %EVR
Provides:      ruby-tzinfo = %EVR
Provides:      tzinfo = %EVR
Provides:      gem(tzinfo) = 2.0.6

%description
TZInfo uses the tz database (http://www.twinsun.com/tz/tz-link.htm) to provide
daylight-savings aware transformations between times in different
timezones.

This is the same database as used for zoneinfo on Unix machines.


%if_enabled    doc
%package       -n gem-tzinfo-doc
Version:       2.0.6
Release:       alt1
Summary:       Daylight-savings aware timezone support for Ruby documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета tzinfo
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(tzinfo) = 2.0.6

%description   -n gem-tzinfo-doc
Daylight-savings aware timezone support for Ruby documentation files.

TZInfo uses the tz database (http://www.twinsun.com/tz/tz-link.htm) to provide
daylight-savings aware transformations between times in different
timezones.

This is the same database as used for zoneinfo on Unix machines.

%description   -n gem-tzinfo-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета tzinfo.
%endif


%if_enabled    devel
%package       -n gem-tzinfo-devel
Version:       2.0.6
Release:       alt1
Summary:       Daylight-savings aware timezone support for Ruby development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета tzinfo
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(tzinfo) = 2.0.6
Requires:      gem(minitest) >= 5.0
Requires:      gem(rake) >= 12.2.1
Requires:      gem(simplecov) >= 0.15.1
Conflicts:     gem(minitest) >= 6
Conflicts:     gem(rake) >= 14
Conflicts:     gem(simplecov) >= 1

%description   -n gem-tzinfo-devel
Daylight-savings aware timezone support for Ruby development package.

TZInfo uses the tz database (http://www.twinsun.com/tz/tz-link.htm) to provide
daylight-savings aware transformations between times in different
timezones.

This is the same database as used for zoneinfo on Unix machines.

%description   -n gem-tzinfo-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета tzinfo.
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
%doc LICENSE README.md
%ruby_gemspec
%ruby_gemlibdir

%if_enabled    doc
%files         -n gem-tzinfo-doc
%doc LICENSE README.md
%ruby_gemdocdir
%endif

%if_enabled    devel
%files         -n gem-tzinfo-devel
%doc LICENSE README.md
%endif


%changelog
* Fri Jan 10 2025 Pavel Skrylev <majioa@altlinux.org> 2.0.6-alt1
- ^ 1.2.9 -> 2.0.6

* Thu Aug 18 2022 Pavel Skrylev <majioa@altlinux.org> 1.2.9-alt1
- ^ 1.2.5 -> 1.2.9

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
