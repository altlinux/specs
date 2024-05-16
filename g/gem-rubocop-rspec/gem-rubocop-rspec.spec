%define        _unpackaged_files_terminate_build 1
%def_enable    check
%def_enable    doc
%def_enable    devel
%define        gemname rubocop-rspec

Name:          gem-rubocop-rspec
Version:       2.29.1
Release:       alt1
Summary:       Code style checking for RSpec files
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/rubocop/rubocop-rspec
Vcs:           https://github.com/rubocop/rubocop-rspec.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
%if_enabled check
BuildRequires: gem(bump) >= 0
BuildRequires: gem(danger) >= 0
BuildRequires: gem(rack) >= 0
BuildRequires: gem(rake) >= 0
BuildRequires: gem(rspec) >= 3.10.0
BuildRequires: gem(rubocop-performance) >= 1.7
BuildRequires: gem(rubocop-rake) >= 0.6
BuildRequires: gem(simplecov) >= 0.17
BuildRequires: gem(yard) >= 0
BuildRequires: gem(rubocop) >= 1.15.0
BuildRequires: gem(rubocop-capybara) >= 2.17
BuildRequires: gem(rubocop-factory_bot) >= 2.22
BuildRequires: gem(rubocop-rspec_rails) >= 2.28
BuildConflicts: gem(rspec) >= 4
BuildConflicts: gem(rubocop-performance) >= 2
BuildConflicts: gem(rubocop-rake) >= 1
BuildConflicts: gem(rubocop) >= 2
BuildConflicts: gem(rubocop-capybara) >= 3
BuildConflicts: gem(rubocop-factory_bot) >= 3
BuildConflicts: gem(rubocop-rspec_rails) >= 3
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_use_gem_dependency rubocop >= 1.15.0,rubocop < 2
%ruby_use_gem_dependency simplecov >= 0.17,simplecov < 1
%ruby_use_gem_dependency rspec >= 3.10.0,rspec < 4
Requires:      gem(rubocop) >= 1.15.0
Requires:      gem(rubocop-capybara) >= 2.17
Requires:      gem(rubocop-factory_bot) >= 2.22
Requires:      gem(rubocop-rspec_rails) >= 2.28
Conflicts:     gem(rubocop) >= 2
Conflicts:     gem(rubocop-capybara) >= 3
Conflicts:     gem(rubocop-factory_bot) >= 3
Conflicts:     gem(rubocop-rspec_rails) >= 3
Provides:      gem(rubocop-rspec) = 2.29.1


%description
Code style checking for RSpec files. A plugin for the RuboCop code style
enforcing & linting tool.


%if_enabled    doc
%package       -n gem-rubocop-rspec-doc
Version:       2.29.1
Release:       alt1
Summary:       Code style checking for RSpec files documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета rubocop-rspec
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(rubocop-rspec) = 2.29.1

%description   -n gem-rubocop-rspec-doc
Code style checking for RSpec files documentation files.

Code style checking for RSpec files. A plugin for the RuboCop code style
enforcing & linting tool.

%description   -n gem-rubocop-rspec-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета rubocop-rspec.
%endif


%if_enabled    devel
%package       -n gem-rubocop-rspec-devel
Version:       2.29.1
Release:       alt1
Summary:       Code style checking for RSpec files development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета rubocop-rspec
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(rubocop-rspec) = 2.29.1
Requires:      gem(bump) >= 0
Requires:      gem(danger) >= 0
Requires:      gem(rack) >= 0
Requires:      gem(rake) >= 0
Requires:      gem(rspec) >= 3.10.0
Requires:      gem(rubocop-performance) >= 1.7
Requires:      gem(rubocop-rake) >= 0.6
Requires:      gem(simplecov) >= 0.17
Requires:      gem(yard) >= 0
Conflicts:     gem(rspec) >= 4
Conflicts:     gem(rubocop-performance) >= 2
Conflicts:     gem(rubocop-rake) >= 1

%description   -n gem-rubocop-rspec-devel
Code style checking for RSpec files development package.

Code style checking for RSpec files. A plugin for the RuboCop code style
enforcing & linting tool.

%description   -n gem-rubocop-rspec-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета rubocop-rspec.
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
%files         -n gem-rubocop-rspec-doc
%doc README.md
%ruby_gemdocdir
%endif

%if_enabled    devel
%files         -n gem-rubocop-rspec-devel
%doc README.md
%endif


%changelog
* Mon Apr 15 2024 Pavel Skrylev <majioa@altlinux.org> 2.29.1-alt1
- ^ 2.18.1 -> 2.29.1

* Wed Jan 25 2023 Pavel Skrylev <majioa@altlinux.org> 2.18.1-alt1
- ^ 2.4.0 -> 2.18.1

* Wed Jun 23 2021 Pavel Skrylev <majioa@altlinux.org> 2.4.0-alt1
- + packaged gem with Ruby Policy 2.0
