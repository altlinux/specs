%define        gemname faraday-net_http_persistent

Name:          gem-faraday-net-http-persistent
Version:       1.1.0
Release:       alt1
Summary:       Faraday adapter for NetHttpPersistent
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/lostisland/faraday-net_http_persistent
Vcs:           https://github.com/lostisland/faraday-net_http_persistent.git
Packager:      Pavel Skrylev <majioa@altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
BuildRequires: gem(bundler) >= 2.0 gem(bundler) < 3
BuildRequires: gem(rake) >= 13.0 gem(rake) < 14
BuildRequires: gem(simplecov) >= 0.17 gem(simplecov) < 1

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_use_gem_dependency simplecov >= 0.17,simplecov < 1
Provides:      gem(faraday-net_http_persistent) = 1.1.0


%description
Faraday adapter for NetHttpPersistent.


%package       -n gem-faraday-net-http-persistent-doc
Version:       1.1.0
Release:       alt1
Summary:       Faraday adapter for NetHttpPersistent documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета faraday-net_http_persistent
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(faraday-net_http_persistent) = 1.1.0

%description   -n gem-faraday-net-http-persistent-doc
Faraday adapter for NetHttpPersistent documentation files.

Faraday adapter for NetHttpPersistent.

%description   -n gem-faraday-net-http-persistent-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета faraday-net_http_persistent.


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

%files         -n gem-faraday-net-http-persistent-doc
%doc README.md
%ruby_gemdocdir


%changelog
* Sat Jun 05 2021 Pavel Skrylev <majioa@altlinux.org> 1.1.0-alt1
- + packaged gem with Ruby Policy 2.0
