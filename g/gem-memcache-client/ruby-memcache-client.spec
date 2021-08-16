%define        gemname memcache-client

Name:          gem-memcache-client
Version:       1.8.5.1
Release:       alt0.1
Summary:       Ruby client for Danga Interactive's memcached
License:       BSD-3-Clause
Group:         Development/Ruby
Url:           https://github.com/mperham/memcache-client
Vcs:           https://github.com/mperham/memcache-client.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
Patch:         version.patch
BuildRequires(pre): rpm-build-ruby

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
Obsoletes:     ruby-memcache-client < %EVR
Provides:      ruby-memcache-client = %EVR
Provides:      gem(memcache-client) = 1.8.5.1


%description
memcache-client is a client for Danga Interactive's memcached.


%package       -n memcached-top
Version:       1.8.5.1
Release:       alt0.1
Summary:       Ruby client for Danga Interactive's memcached executable(s)
Summary(ru_RU.UTF-8): Исполнямка для самоцвета memcache-client
Group:         Other
BuildArch:     noarch

Requires:      gem(memcache-client) = 1.8.5.1

%description   -n memcached-top
Ruby client for Danga Interactive's memcached executable(s).

memcache-client is a client for Danga Interactive's memcached.

%description   -n memcached-top -l ru_RU.UTF-8
Исполнямка для самоцвета memcache-client.


%package       -n gem-memcache-client-doc
Version:       1.8.5.1
Release:       alt0.1
Summary:       Ruby client for Danga Interactive's memcached documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета memcache-client
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(memcache-client) = 1.8.5.1

%description   -n gem-memcache-client-doc
Ruby client for Danga Interactive's memcached documentation
files.

memcache-client is a client for Danga Interactive's memcached.

%description   -n gem-memcache-client-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета memcache-client.


%prep
%setup
%patch

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

%files         -n memcached-top
%doc README.rdoc
%_bindir/memcached_top

%files         -n gem-memcache-client-doc
%doc README.rdoc
%ruby_gemdocdir


%changelog
* Fri Jun 11 2021 Pavel Skrylev <majioa@altlinux.org> 1.8.5.1-alt0.1
- ^ 1.7.8 -> 1.8.5[1]

* Mon Apr 15 2019 Mikhail Gordeev <obirvalger@altlinux.org> 1.7.8-alt1
- Update to 1.7.8
- Move to the new scheme

* Wed Jul 11 2018 Andrey Cherepanov <cas@altlinux.org> 1.7.4-alt1.3
- Rebuild with new Ruby autorequirements.

* Tue Sep 05 2017 Andrey Cherepanov <cas@altlinux.org> 1.7.4-alt1.2
- Rebuild with Ruby 2.4.1

* Sat Dec 08 2012 Led <led@altlinux.ru> 1.7.4-alt1.1
- Rebuilt with ruby-1.9.3-alt1
- fixed BuildRequires

* Fri Jun 26 2009 Alexey I. Froloff <raorn@altlinux.org> 1.7.4-alt1
- [1.7.4]

* Tue Jul 08 2008 Sir Raorn <raorn@altlinux.ru> 1.5.0-alt1
- Built for Sisyphus
