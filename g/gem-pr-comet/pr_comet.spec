%define        _unpackaged_files_terminate_build 1
%def_enable    check
%def_enable    doc
%def_enable    devel
%define        gemname pr_comet

Name:          gem-pr-comet
Version:       0.7.0
Release:       alt1
Summary:       Create a lots of pull request like comets
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/ryz310/pr_comet
Vcs:           https://github.com/ryz310/pr_comet.git
Packager:      Pavel Skrylev <majioa@altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
Autoprov:      yes,noruby
Autoreq:       yes,noruby
BuildRequires(pre): rpm-build-ruby
%if_enabled check
BuildRequires: gem(bundler) >= 2.2
BuildRequires: gem(octokit) >= 0
BuildRequires: gem(pry-byebug) >= 0
BuildRequires: gem(rainbow) >= 0
BuildRequires: gem(rake) >= 13.0
BuildRequires: gem(rspec) >= 0
BuildRequires: gem(rspec_junit_formatter) >= 0
BuildRequires: gem(rubocop) >= 0
BuildRequires: gem(rubocop-performance) >= 0
BuildRequires: gem(rubocop-rspec) >= 0
BuildRequires: gem(simplecov) >= 0.22.0
BuildRequires: gem(yard) >= 0
BuildConflicts: gem(bundler) >= 3
BuildConflicts: gem(rake) >= 14
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_alias_names pr_comet,pr-comet
%ruby_use_gem_dependency simplecov >= 0.22,simplecov < 1
Requires:      ruby >= 2.7.0
Requires:      gem(octokit) >= 0
Requires:      gem(rainbow) >= 0
Provides:      gem(pr_comet) = 0.7.0

%description
It helps to create a pull request on your script


%if_enabled    doc
%package       -n gem-pr-comet-doc
Version:       0.7.0
Release:       alt1
Summary:       Create a lots of pull request like comets documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета pr_comet
Group:         Development/Documentation
BuildArch:     noarch

Autoprov:      yes,noruby
Autoreq:       yes,noruby
Requires:      gem(pr_comet) = 0.7.0

%description   -n gem-pr-comet-doc
Create a lots of pull request like comets documentation files.

It helps to create a pull request on your script

%description   -n gem-pr-comet-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета pr_comet.
%endif


%if_enabled    devel
%package       -n gem-pr-comet-devel
Version:       0.7.0
Release:       alt1
Summary:       Create a lots of pull request like comets development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета pr_comet
Group:         Development/Ruby
BuildArch:     noarch

Autoprov:      yes,noruby
Autoreq:       yes,noruby
Requires:      gem(pr_comet) = 0.7.0
Requires:      gem(bundler) >= 2.2
Requires:      gem(pry-byebug) >= 0
Requires:      gem(rake) >= 13.0
Requires:      gem(rspec) >= 0
Requires:      gem(rspec_junit_formatter) >= 0
Requires:      gem(rubocop) >= 0
Requires:      gem(rubocop-performance) >= 0
Requires:      gem(rubocop-rspec) >= 0
Requires:      gem(simplecov) >= 0.22.0
Requires:      gem(yard) >= 0
Conflicts:     gem(bundler) >= 3
Conflicts:     gem(rake) >= 14

%description   -n gem-pr-comet-devel
Create a lots of pull request like comets development package.

It helps to create a pull request on your script

%description   -n gem-pr-comet-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета pr_comet.
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
%doc CHANGELOG.md CODE_OF_CONDUCT.md LICENSE.txt README.md
%ruby_gemspec
%ruby_gemlibdir

%if_enabled    doc
%files         -n gem-pr-comet-doc
%doc CHANGELOG.md CODE_OF_CONDUCT.md LICENSE.txt README.md
%ruby_gemdocdir
%endif

%if_enabled    devel
%files         -n gem-pr-comet-devel
%doc CHANGELOG.md CODE_OF_CONDUCT.md LICENSE.txt README.md
%endif


%changelog
* Wed Nov 05 2025 Pavel Skrylev <majioa@altlinux.org> 0.7.0-alt1
- + packaged gem with Ruby Policy 2.0
- * define explicit dependencies
