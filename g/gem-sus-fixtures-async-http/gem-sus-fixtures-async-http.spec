%define        gemname sus-fixtures-async-http

Name:          gem-sus-fixtures-async-http
Version:       0.2.3
Release:       alt1
Summary:       Test fixtures for running in Async::HTTP
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/ioquatix/sus-fixtures-async
Vcs:           https://github.com/ioquatix/sus-fixtures-async.git
Packager:      Pavel Skrylev <majioa@altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
BuildRequires: gem(sus-fixtures-async) >= 0.1 gem(sus-fixtures-async) < 1
%if_with check
BuildRequires: gem(async-io) >= 1.34 gem(async-io) < 2
BuildRequires: gem(sus) >= 0.10 gem(sus) < 1
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
Requires:      gem(async-io) >= 1.34 gem(async-io) < 2
Requires:      gem(sus) >= 0.10 gem(sus) < 1
Requires:      gem(sus-fixtures-async) >= 0.1 gem(sus-fixtures-async) < 1
Provides:      gem(sus-fixtures-async-http) = 0.2.3


%description
Test fixtures for running in Async::HTTP.


%package       -n gem-sus-fixtures-async-http-doc
Version:       0.2.3
Release:       alt1
Summary:       Test fixtures for running in Async::HTTP documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета sus-fixtures-async-http
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(sus-fixtures-async-http) = 0.2.3

%description   -n gem-sus-fixtures-async-http-doc
Test fixtures for running in Async::HTTP documentation files.

%description   -n gem-sus-fixtures-async-http-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета sus-fixtures-async-http.


%package       -n gem-sus-fixtures-async-http-devel
Version:       0.2.3
Release:       alt1
Summary:       Test fixtures for running in Async::HTTP development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета sus-fixtures-async-http
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(sus-fixtures-async-http) = 0.2.3

%description   -n gem-sus-fixtures-async-http-devel
Test fixtures for running in Async::HTTP development package.

%description   -n gem-sus-fixtures-async-http-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета sus-fixtures-async-http.


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

%files         -n gem-sus-fixtures-async-http-doc
%ruby_gemdocdir

%files         -n gem-sus-fixtures-async-http-devel


%changelog
* Mon Oct 17 2022 Pavel Skrylev <majioa@altlinux.org> 0.2.3-alt1
- + packaged gem with Ruby Policy 2.0
