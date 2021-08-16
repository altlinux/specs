%define        gemname activerecord-session_store

Name:          gem-activerecord-session-store
Version:       2.0.0
Release:       alt1
Summary:       Active Record's Session Store extracted from Rails
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/rails/activerecord-session_store
Vcs:           https://github.com/rails/activerecord-session_store.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
BuildRequires: gem(activerecord) >= 5.2.4.1
BuildRequires: gem(actionpack) >= 5.2.4.1
BuildRequires: gem(railties) >= 5.2.4.1
BuildRequires: gem(rack) >= 2.0.8 gem(rack) < 3
BuildRequires: gem(multi_json) >= 1.11 gem(multi_json) < 2
BuildRequires: gem(sqlite3) >= 0

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_alias_names activerecord-session_store,activerecord-session-store
Requires:      gem(activerecord) >= 5.2.4.1
Requires:      gem(actionpack) >= 5.2.4.1
Requires:      gem(railties) >= 5.2.4.1
Requires:      gem(rack) >= 2.0.8 gem(rack) < 3
Requires:      gem(multi_json) >= 1.11 gem(multi_json) < 2
Obsoletes:     ruby-activerecord-session_store < %EVR
Provides:      ruby-activerecord-session_store = %EVR
Provides:      gem(activerecord-session_store) = 2.0.0


%description
A session store backed by an Active Record class. A default class is provided,
but any object duck-typing to an Active Record Session class with text
session_id and data attributes is sufficient.


%package       -n gem-activerecord-session-store-doc
Version:       2.0.0
Release:       alt1
Summary:       Active Record's Session Store extracted from Rails documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета activerecord-session_store
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(activerecord-session_store) = 2.0.0

%description   -n gem-activerecord-session-store-doc
Active Record's Session Store extracted from Rails documentation files.

A session store backed by an Active Record class. A default class is provided,
but any object duck-typing to an Active Record Session class with text
session_id and data attributes is sufficient.

%description   -n gem-activerecord-session-store-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета activerecord-session_store.


%package       -n gem-activerecord-session-store-devel
Version:       2.0.0
Release:       alt1
Summary:       Active Record's Session Store extracted from Rails development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета activerecord-session_store
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(activerecord-session_store) = 2.0.0
Requires:      gem(sqlite3) >= 0

%description   -n gem-activerecord-session-store-devel
Active Record's Session Store extracted from Rails development package.

A session store backed by an Active Record class. A default class is provided,
but any object duck-typing to an Active Record Session class with text
session_id and data attributes is sufficient.

%description   -n gem-activerecord-session-store-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета activerecord-session_store.


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

%files         -n gem-activerecord-session-store-doc
%doc README.md
%ruby_gemdocdir

%files         -n gem-activerecord-session-store-devel
%doc README.md


%changelog
* Tue Jun 22 2021 Pavel Skrylev <majioa@altlinux.org> 2.0.0-alt1
- ^ 1.1.3 -> 2.0.0

* Thu Mar 05 2020 Pavel Skrylev <majioa@altlinux.org> 1.1.3-alt1.1
- fixed (!) spec

* Mon Sep 16 2019 Pavel Skrylev <majioa@altlinux.org> 1.1.3-alt1
- used (>) Ruby Policy 2.0
- updated (^) 1.1.1 -> 1.1.3

* Fri Sep 21 2018 Pavel Skrylev <majioa@altlinux.org> 1.1.1-alt1
- Initial gemified build for Sisyphus
