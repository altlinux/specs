%define        _unpackaged_files_terminate_build 1
%define        gemname version_gem

Name:          gem-version-gem
Version:       1.1.3
Release:       alt1
Summary:       Enhance your VERSION! Sugar for Version modules
License:       MIT
Group:         Development/Ruby
Url:           https://gitlab.com/oauth-xx/version_gem
Vcs:           https://gitlab.com/oauth-xx/version_gem/-/tree/v1.1.1.git
Packager:      Pavel Skrylev <majioa@altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
%if_with check
BuildRequires: gem(rspec) >= 3.10.0
BuildRequires: gem(rspec-block_is_expected) >= 1.0
BuildRequires: gem(rake) >= 13.0
BuildRequires: gem(pry) >= 0.13.1
BuildRequires: gem(simplecov) >= 0.17
BuildRequires: gem(simplecov-cobertura) >= 0
BuildRequires: gem(simplecov-json) >= 0.2
BuildRequires: gem(simplecov-lcov) >= 0.8
BuildRequires: gem(rubocop-lts) >= 8.1
BuildRequires: gem(rubocop-rspec) >= 2.4.0
BuildRequires: gem(rubocop-packaging) >= 0.5
BuildRequires: gem(rubocop-ruby2_2) >= 2.0
BuildRequires: gem(standard-rubocop-lts) >= 1.0
BuildRequires: gem(yard) >= 0.9
BuildRequires: gem(yard-junk) >= 0.0
BuildRequires: gem(redcarpet) >= 3.6
BuildRequires: gem(pry-suite) >= 1.2
BuildConflicts: gem(rspec) >= 4
BuildConflicts: gem(rspec-block_is_expected) >= 2
BuildConflicts: gem(rake) >= 14
BuildConflicts: gem(pry) >= 1
BuildConflicts: gem(simplecov) >= 1
BuildConflicts: gem(simplecov-json) >= 1
BuildConflicts: gem(simplecov-lcov) >= 1
BuildConflicts: gem(rubocop-lts) >= 9
BuildConflicts: gem(rubocop-rspec) >= 3
BuildConflicts: gem(rubocop-packaging) >= 1
BuildConflicts: gem(rubocop-ruby2_2) >= 3
BuildConflicts: gem(standard-rubocop-lts) >= 2
BuildConflicts: gem(yard-junk) >= 1
BuildConflicts: gem(redcarpet) >= 4
BuildConflicts: gem(pry-suite) >= 2
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_use_gem_dependency simplecov >= 0.17,simplecov < 1
%ruby_use_gem_dependency pry >= 0.13.1,pry < 1
%ruby_use_gem_dependency rspec >= 3.10.0,rspec < 4
%ruby_use_gem_dependency rubocop-rspec >= 2.4.0,rubocop-rspec < 3
%ruby_use_gem_dependency yard >= 0.9.34,yard < 1
%ruby_alias_names version_gem,version-gem
Provides:      gem(version_gem) = 1.1.3


%description
Versions are good. Versions are cool. Versions will win.


%package       -n gem-version-gem-doc
Version:       1.1.3
Release:       alt1
Summary:       Enhance your VERSION! Sugar for Version modules documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета version_gem
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(version_gem) = 1.1.3

%description   -n gem-version-gem-doc
Enhance your VERSION! Sugar for Version modules documentation files.

Versions are good. Versions are cool. Versions will win.

%description   -n gem-version-gem-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета version_gem.


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

%files         -n gem-version-gem-doc
%doc README.md
%ruby_gemdocdir


%changelog
* Mon Dec 11 2023 Pavel Skrylev <majioa@altlinux.org> 1.1.3-alt1
- ^ 1.1.1 -> 1.1.3

* Thu Sep 29 2022 Pavel Skrylev <majioa@altlinux.org> 1.1.1-alt1
- + packaged gem with Ruby Policy 2.0
