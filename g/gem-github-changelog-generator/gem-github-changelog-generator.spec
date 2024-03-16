%define        _unpackaged_files_terminate_build 1
%def_enable    check
%def_enable    doc
%def_enable    devel
%define        gemname github_changelog_generator

Name:          gem-github-changelog-generator
Version:       1.16.4.37
Release:       alt0.1
Summary:       Script that automatically generates a changelog from your tags, issues, labels and pull requests
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/github-changelog-generator/Github-Changelog-Generator
Vcs:           https://github.com/github-changelog-generator/github-changelog-generator.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
Patch:         octokit.patch
BuildRequires(pre): rpm-build-ruby
%if_enabled check
BuildRequires: gem(bundler) >= 0
BuildRequires: gem(overcommit) >= 0.60
BuildRequires: gem(rake) >= 10.0
BuildRequires: gem(rubocop) >= 1.15.0
BuildRequires: gem(rubocop-performance) >= 0
BuildRequires: gem(yard-junk) >= 0
BuildRequires: gem(bump) >= 0
BuildRequires: gem(codeclimate-test-reporter) >= 1.0
BuildRequires: gem(json) >= 0
BuildRequires: gem(rspec_junit_formatter) >= 0
BuildRequires: gem(simplecov) >= 0.10
BuildRequires: gem(vcr) >= 6
BuildRequires: gem(webmock) >= 0
BuildRequires: gem(activesupport) >= 0
BuildRequires: gem(async) >= 1.25.0
BuildRequires: gem(async-http-faraday) >= 0
BuildRequires: gem(faraday-http-cache) >= 0
BuildRequires: gem(octokit) >= 4.6
BuildRequires: gem(rainbow) >= 2.2.1
BuildConflicts: gem(codeclimate-test-reporter) >= 2
BuildConflicts: gem(rspec) >= 4
BuildConflicts: gem(simplecov) >= 1
BuildConflicts: gem(vcr) >= 7
BuildConflicts: gem(octokit) >= 9
%endif
%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_use_gem_dependency octokit >= 5.6.1,octokit < 9
%ruby_use_gem_dependency rubocop >= 1.15.0,rubocop < 2
%ruby_alias_names github_changelog_generator,github-changelog-generator
Requires:      gem(rake) >= 10.0
Requires:      gem(activesupport) >= 0
Requires:      gem(async) >= 1.25.0
Requires:      gem(async-http-faraday) >= 0
Requires:      gem(faraday-http-cache) >= 0
Requires:      gem(octokit) >= 4.6
Requires:      gem(rainbow) >= 2.2.1
Conflicts:     gem(octokit) >= 9
Provides:      gem(github_changelog_generator) = 1.16.4.37

%ruby_use_gem_version github_changelog_generator:1.16.4.37

%description
Changelog generation has never been so easy. Fully automate changelog
generation
- this gem generate changelog file based on tags, issues and merged pull
requests from GitHub.


%package       -n changelog-generator
Version:       1.16.4.37
Release:       alt0.1
Summary:       Script that automatically generates a changelog from your tags, issues, labels and pull requests executable(s)
Summary(ru_RU.UTF-8): Исполнямка для самоцвета github_changelog_generator
Group:         Other
BuildArch:     noarch

Requires:      gem(github_changelog_generator) = 1.16.4.37

%description   -n changelog-generator
Script that automatically generates a changelog from your tags, issues, labels
and pull requests executable(s).

Changelog generation has never been so easy. Fully automate changelog
generation
- this gem generate changelog file based on tags, issues and merged pull
requests from GitHub.

%description   -n changelog-generator -l ru_RU.UTF-8
Исполнямка для самоцвета github_changelog_generator.


%if_enabled    doc
%package       -n gem-github-changelog-generator-doc
Version:       1.16.4.37
Release:       alt0.1
Summary:       Script that automatically generates a changelog from your tags, issues, labels and pull requests documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета github_changelog_generator
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(github_changelog_generator) = 1.16.4.37

%description   -n gem-github-changelog-generator-doc
Script that automatically generates a changelog from your tags, issues, labels
and pull requests documentation files.

Changelog generation has never been so easy. Fully automate changelog
generation
- this gem generate changelog file based on tags, issues and merged pull
requests from GitHub.

%description   -n gem-github-changelog-generator-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета github_changelog_generator.
%endif


%if_enabled    devel
%package       -n gem-github-changelog-generator-devel
Version:       1.16.4.37
Release:       alt0.1
Summary:       Script that automatically generates a changelog from your tags, issues, labels and pull requests development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета github_changelog_generator
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(github_changelog_generator) = 1.16.4.37
Requires:      gem(bundler) >= 0
Requires:      gem(overcommit) >= 0.60
Requires:      gem(rubocop) >= 1.15.0
Requires:      gem(rubocop-performance) >= 0
Requires:      gem(yard-junk) >= 0
Requires:      gem(bump) >= 0
Requires:      gem(codeclimate-test-reporter) >= 1.0
Requires:      gem(json) >= 0
Requires:      gem(rspec_junit_formatter) >= 0
Requires:      gem(simplecov) >= 0.10
Requires:      gem(vcr) >= 6
Requires:      gem(webmock) >= 0
Conflicts:     gem(codeclimate-test-reporter) >= 2
Conflicts:     gem(rspec) >= 4
Conflicts:     gem(simplecov) >= 1
Conflicts:     gem(vcr) >= 7

%description   -n gem-github-changelog-generator-devel
Script that automatically generates a changelog from your tags, issues, labels
and pull requests development package.

Changelog generation has never been so easy. Fully automate changelog
generation
- this gem generate changelog file based on tags, issues and merged pull
requests from GitHub.

%description   -n gem-github-changelog-generator-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета github_changelog_generator.
%endif


%prep
%setup
%autopatch

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

%files         -n changelog-generator
%doc README.md
%_bindir/git-generate-changelog
%_bindir/github_changelog_generator
%_mandir/git-generate-changelog.1.xz

%if_enabled    doc
%files         -n gem-github-changelog-generator-doc
%doc README.md
%ruby_gemdocdir
%endif

%if_enabled    devel
%files         -n gem-github-changelog-generator-devel
%doc README.md
%endif


%changelog
* Thu Mar 14 2024 Pavel Skrylev <majioa@altlinux.org> 1.16.4.37-alt0.1
- ^ 1.16.4 -> 1.16.4p37
- ! fixed deprecated octokit preview constant (closes #49693)

* Wed Dec 20 2023 Pavel Skrylev <majioa@altlinux.org> 1.16.4-alt1
- + packaged gem with Ruby Policy 2.0
