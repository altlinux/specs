%define        gemname async-rest

Name:          gem-async-rest
Version:       0.12.4
Release:       alt1
Summary:       A library for RESTful clients (and hopefully servers)
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/socketry/async-rest
Vcs:           https://github.com/socketry/async-rest.git
Packager:      Pavel Skrylev <majioa@altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
BuildRequires: gem(async-http) >= 0.42 gem(async-http) < 1
BuildRequires: gem(protocol-http) >= 0.7 gem(protocol-http) < 1
BuildRequires: gem(async-rspec) >= 1.1 gem(async-rspec) < 2
BuildRequires: gem(bundler) >= 0
# BuildRequires: gem(covered) >= 0
BuildRequires: gem(rake) >= 0
BuildRequires: gem(rspec) >= 3.6 gem(rspec) < 4

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
Requires:      gem(async-http) >= 0.42 gem(async-http) < 1
Requires:      gem(protocol-http) >= 0.7 gem(protocol-http) < 1
Provides:      gem(async-rest) = 0.12.4

%description
Roy Thomas Fielding's thesis Architectural Styles and the Design of
Network-based Software Architectures describes Representational State Transfer
which comprises several core concepts:

* Resource: A conceptual mapping to one or more entities.
* Representation: An instance of a resource at a given point in time.

This gem models these abstractions as closely and practically as possible and
serves as a basis for building asynchronous web clients.


%package       -n gem-async-rest-doc
Version:       0.12.4
Release:       alt1
Summary:       A library for RESTful clients (and hopefully servers) documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета async-rest
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(async-rest) = 0.12.4

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


%package       -n gem-async-rest-devel
Version:       0.12.4
Release:       alt1
Summary:       A library for RESTful clients (and hopefully servers) development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета async-rest
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(async-rest) = 0.12.4
Requires:      gem(async-rspec) >= 1.1 gem(async-rspec) < 2
Requires:      gem(bundler) >= 0 gem(bundler) < 3
Requires:      gem(covered) >= 0
Requires:      gem(rake) >= 0 gem(rake) < 14
Requires:      gem(rspec) >= 3.6 gem(rspec) < 4

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


%prep
%setup

%build
%ruby_build

%install
%ruby_install

%check
%ruby_test

%files
%ruby_gemspec
%ruby_gemlibdir

%files         -n gem-async-rest-doc
%ruby_gemdocdir

%files         -n gem-async-rest-devel


%changelog
* Fri Sep 03 2021 Pavel Skrylev <majioa@altlinux.org> 0.12.4-alt1
- + packaged gem with Ruby Policy 2.0
