%define        gemname parallel_tests

Name:          gem-parallel-tests
Version:       3.7.0
Release:       alt1
Summary:       Run Test::Unit / RSpec / Cucumber / Spinach in parallel
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/grosser/parallel_tests
Vcs:           https://github.com/grosser/parallel_tests/tree/v3.7.0.git
Packager:      Pavel Skrylev <majioa@altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
BuildRequires: gem(parallel) >= 0

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_ignore_names rails60,rails61
Requires:      gem(parallel) >= 0
Provides:      gem(parallel_tests) = 3.7.0

%description
Ruby: 2 CPUs = 2x Testing Speed for RSpec, Test::Unit and Cucumber.


%package       -n parallel-test
Version:       3.7.0
Release:       alt1
Summary:       Run Test::Unit / RSpec / Cucumber / Spinach in parallel executable(s)
Summary(ru_RU.UTF-8): Исполнямка для самоцвета parallel_tests
Group:         Other
BuildArch:     noarch

Requires:      gem(parallel_tests) = 3.7.0

%description   -n parallel-test
Run Test::Unit / RSpec / Cucumber / Spinach in parallel executable(s).

Ruby: 2 CPUs = 2x Testing Speed for RSpec, Test::Unit and Cucumber.

%description   -n parallel-test -l ru_RU.UTF-8
Исполнямка для самоцвета parallel_tests.


%package       -n gem-parallel-tests-doc
Version:       3.7.0
Release:       alt1
Summary:       Run Test::Unit / RSpec / Cucumber / Spinach in parallel documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета parallel_tests
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(parallel_tests) = 3.7.0

%description   -n gem-parallel-tests-doc
Run Test::Unit / RSpec / Cucumber / Spinach in parallel documentation files.

Ruby: 2 CPUs = 2x Testing Speed for RSpec, Test::Unit and Cucumber.

%description   -n gem-parallel-tests-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета parallel_tests.


%package       -n gem-parallel-tests-devel
Version:       3.7.0
Release:       alt1
Summary:       Run Test::Unit / RSpec / Cucumber / Spinach in parallel development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета parallel_tests
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(parallel_tests) = 3.7.0

%description   -n gem-parallel-tests-devel
Run Test::Unit / RSpec / Cucumber / Spinach in parallel development package.

Ruby: 2 CPUs = 2x Testing Speed for RSpec, Test::Unit and Cucumber.

%description   -n gem-parallel-tests-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета parallel_tests.


%prep
%setup

%build
%ruby_build

%install
%ruby_install

%check
%ruby_test

%files
%doc Readme.md
%ruby_gemspec
%ruby_gemlibdir

%files         -n parallel-test
%doc Readme.md
%_bindir/parallel_spinach
%_bindir/parallel_cucumber
%_bindir/parallel_rspec
%_bindir/parallel_test

%files         -n gem-parallel-tests-doc
%doc Readme.md
%ruby_gemdocdir

%files         -n gem-parallel-tests-devel
%doc Readme.md


%changelog
* Tue Jun 22 2021 Pavel Skrylev <majioa@altlinux.org> 3.7.0-alt1
- + packaged gem with Ruby Policy 2.0
