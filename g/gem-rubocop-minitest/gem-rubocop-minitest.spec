%define        _unpackaged_files_terminate_build 1
%def_enable    check
%def_enable    doc
%def_enable    devel
%define        gemname rubocop-minitest

Name:          gem-rubocop-minitest
Version:       0.38.2
Release:       alt1
Summary:       Automatic Minitest code style checking tool
License:       MIT
Group:         Development/Ruby
Url:           https://docs.rubocop.org/rubocop-minitest/
Vcs:           https://github.com/rubocop/rubocop-minitest.git
Packager:      Baltix Maintaining Team <baltix@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
Autoprov:      yes,noruby
Autoreq:       yes,noruby
BuildRequires(pre): rpm-build-ruby
%if_enabled check
BuildRequires: gem(bump) >= 0
BuildRequires: gem(lint_roller) >= 1.1
BuildRequires: gem(minitest) >= 5.11
BuildRequires: gem(minitest-proveit) >= 0
BuildRequires: gem(prism) >= 0
BuildRequires: gem(rake) >= 0
BuildRequires: gem(rubocop) >= 1.15.0
BuildRequires: gem(rubocop-ast) >= 1.7.0
BuildRequires: gem(rubocop-performance) >= 1.11.3
BuildRequires: gem(test-queue) >= 0
BuildRequires: gem(yard) >= 0.9
BuildConflicts: gem(lint_roller) >= 2
BuildConflicts: gem(minitest) >= 6
BuildConflicts: gem(rubocop) >= 2
BuildConflicts: gem(rubocop-ast) >= 2
BuildConflicts: gem(rubocop-performance) >= 2
BuildConflicts: gem(yard) >= 1
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_use_gem_dependency rubocop >= 1.15.0,rubocop < 2
%ruby_use_gem_dependency rubocop-performance >= 1.11.3,rubocop-performance < 2
%ruby_use_gem_dependency rubocop-ast >= 1.7.0,rubocop-ast < 2
Requires:      ruby >= 2.7.0
Requires:      gem(lint_roller) >= 1.1
Requires:      gem(rubocop) >= 1.15.0
Requires:      gem(rubocop-ast) >= 1.7.0
Conflicts:     gem(lint_roller) >= 2
Conflicts:     gem(rubocop) >= 2
Conflicts:     gem(rubocop-ast) >= 2
Provides:      gem(rubocop-minitest) = 0.38.2

%description
Automatic Minitest code style checking tool. A RuboCop extension focused on
enforcing Minitest best practices and coding conventions.


%if_enabled    doc
%package       -n gem-rubocop-minitest-doc
Version:       0.38.2
Release:       alt1
Summary:       Automatic Minitest code style checking tool documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета rubocop-minitest
Group:         Development/Documentation
BuildArch:     noarch

Autoprov:      yes,noruby
Autoreq:       yes,noruby
Requires:      gem(rubocop-minitest) = 0.38.2

%description   -n gem-rubocop-minitest-doc
Automatic Minitest code style checking tool documentation files.

Automatic Minitest code style checking tool. A RuboCop extension focused on
enforcing Minitest best practices and coding conventions.

%description   -n gem-rubocop-minitest-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета rubocop-minitest.
%endif


%if_enabled    devel
%package       -n gem-rubocop-minitest-devel
Version:       0.38.2
Release:       alt1
Summary:       Automatic Minitest code style checking tool development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета rubocop-minitest
Group:         Development/Ruby
BuildArch:     noarch

Autoprov:      yes,noruby
Autoreq:       yes,noruby
Requires:      gem(rubocop-minitest) = 0.38.2
Requires:      gem(bump) >= 0
Requires:      gem(lint_roller) >= 1.1
Requires:      gem(minitest) >= 5.11
Requires:      gem(minitest-proveit) >= 0
Requires:      gem(prism) >= 0
Requires:      gem(rake) >= 0
Requires:      gem(rubocop) >= 1.15.0
Requires:      gem(rubocop-ast) >= 1.7.0
Requires:      gem(rubocop-performance) >= 1.11.3
Requires:      gem(test-queue) >= 0
Requires:      gem(yard) >= 0.9
Conflicts:     gem(lint_roller) >= 2
Conflicts:     gem(minitest) >= 6
Conflicts:     gem(rubocop) >= 2
Conflicts:     gem(rubocop-ast) >= 2
Conflicts:     gem(rubocop-performance) >= 2
Conflicts:     gem(yard) >= 1

%description   -n gem-rubocop-minitest-devel
Automatic Minitest code style checking tool development package.

Automatic Minitest code style checking tool. A RuboCop extension focused on
enforcing Minitest best practices and coding conventions.

%description   -n gem-rubocop-minitest-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета rubocop-minitest.
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
%files         -n gem-rubocop-minitest-doc
%doc LICENSE.txt README.md CHANGELOG.md CONTRIBUTING.md changelog
%ruby_gemdocdir
%endif

%if_enabled    devel
%files         -n gem-rubocop-minitest-devel
%doc LICENSE.txt README.md CHANGELOG.md CONTRIBUTING.md changelog
%endif


%changelog
* Sun Nov 23 2025 Pavel Skrylev <majioa@altlinux.org> 0.38.2-alt1
- ^ 0.19.1 -> 0.38.2

* Sat Apr 16 2022 Pavel Skrylev <majioa@altlinux.org> 0.19.1-alt1
- ^ 0.13.0 -> 0.19.1

* Wed Jun 23 2021 Pavel Skrylev <majioa@altlinux.org> 0.13.0-alt1
- + packaged gem with Ruby Policy 2.0
