%define        _unpackaged_files_terminate_build 1
%define        gemname create_github_release

Name:          gem-create-github-release
Version:       1.0.0
Release:       alt1
Summary:       A script to create a GitHub release for a Ruby Gem
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/main-branch/create_github_release
Vcs:           https://github.com/main-branch/create_github_release.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
%if_with check
BuildRequires: gem(bump) >= 0.10
BuildRequires: gem(bundler-audit) >= 0.9
BuildRequires: gem(rake) >= 13.0
BuildRequires: gem(redcarpet) >= 3.5
BuildRequires: gem(rspec) >= 3.10
BuildRequires: gem(rubocop) >= 1.15.0
BuildRequires: gem(simplecov) >= 0.17
BuildRequires: gem(simplecov-lcov) >= 0.8
BuildRequires: gem(solargraph) >= 0.47
BuildRequires: gem(timecop) >= 0.9
BuildRequires: gem(yard) >= 0.9
BuildRequires: gem(yardstick) >= 0.9
BuildConflicts: gem(bump) >= 1
BuildConflicts: gem(bundler-audit) >= 1
BuildConflicts: gem(rake) >= 14
BuildConflicts: gem(redcarpet) >= 4
BuildConflicts: gem(rspec) >= 4
BuildConflicts: gem(rubocop) >= 2
BuildConflicts: gem(simplecov) >= 1
BuildConflicts: gem(simplecov-lcov) >= 1
BuildConflicts: gem(solargraph) >= 1
BuildConflicts: gem(timecop) >= 1
BuildConflicts: gem(yard) >= 1
BuildConflicts: gem(yardstick) >= 1
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_use_gem_dependency rubocop >= 1.15.0,rubocop < 2
%ruby_use_gem_dependency simplecov >= 0.17,simplecov < 1
Provides:      gem(create_github_release) = 1.0.0


%description
A script that manages your gem version and creates a GitHub branch, PR, and
release for a new gem version.


%package       -n create-github-release
Version:       1.0.0
Release:       alt1
Summary:       A script to create a GitHub release for a Ruby Gem executable(s)
Summary(ru_RU.UTF-8): Исполнямка для самоцвета create_github_release
Group:         Other
BuildArch:     noarch

Requires:      gem(create_github_release) = 1.0.0

%description   -n create-github-release
A script to create a GitHub release for a Ruby Gem executable(s).

A script that manages your gem version and creates a GitHub branch, PR, and
release for a new gem version.

%description   -n create-github-release -l ru_RU.UTF-8
Исполнямка для самоцвета create_github_release.


%package       -n gem-create-github-release-doc
Version:       1.0.0
Release:       alt1
Summary:       A script to create a GitHub release for a Ruby Gem documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета create_github_release
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(create_github_release) = 1.0.0

%description   -n gem-create-github-release-doc
A script to create a GitHub release for a Ruby Gem documentation files.

A script that manages your gem version and creates a GitHub branch, PR, and
release for a new gem version.

%description   -n gem-create-github-release-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета create_github_release.


%package       -n gem-create-github-release-devel
Version:       1.0.0
Release:       alt1
Summary:       A script to create a GitHub release for a Ruby Gem development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета create_github_release
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(create_github_release) = 1.0.0
Requires:      gem(bump) >= 0.10
Requires:      gem(bundler-audit) >= 0.9
Requires:      gem(rake) >= 13.0
Requires:      gem(redcarpet) >= 3.5
Requires:      gem(rspec) >= 3.10
Requires:      gem(rubocop) >= 1.15.0
Requires:      gem(simplecov) >= 0.17
Requires:      gem(simplecov-lcov) >= 0.8
Requires:      gem(solargraph) >= 0.47
Requires:      gem(timecop) >= 0.9
Requires:      gem(yard) >= 0.9
Requires:      gem(yardstick) >= 0.9
Conflicts:     gem(bump) >= 1
Conflicts:     gem(bundler-audit) >= 1
Conflicts:     gem(rake) >= 14
Conflicts:     gem(redcarpet) >= 4
Conflicts:     gem(rspec) >= 4
Conflicts:     gem(rubocop) >= 2
Conflicts:     gem(simplecov) >= 1
Conflicts:     gem(simplecov-lcov) >= 1
Conflicts:     gem(solargraph) >= 1
Conflicts:     gem(timecop) >= 1
Conflicts:     gem(yard) >= 1
Conflicts:     gem(yardstick) >= 1

%description   -n gem-create-github-release-devel
A script to create a GitHub release for a Ruby Gem development package.

A script that manages your gem version and creates a GitHub branch, PR, and
release for a new gem version.

%description   -n gem-create-github-release-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета create_github_release.


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

%files         -n create-github-release
%doc README.md
%_bindir/create-github-release

%files         -n gem-create-github-release-doc
%doc README.md
%ruby_gemdocdir

%files         -n gem-create-github-release-devel
%doc README.md


%changelog
* Wed Jun 21 2023 Pavel Skrylev <majioa@altlinux.org> 1.0.0-alt1
- + packaged gem with Ruby Policy 2.0
