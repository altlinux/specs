%define        gemname rspec-rails

Name:          gem-rspec-rails
Version:       5.1.2
Release:       alt1
Summary:       RSpec for Rails
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/rspec/rspec-rails
Vcs:           https://github.com/rspec/rspec-rails.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
%if_with check
BuildRequires: gem(ammeter) >= 1.1.5
BuildRequires: gem(aruba) >= 0.14.12
BuildRequires: gem(cucumber) > 4.0.0
BuildRequires: gem(yard) >= 0.9.24
BuildRequires: gem(github-markup) >= 3.0.3
BuildRequires: gem(redcarpet) >= 3.5.1
BuildRequires: gem(relish) >= 0.7.1
BuildRequires: gem(rake) > 12
BuildRequires: gem(rubocop) >= 0.80.1
BuildRequires: gem(capybara) >= 0
BuildRequires: gem(ffi) >= 1.15.5
BuildRequires: gem(sqlite3) >= 1.4
BuildRequires: gem(rails) >= 6.0.0
BuildRequires: gem(puma) >= 0
BuildRequires: gem(selenium-webdriver) >= 0
BuildRequires: gem(actionpack) >= 5.2
BuildRequires: gem(activesupport) >= 5.2
BuildRequires: gem(railties) >= 5.2
BuildRequires: gem(rspec-core) >= 3.10
BuildRequires: gem(rspec-expectations) >= 3.10
BuildRequires: gem(rspec-mocks) >= 3.10
BuildRequires: gem(rspec-support) >= 3.10
BuildConflicts: gem(ammeter) >= 1.2
BuildConflicts: gem(aruba) >= 0.15
BuildConflicts: gem(cucumber) >= 8.0.0
BuildConflicts: gem(yard) >= 0.10
BuildConflicts: gem(github-markup) >= 3.1
BuildConflicts: gem(redcarpet) >= 3.6
BuildConflicts: gem(relish) >= 0.8
BuildConflicts: gem(rubocop) >= 2
BuildConflicts: gem(ffi) >= 1.16
BuildConflicts: gem(sqlite3) >= 2
BuildConflicts: gem(rails) >= 7
BuildConflicts: gem(rspec-core) >= 4
BuildConflicts: gem(rspec-expectations) >= 4
BuildConflicts: gem(rspec-mocks) >= 4
BuildConflicts: gem(rspec-support) >= 4
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_use_gem_dependency rubocop >= 1.15.0,rubocop < 2
%ruby_use_gem_dependency rails >= 6.1.3.2,rails < 7
Requires:      gem(actionpack) >= 5.2
Requires:      gem(activesupport) >= 5.2
Requires:      gem(railties) >= 5.2
Requires:      gem(rspec-core) >= 3.10
Requires:      gem(rspec-expectations) >= 3.10
Requires:      gem(rspec-mocks) >= 3.10
Requires:      gem(rspec-support) >= 3.10
Conflicts:     gem(rspec-core) >= 4
Conflicts:     gem(rspec-expectations) >= 4
Conflicts:     gem(rspec-mocks) >= 4
Conflicts:     gem(rspec-support) >= 4
Provides:      gem(rspec-rails) = 5.1.2


%description
rspec-rails is a testing framework for Rails 5+.


%package       -n gem-rspec-rails-doc
Version:       5.1.2
Release:       alt1
Summary:       RSpec for Rails documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета rspec-rails
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(rspec-rails) = 5.1.2

%description   -n gem-rspec-rails-doc
RSpec for Rails documentation files.

rspec-rails is a testing framework for Rails 5+.

%description   -n gem-rspec-rails-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета rspec-rails.


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

%files         -n gem-rspec-rails-doc
%doc README.md
%ruby_gemdocdir


%changelog
* Thu Jan 26 2023 Pavel Skrylev <majioa@altlinux.org> 5.1.2-alt1
- ^ 5.0.1 -> 5.1.2 (no devel)

* Mon Jun 21 2021 Pavel Skrylev <majioa@altlinux.org> 5.0.1-alt1
- + packaged gem with Ruby Policy 2.0
