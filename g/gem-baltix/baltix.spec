%define        _unpackaged_files_terminate_build 1
%def_disable   check
%def_enable    doc
%def_disable   devel
%define        gemname baltix

Name:          gem-baltix
Version:       0.1.2
Release:       alt1
Summary:       Baltix is setup replacement and spec control utility for RPM/local packages
License:       MIT
Group:         Development/Ruby
Url:           https://github.org/majioa/baltix
Vcs:           https://github.org/majioa/baltix.git
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-macros-ruby setup-rb rake
%if_enabled check
BuildRequires: gem(bundler) >= 2.0
BuildRequires: gem(cucumber) >= 5.2
BuildRequires: gem(pry) >= 0.13
BuildRequires: gem(rake) >= 12.0
BuildRequires: gem(shoulda-matchers-cucumber) >= 1.0.1
BuildRequires: gem(simplecov) >= 0
BuildRequires: gem(simplecov-lcov) >= 0
BuildRequires: gem(timecop) >= 0
BuildConflicts: gem(bundler) >= 3
BuildConflicts: gem(cucumber) >= 6
BuildConflicts: gem(pry) >= 1
BuildConflicts: gem(rake) >= 14
BuildConflicts: gem(shoulda-matchers-cucumber) >= 2
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_use_gem_dependency rake >= 13.1.0,rake < 14
Requires:      ruby >= 3.0.0
Requires:      gem(rake) >= 12.0
Conflicts:     gem(rake) >= 14
Provides:      gem(baltix) = 0.1.2

%description
Baltix is setup replacement and spec control utility for RPM/local packages


%package       -n baltix
Version:       0.1.2
Release:       alt1
Summary:       Baltix is setup replacement and spec control utility for RPM/local packages executable(s)
Summary(ru_RU.UTF-8): Исполнямка для самоцвета baltix
Group:         Other
BuildArch:     noarch

Requires:      gem(baltix) = 0.1.2
Requires:      gem(rake) >= 12.0
Conflicts:     gem(rake) >= 14

%description   -n baltix
Baltix is setup replacement and spec control utility for RPM/local packages
executable(s).

%description   -n baltix -l ru_RU.UTF-8
Исполнямка для самоцвета baltix.


%if_enabled    doc
%package       -n gem-baltix-doc
Version:       0.1.2
Release:       alt1
Summary:       Baltix is setup replacement and spec control utility for RPM/local packages documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета baltix
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(baltix) = 0.1.2

%description   -n gem-baltix-doc
Baltix is setup replacement and spec control utility for RPM/local packages
documentation files.

%description   -n gem-baltix-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета baltix.
%endif


%if_enabled    devel
%package       -n gem-baltix-devel
Version:       0.1.2
Release:       alt1
Summary:       Baltix is setup replacement and spec control utility for RPM/local packages development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета baltix
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(baltix) = 0.1.2
Requires:      gem(bundler) >= 2.0
Requires:      gem(cucumber) >= 5.2
Requires:      gem(pry) >= 0.13
Requires:      gem(shoulda-matchers-cucumber) >= 1.0.1
Requires:      gem(simplecov) >= 0
Requires:      gem(simplecov-lcov) >= 0
Requires:      gem(timecop) >= 0
Conflicts:     gem(bundler) >= 3
Conflicts:     gem(cucumber) >= 6
Conflicts:     gem(pry) >= 1
Conflicts:     gem(shoulda-matchers-cucumber) >= 2

%description   -n gem-baltix-devel
Baltix is setup replacement and spec control utility for RPM/local packages
development package.

%description   -n gem-baltix-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета baltix.
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
%doc LICENSE README.md
%ruby_gemspec
%ruby_gemlibdir

%files         -n baltix
%doc LICENSE README.md
%_bindir/baltix

%if_enabled    doc
%files         -n gem-baltix-doc
%doc LICENSE README.md
%ruby_gemdocdir
%endif

%if_enabled    devel
%files         -n gem-baltix-devel
%doc LICENSE README.md
%endif


%changelog
* Wed Jul 22 2026 Pavel Skrylev <majioa@altlinux.org> 0.1.2-alt1
- + packaged gem with Ruby Policy 2.0
- * define explicit dependencies
