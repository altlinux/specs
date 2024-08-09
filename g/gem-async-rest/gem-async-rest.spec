%define        _unpackaged_files_terminate_build 1
%def_disable   check
%def_enable    doc
%def_enable    devel
%define        gemname async-rest

Name:          gem-async-rest
Version:       0.13.0
Release:       alt1
Summary:       A library for RESTful clients (and hopefully servers)
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/socketry/async-rest
Vcs:           https://github.com/socketry/async-rest.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
%if_enabled check
BuildRequires: gem(async-http) >= 0.42
BuildRequires: gem(protocol-http) >= 0.7
BuildConflicts: gem(async-http) >= 1
BuildConflicts: gem(protocol-http) >= 1
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
Requires:      gem(async-http) >= 0.42
Requires:      gem(protocol-http) >= 0.7
Conflicts:     gem(async-http) >= 1
Conflicts:     gem(protocol-http) >= 1
Provides:      gem(async-rest) = 0.13.0


%description
Roy Thomas Fielding's thesis Architectural Styles and the Design of
Network-based Software Architectures describes Representational State Transfer
which comprises several core concepts:

* Resource: A conceptual mapping to one or more entities.
* Representation: An instance of a resource at a given point in time.

This gem models these abstractions as closely and practically as possible and
serves as a basis for building asynchronous web clients.


%if_enabled    doc
%package       -n gem-async-rest-doc
Version:       0.13.0
Release:       alt1
Summary:       A library for RESTful clients (and hopefully servers) documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета async-rest
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(async-rest) = 0.13.0

%description   -n gem-async-rest-doc
A library for RESTful clients (and hopefully servers) documentation files.

Roy Thomas Fielding's thesis Architectural Styles and the Design of
Network-based Software Architectures describes Representational State Transfer
which comprises several core concepts:

* Resource: A conceptual mapping to one or more entities.
* Representation: An instance of a resource at a given point in time.

This gem models these abstractions as closely and practically as possible and
serves as a basis for building asynchronous web clients.

%description   -n gem-async-rest-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета async-rest.
%endif


%if_enabled    devel
%package       -n gem-async-rest-devel
Version:       0.13.0
Release:       alt1
Summary:       A library for RESTful clients (and hopefully servers) development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета async-rest
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(async-rest) = 0.13.0

%description   -n gem-async-rest-devel
A library for RESTful clients (and hopefully servers) development package.

Roy Thomas Fielding's thesis Architectural Styles and the Design of
Network-based Software Architectures describes Representational State Transfer
which comprises several core concepts:

* Resource: A conceptual mapping to one or more entities.
* Representation: An instance of a resource at a given point in time.

This gem models these abstractions as closely and practically as possible and
serves as a basis for building asynchronous web clients.

%description   -n gem-async-rest-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета async-rest.
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
%doc readme.md
%ruby_gemspec
%ruby_gemlibdir

%if_enabled    doc
%files         -n gem-async-rest-doc
%doc readme.md
%ruby_gemdocdir
%endif

%if_enabled    devel
%files         -n gem-async-rest-devel
%doc readme.md
%endif


%changelog
* Thu Jul 25 2024 Pavel Skrylev <majioa@altlinux.org> 0.13.0-alt1
- ^ 0.12.4 -> 0.13.0

* Fri Sep 03 2021 Pavel Skrylev <majioa@altlinux.org> 0.12.4-alt1
- + packaged gem with Ruby Policy 2.0
