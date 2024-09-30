%define        _unpackaged_files_terminate_build 1
%def_enable    check
%def_enable    doc
%def_enable    devel
%define        gemname net-http-persistent

Name:          gem-net-http-persistent
Version:       4.0.4
Release:       alt1
Summary:       Thread-safe persistent connections with Net::HTTP
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/drbrain/net-http-persistent
Vcs:           https://github.com/drbrain/net-http-persistent.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
%if_enabled check
BuildRequires: gem(rake) >= 13.0
BuildRequires: gem(minitest) >= 5.15
BuildRequires: gem(rdoc) >= 4.0
BuildRequires: gem(rake-manifest) >= 0.2
BuildRequires: gem(connection_pool) >= 2.2
BuildConflicts: gem(rake) >= 14
BuildConflicts: gem(minitest) >= 6
BuildConflicts: gem(rdoc) >= 7
BuildConflicts: gem(rake-manifest) >= 1
BuildConflicts: gem(connection_pool) >= 3
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
Requires:      gem(connection_pool) >= 2.2
Conflicts:     gem(connection_pool) >= 3
Obsoletes:     ruby-net-http-persistent < %EVR
Provides:      ruby-net-http-persistent = %EVR
Provides:      gem(net-http-persistent) = 4.0.4


%description
Manages persistent connections using Net::HTTP plus a speed fix for Ruby 1.8.
It's thread-safe too!

Using persistent HTTP connections can dramatically increase the speed of HTTP.
Creating a new HTTP connection for every request involves an extra TCP
round-trip and causes TCP congestion avoidance negotiation to start
over.

Net::HTTP supports persistent connections with some API methods but does not
handle reconnection gracefully. Net::HTTP::Persistent supports reconnection and
retry according to RFC 2616.


%if_enabled    doc
%package       -n gem-net-http-persistent-doc
Version:       4.0.4
Release:       alt1
Summary:       Thread-safe persistent connections with Net::HTTP documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета net-http-persistent
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(net-http-persistent) = 4.0.4

%description   -n gem-net-http-persistent-doc
Thread-safe persistent connections with Net::HTTP documentation files.

Manages persistent connections using Net::HTTP plus a speed fix for Ruby 1.8.
It's thread-safe too!

Using persistent HTTP connections can dramatically increase the speed of HTTP.
Creating a new HTTP connection for every request involves an extra TCP
round-trip and causes TCP congestion avoidance negotiation to start
over.

Net::HTTP supports persistent connections with some API methods but does not
handle reconnection gracefully. Net::HTTP::Persistent supports reconnection and
retry according to RFC 2616.

%description   -n gem-net-http-persistent-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета net-http-persistent.
%endif


%if_enabled    devel
%package       -n gem-net-http-persistent-devel
Version:       4.0.4
Release:       alt1
Summary:       Thread-safe persistent connections with Net::HTTP development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета net-http-persistent
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(net-http-persistent) = 4.0.4
Requires:      gem(rake) >= 13.0
Requires:      gem(minitest) >= 5.15
Requires:      gem(rdoc) >= 4.0
Requires:      gem(rake-manifest) >= 0.2
Conflicts:     gem(rake) >= 14
Conflicts:     gem(minitest) >= 6
Conflicts:     gem(rdoc) >= 7
Conflicts:     gem(rake-manifest) >= 1

%description   -n gem-net-http-persistent-devel
Thread-safe persistent connections with Net::HTTP development package.

Manages persistent connections using Net::HTTP plus a speed fix for Ruby 1.8.
It's thread-safe too!

Using persistent HTTP connections can dramatically increase the speed of HTTP.
Creating a new HTTP connection for every request involves an extra TCP
round-trip and causes TCP congestion avoidance negotiation to start
over.

Net::HTTP supports persistent connections with some API methods but does not
handle reconnection gracefully. Net::HTTP::Persistent supports reconnection and
retry according to RFC 2616.

%description   -n gem-net-http-persistent-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета net-http-persistent.
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
%files         -n gem-net-http-persistent-doc
%doc README.rdoc
%ruby_gemdocdir
%endif

%if_enabled    devel
%files         -n gem-net-http-persistent-devel
%doc README.rdoc
%endif


%changelog
* Fri Sep 27 2024 Pavel Skrylev <majioa@altlinux.org> 4.0.4-alt1
- ^ 4.0.1 -> 4.0.4

* Thu Mar 17 2022 Pavel Skrylev <majioa@altlinux.org> 4.0.1-alt1
- ^ 4.0.0 -> 4.0.1

* Mon May 25 2020 Pavel Skrylev <majioa@altlinux.org> 4.0.0-alt0.1
- ^ 3.0.1 -> 4.0.0
- ! spec tags

* Fri Jul 19 2019 Pavel Skrylev <majioa@altlinux.org> 3.0.1-alt1
- > Ruby Policy 2.0
- ^ 3.0.0 -> 3.0.1

* Wed Jul 11 2018 Andrey Cherepanov <cas@altlinux.org> 3.0.0-alt1.1
- Rebuild with new Ruby autorequirements.

* Thu Jun 14 2018 Andrey Cherepanov <cas@altlinux.org> 3.0.0-alt1
- Initial build for Sisyphus
