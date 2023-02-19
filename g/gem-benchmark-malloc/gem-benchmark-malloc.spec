%define        gemname benchmark-malloc

Name:          gem-benchmark-malloc
Version:       0.2.0
Release:       alt1
Summary:       Trace memory allocations and collect stats
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/piotrmurach/benchmark-malloc
Vcs:           https://github.com/piotrmurach/benchmark-malloc.git
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
Provides:      gem(benchmark-malloc) = 0.2.0


%description
Trace memory allocations and collect stats.


%package       -n gem-benchmark-malloc-doc
Version:       0.2.0
Release:       alt1
Summary:       Trace memory allocations and collect stats documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета benchmark-malloc
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(benchmark-malloc) = 0.2.0

%description   -n gem-benchmark-malloc-doc
Trace memory allocations and collect stats documentation files.

%description   -n gem-benchmark-malloc-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета benchmark-malloc.


%package       -n gem-benchmark-malloc-devel
Version:       0.2.0
Release:       alt1
Summary:       Trace memory allocations and collect stats development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета benchmark-malloc
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(benchmark-malloc) = 0.2.0
Requires:      gem(rake) >= 0
Requires:      gem(rspec) >= 3.0
Requires:      gem(simplecov) >= 0.16.1
Requires:      gem(coveralls) >= 0.8.22
Requires:      gem(yardstick) >= 0.9.9
Conflicts:     gem(rspec) >= 4
Conflicts:     gem(simplecov) >= 1
Conflicts:     gem(coveralls) >= 0.9
Conflicts:     gem(yardstick) >= 0.10

%description   -n gem-benchmark-malloc-devel
Trace memory allocations and collect stats development package.

%description   -n gem-benchmark-malloc-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета benchmark-malloc.


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

%files         -n gem-benchmark-malloc-doc
%doc README.md
%ruby_gemdocdir

%files         -n gem-benchmark-malloc-devel
%doc README.md


%changelog
* Tue Feb 07 2023 Pavel Skrylev <majioa@altlinux.org> 0.2.0-alt1
- + packaged gem with Ruby Policy 2.0
