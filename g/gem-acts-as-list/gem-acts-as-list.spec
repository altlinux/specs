%define        _unpackaged_files_terminate_build 1
%def_enable    check
%def_enable    doc
%def_enable    devel
%define        gemname acts_as_list

Name:          gem-acts-as-list
Version:       1.2.6
Release:       alt1
Summary:       A gem adding sorting, reordering capabilities to an active_record model
License:       MIT
Group:         Development/Ruby
Url:           http://github.com/brendon/acts_as_list
Vcs:           https://github.com/brendon/acts_as_list.git
Packager:      Baltix Maintaining Team <baltix@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
%if_enabled check
BuildRequires: gem(activerecord) >= 6.1
BuildRequires: gem(activesupport) >= 6.1
BuildRequires: gem(base64) >= 0
BuildRequires: gem(benchmark) >= 0
BuildRequires: gem(bigdecimal) >= 0
BuildRequires: gem(logger) >= 0
BuildRequires: gem(minitest) >= 5.0
BuildRequires: gem(minitest-hooks) >= 1.5.1
BuildRequires: gem(mocha) >= 2.0
BuildRequires: gem(mutex_m) >= 0
BuildRequires: gem(mysql2) >= 0.5.6
BuildRequires: gem(pg) >= 1.5.5
BuildRequires: gem(rake) >= 13.0
BuildRequires: gem(sqlite3) >= 1.7.3
BuildRequires: gem(timecop) >= 0.9.8
BuildConflicts: gem(minitest) >= 6
BuildConflicts: gem(minitest-hooks) >= 1.6
BuildConflicts: gem(mocha) >= 3
BuildConflicts: gem(pg) >= 1.6
BuildConflicts: gem(rake) >= 14
BuildConflicts: gem(sqlite3) >= 1.8
BuildConflicts: gem(timecop) >= 0.10
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_use_gem_dependency mocha >= 2.0,mocha < 3
%ruby_use_gem_dependency mysql2 >= 0.5.7,mysql2 < 1
%ruby_alias_names acts_as_list,acts-as-list
Requires:      ruby >= 2.5
Requires:      gem(activerecord) >= 6.1
Requires:      gem(activesupport) >= 6.1
Provides:      gem(acts_as_list) = 1.2.6

%description
This "acts_as" extension provides the capabilities for sorting and reordering a
number of objects in a list. The class that has this specified needs to have a
"position" column defined as an integer on the mapped database table.


%if_enabled    doc
%package       -n gem-acts-as-list-doc
Version:       1.2.6
Release:       alt1
Summary:       A gem adding sorting, reordering capabilities to an active_record model documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета acts_as_list
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(acts_as_list) = 1.2.6

%description   -n gem-acts-as-list-doc
A gem adding sorting, reordering capabilities to an active_record model
documentation files.

This "acts_as" extension provides the capabilities for sorting and reordering a
number of objects in a list. The class that has this specified needs to have a
"position" column defined as an integer on the mapped database table.

%description   -n gem-acts-as-list-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета acts_as_list.
%endif


%if_enabled    devel
%package       -n gem-acts-as-list-devel
Version:       1.2.6
Release:       alt1
Summary:       A gem adding sorting, reordering capabilities to an active_record model development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета acts_as_list
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(acts_as_list) = 1.2.6
Requires:      gem(base64) >= 0
Requires:      gem(benchmark) >= 0
Requires:      gem(bigdecimal) >= 0
Requires:      gem(logger) >= 0
Requires:      gem(minitest) >= 5.0
Requires:      gem(minitest-hooks) >= 1.5.1
Requires:      gem(mocha) >= 2.0
Requires:      gem(mutex_m) >= 0
Requires:      gem(mysql2) >= 0.5.6
Requires:      gem(pg) >= 1.5.5
Requires:      gem(rake) >= 13.0
Requires:      gem(sqlite3) >= 1.7.3
Requires:      gem(timecop) >= 0.9.8
Conflicts:     gem(minitest) >= 6
Conflicts:     gem(minitest-hooks) >= 1.6
Conflicts:     gem(mocha) >= 3
Conflicts:     gem(pg) >= 1.6
Conflicts:     gem(rake) >= 14
Conflicts:     gem(sqlite3) >= 1.8
Conflicts:     gem(timecop) >= 0.10

%description   -n gem-acts-as-list-devel
A gem adding sorting, reordering capabilities to an active_record model
development package.

This "acts_as" extension provides the capabilities for sorting and reordering a
number of objects in a list. The class that has this specified needs to have a
"position" column defined as an integer on the mapped database table.

%description   -n gem-acts-as-list-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета acts_as_list.
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
%doc CHANGELOG.md MIT-LICENSE README.md
%ruby_gemspec
%ruby_gemlibdir

%if_enabled    doc
%files         -n gem-acts-as-list-doc
%doc CHANGELOG.md MIT-LICENSE README.md
%ruby_gemdocdir
%endif

%if_enabled    devel
%files         -n gem-acts-as-list-devel
%doc CHANGELOG.md MIT-LICENSE README.md
%endif


%changelog
* Wed Oct 22 2025 Pavel Skrylev <majioa@altlinux.org> 1.2.6-alt1
- ^ 1.0.4 -> 1.2.6
- * define explicit dependencies

* Fri Jan 20 2023 Pavel Skrylev <majioa@altlinux.org> 1.0.4-alt1.1
- ! add adomatic alias finding macros

* Wed Sep 01 2021 Pavel Skrylev <majioa@altlinux.org> 1.0.4-alt1
- + packaged gem with Ruby Policy 2.0
