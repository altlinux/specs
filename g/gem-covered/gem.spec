%define        gemname covered

Name:          gem-covered
Version:       0.13.1
Release:       alt1
Summary:       A modern approach to code coverage
License:       Unlicensed
Group:         Development/Ruby
Url:           https://github.com/ioquatix/covered
Vcs:           https://github.com/ioquatix/covered.git
Packager:      Pavel Skrylev <majioa@altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
BuildRequires: gem(console) >= 1.0 gem(console) < 2
BuildRequires: gem(parser) >= 0
BuildRequires: gem(msgpack) >= 0
BuildRequires: gem(async-rest) >= 0
# BuildRequires: gem(trenni) >= 3.6 gem(trenni) < 4
BuildRequires: gem(bundler) >= 0
BuildRequires: gem(rake) >= 10.0 gem(rake) < 14
BuildRequires: gem(rspec) >= 3.6 gem(rspec) < 4
BuildRequires: gem(minitest) >= 0

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_use_gem_dependency rake >= 13.0.1,rake < 14
Requires:      gem(console) >= 1.0 gem(console) < 2
Requires:      gem(parser) >= 0
Requires:      gem(msgpack) >= 0
Requires:      gem(async-rest) >= 0
Provides:      gem(covered) = 0.13.1

%description
Covered uses modern Ruby features to generate comprehensive coverage, including
support for templates which are compiled into Ruby.

* Incremental coverage - if you run your full test suite, and the run a subset,
  it will still report the correct coverage - so you can incrementally work on
  improving coverage.
* Integration with RSpec, Minitest, Travis & Coveralls - no need to configure
  anything - out of the box support for these platforms.
* Supports coverage of views - templates compiled to Ruby code can be tracked
  for coverage reporting.


%package       -n gem-covered-doc
Version:       0.13.1
Release:       alt1
Summary:       A modern approach to code coverage documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета covered
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(covered) = 0.13.1

%description   -n gem-covered-doc
A modern approach to code coverage documentation files.

Covered uses modern Ruby features to generate comprehensive coverage, including
support for templates which are compiled into Ruby.

* Incremental coverage - if you run your full test suite, and the run a subset,
  it will still report the correct coverage - so you can incrementally work on
  improving coverage.
* Integration with RSpec, Minitest, Travis & Coveralls - no need to configure
  anything - out of the box support for these platforms.
* Supports coverage of views - templates compiled to Ruby code can be tracked
  for coverage reporting.

%description   -n gem-covered-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета covered.


%package       -n gem-covered-devel
Version:       0.13.1
Release:       alt1
Summary:       A modern approach to code coverage development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета covered
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(covered) = 0.13.1
# Requires:      gem(trenni) >= 3.6 gem(trenni) < 4
Requires:      gem(bundler) >= 0
Requires:      gem(rake) >= 10.0 gem(rake) < 14
Requires:      gem(rspec) >= 3.6 gem(rspec) < 4
Requires:      gem(minitest) >= 0

%description   -n gem-covered-devel
A modern approach to code coverage development package.

Covered uses modern Ruby features to generate comprehensive coverage, including
support for templates which are compiled into Ruby.

* Incremental coverage - if you run your full test suite, and the run a subset,
  it will still report the correct coverage - so you can incrementally work on
  improving coverage.
* Integration with RSpec, Minitest, Travis & Coveralls - no need to configure
  anything - out of the box support for these platforms.
* Supports coverage of views - templates compiled to Ruby code can be tracked
  for coverage reporting.

%description   -n gem-covered-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета covered.


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

%files         -n gem-covered-doc
%doc README.md
%ruby_gemdocdir

%files         -n gem-covered-devel
%doc README.md


%changelog
* Thu Sep 02 2021 Pavel Skrylev <majioa@altlinux.org> 0.13.1-alt1
- + packaged gem with Ruby Policy 2.0
