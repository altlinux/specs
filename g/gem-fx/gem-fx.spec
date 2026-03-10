%define        _unpackaged_files_terminate_build 1
%def_enable    check
%def_enable    doc
%def_enable    devel
%define        gemname fx

Name:          gem-fx
Version:       0.9.0
Release:       alt1
Summary:       Support for database functions and triggers in Rails migrations
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/teoljungberg/fx
Vcs:           https://github.com/teoljungberg/fx.git
BuildArch:     noarch

Source:        %name-%version.tar
Autoprov:      yes,noruby
Autoreq:       yes,noruby
BuildRequires(pre): rpm-build-ruby
%if_enabled check
BuildRequires: gem(activerecord) >= 7.0
BuildRequires: gem(bundler) >= 1.5
BuildRequires: gem(pg) >= 0
BuildRequires: gem(pry) >= 0
BuildRequires: gem(railties) >= 7.0
BuildRequires: gem(rake) >= 0
BuildRequires: gem(redcarpet) >= 0
BuildRequires: gem(rspec) >= 3.3
BuildRequires: gem(standardrb) >= 0
BuildRequires: gem(warning) >= 0
BuildRequires: gem(yard) >= 0
BuildConflicts: gem(activerecord) >= 8
BuildConflicts: gem(railties) >= 8
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
Requires:      ruby >= 3.2
Requires:      gem(activerecord) >= 7.0
Requires:      gem(railties) >= 7.0
Conflicts:     gem(activerecord) >= 8
Conflicts:     gem(railties) >= 8
Provides:      gem(fx) = 0.9.0

%description
Adds methods to ActiveRecord::Migration to create and manage database functions
and triggers in Rails


%if_enabled    doc
%package       -n gem-fx-doc
Version:       0.9.0
Release:       alt1
Summary:       Support for database functions and triggers in Rails migrations documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета fx
Group:         Development/Documentation
BuildArch:     noarch

Autoprov:      yes,noruby
Autoreq:       yes,noruby
Requires:      gem(fx) = 0.9.0

%description   -n gem-fx-doc
Support for database functions and triggers in Rails migrations documentation
files.

Adds methods to ActiveRecord::Migration to create and manage database functions
and triggers in Rails

%description   -n gem-fx-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета fx.
%endif


%if_enabled    devel
%package       -n gem-fx-devel
Version:       0.9.0
Release:       alt1
Summary:       Support for database functions and triggers in Rails migrations development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета fx
Group:         Development/Ruby
BuildArch:     noarch

Autoprov:      yes,noruby
Autoreq:       yes,noruby
Requires:      gem(fx) = 0.9.0
Requires:      gem(bundler) >= 1.5
Requires:      gem(pg) >= 0
Requires:      gem(pry) >= 0
Requires:      gem(rake) >= 0
Requires:      gem(redcarpet) >= 0
Requires:      gem(rspec) >= 3.3
Requires:      gem(standardrb) >= 0
Requires:      gem(warning) >= 0
Requires:      gem(yard) >= 0

%description   -n gem-fx-devel
Support for database functions and triggers in Rails migrations development
package.

Adds methods to ActiveRecord::Migration to create and manage database functions
and triggers in Rails

%description   -n gem-fx-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета fx.
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
%doc CHANGELOG.md CONTRIBUTING.md LICENSE README.md
%ruby_gemspec
%ruby_gemlibdir

%if_enabled    doc
%files         -n gem-fx-doc
%doc CHANGELOG.md CONTRIBUTING.md LICENSE README.md
%ruby_gemdocdir
%endif

%if_enabled    devel
%files         -n gem-fx-devel
%doc CHANGELOG.md CONTRIBUTING.md LICENSE README.md
%endif


%changelog
* Tue Mar 10 2026 Pavel Skrylev <majioa@altlinux.org> 0.9.0-alt1
- + packaged gem with Ruby Policy 2.0
- * define explicit dependencies
