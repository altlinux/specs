%define        _unpackaged_files_terminate_build 1
%def_enable    check
%def_enable    doc
%def_enable    devel
%define        gemname memcached

Name:          gem-memcached
Version:       2.0.0.20
Release:       alt0.1
Summary:       A Ruby interface to the libmemcached C client
License:       AFL-3.0
Group:         Development/Ruby
Url:           https://github.com/arthurnn/memcached
Vcs:           https://github.com/arthurnn/memcached.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>

Source:        %name-%version.tar
Patch:         allow-use-system-libraries-arg.patch
BuildRequires(pre): rpm-build-ruby
%if_enabled check
BuildRequires: gem(rake) >= 0
BuildRequires: gem(minitest) >= 0
BuildRequires: gem(mocha) >= 0
BuildRequires: gem(activesupport) >= 0
BuildRequires: gem(rake-compiler) >= 0
BuildRequires: gem(remix-stash) >= 1.1.3
BuildRequires: gem(dalli) >= 0
BuildRequires: gem(memcache-client) >= 0
BuildConflicts: gem(remix-stash) >= 1.2
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
Obsoletes:     ruby-memcached < %EVR
Provides:      ruby-memcached = %EVR
Provides:      gem(memcached) = 2.0.0.20

%ruby_use_gem_version memcached:2.0.0.20

%description
An interface to the libmemcached C client.

Features:
* clean API
* robust access to all memcached features
* SASL support for the binary protocol
* multiple hashing modes, including consistent hashing
* ludicrous speed, including optional pipelined IO with no_reply

The memcached library wraps the pure-C libmemcached client via SWIG.


%if_enabled    doc
%package       -n gem-memcached-doc
Version:       2.0.0.20
Release:       alt0.1
Summary:       A Ruby interface to the libmemcached C client documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета memcached
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(memcached) = 2.0.0.20

%description   -n gem-memcached-doc
A Ruby interface to the libmemcached C client documentation files.

An interface to the libmemcached C client.

Features:
* clean API
* robust access to all memcached features
* SASL support for the binary protocol
* multiple hashing modes, including consistent hashing
* ludicrous speed, including optional pipelined IO with no_reply

The memcached library wraps the pure-C libmemcached client via SWIG.

%description   -n gem-memcached-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета memcached.
%endif


%if_enabled    devel
%package       -n gem-memcached-devel
Version:       2.0.0.20
Release:       alt0.1
Summary:       A Ruby interface to the libmemcached C client development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета memcached
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(memcached) = 2.0.0.20
Requires:      gem(rake) >= 0
Requires:      gem(minitest) >= 0
Requires:      gem(mocha) >= 0
Requires:      gem(activesupport) >= 0
Requires:      gem(rake-compiler) >= 0
Requires:      gem(remix-stash) >= 1.1.3
Requires:      gem(dalli) >= 0
Requires:      gem(memcache-client) >= 0
Requires:      libsasl2-devel
Requires:      libstdc++-devel
Requires:      libmemcached-devel
Requires:      gnu-config
Conflicts:     gem(remix-stash) >= 1.2

%description   -n gem-memcached-devel
A Ruby interface to the libmemcached C client development package.

An interface to the libmemcached C client.

Features:
* clean API
* robust access to all memcached features
* SASL support for the binary protocol
* multiple hashing modes, including consistent hashing
* ludicrous speed, including optional pipelined IO with no_reply

The memcached library wraps the pure-C libmemcached client via SWIG.

%description   -n gem-memcached-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета memcached.
%endif


%prep
%setup
%autopatch

%build
%ruby_build

%install
%ruby_install

%check
%ruby_test

%files
%doc README.md vendor/libmemcached-1.0.18/README vendor/libmemcached-1.0.18/README.FIRST vendor/libmemcached-1.0.18/README.win32 vendor/libmemcached-1.0.18/libmemcached/memcached/README.txt
%ruby_gemspec
%ruby_gemlibdir
%ruby_gemextdir

%if_enabled    doc
%files         -n gem-memcached-doc
%doc README.md vendor/libmemcached-1.0.18/README vendor/libmemcached-1.0.18/README.FIRST vendor/libmemcached-1.0.18/README.win32 vendor/libmemcached-1.0.18/libmemcached/memcached/README.txt
%ruby_gemdocdir
%endif

%if_enabled    devel
%files         -n gem-memcached-devel
%doc README.md vendor/libmemcached-1.0.18/README vendor/libmemcached-1.0.18/README.FIRST vendor/libmemcached-1.0.18/README.win32 vendor/libmemcached-1.0.18/libmemcached/memcached/README.txt
%ruby_includedir/*
%endif


%changelog
* Thu Jul 25 2024 Pavel Skrylev <majioa@altlinux.org> 2.0.0.20-alt0.1
- ^ 2.0.0 -> 2.0.0p20

* Wed Apr 01 2020 Pavel Skrylev <majioa@altlinux.org> 2.0.0-alt1.1
- ! spec tags and syntax

* Tue Apr 30 2019 Pavel Skrylev <majioa@altlinux.org> 2.0.0-alt1
- > Ruby Policy 2.0
- ^ 1.8.0 -> 2.0.0alpha

* Mon Jun 18 2018 Andrey Cherepanov <cas@altlinux.org> 1.8.0-alt1
- Initial build for Sisyphus
