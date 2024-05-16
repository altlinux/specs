%define        _unpackaged_files_terminate_build 1
%def_enable    check
%def_enable    doc
%def_enable    devel
%define        gemname activerecord-session_store

Name:          gem-activerecord-session-store
Version:       2.1.0
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
%if_enabled check
BuildRequires: gem(sqlite3) >= 0
BuildRequires: gem(activerecord) >= 6.1
BuildRequires: gem(actionpack) >= 6.1
BuildRequires: gem(railties) >= 6.1
BuildRequires: gem(rack) >= 2.0.8
BuildRequires: gem(multi_json) >= 1.11
BuildRequires: gem(cgi) >= 0.3.6
BuildConflicts: gem(rack) >= 4
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_alias_names activerecord-session_store,activerecord-session-store
Requires:      gem(activerecord) >= 6.1
Requires:      gem(actionpack) >= 6.1
Requires:      gem(railties) >= 6.1
Requires:      gem(rack) >= 2.0.8
Requires:      gem(multi_json) >= 1.11
Requires:      gem(cgi) >= 0.3.6
Conflicts:     gem(rack) >= 4
Obsoletes:     ruby-activerecord-session_store < %EVR
Provides:      ruby-activerecord-session_store = %EVR
Provides:      gem(activerecord-session_store) = 2.1.0


%description
A session store backed by an Active Record class. A default class is provided,
but any object duck-typing to an Active Record Session class with text
session_id and data attributes is sufficient.


%if_enabled    doc
%package       -n gem-activerecord-session-store-doc
Version:       2.1.0
Release:       alt1
Summary:       Active Record's Session Store extracted from Rails documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета activerecord-session_store
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(activerecord-session_store) = 2.1.0

%description   -n gem-activerecord-session-store-doc
Active Record's Session Store extracted from Rails documentation files.

A session store backed by an Active Record class. A default class is provided,
but any object duck-typing to an Active Record Session class with text
session_id and data attributes is sufficient.
%description   -n gem-activerecord-session-store-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета activerecord-session_store.
%endif


%if_enabled    devel
%package       -n gem-activerecord-session-store-devel
Version:       2.1.0
Release:       alt1
Summary:       Active Record's Session Store extracted from Rails development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета activerecord-session_store
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(activerecord-session_store) = 2.1.0
Requires:      gem(sqlite3) >= 0

%description   -n gem-activerecord-session-store-devel
Active Record's Session Store extracted from Rails development package.

A session store backed by an Active Record class. A default class is provided,
but any object duck-typing to an Active Record Session class with text
session_id and data attributes is sufficient.
%description   -n gem-activerecord-session-store-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета activerecord-session_store.
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
%files         -n gem-activerecord-session-store-doc
%doc README.md
%ruby_gemdocdir
%endif

%if_enabled    devel
%files         -n gem-activerecord-session-store-devel
%doc README.md
%endif


%changelog
* Thu Apr 18 2024 Pavel Skrylev <majioa@altlinux.org> 2.1.0-alt1
- ^ 2.0.0[1] -> 2.1.0

* Mon Oct 10 2022 Pavel Skrylev <majioa@altlinux.org> 2.0.0.1-alt1
- ^ 2.0.0 -> 2.0.0[1]

* Tue Jun 22 2021 Pavel Skrylev <majioa@altlinux.org> 2.0.0-alt1
- ^ 1.1.3 -> 2.0.0

* Thu Mar 05 2020 Pavel Skrylev <majioa@altlinux.org> 1.1.3-alt1.1
- fixed (!) spec

* Mon Sep 16 2019 Pavel Skrylev <majioa@altlinux.org> 1.1.3-alt1
- used (>) Ruby Policy 2.0
- updated (^) 1.1.1 -> 1.1.3

* Fri Sep 21 2018 Pavel Skrylev <majioa@altlinux.org> 1.1.1-alt1
- Initial gemified build for Sisyphus
