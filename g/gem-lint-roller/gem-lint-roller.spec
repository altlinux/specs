%define        _unpackaged_files_terminate_build 1
%def_disable   check
%def_enable    doc
%def_enable    devel
%define        gemname lint_roller

Name:          gem-lint-roller
Version:       1.1.0
Release:       alt1
Summary:       A plugin specification for linter and formatter rulesets
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/standardrb/lint_roller
Vcs:           https://github.com/standardrb/lint_roller.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
%if_enabled check
BuildRequires: gem(rake) >= 0
BuildRequires: gem(minitest) >= 0
BuildRequires: gem(standard) >= 0
BuildRequires: gem(m) >= 0
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
Provides:      gem(lint_roller) = 1.1.0


%description
A plugin specification for linter and formatter rulesets


%if_enabled    doc
%package       -n gem-lint-roller-doc
Version:       1.1.0
Release:       alt1
Summary:       A plugin specification for linter and formatter rulesets documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета lint_roller
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(lint_roller) = 1.1.0

%description   -n gem-lint-roller-doc
A plugin specification for linter and formatter rulesets documentation files.

%description   -n gem-lint-roller-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета lint_roller.
%endif


%if_enabled    devel
%package       -n gem-lint-roller-devel
Version:       1.1.0
Release:       alt1
Summary:       A plugin specification for linter and formatter rulesets development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета lint_roller
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(lint_roller) = 1.1.0
Requires:      gem(rake) >= 0
Requires:      gem(minitest) >= 0
Requires:      gem(standard) >= 0
Requires:      gem(m) >= 0

%description   -n gem-lint-roller-devel
A plugin specification for linter and formatter rulesets development package.

%description   -n gem-lint-roller-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета lint_roller.
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

%if_enabled    doc
%files         -n gem-lint-roller-doc
%doc README.md
%ruby_gemdocdir
%endif

%if_enabled    devel
%files         -n gem-lint-roller-devel
%doc README.md
%endif


%changelog
* Wed Apr 17 2024 Pavel Skrylev <majioa@altlinux.org> 1.1.0-alt1
- + packaged gem with Ruby Policy 2.0
