%define        _unpackaged_files_terminate_build 1
%def_enable    check
%def_enable    doc
%def_enable    devel
%define        gemname benchmark-ips

Name:          gem-benchmark-ips
Version:       2.15.1
Release:       alt1
Summary:       A iterations per second enhancement to Benchmark
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/evanphx/benchmark-ips
Vcs:           https://github.com/evanphx/benchmark-ips.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
%if_enabled check
BuildRequires: gem(minitest) >= 5.4
BuildRequires: gem(rake) >= 10.5
BuildRequires: gem(rdoc) >= 4.0
BuildConflicts: gem(minitest) >= 7
BuildConflicts: gem(rdoc) >= 7
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_use_gem_dependency rdoc >= 6.1.1,rdoc < 7
%ruby_use_gem_dependency minitest >= 6.0
Requires:      gem(rake) >= 10.5
Obsoletes:     ruby-benchmark-ips < %EVR
Provides:      ruby-benchmark-ips = %EVR
Provides:      gem(benchmark-ips) = 2.15.1

%description
Benchmark/ips benchmarks a blocks iterations/second. For short snippets of code,
ips automatically figures out how many times to run the code to get interesting
data. No more guessing at random iteration counts.


%if_enabled    doc
%package       -n gem-benchmark-ips-doc
Version:       2.15.1
Release:       alt1
Summary:       A iterations per second enhancement to Benchmark documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета benchmark-ips
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(benchmark-ips) = 2.15.1

%description   -n gem-benchmark-ips-doc
A iterations per second enhancement to Benchmark documentation
files.

Benchmark/ips benchmarks a blocks iterations/second. For short snippets of code,
ips automatically figures out how many times to run the code to get interesting
data. No more guessing at random iteration counts.

%description   -n gem-benchmark-ips-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета benchmark-ips.
%endif


%if_enabled    devel
%package       -n gem-benchmark-ips-devel
Version:       2.15.1
Release:       alt1
Summary:       A iterations per second enhancement to Benchmark development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета benchmark-ips
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(benchmark-ips) = 2.15.1
Requires:      gem(minitest) >= 5.4
Requires:      gem(rdoc) >= 4.0
Conflicts:     gem(minitest) >= 7
Conflicts:     gem(rdoc) >= 7

%description   -n gem-benchmark-ips-devel
A iterations per second enhancement to Benchmark development
package.

Benchmark/ips benchmarks a blocks iterations/second. For short snippets of code,
ips automatically figures out how many times to run the code to get interesting
data. No more guessing at random iteration counts.

%description   -n gem-benchmark-ips-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета benchmark-ips.
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
%doc History.md LICENSE README.md
%ruby_gemspec
%ruby_gemlibdir

%if_enabled    doc
%files         -n gem-benchmark-ips-doc
%doc History.md LICENSE README.md
%ruby_gemdocdir
%endif

%if_enabled    devel
%files         -n gem-benchmark-ips-devel
%doc History.md LICENSE README.md
%endif


%changelog
* Tue Aug 18 2026 Pavel Skrylev <majioa@altlinux.org> 2.15.1-alt1
- ^ 2.10.0 -> 2.15.1

* Wed Sep 21 2022 Pavel Skrylev <majioa@altlinux.org> 2.10.0-alt1
- ^ 2.9.1 -> 2.10.0

* Tue Jun 22 2021 Pavel Skrylev <majioa@altlinux.org> 2.9.1-alt1
- ^ 2.7.2 -> 2.9.1

* Fri Jul 19 2019 Pavel Skrylev <majioa@altlinux.org> 2.7.2-alt1
- > Ruby Policy 2.0
- > git source
- ^ 1.2.0 -> 2.7.2

* Mon Aug 27 2018 Andrey Cherepanov <cas@altlinux.org> 1.2.0-alt2.gite47e416
- Rebuild for new Ruby autorequirements.

* Tue Apr 22 2014 Andrey Cherepanov <cas@altlinux.org> 1.2.0-alt1.gite47e416
- Initial build for ALT Linux
