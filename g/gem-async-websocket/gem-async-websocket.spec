%define        gemname async-websocket

Name:          gem-async-websocket
Version:       0.22.1
Release:       alt1
Summary:       An async websocket library on top of websocket-driver
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/socketry/async-websocket
Vcs:           https://github.com/socketry/async-websocket.git
Packager:      Pavel Skrylev <majioa@altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
%if_with check
BuildRequires: gem(async-http) >= 0.54 gem(async-http) < 1
BuildRequires: gem(async-io) >= 1.23 gem(async-io) < 2
BuildRequires: gem(protocol-rack) >= 0.1 gem(protocol-rack) < 1
BuildRequires: gem(protocol-websocket) >= 0.9.1 gem(protocol-websocket) < 0.10
BuildRequires: gem(bundler) >= 0
BuildRequires: gem(covered) >= 0
BuildRequires: gem(sus) >= 0.12.0 gem(sus) < 1
BuildRequires: gem(sus-fixtures-async-http) >= 0.2.3 gem(sus-fixtures-async-http) < 0.3
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_use_gem_dependency sus >= 0.14.0,sus < 1
Requires:      gem(async-http) >= 0.54 gem(async-http) < 1
Requires:      gem(async-io) >= 1.23 gem(async-io) < 2
Requires:      gem(protocol-rack) >= 0.1 gem(protocol-rack) < 1
Requires:      gem(protocol-websocket) >= 0.9.1 gem(protocol-websocket) < 0.10
Provides:      gem(async-websocket) = 0.22.1

%description
An async websocket library on top of websocket-driver.


%package       -n gem-async-websocket-doc
Version:       0.22.1
Release:       alt1
Summary:       An async websocket library on top of websocket-driver documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета async-websocket
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(async-websocket) = 0.22.1

%description   -n gem-async-websocket-doc
An async websocket library on top of websocket-driver documentation files.

%description   -n gem-async-websocket-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета async-websocket.


%package       -n gem-async-websocket-devel
Version:       0.22.1
Release:       alt1
Summary:       An async websocket library on top of websocket-driver development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета async-websocket
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(async-websocket) = 0.22.1
Requires:      gem(bundler) >= 0
Requires:      gem(covered) >= 0
Requires:      gem(sus) >= 0.12.0 gem(sus) < 1
Requires:      gem(sus-fixtures-async-http) >= 0.2.3 gem(sus-fixtures-async-http) < 0.3

%description   -n gem-async-websocket-devel
An async websocket library on top of websocket-driver development package.

%description   -n gem-async-websocket-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета async-websocket.


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

%files         -n gem-async-websocket-doc
%doc readme.md
%ruby_gemdocdir

%files         -n gem-async-websocket-devel
%doc readme.md


%changelog
* Mon Oct 17 2022 Pavel Skrylev <majioa@altlinux.org> 0.22.1-alt1
- + packaged gem with Ruby Policy 2.0
