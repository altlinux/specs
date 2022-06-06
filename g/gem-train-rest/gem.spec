%define        gemname train-rest

Name:          gem-train-rest
Version:       0.4.2
Release:       alt1
Summary:       Train transport for REST
License:       Apache-2.0
Group:         Development/Ruby
Url:           https://github.com/tecracer-chef/train-rest
Vcs:           https://github.com/tecracer-chef/train-rest.git
Packager:      Pavel Skrylev <majioa@altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
BuildRequires: gem(train-core) >= 3.0 gem(train-core) < 4
BuildRequires: gem(rest-client) >= 2.1 gem(rest-client) < 3
BuildRequires: gem(bump) >= 0.9 gem(bump) < 1
BuildRequires: gem(chefstyle) >= 2.2 gem(chefstyle) < 3
# BuildRequires: gem(guard) >= 2.16 gem(guard) < 3
# BuildRequires: gem(mdl) >= 0.9 gem(mdl) < 1
BuildRequires: gem(rake) >= 13.0 gem(rake) < 14

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_ignore_names omnibus,kitchen-tests
Requires:      gem(train-core) >= 3.0 gem(train-core) < 4
Requires:      gem(rest-client) >= 2.1 gem(rest-client) < 3
Provides:      gem(train-rest) = 0.4.2


%description
Provides a transport to communicate easily with RESTful APIs.


%package       -n gem-train-rest-doc
Version:       0.4.2
Release:       alt1
Summary:       Train transport for REST documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета train-rest
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(train-rest) = 0.4.2

%description   -n gem-train-rest-doc
Train transport for REST documentation files.

Provides a transport to communicate easily with RESTful APIs.

%description   -n gem-train-rest-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета train-rest.


%package       -n gem-train-rest-devel
Version:       0.4.2
Release:       alt1
Summary:       Train transport for REST development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета train-rest
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(train-rest) = 0.4.2
Requires:      gem(bump) >= 0.9 gem(bump) < 1
Requires:      gem(chefstyle) >= 2.2 gem(chefstyle) < 3
# Requires:      gem(guard) >= 2.16 gem(guard) < 3
# Requires:      gem(mdl) >= 0.9 gem(mdl) < 1
Requires:      gem(rake) >= 13.0 gem(rake) < 14

%description   -n gem-train-rest-devel
Train transport for REST development package.

Provides a transport to communicate easily with RESTful APIs.

%description   -n gem-train-rest-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета train-rest.


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

%files         -n gem-train-rest-doc
%ruby_gemdocdir

%files         -n gem-train-rest-devel


%changelog
* Thu Apr 21 2022 Pavel Skrylev <majioa@altlinux.org> 0.4.2-alt1
- + packaged gem with Ruby Policy 2.0
