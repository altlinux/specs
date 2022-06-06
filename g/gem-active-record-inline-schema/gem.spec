%define        gemname active_record_inline_schema

Name:          gem-active-record-inline-schema
Version:       0.6.1
Release:       alt1
Summary:       Define table structure (columns and indexes) inside your ActiveRecord models like you can do in migrations. Also similar to DataMapper inline schema syntax
License:       Unlicense
Group:         Development/Ruby
Url:           https://github.com/seamusabshere/active_record_inline_schema
Vcs:           https://github.com/seamusabshere/active_record_inline_schema.git
Packager:      Pavel Skrylev <majioa@altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
BuildRequires: gem(activesupport) >= 0
BuildRequires: gem(activerecord) >= 3

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
Requires:      gem(activesupport) >= 0
Requires:      gem(activerecord) >= 3
Provides:      gem(active_record_inline_schema) = 0.6.1


%description
Specify columns like you would with ActiveRecord migrations and then run
.auto_upgrade! Based on the mini_record gem from Davide D'Agostino, it adds
fewer aliases, doesn't create timestamps and relationship columns automatically.


%package       -n gem-active-record-inline-schema-doc
Version:       0.6.1
Release:       alt1
Summary:       Define table structure (columns and indexes) inside your ActiveRecord models like you can do in migrations. Also similar to DataMapper inline schema syntax documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета active_record_inline_schema
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(active_record_inline_schema) = 0.6.1

%description   -n gem-active-record-inline-schema-doc
Define table structure (columns and indexes) inside your ActiveRecord models
like you can do in migrations. Also similar to DataMapper inline schema syntax
documentation files.

Specify columns like you would with ActiveRecord migrations and then run
.auto_upgrade! Based on the mini_record gem from Davide D'Agostino, it adds
fewer aliases, doesn't create timestamps and relationship columns automatically.

%description   -n gem-active-record-inline-schema-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета active_record_inline_schema.


%package       -n gem-active-record-inline-schema-devel
Version:       0.6.1
Release:       alt1
Summary:       Define table structure (columns and indexes) inside your ActiveRecord models like you can do in migrations. Also similar to DataMapper inline schema syntax development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета active_record_inline_schema
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(active_record_inline_schema) = 0.6.1

%description   -n gem-active-record-inline-schema-devel
Define table structure (columns and indexes) inside your ActiveRecord models
like you can do in migrations. Also similar to DataMapper inline schema syntax
development package.

Specify columns like you would with ActiveRecord migrations and then run
.auto_upgrade! Based on the mini_record gem from Davide D'Agostino, it adds
fewer aliases, doesn't create timestamps and relationship columns automatically.

%description   -n gem-active-record-inline-schema-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета active_record_inline_schema.


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

%files         -n gem-active-record-inline-schema-doc
%doc README.md
%ruby_gemdocdir

%files         -n gem-active-record-inline-schema-devel
%doc README.md


%changelog
* Tue Apr 19 2022 Pavel Skrylev <majioa@altlinux.org> 0.6.1-alt1
- + packaged gem with Ruby Policy 2.0
