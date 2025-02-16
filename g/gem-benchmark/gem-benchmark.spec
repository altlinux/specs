%define        _unpackaged_files_terminate_build 1
%def_enable    check
%def_enable    doc
%def_enable    devel
%define        gemname benchmark

Name:          gem-benchmark
Version:       0.4.0
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
BuildRequires: gem(bundler) >= 0
BuildRequires: gem(rake) >= 0
BuildRequires: gem(test-unit) >= 0

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
Requires:      ruby >= 2.1.0
Provides:      benchmark = %EVR
Provides:      gem(benchmark) = 0.4.0

%description
a performance benchmarking library


%if_enabled    doc
%package       -n gem-benchmark-doc
Version:       0.4.0
Release:       alt1
Summary:       a performance benchmarking library documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета benchmark
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(benchmark) = 0.4.0

%description   -n gem-benchmark-doc
a performance benchmarking library documentation files.

%description   -n gem-benchmark-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета benchmark.
%endif


%if_enabled    devel
%package       -n gem-benchmark-devel
Version:       0.4.0
Release:       alt1
Summary:       a performance benchmarking library development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета benchmark
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(benchmark) = 0.4.0
Requires:      gem(bundler) >= 0
Requires:      gem(rake) >= 0
Requires:      gem(test-unit) >= 0

%description   -n gem-benchmark-devel
a performance benchmarking library development package.

%description   -n gem-benchmark-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета benchmark.
%endif


%prep
%setup

%build
%ruby_build

%install
%ruby_install

%check
%ruby_test

%files
%doc COPYING README.md
%ruby_gemspec
%ruby_gemlibdir

%if_enabled    doc
%files         -n gem-benchmark-doc
%doc COPYING README.md
%ruby_gemdocdir
%endif

%if_enabled    devel
%files         -n gem-benchmark-devel
%doc COPYING README.md
%endif


%changelog
* Sat Feb 15 2025 Pavel Skrylev <majioa@altlinux.org> 0.4.0-alt1
- ^ 0.2.1 -> 0.4.0

* Wed Jun 21 2023 Pavel Skrylev <majioa@altlinux.org> 0.2.1-alt1
- + packaged gem with Ruby Policy 2.0
