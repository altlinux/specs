%define        _unpackaged_files_terminate_build 1
%define        gemname faker

Name:          gem-faker
Version:       3.2.0
Release:       alt1
Summary:       Easily generate fake data
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/faker-ruby/faker
Vcs:           https://github.com/faker-ruby/faker.git
Packager:      Pavel Skrylev <majioa@altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
%if_with check
BuildRequires: gem(minitest) >= 5.17.0
BuildRequires: gem(pry) >= 0.13.1
BuildRequires: gem(rake) >= 13.0.1
BuildRequires: gem(rubocop) >= 1.15.0
BuildRequires: gem(rubocop-minitest) >= 0.13.0
BuildRequires: gem(rubocop-rake) >= 0.6.0
BuildRequires: gem(simplecov) >= 0.17
BuildRequires: gem(test-unit) >= 3.3.5
BuildRequires: gem(timecop) >= 0.9.6
BuildRequires: gem(yard) >= 0.9.34
BuildRequires: gem(i18n) >= 1.8.11
BuildConflicts: gem(minitest) >= 6
BuildConflicts: gem(pry) >= 1
BuildConflicts: gem(rake) >= 14
BuildConflicts: gem(rubocop) >= 2
BuildConflicts: gem(rubocop-minitest) >= 1
BuildConflicts: gem(rubocop-rake) >= 1
BuildConflicts: gem(simplecov) >= 1
BuildConflicts: gem(test-unit) >= 4
BuildConflicts: gem(timecop) >= 1
BuildConflicts: gem(yard) >= 1
BuildConflicts: gem(i18n) >= 2
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_use_gem_dependency rake >= 13.0.1,rake < 14
%ruby_use_gem_dependency rubocop >= 1.15.0,rubocop < 2
%ruby_use_gem_dependency test-unit >= 3.3.5,test-unit < 4
%ruby_use_gem_dependency minitest >= 5.17.0,minitest < 6
%ruby_use_gem_dependency simplecov >= 0.17,simplecov < 1
%ruby_use_gem_dependency pry >= 0.13.1,pry < 1
%ruby_use_gem_dependency rubocop-minitest >= 0.13.0,rubocop-minitest < 1
%ruby_use_gem_dependency rubocop-rake >= 0.6.0,rubocop-rake < 1
%ruby_use_gem_dependency yard >= 0.9.34,yard < 1
%ruby_use_gem_dependency timecop >= 0.9.6,timecop < 1
Requires:      gem(i18n) >= 1.8.11
Conflicts:     gem(i18n) >= 2
Provides:      gem(faker) = 3.2.0


%description
Faker, a port of Data::Faker from Perl, is used to easily generate fake data:
names, addresses, phone numbers, etc.


%package       -n faker
Version:       3.2.0
Release:       alt1
Summary:       Easily generate fake data executable(s)
Summary(ru_RU.UTF-8): Исполнямка для самоцвета faker
Group:         Other
BuildArch:     noarch

Requires:      gem(faker) = 3.2.0
Conflicts:     python3-module-faker

%description   -n faker
Easily generate fake data executable(s).

Faker, a port of Data::Faker from Perl, is used to easily generate fake data:
names, addresses, phone numbers, etc.

%description   -n faker -l ru_RU.UTF-8
Исполнямка для самоцвета faker.


%package       -n gem-faker-doc
Version:       3.2.0
Release:       alt1
Summary:       Easily generate fake data documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета faker
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(faker) = 3.2.0

%description   -n gem-faker-doc
Easily generate fake data documentation files.

Faker, a port of Data::Faker from Perl, is used to easily generate fake data:
names, addresses, phone numbers, etc.

%description   -n gem-faker-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета faker.


%package       -n gem-faker-devel
Version:       3.2.0
Release:       alt1
Summary:       Easily generate fake data development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета faker
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(faker) = 3.2.0
Requires:      gem(minitest) >= 5.17.0
Requires:      gem(pry) >= 0.13.1
Requires:      gem(rake) >= 13.0.1
Requires:      gem(rubocop) >= 1.15.0
Requires:      gem(rubocop-minitest) >= 0.13.0
Requires:      gem(rubocop-rake) >= 0.6.0
Requires:      gem(simplecov) >= 0.17
Requires:      gem(test-unit) >= 3.3.5
Requires:      gem(timecop) >= 0.9.6
Requires:      gem(yard) >= 0.9.34
Conflicts:     gem(minitest) >= 6
Conflicts:     gem(pry) >= 1
Conflicts:     gem(rake) >= 14
Conflicts:     gem(rubocop) >= 2
Conflicts:     gem(rubocop-minitest) >= 1
Conflicts:     gem(rubocop-rake) >= 1
Conflicts:     gem(simplecov) >= 1
Conflicts:     gem(test-unit) >= 4
Conflicts:     gem(timecop) >= 1
Conflicts:     gem(yard) >= 1

%description   -n gem-faker-devel
Easily generate fake data development package.

Faker, a port of Data::Faker from Perl, is used to easily generate fake data:
names, addresses, phone numbers, etc.

%description   -n gem-faker-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета faker.


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

%files         -n faker
%doc README.md
%_bindir/faker

%files         -n gem-faker-doc
%doc README.md
%ruby_gemdocdir

%files         -n gem-faker-devel
%doc README.md


%changelog
* Wed Jun 21 2023 Pavel Skrylev <majioa@altlinux.org> 3.2.0-alt1
- ^ 2.23.0 -> 3.2.0

* Sat Jan 07 2023 Pavel Skrylev <majioa@altlinux.org> 2.23.0-alt1
- ^ 2.21.0 -> 2.23.0

* Wed May 18 2022 Pavel Skrylev <majioa@altlinux.org> 2.21.0-alt1
- + packaged gem with Ruby Policy 2.0
