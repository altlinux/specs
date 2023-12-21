%define        _unpackaged_files_terminate_build 1
%define        gemname github_changelog_generator

Name:          gem-github-changelog-generator
Version:       1.16.4
Release:       alt1
Summary:       Script that automatically generates a changelog from your tags, issues, labels and pull requests
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/github-changelog-generator/Github-Changelog-Generator
Vcs:           https://github.com/github-changelog-generator/github-changelog-generator.git
Packager:      Pavel Skrylev <majioa@altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
%if_with check
BuildRequires: gem(bundler) >= 0
BuildRequires: gem(overcommit) >= 0.31
BuildRequires: gem(rake) >= 10.0
BuildRequires: gem(rubocop) >= 0.50
BuildRequires: gem(rubocop-performance) >= 0
BuildRequires: gem(yard-junk) >= 0
BuildRequires: gem(bump) >= 0
BuildRequires: gem(codeclimate-test-reporter) >= 1.0
BuildRequires: gem(json) >= 0
BuildRequires: gem(multi_json) >= 0
BuildRequires: gem(rspec_junit_formatter) >= 0
BuildRequires: gem(simplecov) >= 0.10
BuildRequires: gem(vcr) >= 0
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
BuildConflicts: gem(octokit) >= 6
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_use_gem_dependency octokit >= 5.6.1,octokit < 6
Requires:      gem(rake) >= 10.0
Requires:      gem(multi_json) >= 0
Requires:      gem(activesupport) >= 0
Requires:      gem(async) >= 1.25.0
Requires:      gem(async-http-faraday) >= 0
Requires:      gem(faraday-http-cache) >= 0
Requires:      gem(octokit) >= 4.6
Requires:      gem(rainbow) >= 2.2.1
Conflicts:     gem(octokit) >= 6
Provides:      gem(github_changelog_generator) = 1.16.4

%ruby_bindir_to %ruby_bindir

%description
Changelog generation has never been so easy. Fully automate changelog generation
- this gem generate changelog file based on tags, issues and merged pull
requests from GitHub.


%package       -n changelog-generator
Version:       1.16.4
Release:       alt1
Summary:       Script that automatically generates a changelog from your tags, issues, labels and pull requests executable(s)
Summary(ru_RU.UTF-8): Исполнямка для самоцвета github_changelog_generator
Group:         Other
BuildArch:     noarch

Requires:      gem(github_changelog_generator) = 1.16.4

%description   -n changelog-generator
Script that automatically generates a changelog from your tags, issues, labels
and pull requests executable(s).

Changelog generation has never been so easy. Fully automate changelog
generation
- this gem generate changelog file based on tags, issues and merged pull
requests from GitHub.

%description   -n changelog-generator -l ru_RU.UTF-8
Исполнямка для самоцвета github_changelog_generator.


%package       -n gem-github-changelog-generator-doc
Version:       1.16.4
Release:       alt1
Summary:       Script that automatically generates a changelog from your tags, issues, labels and pull requests documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета github_changelog_generator
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(github_changelog_generator) = 1.16.4

%description   -n gem-github-changelog-generator-doc
Script that automatically generates a changelog from your tags, issues, labels
and pull requests documentation files.

Changelog generation has never been so easy. Fully automate changelog
generation
- this gem generate changelog file based on tags, issues and merged pull
requests from GitHub.

%description   -n gem-github-changelog-generator-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета github_changelog_generator.


%package       -n gem-github-changelog-generator-devel
Version:       1.16.4
Release:       alt1
Summary:       Script that automatically generates a changelog from your tags, issues, labels and pull requests development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета github_changelog_generator
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(github_changelog_generator) = 1.16.4
Requires:      gem(bundler) >= 0
Requires:      gem(overcommit) >= 0.31
Requires:      gem(rubocop) >= 0.50
Requires:      gem(rubocop-performance) >= 0
Requires:      gem(yard-junk) >= 0
Requires:      gem(bump) >= 0
Requires:      gem(codeclimate-test-reporter) >= 1.0
Requires:      gem(json) >= 0
Requires:      gem(rspec_junit_formatter) >= 0
Requires:      gem(simplecov) >= 0.10
Requires:      gem(vcr) >= 0
Requires:      gem(webmock) >= 0
Conflicts:     gem(codeclimate-test-reporter) >= 2
Conflicts:     gem(rspec) >= 4
Conflicts:     gem(simplecov) >= 1

%description   -n gem-github-changelog-generator-devel
Script that automatically generates a changelog from your tags, issues, labels
and pull requests development package.

Changelog generation has never been so easy. Fully automate changelog
generation
- this gem generate changelog file based on tags, issues and merged pull
requests from GitHub.

%description   -n gem-github-changelog-generator-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета github_changelog_generator.


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

%files         -n changelog-generator
%doc README.md
%ruby_bindir/git-generate-changelog
%ruby_bindir/github_changelog_generator
%ruby_mandir/git-generate-changelog*

%files         -n gem-github-changelog-generator-doc
%doc README.md
%ruby_gemdocdir

%files         -n gem-github-changelog-generator-devel
%doc README.md


%changelog
* Wed Dec 20 2023 Pavel Skrylev <majioa@altlinux.org> 1.16.4-alt1
- + packaged gem with Ruby Policy 2.0
