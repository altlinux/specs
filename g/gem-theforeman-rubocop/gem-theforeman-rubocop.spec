%define        _unpackaged_files_terminate_build 1
%def_disable   check
%def_enable    doc
%def_enable    devel
%define        gemname theforeman-rubocop

Name:          gem-theforeman-rubocop
Version:       0.1.2
Release:       alt1.1
Summary:       Shared Rubocop configuration for theforeman.org family of projects
License:       GPL-3.0
Group:         Development/Ruby
Url:           https://github.com/theforeman/theforeman-rubocop
Vcs:           https://github.com/theforeman/theforeman-rubocop.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
%if_enabled check
BuildRequires: gem(rubocop) >= 1.15.0
BuildRequires: gem(rubocop-checkstyle_formatter) >= 0.6.0
BuildRequires: gem(rubocop-graphql) >= 1.4.0
BuildRequires: gem(rubocop-minitest) >= 0.13.0
BuildRequires: gem(rubocop-performance) >= 1.11.3
BuildRequires: gem(rubocop-rails) >= 2.11.0
BuildRequires: gem(rubocop-rspec) >= 2.4.0
BuildRequires: gem(bundler) >= 2.1.4
BuildRequires: gem(rake) >= 13.0
BuildConflicts: gem(rubocop) >= 2
BuildConflicts: gem(rubocop-checkstyle_formatter) >= 0.7
BuildConflicts: gem(rubocop-graphql) >= 2
BuildConflicts: gem(rubocop-minitest) >= 1
BuildConflicts: gem(rubocop-performance) >= 2
BuildConflicts: gem(rubocop-rails) >= 3
BuildConflicts: gem(rubocop-rspec) >= 3
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_use_gem_dependency bundler >= 2.1.4,bundler < 3
%ruby_use_gem_dependency rake >= 13.1.0,rake < 14
%ruby_use_gem_dependency rubocop >= 1.15.0,rubocop < 2
%ruby_use_gem_dependency rubocop-rspec >= 2.4.0,rubocop-rspec < 3
%ruby_use_gem_dependency rubocop-minitest >= 0.13.0,rubocop-minitest < 1
%ruby_use_gem_dependency rubocop-rails >= 2.11.0,rubocop-rails < 3
%ruby_use_gem_dependency rubocop-performance >= 1.11.3,rubocop-performance < 2
%ruby_use_gem_dependency rubocop-graphql >= 1.5,rubocop-graphql < 2
%ruby_use_gem_dependency rubocop-checkstyle_formatter >= 0.6,rubocop-checkstyle_formatter < 1
Requires:      gem(rubocop) >= 1.15.0
Requires:      gem(rubocop-checkstyle_formatter) >= 0.6.0
Requires:      gem(rubocop-graphql) >= 1.4.0
Requires:      gem(rubocop-minitest) >= 0.13.0
Requires:      gem(rubocop-performance) >= 1.11.3
Requires:      gem(rubocop-rails) >= 2.11.0
Requires:      gem(rubocop-rspec) >= 2.4.0
Conflicts:     gem(rubocop) >= 2
Conflicts:     gem(rubocop-checkstyle_formatter) >= 0.7
Conflicts:     gem(rubocop-graphql) >= 2
Conflicts:     gem(rubocop-minitest) >= 1
Conflicts:     gem(rubocop-performance) >= 2
Conflicts:     gem(rubocop-rails) >= 3
Conflicts:     gem(rubocop-rspec) >= 3
Provides:      gem(theforeman-rubocop) = 0.1.2


%description
Shared Rubocop configuration for theforeman.org family of projects.


%if_enabled    doc
%package       -n gem-theforeman-rubocop-doc
Version:       0.1.2
Release:       alt1.1
Summary:       Shared Rubocop configuration for theforeman.org family of projects documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета theforeman-rubocop
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(theforeman-rubocop) = 0.1.2

%description   -n gem-theforeman-rubocop-doc
Shared Rubocop configuration for theforeman.org family of projects documentation
files.

%description   -n gem-theforeman-rubocop-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета theforeman-rubocop.
%endif


%if_enabled    devel
%package       -n gem-theforeman-rubocop-devel
Version:       0.1.2
Release:       alt1.1
Summary:       Shared Rubocop configuration for theforeman.org family of projects development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета theforeman-rubocop
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(theforeman-rubocop) = 0.1.2
Requires:      gem(bundler) >= 2.1.4
Requires:      gem(rake) >= 13.0

%description   -n gem-theforeman-rubocop-devel
Shared Rubocop configuration for theforeman.org family of projects development
package.

%description   -n gem-theforeman-rubocop-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета theforeman-rubocop.
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
%doc README.md
%ruby_gemspec
%ruby_gemlibdir

%if_enabled    doc
%files         -n gem-theforeman-rubocop-doc
%doc README.md
%ruby_gemdocdir
%endif

%if_enabled    devel
%files         -n gem-theforeman-rubocop-devel
%doc README.md
%endif


%changelog
* Tue Jan 14 2025 Pavel Skrylev <majioa@altlinux.org> 0.1.2-alt1.1
- ! fixed dep to rubocop-checkstyle_formatter gem

* Tue Oct 01 2024 Pavel Skrylev <majioa@altlinux.org> 0.1.2-alt1
- ^ 0.0.6 -> 0.1.2

* Wed Jun 23 2021 Pavel Skrylev <majioa@altlinux.org> 0.0.6-alt1
- + packaged gem with Ruby Policy 2.0
