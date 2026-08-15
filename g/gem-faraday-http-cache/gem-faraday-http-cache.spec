%define        _unpackaged_files_terminate_build 1
%def_enable    check
%def_enable    doc
%def_enable    devel
%define        gemname faraday-http-cache

Name:          gem-faraday-http-cache
Version:       2.7.0
Release:       alt1
Summary:       A Faraday middleware that stores and validates cache expiration
License:       Apache-2.0
Group:         Development/Ruby
Url:           https://github.com/sourcelevel/faraday-http-cache
Vcs:           https://github.com/sourcelevel/faraday-http-cache.git
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-macros-ruby setup-rb rake
%if_enabled check
BuildRequires: gem(activesupport) >= 7.0
BuildRequires: gem(em-http-request) >= 1.1
BuildRequires: gem(faraday) >= 0.8
BuildRequires: gem(rackup) >= 0
BuildRequires: gem(rake) >= 13.0
BuildRequires: gem(rspec) >= 3.1
BuildRequires: gem(rubocop) >= 1.15.0
BuildRequires: gem(sinatra) >= 3.0
BuildRequires: gem(webrick) >= 0
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_use_gem_dependency rubocop >= 1.15.0,rubocop < 2
Requires:      ruby >= 3.2.0
Requires:      gem(faraday) >= 0.8
Provides:      gem(faraday-http-cache) = 2.7.0

%ruby_use_gem_version faraday-http-cache:2.7.0

%description
Middleware to handle HTTP caching


%if_enabled    doc
%package       -n gem-faraday-http-cache-doc
Version:       2.7.0
Release:       alt1
Summary:       A Faraday middleware that stores and validates cache expiration documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета faraday-http-cache
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(faraday-http-cache) = 2.7.0

%description   -n gem-faraday-http-cache-doc
A Faraday middleware that stores and validates cache expiration documentation
files.

Middleware to handle HTTP caching

%description   -n gem-faraday-http-cache-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета faraday-http-cache.
%endif


%if_enabled    devel
%package       -n gem-faraday-http-cache-devel
Version:       2.7.0
Release:       alt1
Summary:       A Faraday middleware that stores and validates cache expiration development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета faraday-http-cache
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(faraday-http-cache) = 2.7.0
Requires:      gem(activesupport) >= 7.0
Requires:      gem(em-http-request) >= 1.1
Requires:      gem(faraday) >= 0.8
Requires:      gem(rackup) >= 0
Requires:      gem(rake) >= 13.0
Requires:      gem(rspec) >= 3.1
Requires:      gem(rubocop) >= 1.15.0
Requires:      gem(sinatra) >= 3.0
Requires:      gem(webrick) >= 0

%description   -n gem-faraday-http-cache-devel
A Faraday middleware that stores and validates cache expiration development
package.

Middleware to handle HTTP caching

%description   -n gem-faraday-http-cache-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета faraday-http-cache.
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
%doc LICENSE README.md CHANGELOG.md CONTRIBUTING.md
%ruby_gemspec
%ruby_gemlibdir
%_logdir/%gemname

%if_enabled    doc
%files         -n gem-faraday-http-cache-doc
%doc LICENSE README.md CHANGELOG.md CONTRIBUTING.md
%ruby_gemdocdir
%endif

%if_enabled    devel
%files         -n gem-faraday-http-cache-devel
%doc LICENSE README.md CHANGELOG.md CONTRIBUTING.md
%endif


%changelog
* Fri Aug 14 2026 Pavel Skrylev <majioa@altlinux.org> 2.7.0-alt1
- ^ 2.2.0 -> 2.7.0

* Fri May 06 2022 Pavel Skrylev <majioa@altlinux.org> 2.2.0-alt1
- + packaged gem with Ruby Policy 2.0
