# vim: set ft=spec: -*- rpm-spec -*-
%define        _unpackaged_files_terminate_build 1
%def_enable    check
%def_enable    doc
%def_enable    devel
%define        gemname activerecord-nulldb-adapter

Name:          gem-activerecord-nulldb-adapter
Version:       1.1.1
Release:       alt1
Summary:       An ActiveRecord null database adapter for greater speed and isolation in unit tests
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/nulldb/nulldb
Vcs:           https://github.com/nulldb/nulldb.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
BuildRequires: gem(activerecord) >= 6.0
BuildRequires: gem(appraisal) >= 0
BuildRequires: gem(pry-byebug) >= 0
BuildRequires: gem(rake) >= 0
BuildRequires: gem(rdoc) >= 0
BuildRequires: gem(rspec) >= 1.2.9
BuildRequires: gem(simplecov) >= 0
BuildRequires: gem(spec) >= 0
BuildConflicts: gem(activerecord) >= 8.1

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
Requires:      gem(activerecord) >= 6.0
Conflicts:     gem(activerecord) >= 8.1
Provides:      activerecord-nulldb-adapter = %EVR
Provides:      gem(activerecord-nulldb-adapter) = 1.1.1

%description
An ActiveRecord null database adapter for greater speed and isolation in unit
tests.

A database backend that translates database interactions into no-ops. Using
NullDB enables you to test your model business logic - including after_save
hooks - without ever touching a real database.


%if_enabled    doc
%package       -n gem-activerecord-nulldb-adapter-doc
Version:       1.1.1
Release:       alt1
Summary:       An ActiveRecord null database adapter for greater speed and isolation in unit tests documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета activerecord-nulldb-adapter
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(activerecord-nulldb-adapter) = 1.1.1

%description   -n gem-activerecord-nulldb-adapter-doc
An ActiveRecord null database adapter for greater speed and isolation in unit
tests documentation files.

%description   -n gem-activerecord-nulldb-adapter-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета activerecord-nulldb-adapter.
%endif


%if_enabled    devel
%package       -n gem-activerecord-nulldb-adapter-devel
Version:       1.1.1
Release:       alt1
Summary:       An ActiveRecord null database adapter for greater speed and isolation in unit tests development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета activerecord-nulldb-adapter
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(activerecord-nulldb-adapter) = 1.1.1
Requires:      gem(appraisal) >= 0
Requires:      gem(pry-byebug) >= 0
Requires:      gem(rake) >= 0
Requires:      gem(rdoc) >= 0
Requires:      gem(rspec) >= 1.2.9
Requires:      gem(simplecov) >= 0
Requires:      gem(spec) >= 0

%description   -n gem-activerecord-nulldb-adapter-devel
An ActiveRecord null database adapter for greater speed and isolation in unit
tests development package.

%description   -n gem-activerecord-nulldb-adapter-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета activerecord-nulldb-adapter.
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

%if_enabled    doc
%files         -n gem-activerecord-nulldb-adapter-doc
%doc LICENSE README.md
%ruby_gemdocdir
%endif

%if_enabled    devel
%files         -n gem-activerecord-nulldb-adapter-devel
%doc LICENSE README.md
%endif


%changelog
* Fri Jan 10 2025 Pavel Skrylev <majioa@altlinux.org> 1.1.1-alt1
- ^ 0.8.0 -> 1.1.1

* Thu Jan 26 2023 Pavel Skrylev <majioa@altlinux.org> 0.8.0-alt1
- ^ 0.5.1 -> 0.8.0

* Thu Dec 03 2020 Pavel Skrylev <majioa@altlinux.org> 0.5.1-alt1
- + packaged gem with usage Ruby Policy 2.0
