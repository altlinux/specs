%define        gemname sus-fixtures-async

Name:          gem-sus-fixtures-async
Version:       0.1.1
Release:       alt1
Summary:       Test fixtures for running in Async
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/ioquatix/sus-fixtures-async
Vcs:           https://github.com/ioquatix/sus-fixtures-async.git
Packager:      Pavel Skrylev <majioa@altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
%if_with check
BuildRequires: gem(async) >= 0
BuildRequires: gem(sus) >= 0.10 gem(sus) < 1
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
Requires:      gem(async) >= 0
Requires:      gem(sus) >= 0.10 gem(sus) < 1
Provides:      gem(sus-fixtures-async) = 0.1.1


%description
Test fixtures for running in Async.


%package       -n gem-sus-fixtures-async-doc
Version:       0.1.1
Release:       alt1
Summary:       Test fixtures for running in Async documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета sus-fixtures-async
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(sus-fixtures-async) = 0.1.1

%description   -n gem-sus-fixtures-async-doc
Test fixtures for running in Async documentation files.

%description   -n gem-sus-fixtures-async-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета sus-fixtures-async.


%package       -n gem-sus-fixtures-async-devel
Version:       0.1.1
Release:       alt1
Summary:       Test fixtures for running in Async development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета sus-fixtures-async
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(sus-fixtures-async) = 0.1.1

%description   -n gem-sus-fixtures-async-devel
Test fixtures for running in Async development package.

%description   -n gem-sus-fixtures-async-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета sus-fixtures-async.


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

%files         -n gem-sus-fixtures-async-doc
%doc readme.md
%ruby_gemdocdir

%files         -n gem-sus-fixtures-async-devel
%doc readme.md


%changelog
* Mon Oct 17 2022 Pavel Skrylev <majioa@altlinux.org> 0.1.1-alt1
- + packaged gem with Ruby Policy 2.0
