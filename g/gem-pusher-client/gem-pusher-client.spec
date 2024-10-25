%define        _unpackaged_files_terminate_build 1
%def_enable    check
%def_enable    doc
%def_enable    devel
%define        gemname pusher-client

Name:          gem-pusher-client
Version:       0.6.2
Release:       alt1
Summary:       Client for consuming WebSockets from http://pusher.com
License:       MIT
Group:         Development/Ruby
Url:           http://github.com/pusher/pusher-ruby-client
Vcs:           https://github.com/pusher/pusher-ruby-client.git
Packager:      Pavel Skrylev <majioa@altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
%if_enabled check
BuildRequires: gem(rspec) >= 0
BuildRequires: gem(rake) >= 0
BuildRequires: gem(bundler) >= 0
BuildRequires: gem(websocket) >= 1.0
BuildRequires: gem(json) >= 0
BuildConflicts: gem(websocket) >= 2
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
Requires:      gem(websocket) >= 1.0
Requires:      gem(json) >= 0
Conflicts:     gem(websocket) >= 2
Provides:      gem(pusher-client) = 0.6.2


%description
Client for consuming WebSockets from http://pusher.com


%if_enabled    doc
%package       -n gem-pusher-client-doc
Version:       0.6.2
Release:       alt1
Summary:       Client for consuming WebSockets from http://pusher.com documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета pusher-client
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(pusher-client) = 0.6.2

%description   -n gem-pusher-client-doc
Client for consuming WebSockets from http://pusher.com documentation files.

%description   -n gem-pusher-client-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета pusher-client.
%endif


%if_enabled    devel
%package       -n gem-pusher-client-devel
Version:       0.6.2
Release:       alt1
Summary:       Client for consuming WebSockets from http://pusher.com development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета pusher-client
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(pusher-client) = 0.6.2
Requires:      gem(rspec) >= 0
Requires:      gem(rake) >= 0
Requires:      gem(bundler) >= 0

%description   -n gem-pusher-client-devel
Client for consuming WebSockets from http://pusher.com development package.

%description   -n gem-pusher-client-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета pusher-client.
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
%doc README.rdoc
%ruby_gemspec
%ruby_gemlibdir

%if_enabled    doc
%files         -n gem-pusher-client-doc
%doc README.rdoc
%ruby_gemdocdir
%endif

%if_enabled    devel
%files         -n gem-pusher-client-devel
%doc README.rdoc
%endif


%changelog
* Fri Oct 18 2024 Pavel Skrylev <majioa@altlinux.org> 0.6.2-alt1
- + packaged gem with Ruby Policy 2.0
