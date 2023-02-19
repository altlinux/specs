%define        gemname benchmark-trend

Name:          gem-benchmark-trend
Version:       0.4.0
Release:       alt1
Summary:       Measure performance trends of Ruby code based on the input size distribution
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/piotrmurach/benchmark-trend
Vcs:           https://github.com/piotrmurach/benchmark-trend.git
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
Provides:      gem(benchmark-trend) = 0.4.0


%description
Benchmark::Trend will help you estimate the computational complexity of Ruby
code by running it on inputs increasing in size, measuring their execution
times, and then fitting these observations into a model that best predicts how a
given Ruby code will scale as a function of growing workload.


%package       -n gem-benchmark-trend-doc
Version:       0.4.0
Release:       alt1
Summary:       Measure performance trends of Ruby code based on the input size distribution documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета benchmark-trend
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(benchmark-trend) = 0.4.0

%description   -n gem-benchmark-trend-doc
Measure performance trends of Ruby code based on the input size distribution
documentation files.

Benchmark::Trend will help you estimate the computational complexity of Ruby
code by running it on inputs increasing in size, measuring their execution
times, and then fitting these observations into a model that best predicts how a
given Ruby code will scale as a function of growing workload.

%description   -n gem-benchmark-trend-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета benchmark-trend.


%package       -n gem-benchmark-trend-devel
Version:       0.4.0
Release:       alt1
Summary:       Measure performance trends of Ruby code based on the input size distribution development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета benchmark-trend
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(benchmark-trend) = 0.4.0
Requires:      gem(rake) >= 0
Requires:      gem(rspec) >= 3.0
Requires:      gem(simplecov) >= 0.16.1
Requires:      gem(coveralls) >= 0.8.22
Requires:      gem(yardstick) >= 0.9.9
Conflicts:     gem(rspec) >= 4
Conflicts:     gem(simplecov) >= 1
Conflicts:     gem(coveralls) >= 0.9
Conflicts:     gem(yardstick) >= 0.10

%description   -n gem-benchmark-trend-devel
Measure performance trends of Ruby code based on the input size distribution
development package.

Benchmark::Trend will help you estimate the computational complexity of Ruby
code by running it on inputs increasing in size, measuring their execution
times, and then fitting these observations into a model that best predicts how a
given Ruby code will scale as a function of growing workload.

%description   -n gem-benchmark-trend-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета benchmark-trend.


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

%files         -n gem-benchmark-trend-doc
%doc README.md
%ruby_gemdocdir

%files         -n gem-benchmark-trend-devel
%doc README.md


%changelog
* Tue Feb 07 2023 Pavel Skrylev <majioa@altlinux.org> 0.4.0-alt1
- + packaged gem with Ruby Policy 2.0
