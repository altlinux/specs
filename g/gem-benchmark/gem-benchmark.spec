%define        _unpackaged_files_terminate_build 1
%define        gemname benchmark

Name:          gem-benchmark
Version:       0.2.1
Release:       alt1
Summary:       a performance benchmarking library
License:       Ruby or BSD-2-Clause
Group:         Development/Ruby
Url:           https://github.com/ruby/benchmark
Vcs:           https://github.com/ruby/benchmark.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
%if_with check
BuildRequires: gem(bundler) >= 0
BuildRequires: gem(rake) >= 0
BuildRequires: gem(test-unit) >= 0
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
Provides:      gem(benchmark) = 0.2.1


%description
a performance benchmarking library


%package       -n gem-benchmark-doc
Version:       0.2.1
Release:       alt1
Summary:       a performance benchmarking library documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета benchmark
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(benchmark) = 0.2.1

%description   -n gem-benchmark-doc
a performance benchmarking library documentation files.

%description   -n gem-benchmark-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета benchmark.


%package       -n gem-benchmark-devel
Version:       0.2.1
Release:       alt1
Summary:       a performance benchmarking library development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета benchmark
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(benchmark) = 0.2.1
Requires:      gem(bundler) >= 0
Requires:      gem(rake) >= 0
Requires:      gem(test-unit) >= 0

%description   -n gem-benchmark-devel
a performance benchmarking library development package.

%description   -n gem-benchmark-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета benchmark.


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

%files         -n gem-benchmark-doc
%doc README.md
%ruby_gemdocdir

%files         -n gem-benchmark-devel
%doc README.md


%changelog
* Wed Jun 21 2023 Pavel Skrylev <majioa@altlinux.org> 0.2.1-alt1
- + packaged gem with Ruby Policy 2.0
