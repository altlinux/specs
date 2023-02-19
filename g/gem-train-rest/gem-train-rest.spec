%define        gemname train-rest

Name:          gem-train-rest
Version:       0.5.0
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
%if_with check
BuildRequires: gem(bump) >= 0.9
BuildRequires: gem(chefstyle) >= 2.2
BuildRequires: gem(guard) >= 2.16
BuildRequires: gem(mdl) >= 0.9
BuildRequires: gem(rake) >= 13.0
BuildRequires: gem(aws-sigv4) >= 1.5
BuildRequires: gem(train-core) >= 3.0
BuildRequires: gem(rest-client) >= 2.1
BuildConflicts: gem(bump) >= 1
BuildConflicts: gem(chefstyle) >= 3
BuildConflicts: gem(guard) >= 3
BuildConflicts: gem(mdl) >= 1
BuildConflicts: gem(rake) >= 14
BuildConflicts: gem(aws-sigv4) >= 2
BuildConflicts: gem(train-core) >= 4
BuildConflicts: gem(rest-client) >= 3
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
Requires:      gem(aws-sigv4) >= 1.5
Requires:      gem(train-core) >= 3.0
Requires:      gem(rest-client) >= 2.1
Conflicts:     gem(aws-sigv4) >= 2
Conflicts:     gem(train-core) >= 4
Conflicts:     gem(rest-client) >= 3
Provides:      gem(train-rest) = 0.5.0


%description
Provides a transport to communicate easily with RESTful APIs.


%package       -n gem-train-rest-doc
Version:       0.5.0
Release:       alt1
Summary:       Train transport for REST documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета train-rest
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(train-rest) = 0.5.0

%description   -n gem-train-rest-doc
Train transport for REST documentation files.

Provides a transport to communicate easily with RESTful APIs.

%description   -n gem-train-rest-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета train-rest.


%package       -n gem-train-rest-devel
Version:       0.5.0
Release:       alt1
Summary:       Train transport for REST development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета train-rest
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(train-rest) = 0.5.0
Requires:      gem(bump) >= 0.9
Requires:      gem(chefstyle) >= 2.2
Requires:      gem(mdl) >= 0.9
Requires:      gem(rake) >= 13.0
Conflicts:     gem(bump) >= 1
Conflicts:     gem(chefstyle) >= 3
Conflicts:     gem(mdl) >= 1
Conflicts:     gem(rake) >= 14

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
%doc README.md
%ruby_gemspec
%ruby_gemlibdir

%files         -n gem-train-rest-doc
%doc README.md
%ruby_gemdocdir

%files         -n gem-train-rest-devel
%doc README.md


%changelog
* Sat Jan 28 2023 Pavel Skrylev <majioa@altlinux.org> 0.5.0-alt1
- ^ 0.4.2 -> 0.5.0

* Thu Apr 21 2022 Pavel Skrylev <majioa@altlinux.org> 0.4.2-alt1
- + packaged gem with Ruby Policy 2.0
