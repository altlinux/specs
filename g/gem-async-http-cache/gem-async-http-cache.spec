%define        gemname async-http-cache

Name:          gem-async-http-cache
Version:       0.4.3
Release:       alt1
Summary:       Standard-compliant cache for async-http
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/socketry/async-http-cache
Vcs:           https://github.com/socketry/async-http-cache.git
Packager:      Pavel Skrylev <majioa@altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
%if_with check
BuildRequires: gem(async-http) >= 0.56 gem(async-http) < 1
BuildRequires: gem(async-rspec) >= 1.10 gem(async-rspec) < 2
BuildRequires: gem(covered) >= 0
BuildRequires: gem(rspec) >= 0
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
Requires:      gem(async-http) >= 0.56 gem(async-http) < 1
Provides:      gem(async-http-cache) = 0.4.3

%description
Standard-compliant cache for async-http.


%package       -n gem-async-http-cache-doc
Version:       0.4.3
Release:       alt1
Summary:       Standard-compliant cache for async-http documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета async-http-cache
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(async-http-cache) = 0.4.3

%description   -n gem-async-http-cache-doc
Standard-compliant cache for async-http documentation files.

%description   -n gem-async-http-cache-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета async-http-cache.


%package       -n gem-async-http-cache-devel
Version:       0.4.3
Release:       alt1
Summary:       Standard-compliant cache for async-http development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета async-http-cache
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(async-http-cache) = 0.4.3
Requires:      gem(async-rspec) >= 1.10 gem(async-rspec) < 2
Requires:      gem(covered) >= 0
Requires:      gem(rspec) >= 0

%description   -n gem-async-http-cache-devel
Standard-compliant cache for async-http development package.

%description   -n gem-async-http-cache-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета async-http-cache.


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

%files         -n gem-async-http-cache-doc
%ruby_gemdocdir

%files         -n gem-async-http-cache-devel


%changelog
* Mon Oct 17 2022 Pavel Skrylev <majioa@altlinux.org> 0.4.3-alt1
- + packaged gem with Ruby Policy 2.0
