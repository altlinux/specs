%define        _unpackaged_files_terminate_build 1
%def_enable    check
%def_enable    doc
%def_enable    devel
%define        gemname async-dns

Name:          gem-async-dns
Version:       1.3.0
Release:       alt1
Summary:       An easy to use DNS client resolver and server for Ruby
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/socketry/async-dns
Vcs:           https://github.com/socketry/async-dns.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
%if_enabled check
BuildRequires: gem(io-endpoint) >= 0
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
Requires:      gem(io-endpoint) >= 0
Provides:      gem(async-dns) = 1.3.0


%description
Async::DNS is a high-performance DNS client resolver and server which can be
easily integrated into other projects or used as a stand-alone daemon. It was
forked from RubyDNS which is now implemented in terms of this library.


%if_enabled    doc
%package       -n gem-async-dns-doc
Version:       1.3.0
Release:       alt1
Summary:       An easy to use DNS client resolver and server for Ruby documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета async-dns
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(async-dns) = 1.3.0

%description   -n gem-async-dns-doc
An easy to use DNS client resolver and server for Ruby documentation files.

Async::DNS is a high-performance DNS client resolver and server which can be
easily integrated into other projects or used as a stand-alone daemon. It was
forked from RubyDNS which is now implemented in terms of this library.

%description   -n gem-async-dns-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета async-dns.
%endif


%if_enabled    devel
%package       -n gem-async-dns-devel
Version:       1.3.0
Release:       alt1
Summary:       An easy to use DNS client resolver and server for Ruby development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета async-dns
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(async-dns) = 1.3.0

%description   -n gem-async-dns-devel
An easy to use DNS client resolver and server for Ruby development package.

Async::DNS is a high-performance DNS client resolver and server which can be
easily integrated into other projects or used as a stand-alone daemon. It was
forked from RubyDNS which is now implemented in terms of this library.

%description   -n gem-async-dns-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета async-dns.
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
%doc README.md
%ruby_gemspec
%ruby_gemlibdir

%if_enabled    doc
%files         -n gem-async-dns-doc
%doc README.md
%ruby_gemdocdir
%endif

%if_enabled    devel
%files         -n gem-async-dns-devel
%doc README.md
%endif


%changelog
* Tue Jul 30 2024 Pavel Skrylev <majioa@altlinux.org> 1.3.0-alt1
- + packaged gem with Ruby Policy 2.0
