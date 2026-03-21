%define        _unpackaged_files_terminate_build 1
%def_enable    check
%def_enable    doc
%def_enable    devel
%define        gemname net-http

Name:          gem-net-http
Version:       0.9.1
Release:       alt1
Summary:       HTTP client api for Ruby
License:       Ruby or BSD-2-Clause
Group:         Development/Ruby
Url:           https://github.com/ruby/net-http
Vcs:           https://github.com/ruby/net-http.git
BuildArch:     noarch

Source:        %name-%version.tar
Autoprov:      yes,noruby
Autoreq:       yes,noruby
BuildRequires(pre): rpm-build-ruby
%if_enabled check
BuildRequires: gem(rake) >= 0
BuildRequires: gem(test-unit) >= 0
BuildRequires: gem(test-unit-ruby-core) >= 0
BuildRequires: gem(uri) >= 0.11.1
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
Requires:      ruby >= 2.7.0
Requires:      gem(uri) >= 0.11.1
Provides:      gem(net-http) = 0.9.1

%description
HTTP client api for Ruby.

Net::HTTP provides a rich library which can be used to build HTTP user-agents.
For more details about HTTP see RFC9110 HTTP Semantics and RFC9112 HTTP/1.1.

Net::HTTP is designed to work closely with URI. URI::HTTP#host, URI::HTTP#port
and URI::HTTP#request_uri are designed to work with Net::HTTP.

If you are only performing a few GET requests you should try OpenURI.


%if_enabled    doc
%package       -n gem-net-http-doc
Version:       0.9.1
Release:       alt1
Summary:       HTTP client api for Ruby documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета net-http
Group:         Development/Documentation
BuildArch:     noarch

Autoprov:      yes,noruby
Autoreq:       yes,noruby
Requires:      gem(net-http) = 0.9.1

%description   -n gem-net-http-doc
HTTP client api for Ruby documentation files.

Net::HTTP provides a rich library which can be used to build HTTP user-agents.
For more details about HTTP see RFC9110 HTTP Semantics and RFC9112 HTTP/1.1.

Net::HTTP is designed to work closely with URI. URI::HTTP#host, URI::HTTP#port
and URI::HTTP#request_uri are designed to work with Net::HTTP.

If you are only performing a few GET requests you should try OpenURI.

%description   -n gem-net-http-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета net-http.
%endif


%if_enabled    devel
%package       -n gem-net-http-devel
Version:       0.9.1
Release:       alt1
Summary:       HTTP client api for Ruby development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета net-http
Group:         Development/Ruby
BuildArch:     noarch

Autoprov:      yes,noruby
Autoreq:       yes,noruby
Requires:      gem(net-http) = 0.9.1
Requires:      gem(rake) >= 0
Requires:      gem(test-unit) >= 0
Requires:      gem(test-unit-ruby-core) >= 0

%description   -n gem-net-http-devel
HTTP client api for Ruby development package.

Net::HTTP provides a rich library which can be used to build HTTP user-agents.
For more details about HTTP see RFC9110 HTTP Semantics and RFC9112 HTTP/1.1.

Net::HTTP is designed to work closely with URI. URI::HTTP#host, URI::HTTP#port
and URI::HTTP#request_uri are designed to work with Net::HTTP.

If you are only performing a few GET requests you should try OpenURI.

%description   -n gem-net-http-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета net-http.
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
%doc COPYING README.md
%ruby_gemspec
%ruby_gemlibdir

%if_enabled    doc
%files         -n gem-net-http-doc
%doc COPYING README.md
%ruby_gemdocdir
%endif

%if_enabled    devel
%files         -n gem-net-http-devel
%doc COPYING README.md
%endif


%changelog
* Sat Mar 21 2026 Pavel Skrylev <majioa@altlinux.org> 0.9.1-alt1
- + packaged gem with Ruby Policy 2.0
- * define explicit dependencies
