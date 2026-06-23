%define        _unpackaged_files_terminate_build 1
%def_disable   check
%def_enable    doc
%def_disable   devel
%define        gemname unparser

Name:          gem-unparser
Version:       0.9.0
Release:       alt1
Summary:       Generate equivalent source for parser gem AST nodes
License:       MIT
Group:         Development/Ruby
Url:           http://github.com/mbj/unparser
Vcs:           https://github.com/mbj/unparser.git
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-macros-ruby setup-rb rake
%if_enabled check
BuildRequires: gem(benchmark) >= 0.5.0
BuildRequires: gem(diff-lcs) >= 1.6
BuildRequires: gem(mutant) >= 0.14.2
BuildRequires: gem(mutant-rspec) >= 0.14.2
BuildRequires: gem(parser) >= 3.3.0
BuildRequires: gem(prism) >= 1.5.1
BuildRequires: gem(rspec) >= 3.10.0
BuildRequires: gem(rspec-core) >= 3.10.1
BuildRequires: gem(rspec-its) >= 2.0
BuildRequires: gem(rspectre) >= 0.2.0
BuildRequires: gem(rubocop) >= 1.7
BuildRequires: gem(rubocop-packaging) >= 0.5
BuildConflicts: gem(benchmark) >= 0.6
BuildConflicts: gem(diff-lcs) >= 3
BuildConflicts: gem(rspec) >= 5
BuildConflicts: gem(rspec-core) >= 5
BuildConflicts: gem(rspec-its) >= 3
BuildConflicts: gem(rspectre) >= 0.3
BuildConflicts: gem(rubocop) >= 2
BuildConflicts: gem(rubocop-packaging) >= 1
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_use_gem_dependency rspec >= 3.10.0,rspec < 4
%ruby_use_gem_dependency rspec-core >= 3.10.1,rspec-core < 4
Requires:      ruby >= 3.3
Requires:      gem(diff-lcs) >= 1.6
Requires:      gem(parser) >= 3.3.0
Requires:      gem(prism) >= 1.5.1
Conflicts:     gem(diff-lcs) >= 3
Provides:      gem(unparser) = 0.9.0

%description
Generate equivalent source for parser gem AST nodes


%package       -n unparser
Version:       0.9.0
Release:       alt1
Summary:       Generate equivalent source for parser gem AST nodes executable(s)
Summary(ru_RU.UTF-8): Исполнямка для самоцвета unparser
Group:         Other
BuildArch:     noarch

Requires:      gem(unparser) = 0.9.0

%description   -n unparser
Generate equivalent source for parser gem AST nodes executable(s).

%description   -n unparser -l ru_RU.UTF-8
Исполнямка для самоцвета unparser.


%if_enabled    doc
%package       -n gem-unparser-doc
Version:       0.9.0
Release:       alt1
Summary:       Generate equivalent source for parser gem AST nodes documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета unparser
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(unparser) = 0.9.0

%description   -n gem-unparser-doc
Generate equivalent source for parser gem AST nodes documentation files.

%description   -n gem-unparser-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета unparser.
%endif


%if_enabled    devel
%package       -n gem-unparser-devel
Version:       0.9.0
Release:       alt1
Summary:       Generate equivalent source for parser gem AST nodes development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета unparser
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(unparser) = 0.9.0
Requires:      gem(benchmark) >= 0.5.0
Requires:      gem(rspec) >= 3.10.0
Requires:      gem(rspec-core) >= 3.10.1
Requires:      gem(rspec-its) >= 2.0
Requires:      gem(rspectre) >= 0.2.0
Requires:      gem(rubocop) >= 1.7
Requires:      gem(rubocop-packaging) >= 0.5
Conflicts:     gem(benchmark) >= 0.6
Conflicts:     gem(rspec) >= 5
Conflicts:     gem(rspec-core) >= 5
Conflicts:     gem(rspec-its) >= 3
Conflicts:     gem(rspectre) >= 0.3
Conflicts:     gem(rubocop) >= 2
Conflicts:     gem(rubocop-packaging) >= 1

%description   -n gem-unparser-devel
Generate equivalent source for parser gem AST nodes development package.

%description   -n gem-unparser-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета unparser.
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
%doc README.md Changelog.md LICENSE
%ruby_gemspec
%ruby_gemlibdir

%files         -n unparser
%doc README.md Changelog.md LICENSE
%_bindir/unparser

%if_enabled    doc
%files         -n gem-unparser-doc
%doc README.md Changelog.md LICENSE
%ruby_gemdocdir
%endif

%if_enabled    devel
%files         -n gem-unparser-devel
%doc README.md Changelog.md LICENSE
%endif


%changelog
* Mon Jun 22 2026 Pavel Skrylev <majioa@altlinux.org> 0.9.0-alt1
- ^ 0.6.13 -> 0.9.0

* Wed Apr 17 2024 Pavel Skrylev <majioa@altlinux.org> 0.6.13-alt1
- + packaged gem with Ruby Policy 2.0
