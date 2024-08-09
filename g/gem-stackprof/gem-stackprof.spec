%define        _unpackaged_files_terminate_build 1
%def_enable    check
%def_enable    doc
%def_enable    devel
%define        gemname stackprof

Name:          gem-stackprof
Version:       0.2.26
Release:       alt1
Summary:       sampling callstack-profiler for ruby 2.2+
License:       MIT
Group:         Development/Ruby
Url:           http://github.com/tmm1/stackprof
Vcs:           https://github.com/tmm1/stackprof/tree/v0.2.19.git
Packager:      Pavel Skrylev <majioa@altlinux.org>

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
%if_enabled check
BuildRequires: gem(rake-compiler) >= 0.9
BuildRequires: gem(minitest) >= 5.0
BuildConflicts: gem(rake-compiler) >= 2
BuildConflicts: gem(minitest) >= 6
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_use_gem_dependency rake-compiler >= 1.1.2,rake-compiler < 2
Provides:      gem(stackprof) = 0.2.26


%description
stackprof is a fast sampling profiler for ruby code, with cpu, wallclock and
object allocation samplers.


%package       -n stackprof
Version:       0.2.26
Release:       alt1
Summary:       sampling callstack-profiler for ruby 2.2+ executable(s)
Summary(ru_RU.UTF-8): Исполнямка для самоцвета stackprof
Group:         Other
BuildArch:     noarch

Requires:      gem(stackprof) = 0.2.26

%description   -n stackprof
sampling callstack-profiler for ruby 2.2+ executable(s).

stackprof is a fast sampling profiler for ruby code, with cpu, wallclock and
object allocation samplers.

%description   -n stackprof -l ru_RU.UTF-8
Исполнямка для самоцвета stackprof.


%if_enabled    doc
%package       -n gem-stackprof-doc
Version:       0.2.26
Release:       alt1
Summary:       sampling callstack-profiler for ruby 2.2+ documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета stackprof
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(stackprof) = 0.2.26

%description   -n gem-stackprof-doc
sampling callstack-profiler for ruby 2.2+ documentation files.

stackprof is a fast sampling profiler for ruby code, with cpu, wallclock and
object allocation samplers.

%description   -n gem-stackprof-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета stackprof.
%endif


%if_enabled    devel
%package       -n gem-stackprof-devel
Version:       0.2.26
Release:       alt1
Summary:       sampling callstack-profiler for ruby 2.2+ development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета stackprof
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(stackprof) = 0.2.26
Requires:      gem(rake-compiler) >= 0.9
Requires:      gem(minitest) >= 5.0
Conflicts:     gem(rake-compiler) >= 2
Conflicts:     gem(minitest) >= 6

%description   -n gem-stackprof-devel
sampling callstack-profiler for ruby 2.2+ development package.

stackprof is a fast sampling profiler for ruby code, with cpu, wallclock and
object allocation samplers.

%description   -n gem-stackprof-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета stackprof.
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
%doc README.md vendor/FlameGraph/README
%ruby_gemspec
%ruby_gemlibdir
%ruby_gemextdir

%files         -n stackprof
%doc README.md vendor/FlameGraph/README
%_bindir/stackprof
%_bindir/stackprof-flamegraph.pl
%_bindir/stackprof-gprof2dot.py

%if_enabled    doc
%files         -n gem-stackprof-doc
%doc README.md vendor/FlameGraph/README
%ruby_gemdocdir
%endif

%if_enabled    devel
%files         -n gem-stackprof-devel
%doc README.md vendor/FlameGraph/README
%endif


%changelog
* Fri Jul 26 2024 Pavel Skrylev <majioa@altlinux.org> 0.2.26-alt1
- ^ 0.2.19 -> 0.2.26

* Tue May 17 2022 Pavel Skrylev <majioa@altlinux.org> 0.2.19-alt1
- + packaged gem with Ruby Policy 2.0
