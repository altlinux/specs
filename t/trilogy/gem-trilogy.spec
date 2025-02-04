%define        _unpackaged_files_terminate_build 1
%def_enable    check
%def_enable    doc
%def_enable    devel

Name:          trilogy
Version:       2.9.0
Release:       alt1
Summary:       A friendly MySQL-compatible library for Ruby, binding to libtrilogy
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/trilogy-libraries/trilogy
Vcs:           https://github.com/trilogy-libraries/trilogy.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
BuildRequires: openssl-devel
BuildRequires: gem(rake-compiler) >= 1.0
BuildConflicts: gem(rake-compiler) >= 2
%if_enabled check
BuildRequires: gem(benchmark-ips) >= 0
BuildRequires: gem(bigdecimal) >= 0
BuildRequires: gem(minitest) >= 5.5
BuildRequires: gem(mysql2) >= 0
BuildConflicts: gem(minitest) >= 6
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*

%description
A friendly MySQL-compatible library for Ruby, binding to libtrilogy.

Trilogy is a client library for MySQL-compatible database servers, designed for
performance, flexibility, and ease of embedding.

Features:
* Supports the most frequently used parts of the text protocol
  * Handshake
  * Password authentication
  * Query, ping, and quit commands
* Support prepared statements (binary protocol)
* Low-level protocol API completely decoupled from IO
* Non-blocking client API wrapping the protocol API
* Blocking client API wrapping the non-blocking API
* No dependencies outside of POSIX, the C standard library & OpenSSL
* Minimal dynamic allocation
* MIT licensed


%package       -n gem-trilogy
Version:       2.9.0
Release:       alt1
Summary:       A friendly MySQL-compatible library for Ruby, binding to libtrilogy
Group:         Development/Ruby
#BuildArch:     noarch

Requires:      gem(bigdecimal) >= 0
Requires:      gem(trilogy) >= 0
Provides:      gem(trilogy) = 2.9.0

%description   -n gem-trilogy
A friendly MySQL-compatible library for Ruby, binding to libtrilogy.

Trilogy is a client library for MySQL-compatible database servers, designed for
performance, flexibility, and ease of embedding.

Features:
* Supports the most frequently used parts of the text protocol
  * Handshake
  * Password authentication
  * Query, ping, and quit commands
* Support prepared statements (binary protocol)
* Low-level protocol API completely decoupled from IO
* Non-blocking client API wrapping the protocol API
* Blocking client API wrapping the non-blocking API
* No dependencies outside of POSIX, the C standard library & OpenSSL
* Minimal dynamic allocation
* MIT licensed


%if_enabled    doc
%package       -n gem-trilogy-doc
Version:       2.9.0
Release:       alt1
Summary:       A friendly MySQL-compatible library for Ruby, binding to libtrilogy documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета trilogy
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(trilogy) = 2.9.0

%description   -n gem-trilogy-doc
A friendly MySQL-compatible library for Ruby, binding to libtrilogy
documentation files.

Trilogy is a client library for MySQL-compatible database servers, designed for
performance, flexibility, and ease of embedding.

Features:
* Supports the most frequently used parts of the text protocol
  * Handshake
  * Password authentication
  * Query, ping, and quit commands
* Support prepared statements (binary protocol)
* Low-level protocol API completely decoupled from IO
* Non-blocking client API wrapping the protocol API
* Blocking client API wrapping the non-blocking API
* No dependencies outside of POSIX, the C standard library & OpenSSL
* Minimal dynamic allocation
* MIT licensed

%description   -n gem-trilogy-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета trilogy.
%endif


%if_enabled    devel
%package       -n gem-trilogy-devel
Version:       2.9.0
Release:       alt1
Summary:       A friendly MySQL-compatible library for Ruby, binding to libtrilogy development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета trilogy
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(trilogy) = 2.9.0
Requires:      gem(benchmark-ips) >= 0
Requires:      gem(bigdecimal) >= 0
Requires:      gem(minitest) >= 5.5
Requires:      gem(mysql2) >= 0
Requires:      gem(rake-compiler) >= 1.0
Requires:      gem(trilogy) >= 0
Conflicts:     gem(minitest) >= 6
Conflicts:     gem(rake-compiler) >= 2

%description   -n gem-trilogy-devel
A friendly MySQL-compatible library for Ruby, binding to libtrilogy development
package.

Trilogy is a client library for MySQL-compatible database servers, designed for
performance, flexibility, and ease of embedding.

Features:
* Supports the most frequently used parts of the text protocol
  * Handshake
  * Password authentication
  * Query, ping, and quit commands
* Support prepared statements (binary protocol)
* Low-level protocol API completely decoupled from IO
* Non-blocking client API wrapping the protocol API
* Blocking client API wrapping the non-blocking API
* No dependencies outside of POSIX, the C standard library & OpenSSL
* Minimal dynamic allocation
* MIT licensed

%description   -n gem-trilogy-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета trilogy.
%endif


%prep
%setup
mv contrib gem

%build
%make_build
%ruby_build

%install
%make_install
%ruby_install

%check
%ruby_test

%files
%doc LICENSE README.md

%files         -n gem-trilogy
%doc LICENSE README.md
%ruby_gemspecdir/trilogy-2.9.0.gemspec
%ruby_gemslibdir/trilogy-2.9.0
%ruby_gemsextdir/trilogy-2.9.0

%if_enabled    doc
%files         -n gem-trilogy-doc
%doc LICENSE README.md
%ruby_gemsdocdir/trilogy-2.9.0
%endif

%if_enabled    devel
%files         -n gem-trilogy-devel
%doc LICENSE README.md
%ruby_includedir/trilogy-ruby/
%endif


%changelog
* Tue Feb 04 2025 Pavel Skrylev <majioa@altlinux.org> 2.9.0-alt1
- + packaged gem with Ruby Policy 2.0
