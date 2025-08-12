%define        _unpackaged_files_terminate_build 1
%def_enable    check
%def_enable    doc
%def_enable    devel
%define        gemname standard

Name:          gem-standard
Version:       1.50.0
Release:       alt1
Summary:       Ruby Style Guide, with linter & automatic code fixer
License:       ALT-XFree86-other and MIT
Group:         Development/Ruby
Url:           https://github.com/testdouble/standard
Vcs:           https://github.com/testdouble/standard.git
Packager:      Baltix Maintaining Team <baltix@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
%if_enabled check
BuildRequires: gem(bundler) >= 0
BuildRequires: gem(language_server-protocol) >= 3.17.0.2
BuildRequires: gem(lint_roller) >= 1.0
BuildRequires: gem(m) >= 0
BuildRequires: gem(minitest) >= 5.17.0
BuildRequires: gem(mutex_m) >= 0
BuildRequires: gem(rake) >= 13.1.0
BuildRequires: gem(rubocop) >= 1.15.0
BuildRequires: gem(ruby-lsp) >= 0
BuildRequires: gem(simplecov) >= 0
BuildRequires: gem(standard-custom) >= 1.0.0
BuildRequires: gem(standard-performance) >= 1.8
BuildConflicts: gem(language_server-protocol) >= 3.17.1
BuildConflicts: gem(lint_roller) >= 2
BuildConflicts: gem(minitest) >= 6
BuildConflicts: gem(rake) >= 14
BuildConflicts: gem(rubocop) >= 2
BuildConflicts: gem(standard-custom) >= 1.1
BuildConflicts: gem(standard-performance) >= 2
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_use_gem_dependency rake >= 13.1.0,rake < 14
%ruby_use_gem_dependency rubocop >= 1.15.0,rubocop < 2
%ruby_use_gem_dependency minitest >= 5.17.0,minitest < 6
Requires:      ruby >= 3.0.0
Requires:      gem(language_server-protocol) >= 3.17.0.2
Requires:      gem(lint_roller) >= 1.0
Requires:      gem(rubocop) >= 1.15.0
Requires:      gem(standard-custom) >= 1.0.0
Requires:      gem(standard-performance) >= 1.8
Conflicts:     gem(language_server-protocol) >= 3.17.1
Conflicts:     gem(lint_roller) >= 2
Conflicts:     gem(rubocop) >= 2
Conflicts:     gem(standard-custom) >= 1.1
Conflicts:     gem(standard-performance) >= 2
Provides:      gem(standard) = 1.50.0

%description
This gem is a spiritual port of StandardJS and aims to save you (and others!)
time in the same three ways:

* No configuration. The easiest way to enforce consistent style in your project.
Just drop it in.
* Automatically format code. Just run standardrb --fix and say goodbye to messy
or inconsistent code.
* Catch style issues & programmer errors early. Save precious code review time
by eliminating back-and-forth between reviewer & contributor.

No decisions to make. It just works. Here's a zap lightning talk zap about it.


%package       -n standardrb
Version:       1.50.0
Release:       alt1
Summary:       Ruby Style Guide, with linter & automatic code fixer executable(s)
Summary(ru_RU.UTF-8): Исполнямка для самоцвета standard
Group:         Other
BuildArch:     noarch

Requires:      gem(standard) = 1.50.0

%description   -n standardrb
Ruby Style Guide, with linter & automatic code fixer executable(s).

This gem is a spiritual port of StandardJS and aims to save you (and others!)
time in the same three ways:

* No configuration. The easiest way to enforce consistent style in your project.
Just drop it in.
* Automatically format code. Just run standardrb --fix and say goodbye to messy
or inconsistent code.
* Catch style issues & programmer errors early. Save precious code review time
by eliminating back-and-forth between reviewer & contributor.

No decisions to make. It just works. Here's a zap lightning talk zap about it.

%description   -n standardrb -l ru_RU.UTF-8
Исполнямка для самоцвета standard.


%if_enabled    doc
%package       -n gem-standard-doc
Version:       1.50.0
Release:       alt1
Summary:       Ruby Style Guide, with linter & automatic code fixer documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета standard
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(standard) = 1.50.0

%description   -n gem-standard-doc
Ruby Style Guide, with linter & automatic code fixer documentation files.

This gem is a spiritual port of StandardJS and aims to save you (and others!)
time in the same three ways:

* No configuration. The easiest way to enforce consistent style in your project.
Just drop it in.
* Automatically format code. Just run standardrb --fix and say goodbye to messy
or inconsistent code.
* Catch style issues & programmer errors early. Save precious code review time
by eliminating back-and-forth between reviewer & contributor.

No decisions to make. It just works. Here's a zap lightning talk zap about it.

%description   -n gem-standard-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета standard.
%endif


%if_enabled    devel
%package       -n gem-standard-devel
Version:       1.50.0
Release:       alt1
Summary:       Ruby Style Guide, with linter & automatic code fixer development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета standard
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(standard) = 1.50.0

%description   -n gem-standard-devel
Ruby Style Guide, with linter & automatic code fixer development package.

This gem is a spiritual port of StandardJS and aims to save you (and others!)
time in the same three ways:

* No configuration. The easiest way to enforce consistent style in your project.
Just drop it in.
* Automatically format code. Just run standardrb --fix and say goodbye to messy
or inconsistent code.
* Catch style issues & programmer errors early. Save precious code review time
by eliminating back-and-forth between reviewer & contributor.

No decisions to make. It just works. Here's a zap lightning talk zap about it.

%description   -n gem-standard-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета standard.
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

%files         -n standardrb
%doc CHANGELOG.md LICENSE.txt README.md
%_bindir/standardrb

%if_enabled    doc
%files         -n gem-standard-doc
%doc CHANGELOG.md LICENSE.txt README.md
%ruby_gemdocdir
%endif

%if_enabled    devel
%files         -n gem-standard-devel
%doc CHANGELOG.md LICENSE.txt README.md
%endif


%changelog
* Tue Aug 12 2025 Pavel Skrylev <majioa@altlinux.org> 1.50.0-alt1
- ^ 1.41.1 -> 1.50.0

* Fri Oct 25 2024 Pavel Skrylev <majioa@altlinux.org> 1.41.1-alt1
- ^ 1.35.0.1 -> 1.41.1

* Wed Apr 17 2024 Pavel Skrylev <majioa@altlinux.org> 1.35.0.1-alt1
- ^ 1.1.1 -> 1.35.0.1

* Tue Jun 22 2021 Pavel Skrylev <majioa@altlinux.org> 1.1.1-alt1
- + packaged gem with Ruby Policy 2.0
