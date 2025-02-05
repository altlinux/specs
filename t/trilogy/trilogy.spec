%define        _unpackaged_files_terminate_build 1
%def_enable    check
%def_enable    doc
%def_enable    devel

Name:          trilogy
Version:       2.9.0.10
Release:       alt0.1
Summary:       A friendly MySQL-compatible client library
License:       MIT
Group:         Databases
Url:           https://github.com/trilogy-libraries/trilogy
Vcs:           https://github.com/trilogy-libraries/trilogy.git
Packager:      Baltix Maintainers Team <baltix@packages.altlinux.org>

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
BuildRequires(pre): rpm-macros-cmake
BuildRequires: openssl-devel
BuildRequires: cmake
BuildRequires: gcc
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

%ruby_use_gem_version trilogy:2.9.0.10

%description
A friendly MySQL-compatible library.

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


%package       -n libtrilogy
Version:       2.9.0.10
Release:       alt0.1
Summary:       A friendly MySQL-compatible library
Group:         Development/C

%description   -n libtrilogy
A friendly MySQL-compatible library.

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
Version:       2.9.0.10
Release:       alt0.1
Summary:       A friendly MySQL-compatible library for Ruby, binding to libtrilogy
Group:         Development/Ruby
#BuildArch:     noarch

Requires:      gem(bigdecimal) >= 0
Requires:      gem(trilogy) >= 0
Provides:      gem(trilogy) = 2.9.0.10

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
Version:       2.9.0.10
Release:       alt0.1
Summary:       A friendly MySQL-compatible library for Ruby, binding to libtrilogy documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета trilogy
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(trilogy) = 2.9.0.10

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
Version:       2.9.0.10
Release:       alt0.1
Summary:       A friendly MySQL-compatible library for Ruby, binding to libtrilogy development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета trilogy
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(trilogy) = 2.9.0.10
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


%if_enabled    devel
%package       -n libtrilogy-devel
Version:       2.9.0.10
Release:       alt0.1
Summary:       A friendly MySQL-compatible library development package
Summary(ru_RU.UTF-8): Файлы для разработки буковины trilogy
Group:         Development/C

%description   -n libtrilogy-devel
A friendly MySQL-compatible library development package.

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

%description   -n libtrilogy-devel -l ru_RU.UTF-8
Файлы для разработки буковины trilogy.
%endif


%prep
%setup
mv contrib gem

%build
%cmake -DARCH:STRING=%_arch \
       -DCMAKE_BUILD_TYPE=RelWithDebInfo
%cmake_build
%ruby_build

%install
%cmakeinstall_std
%ruby_install

%check
%ruby_test

%files
%doc LICENSE README.md
%_bindir/%{name}*

%files         -n libtrilogy
%doc LICENSE README.md
%_libdir/lib%{name}.*so.*
%_libdir/lib%{name}*.*so.*

%files         -n gem-trilogy
%doc LICENSE README.md
%ruby_gemspecdir/trilogy-2.9.0.10.gemspec
%ruby_gemslibdir/trilogy-2.9.0.10
%ruby_gemsextdir/trilogy-2.9.0.10

%if_enabled    doc
%files         -n gem-trilogy-doc
%doc LICENSE README.md
%ruby_gemsdocdir/trilogy-2.9.0.10
%endif

%if_enabled    devel
%files         -n gem-trilogy-devel
%doc LICENSE README.md
%ruby_includedir/trilogy-ruby/
%endif

%if_enabled    devel
%files         -n libtrilogy-devel
%doc LICENSE README.md
%_includedir/%{name}
%_cmakedir/*
%_libdir/lib%{name}*.*so
%endif


%changelog
* Wed Feb 05 2025 Pavel Skrylev <majioa@altlinux.org> 2.9.0.10-alt0.1
- ^ 2.9.0 -> 2.9.0p10
- * enabled cmake build

* Tue Feb 04 2025 Pavel Skrylev <majioa@altlinux.org> 2.9.0-alt1
- + packaged gem with Ruby Policy 2.0
