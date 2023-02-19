%define        gemname validates_lengths_from_database

Name:          gem-validates-lengths-from-database
Version:       0.8.0.1
Release:       alt0.1
Summary:       Introspects your database string field maximum lengths and automatically defines length validations
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/rubiety/validates_lengths_from_database
Vcs:           https://github.com/rubiety/validates_lengths_from_database.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
%if_with check
BuildRequires: gem(activesupport) >= 4
BuildRequires: gem(rspec) >= 2.0
BuildRequires: gem(appraisal) >= 2.0
BuildRequires: gem(pg) >= 0.17.1
BuildRequires: gem(rdoc) >= 3.12
BuildRequires: gem(i18n) >= 0
BuildRequires: gem(iconv) >= 1.0.4
BuildRequires: gem(activerecord) >= 4
BuildConflicts: gem(rspec) >= 4
BuildConflicts: gem(appraisal) >= 3
BuildConflicts: gem(pg) >= 2
BuildConflicts: gem(rdoc) >= 7
BuildConflicts: gem(rake) >= 14
BuildConflicts: gem(iconv) >= 1.1
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_use_gem_dependency rake >= 13.0.1,rake < 14
%ruby_use_gem_dependency rdoc >= 6.1.1,rdoc < 7
%ruby_use_gem_dependency rspec >= 3.10.0,rspec < 4
%ruby_use_gem_dependency pg >= 1.3.5,pg < 2
%ruby_alias_names validates_lengths_from_database,validates-lengths-from-database
Requires:      gem(activerecord) >= 4
Obsoletes:     ruby-validates_lengths_from_database < %EVR
Provides:      ruby-validates_lengths_from_database = %EVR
Provides:      gem(validates_lengths_from_database) = 0.8.0.1

%ruby_use_gem_version validates_lengths_from_database:0.8.0.1

%description
Few people add length validations to fields in their database, and when saving
such fields that have exhausted their length, an SQL error occurs. This gem
introspects your table schema for maximum lengths on string and text fields and
automatically adds length validations to the model.


%package       -n gem-validates-lengths-from-database-doc
Version:       0.8.0.1
Release:       alt0.1
Summary:       Introspects your database string field maximum lengths and automatically defines length validations documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета validates_lengths_from_database
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(validates_lengths_from_database) = 0.8.0.1

%description   -n gem-validates-lengths-from-database-doc
Introspects your database string field maximum lengths and automatically defines
length validations documentation files.

Few people add length validations to fields in their database, and when saving
such fields that have exhausted their length, an SQL error occurs. This gem
introspects your table schema for maximum lengths on string and text fields and
automatically adds length validations to the model.

%description   -n gem-validates-lengths-from-database-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета validates_lengths_from_database.


%package       -n gem-validates-lengths-from-database-devel
Version:       0.8.0.1
Release:       alt0.1
Summary:       Introspects your database string field maximum lengths and automatically defines length validations development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета validates_lengths_from_database
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(validates_lengths_from_database) = 0.8.0.1
Requires:      gem(activesupport) >= 4
Requires:      gem(rspec) >= 2.0
Requires:      gem(appraisal) >= 2.0
Requires:      gem(pg) >= 0.17.1
Requires:      gem(rdoc) >= 3.12
Requires:      gem(i18n) >= 0
Requires:      gem(iconv) >= 1.0.4
Conflicts:     gem(rspec) >= 4
Conflicts:     gem(appraisal) >= 3
Conflicts:     gem(pg) >= 2
Conflicts:     gem(rdoc) >= 7
Conflicts:     gem(rake) >= 14
Conflicts:     gem(iconv) >= 1.1

%description   -n gem-validates-lengths-from-database-devel
Introspects your database string field maximum lengths and automatically defines
length validations development package.

Few people add length validations to fields in their database, and when saving
such fields that have exhausted their length, an SQL error occurs. This gem
introspects your table schema for maximum lengths on string and text fields and
automatically adds length validations to the model.

%description   -n gem-validates-lengths-from-database-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета validates_lengths_from_database.


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

%files         -n gem-validates-lengths-from-database-doc
%doc README.rdoc
%ruby_gemdocdir

%files         -n gem-validates-lengths-from-database-devel
%doc README.rdoc


%changelog
* Thu Jan 26 2023 Pavel Skrylev <majioa@altlinux.org> 0.8.0.1-alt0.1
- ^ 0.8.0 -> 0.8.0[1]

* Wed May 06 2020 Pavel Skrylev <majioa@altlinux.org> 0.8.0-alt1
- > Ruby Policy 2.0
- ^ 0.7.0 -> 0.8.0
- ! spec tags

* Mon Sep 24 2018 Pavel Skrylev <majioa@altlinux.org> 0.7.0-alt1
- Initial gemified build for Sisyphus
