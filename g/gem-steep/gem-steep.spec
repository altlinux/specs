%define        _unpackaged_files_terminate_build 1
%def_disable   check
%def_enable    doc
%def_enable    devel
%define        gemname steep

Name:          gem-steep
Version:       1.7.1
Release:       alt1
Summary:       Gradual Typing for Ruby
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/soutaro/steep
Vcs:           https://github.com/soutaro/steep.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
%if_enabled check
BuildRequires: gem(rake) >= 0
BuildRequires: gem(minitest) >= 5.17.0
BuildRequires: gem(minitest-hooks) >= 0
BuildRequires: gem(stackprof) >= 0
BuildRequires: gem(minitest-slow_test) >= 0
BuildRequires: gem(debug) >= 0
BuildRequires: gem(parser) >= 3.1
BuildRequires: gem(activesupport) >= 5.1
BuildRequires: gem(rainbow) >= 2.2.2
BuildRequires: gem(listen) >= 3.0
BuildRequires: gem(language_server-protocol) >= 3.15
BuildRequires: gem(rbs) >= 3.5.0
BuildRequires: gem(concurrent-ruby) >= 1.1.10
BuildRequires: gem(terminal-table) >= 2
BuildRequires: gem(securerandom) >= 0.1
BuildRequires: gem(json) >= 2.1.0
BuildRequires: gem(logger) >= 1.3.0
BuildRequires: gem(fileutils) >= 1.1.0
BuildRequires: gem(strscan) >= 1.0.0
BuildRequires: gem(csv) >= 3.0.9
BuildConflicts: gem(minitest) >= 6
BuildConflicts: gem(rainbow) >= 4
BuildConflicts: gem(listen) >= 4
BuildConflicts: gem(language_server-protocol) >= 4.0
BuildConflicts: gem(terminal-table) >= 4
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_use_gem_dependency minitest >= 5.17.0,minitest < 6
%ruby_ignore_names gemfile_steep
Requires:      gem(parser) >= 3.1
Requires:      gem(activesupport) >= 5.1
Requires:      gem(rainbow) >= 2.2.2
Requires:      gem(listen) >= 3.0
Requires:      gem(language_server-protocol) >= 3.15
Requires:      gem(rbs) >= 3.5.0
Requires:      gem(concurrent-ruby) >= 1.1.10
Requires:      gem(terminal-table) >= 2
Requires:      gem(securerandom) >= 0.1
Requires:      gem(json) >= 2.1.0
Requires:      gem(logger) >= 1.3.0
Requires:      gem(fileutils) >= 1.1.0
Requires:      gem(strscan) >= 1.0.0
Requires:      gem(csv) >= 3.0.9
Conflicts:     gem(rainbow) >= 4
Conflicts:     gem(listen) >= 4
Conflicts:     gem(language_server-protocol) >= 4.0
Conflicts:     gem(terminal-table) >= 4
Provides:      gem(steep) = 1.7.1


%description
Gradual Typing for Ruby. Steep does not infer types from Ruby programs, but
requires declaring types and writing annotations.


%package       -n steep
Version:       1.7.1
Release:       alt1
Summary:       Gradual Typing for Ruby executable(s)
Summary(ru_RU.UTF-8): Исполнямка для самоцвета steep
Group:         Other
BuildArch:     noarch

Requires:      gem(steep) = 1.7.1

%description   -n steep
Gradual Typing for Ruby executable(s).

Gradual Typing for Ruby. Steep does not infer types from Ruby programs, but
requires declaring types and writing annotations.

%description   -n steep -l ru_RU.UTF-8
Исполнямка для самоцвета steep.


%if_enabled    doc
%package       -n gem-steep-doc
Version:       1.7.1
Release:       alt1
Summary:       Gradual Typing for Ruby documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета steep
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(steep) = 1.7.1

%description   -n gem-steep-doc
Gradual Typing for Ruby documentation files.

Gradual Typing for Ruby. Steep does not infer types from Ruby programs, but
requires declaring types and writing annotations.

%description   -n gem-steep-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета steep.
%endif


%if_enabled    devel
%package       -n gem-steep-devel
Version:       1.7.1
Release:       alt1
Summary:       Gradual Typing for Ruby development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета steep
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(steep) = 1.7.1
Requires:      gem(rake) >= 0
Requires:      gem(minitest) >= 5.17.0
Requires:      gem(minitest-hooks) >= 0
Requires:      gem(stackprof) >= 0
Requires:      gem(minitest-slow_test) >= 0
Requires:      gem(debug) >= 0
Conflicts:     gem(minitest) >= 6

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
%doc README.md
%ruby_gemspec
%ruby_gemlibdir

%files         -n steep
%doc README.md
%_bindir/steep

%if_enabled    doc
%files         -n gem-steep-doc
%doc README.md
%ruby_gemdocdir
%endif

%if_enabled    devel
%files         -n gem-steep-devel
%doc README.md
%endif


%changelog
* Wed Jul 24 2024 Pavel Skrylev <majioa@altlinux.org> 1.7.1-alt1
- ^ 1.6.0 -> 1.7.1

* Tue Apr 16 2024 Pavel Skrylev <majioa@altlinux.org> 1.6.0-alt1
- + packaged gem with Ruby Policy 2.0
