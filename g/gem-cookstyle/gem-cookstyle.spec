%define        _unpackaged_files_terminate_build 1
%def_enable    check
%def_enable    doc
%def_enable    devel
%define        gemname cookstyle

Name:          gem-cookstyle
Version:       8.5.2
Release:       alt1
Summary:       Cookstyle is a code linting tool
License:       Apache-2.0
Group:         Development/Ruby
Url:           https://docs.chef.io/workstation/cookstyle/
Vcs:           https://github.com/chef/cookstyle.git
Packager:      Baltix Maintaining Team <baltix@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
Autoprov:      yes,noruby
Autoreq:       yes,noruby
BuildRequires(pre): rpm-build-ruby
%if_enabled check
BuildRequires: gem(appbundler) >= 0
BuildRequires: gem(pry) >= 0
BuildRequires: gem(rake) >= 0
BuildRequires: gem(rspec) >= 3.4
BuildRequires: gem(rubocop) >= 1.15.0
BuildConflicts: gem(rubocop) >= 2
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_use_gem_dependency rubocop >= 1.15.0,rubocop < 2
Requires:      ruby >= 2.7
Requires:      gem(appbundler) >= 0
Requires:      gem(rubocop) >= 1.15.0
Conflicts:     gem(rubocop) >= 2
Provides:      gem(cookstyle) = 8.5.2

%description
Cookstyle is a code linting tool that helps you to write better Chef Infra
cookbooks by detecting and automatically correcting style, syntax, and logic
mistakes in your code.


%package       -n cookstyle
Version:       8.5.2
Release:       alt1
Summary:       Cookstyle is a code linting tool executable(s)
Summary(ru_RU.UTF-8): Исполнямка для самоцвета cookstyle
Group:         Other
BuildArch:     noarch

Autoprov:      yes,noruby
Autoreq:       yes,noruby
Requires:      gem(cookstyle) = 8.5.2
Requires:      gem(appbundler) >= 0

%description   -n cookstyle
Cookstyle is a code linting tool executable(s).

Cookstyle is a code linting tool that helps you to write better Chef Infra
cookbooks by detecting and automatically correcting style, syntax, and logic
mistakes in your code.

%description   -n cookstyle -l ru_RU.UTF-8
Исполнямка для самоцвета cookstyle.


%if_enabled    doc
%package       -n gem-cookstyle-doc
Version:       8.5.2
Release:       alt1
Summary:       Cookstyle is a code linting tool documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета cookstyle
Group:         Development/Documentation
BuildArch:     noarch

Autoprov:      yes,noruby
Autoreq:       yes,noruby
Requires:      gem(cookstyle) = 8.5.2

%description   -n gem-cookstyle-doc
Cookstyle is a code linting tool documentation files.

Cookstyle is a code linting tool that helps you to write better Chef Infra
cookbooks by detecting and automatically correcting style, syntax, and logic
mistakes in your code.

%description   -n gem-cookstyle-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета cookstyle.
%endif


%if_enabled    devel
%package       -n gem-cookstyle-devel
Version:       8.5.2
Release:       alt1
Summary:       Cookstyle is a code linting tool development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета cookstyle
Group:         Development/Ruby
BuildArch:     noarch

Autoprov:      yes,noruby
Autoreq:       yes,noruby
Requires:      gem(cookstyle) = 8.5.2
Requires:      gem(appbundler) >= 0
Requires:      gem(pry) >= 0
Requires:      gem(rake) >= 0
Requires:      gem(rspec) >= 3.4
Requires:      gem(rubocop) >= 1.15.0
Conflicts:     gem(rubocop) >= 2

%description   -n gem-cookstyle-devel
Cookstyle is a code linting tool development package.

Cookstyle is a code linting tool that helps you to write better Chef Infra
cookbooks by detecting and automatically correcting style, syntax, and logic
mistakes in your code.

%description   -n gem-cookstyle-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета cookstyle.
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
%doc LICENSE CHANGELOG.md CODE_OF_CONDUCT.md CONTRIBUTING.md README.md
%ruby_gemspec
%ruby_gemlibdir

%files         -n cookstyle
%doc LICENSE CHANGELOG.md CODE_OF_CONDUCT.md CONTRIBUTING.md README.md
%_bindir/cookstyle

%if_enabled    doc
%files         -n gem-cookstyle-doc
%doc LICENSE CHANGELOG.md CODE_OF_CONDUCT.md CONTRIBUTING.md README.md
%ruby_gemdocdir
%endif

%if_enabled    devel
%files         -n gem-cookstyle-devel
%doc LICENSE CHANGELOG.md CODE_OF_CONDUCT.md CONTRIBUTING.md README.md
%endif


%changelog
* Sat Nov 22 2025 Pavel Skrylev <majioa@altlinux.org> 8.5.2-alt1
- ^ 7.32.11 -> 8.5.2

* Mon Oct 28 2024 Pavel Skrylev <majioa@altlinux.org> 7.32.11-alt1
- ^ 7.32.1 -> 7.32.11

* Sat Oct 29 2022 Pavel Skrylev <majioa@altlinux.org> 7.32.1-alt1
- + packaged gem with Ruby Policy 2.0
