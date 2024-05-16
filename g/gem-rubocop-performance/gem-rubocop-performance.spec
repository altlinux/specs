%define        _unpackaged_files_terminate_build 1
%def_enable    check
%def_enable    doc
%def_enable    devel
%define        gemname rubocop-performance

Name:          gem-rubocop-performance
Version:       1.21.0
Release:       alt1
Summary:       Automatic performance checking tool for Ruby code
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/rubocop/rubocop-performance
Vcs:           https://github.com/rubocop/rubocop-performance/.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
%if_enabled check
BuildRequires: gem(bump) >= 0
BuildRequires: gem(prism) >= 0
BuildRequires: gem(rake) >= 0
BuildRequires: gem(rspec) >= 0
BuildRequires: gem(rubocop-rspec) >= 2.4.0
BuildRequires: gem(simplecov) >= 0
BuildRequires: gem(test-queue) >= 0
BuildRequires: gem(yard) >= 0.9
BuildRequires: gem(rubocop) >= 1.15.0
BuildRequires: gem(rubocop-ast) >= 1.7.0
BuildConflicts: gem(rubocop-rspec) >= 3
BuildConflicts: gem(yard) >= 1
BuildConflicts: gem(rubocop) >= 2
BuildConflicts: gem(rubocop-ast) >= 2
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_use_gem_dependency rubocop >= 1.15.0,rubocop < 2
%ruby_use_gem_dependency rubocop-rspec >= 2.4.0,rubocop-rspec < 3
%ruby_use_gem_dependency rubocop-ast >= 1.7.0,rubocop-ast < 2
Requires:      gem(rubocop) >= 1.15.0
Requires:      gem(rubocop-ast) >= 1.7.0
Conflicts:     gem(rubocop) >= 2
Conflicts:     gem(rubocop-ast) >= 2
Provides:      gem(rubocop-performance) = 1.21.0

%description
A collection of RuboCop cops to check for performance optimizations in Ruby
code.


%if_enabled    doc
%package       -n gem-rubocop-performance-doc
Version:       1.21.0
Release:       alt1
Summary:       Automatic performance checking tool for Ruby code documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета rubocop-performance
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(rubocop-performance) = 1.21.0

%description   -n gem-rubocop-performance-doc
Automatic performance checking tool for Ruby code documentation files.

%description   -n gem-rubocop-performance-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета rubocop-performance.
%endif


%if_enabled    devel
%package       -n gem-rubocop-performance-devel
Version:       1.21.0
Release:       alt1
Summary:       Automatic performance checking tool for Ruby code development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета rubocop-performance
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(rubocop-performance) = 1.21.0
Requires:      gem(bump) >= 0
Requires:      gem(prism) >= 0
Requires:      gem(rake) >= 0
Requires:      gem(rspec) >= 0
Requires:      gem(rubocop-rspec) >= 2.4.0
Requires:      gem(simplecov) >= 0
Requires:      gem(test-queue) >= 0
Requires:      gem(yard) >= 0.9
Conflicts:     gem(rubocop-rspec) >= 3
Conflicts:     gem(yard) >= 1

%description   -n gem-rubocop-performance-devel
Automatic performance checking tool for Ruby code development package.

%description   -n gem-rubocop-performance-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета rubocop-performance.
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
%files         -n gem-rubocop-performance-doc
%doc README.md
%ruby_gemdocdir
%endif

%if_enabled    devel
%files         -n gem-rubocop-performance-devel
%doc README.md
%endif


%changelog
* Mon Apr 15 2024 Pavel Skrylev <majioa@altlinux.org> 1.21.0-alt1
- ^ 1.13.3 -> 1.21.0

* Sat Apr 16 2022 Pavel Skrylev <majioa@altlinux.org> 1.13.3-alt1
- ^ 1.11.3 -> 1.13.3

* Tue Jun 22 2021 Pavel Skrylev <majioa@altlinux.org> 1.11.3-alt1
- + packaged gem with Ruby Policy 2.0
