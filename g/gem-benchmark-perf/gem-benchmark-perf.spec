%define        gemname benchmark-perf

Name:          gem-benchmark-perf
Version:       0.6.0
Release:       alt1
Summary:       Execution time and iteration performance benchmarking
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/piotrmurach/benchmark-perf
Vcs:           https://github.com/piotrmurach/benchmark-perf.git
Packager:      Pavel Skrylev <majioa@altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
%if_with check
BuildRequires: gem(rake) >= 0
BuildRequires: gem(rspec) >= 3.0
BuildRequires: gem(simplecov) >= 0.16.1
BuildRequires: gem(coveralls) >= 0.8.22
BuildRequires: gem(yardstick) >= 0.9.9
BuildConflicts: gem(rspec) >= 4
BuildConflicts: gem(simplecov) >= 1
BuildConflicts: gem(coveralls) >= 0.9
BuildConflicts: gem(yardstick) >= 0.10
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_use_gem_dependency simplecov >= 0.17,simplecov < 1
Provides:      gem(benchmark-perf) = 0.6.0


%description
Execution time and iteration performance benchmarking


%package       -n gem-benchmark-perf-doc
Version:       0.6.0
Release:       alt1
Summary:       Execution time and iteration performance benchmarking documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета benchmark-perf
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(benchmark-perf) = 0.6.0

%description   -n gem-benchmark-perf-doc
Execution time and iteration performance benchmarking documentation files.

%description   -n gem-benchmark-perf-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета benchmark-perf.


%package       -n gem-benchmark-perf-devel
Version:       0.6.0
Release:       alt1
Summary:       Execution time and iteration performance benchmarking development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета benchmark-perf
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(benchmark-perf) = 0.6.0
Requires:      gem(rake) >= 0
Requires:      gem(rspec) >= 3.0
Requires:      gem(simplecov) >= 0.16.1
Requires:      gem(coveralls) >= 0.8.22
Requires:      gem(yardstick) >= 0.9.9
Conflicts:     gem(rspec) >= 4
Conflicts:     gem(simplecov) >= 1
Conflicts:     gem(coveralls) >= 0.9
Conflicts:     gem(yardstick) >= 0.10

%description   -n gem-benchmark-perf-devel
Execution time and iteration performance benchmarking development package.

%description   -n gem-benchmark-perf-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета benchmark-perf.


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

%files         -n gem-benchmark-perf-doc
%doc README.md
%ruby_gemdocdir

%files         -n gem-benchmark-perf-devel
%doc README.md


%changelog
* Tue Feb 07 2023 Pavel Skrylev <majioa@altlinux.org> 0.6.0-alt1
- + packaged gem with Ruby Policy 2.0
