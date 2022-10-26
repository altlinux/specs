%define        gemname covered

Name:          gem-covered
Version:       0.18.2
Release:       alt1
Summary:       A modern approach to code coverage
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/ioquatix/covered
Vcs:           https://github.com/ioquatix/covered.git
Packager:      Pavel Skrylev <majioa@altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
%if_with check
BuildRequires: gem(async-rest) >= 0
BuildRequires: gem(console) >= 1.0 gem(console) < 2
BuildRequires: gem(msgpack) >= 1.0 gem(msgpack) < 2
BuildRequires: gem(parser) >= 0
BuildRequires: gem(bundler) >= 0
BuildRequires: gem(rspec) >= 3.6 gem(rspec) < 4
BuildRequires: gem(sus) >= 0.12 gem(sus) < 1
BuildRequires: gem(trenni) >= 3.6 gem(trenni) < 4
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
Requires:      gem(async-rest) >= 0
Requires:      gem(console) >= 1.0 gem(console) < 2
Requires:      gem(msgpack) >= 1.0 gem(msgpack) < 2
Requires:      gem(parser) >= 0
Provides:      gem(covered) = 0.18.2


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
Version:       0.18.2
Release:       alt1
Summary:       A modern approach to code coverage documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета covered
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(covered) = 0.18.2

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
Version:       0.18.2
Release:       alt1
Summary:       A modern approach to code coverage development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета covered
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(covered) = 0.18.2
Requires:      gem(bundler) >= 0
Requires:      gem(rspec) >= 3.6 gem(rspec) < 4
Requires:      gem(sus) >= 0.12 gem(sus) < 1
Requires:      gem(trenni) >= 3.6 gem(trenni) < 4

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
%doc readme.md
%ruby_gemspec
%ruby_gemlibdir

%files         -n gem-covered-doc
%doc readme.md
%ruby_gemdocdir

%files         -n gem-covered-devel
%doc readme.md


%changelog
* Sun Oct 16 2022 Pavel Skrylev <majioa@altlinux.org> 0.18.2-alt1
- ^ 0.13.1 -> 0.18.2

* Thu Sep 02 2021 Pavel Skrylev <majioa@altlinux.org> 0.13.1-alt1
- + packaged gem with Ruby Policy 2.0
