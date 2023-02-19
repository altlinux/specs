%define        gemname fakeredis

Name:          gem-fakeredis
Version:       0.8.0
Release:       alt1.1
Summary:       Fake (In-memory) driver for redis-rb
License:       MIT
Group:         Development/Ruby
Url:           https://guilleiguaran.github.com/fakeredis
Packager:      Pavel Skrylev <majioa@altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
%if_with check
BuildRequires: gem(rake) >= 0
BuildRequires: gem(rdoc) >= 0
BuildRequires: gem(racc) >= 0
BuildRequires: gem(rubysl) >= 2.0 gem(rubysl) < 3
BuildRequires: gem(psych) >= 0
BuildRequires: gem(rspec) >= 3.0 gem(rspec) < 4
BuildRequires: gem(redis) >= 4.1 gem(redis) < 6
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_use_gem_dependency redis >= 5.0,redis < 6
Requires:      gem(redis) >= 4.1 gem(redis) < 6
Provides:      gem(fakeredis) = 0.8.0


%description
Fake (In-memory) driver for redis-rb. Useful for testing environment and
machines without Redis.


%package       -n gem-fakeredis-doc
Version:       0.8.0
Release:       alt1.1
Summary:       Fake (In-memory) driver for redis-rb documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета fakeredis
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(fakeredis) = 0.8.0

%description   -n gem-fakeredis-doc
Fake (In-memory) driver for redis-rb documentation files.

Fake (In-memory) driver for redis-rb. Useful for testing environment and
machines without Redis.

%description   -n gem-fakeredis-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета fakeredis.


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

%files         -n gem-fakeredis-doc
%doc README.md
%ruby_gemdocdir


%changelog
* Sat Feb 04 2023 Pavel Skrylev <majioa@altlinux.org> 0.8.0-alt1.1
- ! fixed dep to redis

* Sun Oct 16 2022 Pavel Skrylev <majioa@altlinux.org> 0.8.0-alt1
- + packaged gem with Ruby Policy 2.0
