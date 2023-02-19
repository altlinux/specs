%define        gemname rubocop-capybara

Name:          gem-rubocop-capybara
Version:       2.17.0
Release:       alt1
Summary:       Code style checking for Capybara test files
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/rubocop/rubocop-capybara
Vcs:           https://github.com/rubocop/rubocop-capybara.git
Packager:      Pavel Skrylev <majioa@altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
%if_with check
BuildRequires: gem(bump) >= 0
BuildRequires: gem(rack) >= 0
BuildRequires: gem(rake) >= 0
BuildRequires: gem(rspec) >= 3.10.0
BuildRequires: gem(rubocop-performance) >= 1.7
BuildRequires: gem(rubocop-rake) >= 0.6
BuildRequires: gem(rubocop-rspec) >= 2.4.0
BuildRequires: gem(yard) >= 0
BuildRequires: gem(rubocop) >= 1.15.0
BuildConflicts: gem(rspec) >= 4
BuildConflicts: gem(rubocop-performance) >= 2
BuildConflicts: gem(rubocop-rake) >= 1
BuildConflicts: gem(rubocop-rspec) >= 3
BuildConflicts: gem(rubocop) >= 2
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_use_gem_dependency rubocop >= 1.15.0,rubocop < 2
%ruby_use_gem_dependency rspec >= 3.10.0,rspec < 4
%ruby_use_gem_dependency rubocop-rspec >= 2.4.0,rubocop-rspec < 3
Requires:      gem(rubocop) >= 1.15.0
Conflicts:     gem(rubocop) >= 2
Provides:      gem(rubocop-capybara) = 2.17.0


%description
Code style checking for Capybara test files (RSpec, Cucumber, Minitest). A
plugin for the RuboCop code style enforcing & linting tool.


%package       -n gem-rubocop-capybara-doc
Version:       2.17.0
Release:       alt1
Summary:       Code style checking for Capybara test files documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета rubocop-capybara
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(rubocop-capybara) = 2.17.0

%description   -n gem-rubocop-capybara-doc
Code style checking for Capybara test files documentation files.

Code style checking for Capybara test files (RSpec, Cucumber, Minitest). A
plugin for the RuboCop code style enforcing & linting tool.

%description   -n gem-rubocop-capybara-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета rubocop-capybara.


%package       -n gem-rubocop-capybara-devel
Version:       2.17.0
Release:       alt1
Summary:       Code style checking for Capybara test files development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета rubocop-capybara
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(rubocop-capybara) = 2.17.0
Requires:      gem(bump) >= 0
Requires:      gem(rack) >= 0
Requires:      gem(rake) >= 0
Requires:      gem(rspec) >= 3.10.0
Requires:      gem(rubocop-performance) >= 1.7
Requires:      gem(rubocop-rake) >= 0.6
Requires:      gem(rubocop-rspec) >= 2.4.0
Requires:      gem(yard) >= 0
Conflicts:     gem(rspec) >= 4
Conflicts:     gem(rubocop-performance) >= 2
Conflicts:     gem(rubocop-rake) >= 1
Conflicts:     gem(rubocop-rspec) >= 3

%description   -n gem-rubocop-capybara-devel
Code style checking for Capybara test files development package.

Code style checking for Capybara test files (RSpec, Cucumber, Minitest). A
plugin for the RuboCop code style enforcing & linting tool.

%description   -n gem-rubocop-capybara-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета rubocop-capybara.


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

%files         -n gem-rubocop-capybara-doc
%doc README.md
%ruby_gemdocdir

%files         -n gem-rubocop-capybara-devel
%doc README.md


%changelog
* Thu Jan 26 2023 Pavel Skrylev <majioa@altlinux.org> 2.17.0-alt1
- + packaged gem with Ruby Policy 2.0
