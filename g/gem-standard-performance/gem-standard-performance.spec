%define        _unpackaged_files_terminate_build 1
%def_disable   check
%def_enable    doc
%def_disable   devel
%define        gemname standard-performance

Name:          gem-standard-performance
Version:       1.8.0
Release:       alt1
Summary:       Standard Ruby Plugin providing configuration for rubocop-performance
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/standardrb/standard-performance
Vcs:           https://github.com/standardrb/standard-performance.git
Packager:      Baltix Maintaining Team <baltix@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
%if_enabled check
BuildRequires: gem(lint_roller) >= 1.1
BuildRequires: gem(m) >= 0
BuildRequires: gem(minitest) >= 0
BuildRequires: gem(mocktail) >= 0
BuildRequires: gem(rake) >= 0
BuildRequires: gem(rubocop-performance) >= 1.11.3
BuildRequires: gem(simplecov) >= 0
BuildRequires: gem(standard) >= 0
BuildConflicts: gem(lint_roller) >= 2
BuildConflicts: gem(rubocop-performance) >= 2
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_use_gem_dependency rubocop-performance >= 1.11.3,rubocop-performance < 2
Requires:      ruby >= 3.0.0
Requires:      gem(lint_roller) >= 1.1
Requires:      gem(rubocop-performance) >= 1.11.3
Requires:      gem(simplecov) >= 0
Conflicts:     gem(lint_roller) >= 2
Conflicts:     gem(rubocop-performance) >= 2
Provides:      standard-performance = %EVR
Provides:      gem(standard-performance) = 1.8.0

%description
Standard Ruby Plugin providing configuration for rubocop-performance


%if_enabled    doc
%package       -n gem-standard-performance-doc
Version:       1.8.0
Release:       alt1
Summary:       Standard Ruby Plugin providing configuration for rubocop-performance documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета standard-performance
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(standard-performance) = 1.8.0

%description   -n gem-standard-performance-doc
Standard Ruby Plugin providing configuration for rubocop-performance
documentation files.

%description   -n gem-standard-performance-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета standard-performance.
%endif


%if_enabled    devel
%package       -n gem-standard-performance-devel
Version:       1.8.0
Release:       alt1
Summary:       Standard Ruby Plugin providing configuration for rubocop-performance development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета standard-performance
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(standard-performance) = 1.8.0
Requires:      gem(lint_roller) >= 1.1
Requires:      gem(m) >= 0
Requires:      gem(minitest) >= 0
Requires:      gem(mocktail) >= 0
Requires:      gem(rake) >= 0
Requires:      gem(rubocop-performance) >= 1.11.3
Requires:      gem(simplecov) >= 0
Requires:      gem(standard) >= 0
Conflicts:     gem(lint_roller) >= 2
Conflicts:     gem(rubocop-performance) >= 2

%description   -n gem-standard-performance-devel
Standard Ruby Plugin providing configuration for rubocop-performance development
package.

%description   -n gem-standard-performance-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета standard-performance.
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
%doc CHANGELOG.md LICENSE.txt README.md
%ruby_gemspec
%ruby_gemlibdir

%if_enabled    doc
%files         -n gem-standard-performance-doc
%doc CHANGELOG.md LICENSE.txt README.md
%ruby_gemdocdir
%endif

%if_enabled    devel
%files         -n gem-standard-performance-devel
%doc CHANGELOG.md LICENSE.txt README.md
%endif


%changelog
* Tue Aug 12 2025 Pavel Skrylev <majioa@altlinux.org> 1.8.0-alt1
- ^ 1.5.0 -> 1.8.0

* Fri Oct 25 2024 Pavel Skrylev <majioa@altlinux.org> 1.5.0-alt1
- ^ 1.3.1 -> 1.5.0

* Wed Apr 17 2024 Pavel Skrylev <majioa@altlinux.org> 1.3.1-alt1
- + packaged gem with Ruby Policy 2.0
