%define        gemname faraday-http-cache

Name:          gem-faraday-http-cache
Version:       2.2.0
Release:       alt1
Summary:       A Faraday middleware that stores and validates cache expiration
License:       Apache 2.0
Group:         Development/Ruby
Url:           https://github.com/sourcelevel/faraday-http-cache
Vcs:           https://github.com/sourcelevel/faraday-http-cache.git
Packager:      Pavel Skrylev <majioa@altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
BuildRequires: gem(faraday) >= 0.8

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
Requires:      gem(faraday) >= 0.8
Provides:      gem(faraday-http-cache) = 2.2.0


%description
Middleware to handle HTTP caching


%package       -n gem-faraday-http-cache-doc
Version:       2.2.0
Release:       alt1
Summary:       A Faraday middleware that stores and validates cache expiration documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета faraday-http-cache
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(faraday-http-cache) = 2.2.0

%description   -n gem-faraday-http-cache-doc
A Faraday middleware that stores and validates cache expiration documentation
files.

Middleware to handle HTTP caching

%description   -n gem-faraday-http-cache-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета faraday-http-cache.


%package       -n gem-faraday-http-cache-devel
Version:       2.2.0
Release:       alt1
Summary:       A Faraday middleware that stores and validates cache expiration development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета faraday-http-cache
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(faraday-http-cache) = 2.2.0

%description   -n gem-faraday-http-cache-devel
A Faraday middleware that stores and validates cache expiration development
package.

Middleware to handle HTTP caching

%description   -n gem-faraday-http-cache-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета faraday-http-cache.


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

%files         -n gem-faraday-http-cache-doc
%doc README.md
%ruby_gemdocdir

%files         -n gem-faraday-http-cache-devel
%doc README.md


%changelog
* Fri May 06 2022 Pavel Skrylev <majioa@altlinux.org> 2.2.0-alt1
- + packaged gem with Ruby Policy 2.0
