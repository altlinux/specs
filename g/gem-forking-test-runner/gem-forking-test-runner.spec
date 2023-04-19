%define        _unpackaged_files_terminate_build 1
%define        gemname forking_test_runner

Name:          gem-forking-test-runner
Version:       1.13.0
Release:       alt1
Summary:       Run every test in a fork to avoid pollution and get clean output per test
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/grosser/forking_test_runner
Vcs:           https://github.com/grosser/forking_test_runner.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
%if_with check
BuildRequires: gem(bump) >= 0
BuildRequires: gem(rake) >= 0
BuildRequires: gem(rspec) >= 0
BuildRequires: gem(sqlite3) >= 0
BuildRequires: gem(minitest) >= 0
BuildRequires: gem(activerecord) >= 0
BuildRequires: gem(parallel_tests) >= 1.3.7
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
Requires:      gem(parallel_tests) >= 1.3.7
Provides:      gem(forking_test_runner) = 1.13.0


%description
Run every test in a fork to avoid pollution and get clean output per test


%package       -n forking-test-runner
Version:       1.13.0
Release:       alt1
Summary:       Run every test in a fork to avoid pollution and get clean output per test executable(s)
Summary(ru_RU.UTF-8): Исполнямка для самоцвета forking_test_runner
Group:         Other
BuildArch:     noarch

Requires:      gem(forking_test_runner) = 1.13.0

%description   -n forking-test-runner
Run every test in a fork to avoid pollution and get clean output per test
executable(s).

%description   -n forking-test-runner -l ru_RU.UTF-8
Исполнямка для самоцвета forking_test_runner.


%package       -n gem-forking-test-runner-doc
Version:       1.13.0
Release:       alt1
Summary:       Run every test in a fork to avoid pollution and get clean output per test documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета forking_test_runner
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(forking_test_runner) = 1.13.0

%description   -n gem-forking-test-runner-doc
Run every test in a fork to avoid pollution and get clean output per test
documentation files.

%description   -n gem-forking-test-runner-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета forking_test_runner.


%package       -n gem-forking-test-runner-devel
Version:       1.13.0
Release:       alt1
Summary:       Run every test in a fork to avoid pollution and get clean output per test development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета forking_test_runner
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(forking_test_runner) = 1.13.0
Requires:      gem(bump) >= 0
Requires:      gem(rake) >= 0
Requires:      gem(rspec) >= 0
Requires:      gem(sqlite3) >= 0
Requires:      gem(minitest) >= 0
Requires:      gem(activerecord) >= 0

%description   -n gem-forking-test-runner-devel
Run every test in a fork to avoid pollution and get clean output per test
development package.

%description   -n gem-forking-test-runner-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета forking_test_runner.


%prep
%setup

%build
%ruby_build

%install
%ruby_install

%check
%ruby_test

%files
%ruby_gemspec
%ruby_gemlibdir

%files         -n forking-test-runner
%_bindir/forking-test-runner

%files         -n gem-forking-test-runner-doc
%ruby_gemdocdir

%files         -n gem-forking-test-runner-devel


%changelog
* Thu Apr 13 2023 Pavel Skrylev <majioa@altlinux.org> 1.13.0-alt1
- + packaged gem with Ruby Policy 2.0
