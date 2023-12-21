%define        _unpackaged_files_terminate_build 1
%define        gemname saharspec

Name:          gem-saharspec
Version:       0.0.10
Release:       alt1
Summary:       Several additions for DRYer RSpec code
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/zverok/saharspec
Vcs:           https://github.com/zverok/saharspec.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
%if_with check
BuildRequires: gem(rubocop) >= 0.93
BuildRequires: gem(rspec) >= 3.7.0
BuildRequires: gem(rspec-its) >= 0
BuildRequires: gem(simplecov) >= 0.9
BuildRequires: gem(rake) >= 0
BuildRequires: gem(rubygems-tasks) >= 0
BuildRequires: gem(yard) >= 0
BuildRequires: gem(ruby2_keywords) >= 0
BuildConflicts: gem(rubocop) >= 2
BuildConflicts: gem(simplecov) >= 1
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_use_gem_dependency rubocop >= 1.15.0,rubocop < 2
Requires:      gem(ruby2_keywords) >= 0
Provides:      gem(saharspec) = 0.0.10


%description
Several additions for DRYer RSpec code


%package       -n gem-saharspec-doc
Version:       0.0.10
Release:       alt1
Summary:       Several additions for DRYer RSpec code documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета saharspec
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(saharspec) = 0.0.10

%description   -n gem-saharspec-doc
Several additions for DRYer RSpec code documentation files.

%description   -n gem-saharspec-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета saharspec.


%package       -n gem-saharspec-devel
Version:       0.0.10
Release:       alt1
Summary:       Several additions for DRYer RSpec code development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета saharspec
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(saharspec) = 0.0.10
Requires:      gem(rubocop) >= 0.93
Requires:      gem(rspec) >= 3.7.0
Requires:      gem(rspec-its) >= 0
Requires:      gem(simplecov) >= 0.9
Requires:      gem(rake) >= 0
Requires:      gem(rubygems-tasks) >= 0
Requires:      gem(yard) >= 0
Conflicts:     gem(rubocop) >= 2
Conflicts:     gem(simplecov) >= 1

%description   -n gem-saharspec-devel
Several additions for DRYer RSpec code development package.

%description   -n gem-saharspec-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета saharspec.


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

%files         -n gem-saharspec-doc
%doc README.md
%ruby_gemdocdir

%files         -n gem-saharspec-devel
%doc README.md


%changelog
* Wed Dec 20 2023 Pavel Skrylev <majioa@altlinux.org> 0.0.10-alt1
- + packaged gem with Ruby Policy 2.0
