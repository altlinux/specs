%define        gemname rspec-benchmark

Name:          gem-rspec-benchmark
Version:       0.6.0
Release:       alt1
Summary:       Performance testing matchers for RSpec
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/piotrmurach/rspec-benchmark
Vcs:           https://github.com/piotrmurach/rspec-benchmark.git
Packager:      Pavel Skrylev <majioa@altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
%if_with check
BuildRequires: gem(rake) >= 0
BuildRequires: gem(activerecord) >= 0
BuildRequires: gem(sqlite3) >= 0
BuildRequires: gem(fast_jsonapi) >= 0
BuildRequires: gem(coveralls) >= 0.8.22
BuildRequires: gem(simplecov) >= 0.16.1
BuildRequires: gem(yardstick) >= 0.9.9
BuildRequires: gem(benchmark-malloc) >= 0.2
BuildRequires: gem(benchmark-perf) >= 0.6
BuildRequires: gem(benchmark-trend) >= 0.4
BuildRequires: gem(rspec) >= 3.0
BuildConflicts: gem(coveralls) >= 0.9
BuildConflicts: gem(simplecov) >= 1
BuildConflicts: gem(yardstick) >= 0.10
BuildConflicts: gem(benchmark-malloc) >= 1
BuildConflicts: gem(benchmark-perf) >= 1
BuildConflicts: gem(benchmark-trend) >= 1
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_use_gem_dependency simplecov >= 0.17,simplecov < 1
Requires:      gem(benchmark-malloc) >= 0.2
Requires:      gem(benchmark-perf) >= 0.6
Requires:      gem(benchmark-trend) >= 0.4
Requires:      gem(rspec) >= 3.0
Conflicts:     gem(benchmark-malloc) >= 1
Conflicts:     gem(benchmark-perf) >= 1
Conflicts:     gem(benchmark-trend) >= 1
Provides:      gem(rspec-benchmark) = 0.6.0


%description
Performance testing matchers for RSpec to set expectations on speed, resources
usage and scalibility.


%package       -n gem-rspec-benchmark-doc
Version:       0.6.0
Release:       alt1
Summary:       Performance testing matchers for RSpec documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета rspec-benchmark
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(rspec-benchmark) = 0.6.0

%description   -n gem-rspec-benchmark-doc
Performance testing matchers for RSpec documentation files.

Performance testing matchers for RSpec to set expectations on speed, resources
usage and scalibility.

%description   -n gem-rspec-benchmark-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета rspec-benchmark.


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

%files         -n gem-rspec-benchmark-doc
%doc README.md
%ruby_gemdocdir


%changelog
* Tue Feb 07 2023 Pavel Skrylev <majioa@altlinux.org> 0.6.0-alt1
- + packaged gem with Ruby Policy 2.0 (no devel)
