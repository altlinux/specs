%define        _unpackaged_files_terminate_build 1
%def_disable   check
%def_enable    doc
%def_disable   devel
%define        gemname unparser

Name:          gem-unparser
Version:       0.6.13
Release:       alt1
Summary:       Generate equivalent source for parser gem AST nodes
License:       MIT
Group:         Development/Ruby
Url:           http://github.com/mbj/unparser
Vcs:           https://github.com/mbj/unparser.git
Packager:      Pavel Skrylev <majioa@altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
%if_enabled check
BuildRequires: gem(mutant) >= 0.11.27
BuildRequires: gem(mutant-rspec) >= 0.11.27
BuildRequires: gem(rspec) >= 3.9
BuildRequires: gem(rspec-core) >= 3.9
BuildRequires: gem(rspec-its) >= 1.3.0
BuildRequires: gem(rubocop) >= 1.7
BuildRequires: gem(rubocop-packaging) >= 0.5
BuildRequires: gem(mutant-license) >= 0
BuildRequires: gem(diff-lcs) >= 1.3
BuildRequires: gem(parser) >= 3.3.0
BuildConflicts: gem(mutant) >= 0.12
BuildConflicts: gem(mutant-rspec) >= 0.12
BuildConflicts: gem(rspec) >= 4
BuildConflicts: gem(rspec-core) >= 4
BuildConflicts: gem(rspec-its) >= 1.4
BuildConflicts: gem(rubocop) >= 2
BuildConflicts: gem(rubocop-packaging) >= 1
BuildConflicts: gem(diff-lcs) >= 2
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
Requires:      gem(diff-lcs) >= 1.3
Requires:      gem(parser) >= 3.3.0
Conflicts:     gem(diff-lcs) >= 2
Provides:      gem(unparser) = 0.6.13


%description
Generate equivalent source for parser gem AST nodes


%package       -n unparser
Version:       0.6.13
Release:       alt1
Summary:       Generate equivalent source for parser gem AST nodes executable(s)
Summary(ru_RU.UTF-8): Исполнямка для самоцвета unparser
Group:         Other
BuildArch:     noarch

Requires:      gem(unparser) = 0.6.13

%description   -n unparser
Generate equivalent source for parser gem AST nodes executable(s).
%description   -n unparser -l ru_RU.UTF-8
Исполнямка для самоцвета unparser.


%if_enabled    doc
%package       -n gem-unparser-doc
Version:       0.6.13
Release:       alt1
Summary:       Generate equivalent source for parser gem AST nodes documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета unparser
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(unparser) = 0.6.13

%description   -n gem-unparser-doc
Generate equivalent source for parser gem AST nodes documentation files.
%description   -n gem-unparser-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета unparser.
%endif


%if_enabled    devel
%package       -n gem-unparser-devel
Version:       0.6.13
Release:       alt1
Summary:       Generate equivalent source for parser gem AST nodes development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета unparser
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(unparser) = 0.6.13
Requires:      gem(mutant) >= 0.11.27
Requires:      gem(mutant-rspec) >= 0.11.27
Requires:      gem(rspec) >= 3.9
Requires:      gem(rspec-core) >= 3.9
Requires:      gem(rspec-its) >= 1.3.0
Requires:      gem(rubocop) >= 1.7
Requires:      gem(rubocop-packaging) >= 0.5
Requires:      gem(mutant-license) >= 0
Conflicts:     gem(mutant) >= 0.12
Conflicts:     gem(mutant-rspec) >= 0.12
Conflicts:     gem(rspec) >= 4
Conflicts:     gem(rspec-core) >= 4
Conflicts:     gem(rspec-its) >= 1.4
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
%doc README.md
%ruby_gemspec
%ruby_gemlibdir

%files         -n unparser
%doc README.md
%_bindir/unparser

%if_enabled    doc
%files         -n gem-unparser-doc
%doc README.md
%ruby_gemdocdir
%endif

%if_enabled    devel
%files         -n gem-unparser-devel
%doc README.md
%endif


%changelog
* Wed Apr 17 2024 Pavel Skrylev <majioa@altlinux.org> 0.6.13-alt1
- + packaged gem with Ruby Policy 2.0
