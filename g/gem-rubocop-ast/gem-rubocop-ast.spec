%define        _unpackaged_files_terminate_build 1
%def_enable    check
%def_enable    doc
%def_enable    devel
%define        gemname rubocop-ast

Name:          gem-rubocop-ast
Version:       1.47.1
Release:       alt1
Summary:       RuboCop's Node and NodePattern classes
License:       MIT
Group:         Development/Ruby
Url:           https://rubocop.org/
Vcs:           https://github.com/rubocop-hq/rubocop-ast.git
Packager:      Baltix Maintaining Team <baltix@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
BuildRequires: fakegit
BuildRequires: gem(oedipus_lex) >= 2.6.0
BuildRequires: gem(rubocop-rspec) >= 3.3.0
BuildConflicts: gem(rubocop-rspec) >= 4
%if_enabled check
BuildRequires: gem(bump) >= 0
BuildRequires: gem(bundler) >= 1.15.0
BuildRequires: gem(parser) >= 3.3.7.2
BuildRequires: gem(prism) >= 1.4
BuildRequires: gem(racc) >= 0
BuildRequires: gem(rake) >= 13.0
BuildRequires: gem(rspec) >= 3.7
BuildRequires: gem(rubocop) >= 1.0
BuildRequires: gem(rubocop-performance) >= 0
BuildRequires: gem(simplecov) >= 0.17
BuildConflicts: gem(bundler) >= 3
BuildConflicts: gem(prism) >= 2
BuildConflicts: gem(rake) >= 14
BuildConflicts: gem(rspec) >= 4
BuildConflicts: gem(simplecov) >= 1
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_use_gem_dependency simplecov >= 0.17,simplecov < 1
%ruby_use_gem_dependency rubocop-rspec >= 3.3.0,rubocop-rspec < 4
Requires:      ruby >= 2.7.0
Requires:      gem(parser) >= 3.3.7.2
Requires:      gem(prism) >= 1.4
Conflicts:     gem(prism) >= 2
Provides:      gem(rubocop-ast) = 1.47.1

%ruby_on_build_rake_tasks generate

%description
RuboCop is a Ruby code style checking and code formatting tool. It aims to
enforce the community-driven Ruby Style Guide.


%if_enabled    doc
%package       -n gem-rubocop-ast-doc
Version:       1.47.1
Release:       alt1
Summary:       RuboCop's Node and NodePattern classes documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета rubocop-ast
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(rubocop-ast) = 1.47.1

%description   -n gem-rubocop-ast-doc
RuboCop's Node and NodePattern classes documentation files.

RuboCop is a Ruby code style checking and code formatting tool. It aims to
enforce the community-driven Ruby Style Guide.

%description   -n gem-rubocop-ast-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета rubocop-ast.
%endif


%if_enabled    devel
%package       -n gem-rubocop-ast-devel
Version:       1.47.1
Release:       alt1
Summary:       RuboCop's Node and NodePattern classes development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета rubocop-ast
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(rubocop-ast) = 1.47.1
Requires:      gem(bump) >= 0
Requires:      gem(oedipus_lex) >= 2.6.0
Requires:      gem(racc) >= 0
Requires:      gem(rake) >= 13.0
Requires:      gem(rspec) >= 3.7
Requires:      gem(rubocop) >= 1.0
Requires:      gem(rubocop-performance) >= 0
Requires:      gem(rubocop-rspec) >= 3.3.0
Requires:      gem(simplecov) >= 0.17
Conflicts:     gem(rake) >= 14
Conflicts:     gem(rspec) >= 4
Conflicts:     gem(rubocop-rspec) >= 4
Conflicts:     gem(simplecov) >= 1

%description   -n gem-rubocop-ast-devel
RuboCop's Node and NodePattern classes development package.

RuboCop is a Ruby code style checking and code formatting tool. It aims to
enforce the community-driven Ruby Style Guide.

%description   -n gem-rubocop-ast-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета rubocop-ast.
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
%doc LICENSE.txt README.md CHANGELOG.md CONTRIBUTING.md changelog
%ruby_gemspec
%ruby_gemlibdir

%if_enabled    doc
%files         -n gem-rubocop-ast-doc
%doc LICENSE.txt README.md CHANGELOG.md CONTRIBUTING.md changelog
%ruby_gemdocdir
%endif

%if_enabled    devel
%files         -n gem-rubocop-ast-devel
%doc LICENSE.txt README.md CHANGELOG.md CONTRIBUTING.md changelog
%endif


%changelog
* Sat Oct 18 2025 Pavel Skrylev <majioa@altlinux.org> 1.47.1-alt1
- ^ 1.17.0 -> 1.47.1 (closes ALT#50197)

* Sat Apr 16 2022 Pavel Skrylev <majioa@altlinux.org> 1.17.0-alt1
- ^ 1.7.0 -> 1.17.0

* Sun May 30 2021 Pavel Skrylev <majioa@altlinux.org> 1.7.0-alt1
- ^ 0.1.0 -> 1.7.0

* Mon Jul 14 2020 Pavel Skrylev <majioa@altlinux.org> 0.1.0-alt1
- + packaged gem with usage Ruby Policy 2.0
