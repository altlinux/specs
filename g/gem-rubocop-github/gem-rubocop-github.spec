%define        _unpackaged_files_terminate_build 1
%def_enable    check
%def_enable    doc
%def_enable    devel
%define        gemname rubocop-github

Name:          gem-rubocop-github
Version:       0.22.0
Release:       alt1
Summary:       RuboCop GitHub
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/github/rubocop-github
Vcs:           https://github.com/github/rubocop-github.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
BuildRequires: gem(rake) >= 0
%if_enabled check
BuildRequires: gem(actionview) >= 0
BuildRequires: gem(minitest) >= 0
BuildRequires: gem(rubocop) >= 1.15.0
BuildRequires: gem(rubocop-performance) >= 1.11.3
BuildRequires: gem(rubocop-rails) >= 2.11.0
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_use_gem_dependency rubocop >= 1.15.0,rubocop < 2
%ruby_use_gem_dependency rubocop-rails >= 2.11.0,rubocop-rails < 3
%ruby_use_gem_dependency rubocop-performance >= 1.11.3,rubocop-performance < 2
Requires:      ruby >= 3.0.0
Requires:      gem(rubocop) >= 1.15.0
Requires:      gem(rubocop-performance) >= 1.11.3
Requires:      gem(rubocop-rails) >= 2.11.0
Provides:      gem(rubocop-github) = 0.22.0

%description
Code style checking for GitHub Ruby repositories


%if_enabled    doc
%package       -n gem-rubocop-github-doc
Version:       0.22.0
Release:       alt1
Summary:       RuboCop GitHub documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета rubocop-github
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(rubocop-github) = 0.22.0

%description   -n gem-rubocop-github-doc
RuboCop GitHub documentation files.

Code style checking for GitHub Ruby repositories

%description   -n gem-rubocop-github-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета rubocop-github.
%endif


%if_enabled    devel
%package       -n gem-rubocop-github-devel
Version:       0.22.0
Release:       alt1
Summary:       RuboCop GitHub development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета rubocop-github
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(rubocop-github) = 0.22.0
Requires:      gem(actionview) >= 0
Requires:      gem(minitest) >= 0
Requires:      gem(rake) >= 0

%description   -n gem-rubocop-github-devel
RuboCop GitHub development package.

Code style checking for GitHub Ruby repositories

%description   -n gem-rubocop-github-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета rubocop-github.
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
%doc LICENSE README.md CHANGELOG.md CODE_OF_CONDUCT.md CONTRIBUTING.md
%ruby_gemspec
%ruby_gemlibdir

%if_enabled    doc
%files         -n gem-rubocop-github-doc
%doc LICENSE README.md CHANGELOG.md CODE_OF_CONDUCT.md CONTRIBUTING.md
%ruby_gemdocdir
%endif

%if_enabled    devel
%files         -n gem-rubocop-github-devel
%doc LICENSE README.md CHANGELOG.md CODE_OF_CONDUCT.md CONTRIBUTING.md
%endif


%changelog
* Mon Jan 27 2025 Pavel Skrylev <majioa@altlinux.org> 0.22.0-alt1
- + packaged gem with Ruby Policy 2.0
- * define explicit dependencies
