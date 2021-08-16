%define        gemname theforeman-rubocop

Name:          gem-theforeman-rubocop
Version:       0.0.6
Release:       alt1
Summary:       Shared Rubocop configuration for theforeman.org family of projects
License:       GPL-3.0
Group:         Development/Ruby
Url:           https://github.com/theforeman/theforeman-rubocop
Vcs:           https://github.com/theforeman/theforeman-rubocop.git
Packager:      Pavel Skrylev <majioa@altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
BuildRequires: gem(rubocop) >= 0.89.0 gem(rubocop) < 2
BuildRequires: gem(rubocop-checkstyle_formatter) >= 0.4.0 gem(rubocop-checkstyle_formatter) < 0.5
BuildRequires: gem(rubocop-rspec) >= 1.43.2 gem(rubocop-rspec) < 3
BuildRequires: gem(rubocop-minitest) >= 0.10.1 gem(rubocop-minitest) < 1
BuildRequires: gem(rubocop-performance) >= 1.8.1 gem(rubocop-performance) < 2
BuildRequires: gem(rubocop-rails) >= 2.8.1 gem(rubocop-rails) < 3
BuildRequires: gem(bundler) >= 2.1 gem(bundler) < 3
BuildRequires: gem(rake) >= 13.0 gem(rake) < 14

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_use_gem_dependency rubocop >= 1.13.0,rubocop < 2
%ruby_use_gem_dependency rubocop-rspec >= 2.4.0,rubocop-rspec < 3
%ruby_use_gem_dependency rubocop-minitest >= 0.13.0,rubocop-minitest < 1
%ruby_use_gem_dependency rubocop-rails >= 2.11.0,rubocop-rails < 3
%ruby_use_gem_dependency rubocop-performance >= 1.11.3,rubocop-performance < 2
Requires:      gem(rubocop) >= 0.89.0 gem(rubocop) < 2
Requires:      gem(rubocop-checkstyle_formatter) >= 0.4.0 gem(rubocop-checkstyle_formatter) < 0.5
Requires:      gem(rubocop-rspec) >= 1.43.2 gem(rubocop-rspec) < 3
Requires:      gem(rubocop-minitest) >= 0.10.1 gem(rubocop-minitest) < 1
Requires:      gem(rubocop-performance) >= 1.8.1 gem(rubocop-performance) < 2
Requires:      gem(rubocop-rails) >= 2.8.1 gem(rubocop-rails) < 3
Provides:      gem(theforeman-rubocop) = 0.0.6

%description
Shared Rubocop configuration for theforeman.org family of projects.


%package       -n gem-theforeman-rubocop-doc
Version:       0.0.6
Release:       alt1
Summary:       Shared Rubocop configuration for theforeman.org family of projects documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета theforeman-rubocop
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(theforeman-rubocop) = 0.0.6

%description   -n gem-theforeman-rubocop-doc
Shared Rubocop configuration for theforeman.org family of projects documentation
files.

%description   -n gem-theforeman-rubocop-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета theforeman-rubocop.


%package       -n gem-theforeman-rubocop-devel
Version:       0.0.6
Release:       alt1
Summary:       Shared Rubocop configuration for theforeman.org family of projects development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета theforeman-rubocop
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(theforeman-rubocop) = 0.0.6
Requires:      gem(bundler) >= 2.1 gem(bundler) < 3
Requires:      gem(rake) >= 13.0 gem(rake) < 14

%description   -n gem-theforeman-rubocop-devel
Shared Rubocop configuration for theforeman.org family of projects development
package.

%description   -n gem-theforeman-rubocop-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета theforeman-rubocop.


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

%files         -n gem-theforeman-rubocop-doc
%doc README.md
%ruby_gemdocdir

%files         -n gem-theforeman-rubocop-devel
%doc README.md


%changelog
* Wed Jun 23 2021 Pavel Skrylev <majioa@altlinux.org> 0.0.6-alt1
- + packaged gem with Ruby Policy 2.0
