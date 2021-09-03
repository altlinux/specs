%define        gemname memory_profiler

Name:          gem-memory-profiler
Version:       1.0.0
Release:       alt1
Summary:       Memory profiling routines for Ruby 2.5+
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/SamSaffron/memory_profiler
Vcs:           https://github.com/samsaffron/memory_profiler.git
Packager:      Pavel Skrylev <majioa@altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_ignore_names longhorn
Provides:      gem(memory_profiler) = 1.0.0


%description
Memory profiling routines for Ruby 2.5+


%package       -n ruby-memory-profiler
Version:       1.0.0
Release:       alt1
Summary:       Memory profiling routines for Ruby 2.5+ executable(s)
Summary(ru_RU.UTF-8): Исполнямка для самоцвета memory_profiler
Group:         Other
BuildArch:     noarch

Requires:      gem(memory_profiler) = 1.0.0

%description   -n ruby-memory-profiler
Memory profiling routines for Ruby 2.5+ executable(s).

%description   -n ruby-memory-profiler -l ru_RU.UTF-8
Исполнямка для самоцвета memory_profiler.


%package       -n gem-memory-profiler-doc
Version:       1.0.0
Release:       alt1
Summary:       Memory profiling routines for Ruby 2.5+ documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета memory_profiler
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(memory_profiler) = 1.0.0

%description   -n gem-memory-profiler-doc
Memory profiling routines for Ruby 2.5+ documentation files.

%description   -n gem-memory-profiler-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета memory_profiler.


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

%files         -n ruby-memory-profiler
%doc README.md
%_bindir/ruby-memory-profiler

%files         -n gem-memory-profiler-doc
%doc README.md
%ruby_gemdocdir


%changelog
* Thu Sep 02 2021 Pavel Skrylev <majioa@altlinux.org> 1.0.0-alt1
- + packaged gem with Ruby Policy 2.0
