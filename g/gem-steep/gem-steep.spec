%define        _unpackaged_files_terminate_build 1
%def_disable   check
%def_enable    doc
%def_enable    devel
%define        gemname steep

Name:          gem-steep
Version:       1.10.0
Release:       alt1.1
Summary:       Gradual Typing for Ruby
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/soutaro/steep
Vcs:           https://github.com/soutaro/steep.git
Packager:      Baltix Maintaining Team <baltix@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
%if_enabled check
BuildRequires: gem(activesupport) >= 5.1
BuildRequires: gem(concurrent-ruby) >= 1.1.10
BuildRequires: gem(csv) >= 3.0.9
BuildRequires: gem(fileutils) >= 1.1.0
BuildRequires: gem(json) >= 2.1.0
BuildRequires: gem(language_server-protocol) >= 3.17.0.4
BuildRequires: gem(listen) >= 3.0
BuildRequires: gem(logger) >= 1.3.0
BuildRequires: gem(majo) >= 0
BuildRequires: gem(memory_profiler) >= 0
BuildRequires: gem(minitest) >= 5.17.0
BuildRequires: gem(minitest-hooks) >= 0
BuildRequires: gem(minitest-slow_test) >= 0
BuildRequires: gem(mutex_m) >= 0.3.0
BuildRequires: gem(parser) >= 3.1
BuildRequires: gem(rainbow) >= 2.2.2
BuildRequires: gem(rake) >= 0
BuildRequires: gem(rbs) >= 3.9
BuildRequires: gem(rbs-inline) >= 0
BuildRequires: gem(securerandom) >= 0.1
BuildRequires: gem(stackprof) >= 0
BuildRequires: gem(strscan) >= 1.0.0
BuildRequires: gem(terminal-table) >= 2
BuildRequires: gem(uri) >= 0.12.0
BuildConflicts: gem(language_server-protocol) >= 4.0
BuildConflicts: gem(listen) >= 4
BuildConflicts: gem(minitest) >= 6
BuildConflicts: gem(rainbow) >= 4
BuildConflicts: gem(rbs) >= 4
BuildConflicts: gem(terminal-table) >= 5
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_use_gem_dependency minitest >= 5.17.0,minitest < 6
Requires:      ruby >= 3.1.0
Requires:      gem(activesupport) >= 5.1
Requires:      gem(concurrent-ruby) >= 1.1.10
Requires:      gem(csv) >= 3.0.9
Requires:      gem(fileutils) >= 1.1.0
Requires:      gem(json) >= 2.1.0
Requires:      gem(language_server-protocol) >= 3.17.0.4
Requires:      gem(listen) >= 3.0
Requires:      gem(logger) >= 1.3.0
Requires:      gem(mutex_m) >= 0.3.0
Requires:      gem(parser) >= 3.1
Requires:      gem(rainbow) >= 2.2.2
Requires:      gem(rbs) >= 3.9
Requires:      gem(securerandom) >= 0.1
Requires:      gem(strscan) >= 1.0.0
Requires:      gem(terminal-table) >= 2
Requires:      gem(uri) >= 0.12.0
Conflicts:     gem(language_server-protocol) >= 4.0
Conflicts:     gem(listen) >= 4
Conflicts:     gem(rainbow) >= 4
Conflicts:     gem(rbs) >= 4
Conflicts:     gem(terminal-table) >= 5
Provides:      gem(steep) = 1.10.0

%ruby_ignore_names gemfile_steep

%description
Gradual Typing for Ruby. Steep does not infer types from Ruby programs, but
requires declaring types and writing annotations.


%package       -n steep
Version:       1.10.0
Release:       alt1.1
Summary:       Gradual Typing for Ruby executable(s)
Summary(ru_RU.UTF-8): Исполнямка для самоцвета steep
Group:         Other
BuildArch:     noarch

Requires:      gem(steep) = 1.10.0
Requires:      gem(rbs-inline) >= 0

%description   -n steep
Gradual Typing for Ruby executable(s).

Gradual Typing for Ruby. Steep does not infer types from Ruby programs, but
requires declaring types and writing annotations.

%description   -n steep -l ru_RU.UTF-8
Исполнямка для самоцвета steep.


%if_enabled    doc
%package       -n gem-steep-doc
Version:       1.10.0
Release:       alt1.1
Summary:       Gradual Typing for Ruby documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета steep
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(steep) = 1.10.0

%description   -n gem-steep-doc
Gradual Typing for Ruby documentation files.

Gradual Typing for Ruby. Steep does not infer types from Ruby programs, but
requires declaring types and writing annotations.

%description   -n gem-steep-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета steep.
%endif


%if_enabled    devel
%package       -n gem-steep-devel
Version:       1.10.0
Release:       alt1.1
Summary:       Gradual Typing for Ruby development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета steep
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(steep) = 1.10.0
Requires:      gem(majo) >= 0
Requires:      gem(memory_profiler) >= 0
Requires:      gem(rbs-inline) >= 0

%description   -n gem-steep-devel
Gradual Typing for Ruby development package.

Gradual Typing for Ruby. Steep does not infer types from Ruby programs, but
requires declaring types and writing annotations.

%description   -n gem-steep-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета steep.
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
%doc CHANGELOG.md LICENSE README.md
%ruby_gemspec
%ruby_gemlibdir

%files         -n steep
%doc CHANGELOG.md LICENSE README.md
%_bindir/steep

%if_enabled    doc
%files         -n gem-steep-doc
%doc CHANGELOG.md LICENSE README.md
%ruby_gemdocdir
%endif

%if_enabled    devel
%files         -n gem-steep-devel
%doc CHANGELOG.md LICENSE README.md
%endif


%changelog
* Mon Mar 23 2026 Pavel Skrylev <majioa@altlinux.org> 1.10.0-alt1.1
- ! fixed spec to filter out gemfile_steep source

* Thu Oct 23 2025 Pavel Skrylev <majioa@altlinux.org> 1.10.0-alt1
- ^ 1.7.1 -> 1.10.0

* Wed Jul 24 2024 Pavel Skrylev <majioa@altlinux.org> 1.7.1-alt1
- ^ 1.6.0 -> 1.7.1

* Tue Apr 16 2024 Pavel Skrylev <majioa@altlinux.org> 1.6.0-alt1
- + packaged gem with Ruby Policy 2.0
