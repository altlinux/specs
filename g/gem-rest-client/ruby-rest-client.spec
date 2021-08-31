%define        gemname rest-client

Name:          gem-rest-client
Version:       2.1.0
Release:       alt1.1
Summary:       Simple REST client for Ruby
License:       MIT
Group:         Development/Ruby
Url:           http://github.com/archiloque/rest-client
Vcs:           https://github.com/archiloque/rest-client.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
BuildRequires: gem(webmock) >= 2.0 gem(webmock) < 4
BuildRequires: gem(rspec) >= 3.0 gem(rspec) < 4
BuildRequires: gem(pry) >= 0
BuildRequires: gem(pry-doc) >= 0
BuildRequires: gem(rdoc) >= 2.4.2 gem(rdoc) < 7
BuildRequires: gem(rubocop) >= 0.49 gem(rubocop) < 2
BuildRequires: gem(http-accept) >= 1.7.0 gem(http-accept) < 2.0
BuildRequires: gem(http-cookie) >= 1.0.2 gem(http-cookie) < 2.0
BuildRequires: gem(mime-types) >= 1.16 gem(mime-types) < 4.0
BuildRequires: gem(netrc) >= 0.8 gem(netrc) < 1

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_use_gem_dependency webmock >= 3.13.0,webmock < 4
%ruby_use_gem_dependency rdoc >= 6.1.1,rdoc < 7
%ruby_use_gem_dependency rubocop >= 1.15.0,rubocop < 2
%ruby_alias_names restclient,rest-client
Requires:      gem(http-accept) >= 1.7.0 gem(http-accept) < 2.0
Requires:      gem(http-cookie) >= 1.0.2 gem(http-cookie) < 2.0
Requires:      gem(mime-types) >= 1.16 gem(mime-types) < 4.0
Requires:      gem(netrc) >= 0.8 gem(netrc) < 1
Obsoletes:     ruby-rest-client < %EVR
Provides:      ruby-rest-client = %EVR
Provides:      gem(rest-client) = 2.1.0


%description
A simple Simple HTTP and REST client for Ruby, inspired by the Sinatra
microframework style of specifying actions: get, put, post, delete.


%package       -n restclient
Version:       2.1.0
Release:       alt1.1
Summary:       Simple REST client for Ruby executable(s)
Summary(ru_RU.UTF-8): Исполнямка для самоцвета rest-client
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(rest-client) = 2.1.0

%description   -n restclient
Simple REST client for Ruby executable(s).

A simple Simple HTTP and REST client for Ruby, inspired by the Sinatra
microframework style of specifying actions: get, put, post, delete.

%description   -n restclient -l ru_RU.UTF-8
Исполнямка для самоцвета rest-client.


%package       -n gem-rest-client-doc
Version:       2.1.0
Release:       alt1.1
Summary:       Simple REST client for Ruby documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета rest-client
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(rest-client) = 2.1.0

%description   -n gem-rest-client-doc
Simple REST client for Ruby documentation files.

A simple Simple HTTP and REST client for Ruby, inspired by the Sinatra
microframework style of specifying actions: get, put, post, delete.

%description   -n gem-rest-client-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета rest-client.


%package       -n gem-rest-client-devel
Version:       2.1.0
Release:       alt1.1
Summary:       Simple REST client for Ruby development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета rest-client
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(rest-client) = 2.1.0
Requires:      gem(webmock) >= 2.0 gem(webmock) < 4
Requires:      gem(rspec) >= 3.0 gem(rspec) < 4
Requires:      gem(pry) >= 0
Requires:      gem(pry-doc) >= 0
Requires:      gem(rdoc) >= 2.4.2 gem(rdoc) < 7
Requires:      gem(rubocop) >= 0.49 gem(rubocop) < 2

%description   -n gem-rest-client-devel
Simple REST client for Ruby development package.

A simple Simple HTTP and REST client for Ruby, inspired by the Sinatra
microframework style of specifying actions: get, put, post, delete.

%description   -n gem-rest-client-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета rest-client.


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

%files         -n restclient
%doc README.md
%_bindir/restclient

%files         -n gem-rest-client-doc
%doc README.md
%ruby_gemdocdir

%files         -n gem-rest-client-devel
%doc README.md


%changelog
* Sun Jul 18 2021 Pavel Skrylev <majioa@altlinux.org> 2.1.0-alt1.1
- ! spec

* Tue Sep 24 2019 Pavel Skrylev <majioa@altlinux.org> 2.1.0-alt1
- update (^) 2.0.2 -> 2.1.0
- update to (^) Ruby Policy 2.0

* Fri Aug 31 2018 Andrey Cherepanov <cas@altlinux.org> 2.0.2-alt1
- New version.

* Wed Jul 11 2018 Andrey Cherepanov <cas@altlinux.org> 1.6.6-alt1.2
- Rebuild with new Ruby autorequirements.

* Fri Dec 07 2012 Led <led@altlinux.ru> 1.6.6-alt1.1
- Rebuilt with ruby-1.9.3-alt1
- cleaned up BuildRequires

* Sat Apr 14 2012 Evgeny Sinelnikov <sin@altlinux.ru> 1.6.6-alt1
- Initial build for Sisyphus
