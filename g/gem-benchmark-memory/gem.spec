%define        gemname benchmark-memory

Name:          gem-benchmark-memory
Version:       0.1.2
Release:       alt1
Summary:       Benchmark-style memory profiling for Ruby 2.1+
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/michaelherold/benchmark-memory
Vcs:           https://github.com/michaelherold/benchmark-memory.git
Packager:      Pavel Skrylev <majioa@altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
BuildRequires: gem(memory_profiler) >= 0.9 gem(memory_profiler) < 2
BuildRequires: gem(bundler) >= 1.12 gem(bundler) < 3

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_use_gem_dependency memory_profiler >= 1.0.0,memory_profiler < 2
%ruby_use_gem_dependency bundler >= 2.1.4,bundler < 3
Requires:      gem(memory_profiler) >= 0.9 gem(memory_profiler) < 2
Provides:      gem(benchmark-memory) = 0.1.2


%description
Benchmark-style memory profiling for Ruby 2.1+


%package       -n gem-benchmark-memory-doc
Version:       0.1.2
Release:       alt1
Summary:       Benchmark-style memory profiling for Ruby 2.1+ documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета benchmark-memory
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(benchmark-memory) = 0.1.2

%description   -n gem-benchmark-memory-doc
Benchmark-style memory profiling for Ruby 2.1+ documentation
files.

Benchmark-style memory profiling for Ruby 2.1+

%description   -n gem-benchmark-memory-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета benchmark-memory.


%package       -n gem-benchmark-memory-devel
Version:       0.1.2
Release:       alt1
Summary:       Benchmark-style memory profiling for Ruby 2.1+ development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета benchmark-memory
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(benchmark-memory) = 0.1.2
Requires:      gem(bundler) >= 1.12 gem(bundler) < 3

%description   -n gem-benchmark-memory-devel
Benchmark-style memory profiling for Ruby 2.1+ development
package.

Benchmark-style memory profiling for Ruby 2.1+

%description   -n gem-benchmark-memory-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета benchmark-memory.


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

%files         -n gem-benchmark-memory-doc
%doc README.md
%ruby_gemdocdir

%files         -n gem-benchmark-memory-devel
%doc README.md


%changelog
* Thu Sep 02 2021 Pavel Skrylev <majioa@altlinux.org> 0.1.2-alt1
- + packaged gem with Ruby Policy 2.0
