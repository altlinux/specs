%define        _unpackaged_files_terminate_build 1
%define        gemname benchmark_suite

Name:          gem-benchmark-suite
Version:       1.0.0.4
Release:       alt0.1
Summary:       A set of enhancements to the standard library benchmark.rb
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/evanphx/benchmark_suite
Vcs:           https://github.com/evanphx/benchmark_suite.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
%if_with check
BuildRequires: gem(benchmark-ips) >= 1.0
BuildRequires: gem(hoe) >= 0
BuildConflicts: gem(benchmark-ips) >= 3
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_alias_names benchmark_suite,benchmark-suite
%ruby_use_gem_dependency benchmark-ips >= 2.10.0,benchmark-ips < 3
Requires:      gem(benchmark-ips) >= 1.0
Conflicts:     gem(benchmark-ips) >= 3
Obsoletes:     ruby-benchmark_suite < %EVR
Provides:      ruby-benchmark_suite = %EVR
Provides:      gem(benchmark_suite) = 1.0.0.4

%ruby_use_gem_version benchmark_suite:1.0.0.4
%ruby_bindir_to %ruby_bindir

%description
This package contains a command line tool for running multiple benchmarks
against multiple rubies. It is also uses benchmark/ips to report iterations per
second.


%package       -n benchmark
Version:       1.0.0.4
Release:       alt0.1
Summary:       A set of enhancements to the standard library benchmark.rb executable(s)
Summary(ru_RU.UTF-8): Исполнямка для самоцвета benchmark_suite
Group:         Other
BuildArch:     noarch

Requires:      gem(benchmark_suite) = 1.0.0.4

%description   -n benchmark
A set of enhancements to the standard library benchmark.rb executable(s).

This package contains a command line tool for running multiple benchmarks
against multiple rubies. It is also uses benchmark/ips to report iterations per
second.

%description   -n benchmark -l ru_RU.UTF-8
Исполнямка для самоцвета benchmark_suite.


%package       -n gem-benchmark-suite-doc
Version:       1.0.0.4
Release:       alt0.1
Summary:       A set of enhancements to the standard library benchmark.rb documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета benchmark_suite
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(benchmark_suite) = 1.0.0.4

%description   -n gem-benchmark-suite-doc
A set of enhancements to the standard library benchmark.rb documentation
files.

This package contains a command line tool for running multiple benchmarks
against multiple rubies. It is also uses benchmark/ips to report iterations per
second.

%description   -n gem-benchmark-suite-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета benchmark_suite.


%package       -n gem-benchmark-suite-devel
Version:       1.0.0.4
Release:       alt0.1
Summary:       A set of enhancements to the standard library benchmark.rb development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета benchmark_suite
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(benchmark_suite) = 1.0.0.4
Requires:      gem(hoe) >= 0

%description   -n gem-benchmark-suite-devel
A set of enhancements to the standard library benchmark.rb development
package.

This package contains a command line tool for running multiple benchmarks
against multiple rubies. It is also uses benchmark/ips to report iterations per
second.

%description   -n gem-benchmark-suite-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета benchmark_suite.


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

%files         -n benchmark
%doc README.md
%ruby_bindir/benchmark

%files         -n gem-benchmark-suite-doc
%doc README.md
%ruby_gemdocdir

%files         -n gem-benchmark-suite-devel
%doc README.md


%changelog
* Wed Nov 29 2023 Pavel Skrylev <majioa@altlinux.org> 1.0.0.4-alt0.1
- ^ 1.0.0 -> 1.0.0p4

* Mon Mar 30 2020 Pavel Skrylev <majioa@altlinux.org> 1.0.0-alt3.git32101ee13
- ! package's spec tags
- ! build to up sources

* Sat Jul 20 2019 Pavel Skrylev <majioa@altlinux.org> 1.0.0-alt2.git5bded6.1
- Use Ruby Policy 2.0

* Wed Jul 11 2018 Andrey Cherepanov <cas@altlinux.org> 1.0.0-alt1.git5bded6.1
- Rebuild with new Ruby autorequirements.

* Tue Apr 22 2014 Andrey Cherepanov <cas@altlinux.org> 1.0.0-alt1.git5bded6
- Initial build for ALT Linux
