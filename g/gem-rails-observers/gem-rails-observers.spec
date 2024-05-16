%define        _unpackaged_files_terminate_build 1
%def_enable    check
%def_enable    doc
%def_enable    devel
%define        gemname rails-observers

Name:          gem-rails-observers
Version:       0.1.5
Release:       alt1
Summary:       Rails observer
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/rails/rails-observers
Vcs:           https://github.com/rails/rails-observers.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
%if_enabled check
BuildRequires: gem(minitest) >= 3
BuildRequires: gem(railties) >= 4.0
BuildRequires: gem(activerecord) >= 4.0
BuildRequires: gem(actionmailer) >= 4.0
BuildRequires: gem(actionpack) >= 4.0
BuildRequires: gem(sqlite3) >= 1.3
BuildRequires: gem(mocha) >= 0
BuildRequires: gem(activemodel) >= 4.0
BuildRequires: gem(activeresource) >= 4.0
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
Requires:      gem(activemodel) >= 4.0
Provides:      gem(rails-observers) = 0.1.5


%description
Rails observer (removed from core in Rails 4.0): ActiveModel::Observer,
ActiveRecord::Observer and ActionController::Caching::Sweeper extracted from
Rails.


%if_enabled    doc
%package       -n gem-rails-observers-doc
Version:       0.1.5
Release:       alt1
Summary:       Rails observer documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета rails-observers
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(rails-observers) = 0.1.5

%description   -n gem-rails-observers-doc
Rails observer documentation files.

Rails observer (removed from core in Rails 4.0): ActiveModel::Observer,
ActiveRecord::Observer and ActionController::Caching::Sweeper extracted from
Rails.

%description   -n gem-rails-observers-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета rails-observers.
%endif


%if_enabled    devel
%package       -n gem-rails-observers-devel
Version:       0.1.5
Release:       alt1
Summary:       Rails observer development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета rails-observers
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(rails-observers) = 0.1.5
Requires:      gem(minitest) >= 3
Requires:      gem(railties) >= 4.0
Requires:      gem(activerecord) >= 4.0
Requires:      gem(actionmailer) >= 4.0
Requires:      gem(actionpack) >= 4.0
Requires:      gem(sqlite3) >= 1.3
Requires:      gem(mocha) >= 0
Requires:      gem(activeresource) >= 4.0

%description   -n gem-rails-observers-devel
Rails observer development package.

Rails observer (removed from core in Rails 4.0): ActiveModel::Observer,
ActiveRecord::Observer and ActionController::Caching::Sweeper extracted from
Rails.

%description   -n gem-rails-observers-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета rails-observers.
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
%files         -n gem-rails-observers-doc
%doc README.md
%ruby_gemdocdir
%endif

%if_enabled    devel
%files         -n gem-rails-observers-devel
%doc README.md
%endif


%changelog
* Wed Apr 17 2024 Pavel Skrylev <majioa@altlinux.org> 0.1.5-alt1
- + packaged gem with Ruby Policy 2.0
