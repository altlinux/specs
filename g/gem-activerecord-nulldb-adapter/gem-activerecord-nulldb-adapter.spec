# vim: set ft=spec: -*- rpm-spec -*-
%define        gemname activerecord-nulldb-adapter

Name:          gem-activerecord-nulldb-adapter
Version:       0.8.0
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
%if_with check
BuildRequires: gem(activerecord) >= 5.2.0
BuildRequires: gem(spec) >= 0
BuildRequires: gem(rspec) >= 1.2.9
BuildRequires: gem(rake) >= 0
BuildRequires: gem(rdoc) >= 0
BuildRequires: gem(appraisal) >= 0
BuildRequires: gem(simplecov) >= 0
BuildRequires: gem(pry-byebug) >= 0
BuildConflicts: gem(activerecord) >= 6.3
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
Requires:      gem(activerecord) >= 5.2.0
Conflicts:     gem(activerecord) >= 6.3
Provides:      gem(activerecord-nulldb-adapter) = 0.8.0


%description
An ActiveRecord null database adapter for greater speed and isolation in unit
tests.

A database backend that translates database interactions into no-ops. Using
NullDB enables you to test your model business logic - including after_save
hooks - without ever touching a real database.


%package       -n gem-activerecord-nulldb-adapter-doc
Version:       0.8.0
Release:       alt1
Summary:       An ActiveRecord null database adapter for greater speed and isolation in unit tests documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета activerecord-nulldb-adapter
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(activerecord-nulldb-adapter) = 0.8.0

%description   -n gem-activerecord-nulldb-adapter-doc
An ActiveRecord null database adapter for greater speed and isolation in unit
tests documentation files.

%description   -n gem-activerecord-nulldb-adapter-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета activerecord-nulldb-adapter.


%package       -n gem-activerecord-nulldb-adapter-devel
Version:       0.8.0
Release:       alt1
Summary:       An ActiveRecord null database adapter for greater speed and isolation in unit tests development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета activerecord-nulldb-adapter
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(activerecord-nulldb-adapter) = 0.8.0
Requires:      gem(rspec) >= 1.2.9
Requires:      gem(rake) >= 0
Requires:      gem(rdoc) >= 0
Requires:      gem(appraisal) >= 0
Requires:      gem(simplecov) >= 0
Requires:      gem(pry-byebug) >= 0

%description   -n gem-activerecord-nulldb-adapter-devel
An ActiveRecord null database adapter for greater speed and isolation in unit
tests development package.

%description   -n gem-activerecord-nulldb-adapter-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета activerecord-nulldb-adapter.


%prep
%setup

%build
%ruby_build

%install
%ruby_install

%check
%ruby_test

%files
%doc README.rdoc
%ruby_gemspec
%ruby_gemlibdir

%files         -n gem-activerecord-nulldb-adapter-doc
%doc README.rdoc
%ruby_gemdocdir

%files         -n gem-activerecord-nulldb-adapter-devel
%doc README.rdoc


%changelog
* Thu Jan 26 2023 Pavel Skrylev <majioa@altlinux.org> 0.8.0-alt1
- ^ 0.5.1 -> 0.8.0

* Thu Dec 03 2020 Pavel Skrylev <majioa@altlinux.org> 0.5.1-alt1
- + packaged gem with usage Ruby Policy 2.0
