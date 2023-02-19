%define        gemname em-http-request

Name:          gem-em-http-request
Version:       1.1.7.1
Release:       alt0.1
Summary:       EventMachine based, async HTTP Request client
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/igrigorik/em-http-request
Vcs:           https://github.com/igrigorik/em-http-request.git
Packager:      Pavel Skrylev <majioa@altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
%if_with check
BuildRequires: gem(mongrel) >= 1.2.0
BuildRequires: gem(multi_json) >= 0
BuildRequires: gem(rake) >= 0
BuildRequires: gem(rspec) >= 0
BuildRequires: gem(curb) >= 0
BuildRequires: gem(excon) >= 0
BuildRequires: gem(httparty) >= 0
BuildRequires: gem(rest-client) >= 0
BuildRequires: gem(sinatra) >= 0
BuildRequires: gem(streamly_ffi) >= 0
BuildRequires: gem(tach) >= 0.0.8
BuildRequires: gem(typhoeus) >= 0
BuildRequires: gem(addressable) >= 2.3.4
BuildRequires: gem(cookiejar) > 0.3.1
BuildRequires: gem(em-socksify) >= 0.3
BuildRequires: gem(eventmachine) >= 1.0.3
BuildRequires: gem(http_parser.rb) >= 0.6.0
BuildConflicts: gem(mongrel) >= 1.3
BuildConflicts: gem(rack) >= 3
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_use_gem_dependency rack >= 2.2.2,rack < 3
Requires:      gem(addressable) >= 2.3.4
Requires:      gem(cookiejar) > 0.3.1
Requires:      gem(em-socksify) >= 0.3
Requires:      gem(eventmachine) >= 1.0.3
Requires:      gem(http_parser.rb) >= 0.6.0
Obsoletes:     ruby-em-http-request < %EVR
Provides:      ruby-em-http-request = %EVR
Provides:      gem(em-http-request) = 1.1.7.1

%ruby_use_gem_version em-http-request:1.1.7.1

%description
em-http-client is an asynchronous HTTP client based on EventMachine with support
for:

* Asynchronous HTTP API for single & parallel request execution
* Keep-Alive and HTTP pipelining support
* Auto-follow 3xx redirects with max depth
* Automatic gzip & deflate decoding
* Streaming response processing
* Streaming file uploads
* HTTP proxy and SOCKS5 support
* Basic Auth & OAuth
* Connection-level & Global middleware support


%package       -n gem-em-http-request-doc
Version:       1.1.7.1
Release:       alt0.1
Summary:       EventMachine based, async HTTP Request client documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета em-http-request
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(em-http-request) = 1.1.7.1
Requires:      gem-em-http-request = 1.1.7.1-alt0.1

%description   -n gem-em-http-request-doc
EventMachine based, async HTTP Request client documentation
files.

em-http-client is an asynchronous HTTP client based on EventMachine with support
for:

* Asynchronous HTTP API for single & parallel request execution
* Keep-Alive and HTTP pipelining support
* Auto-follow 3xx redirects with max depth
* Automatic gzip & deflate decoding
* Streaming response processing
* Streaming file uploads
* HTTP proxy and SOCKS5 support
* Basic Auth & OAuth
* Connection-level & Global middleware support

%description   -n gem-em-http-request-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета em-http-request.


%package       -n gem-em-http-request-devel
Version:       1.1.7.1
Release:       alt0.1
Summary:       EventMachine based, async HTTP Request client development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета em-http-request
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(em-http-request) = 1.1.7.1
Requires:      gem(mongrel) >= 1.2.0
Requires:      gem(multi_json) >= 0
Requires:      gem(rake) >= 0
Requires:      gem(rspec) >= 0
Requires:      gem(curb) >= 0
Requires:      gem(excon) >= 0
Requires:      gem(httparty) >= 0
Requires:      gem(rest-client) >= 0
Requires:      gem(sinatra) >= 0
Requires:      gem(typhoeus) >= 0
Conflicts:     gem(mongrel) >= 1.3
Conflicts:     gem(rack) >= 3

%description   -n gem-em-http-request-devel
EventMachine based, async HTTP Request client development
package.

em-http-client is an asynchronous HTTP client based on EventMachine with support
for:

* Asynchronous HTTP API for single & parallel request execution
* Keep-Alive and HTTP pipelining support
* Auto-follow 3xx redirects with max depth
* Automatic gzip & deflate decoding
* Streaming response processing
* Streaming file uploads
* HTTP proxy and SOCKS5 support
* Basic Auth & OAuth
* Connection-level & Global middleware support

%description   -n gem-em-http-request-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета em-http-request.


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

%files         -n gem-em-http-request-doc
%doc README.md
%ruby_gemdocdir

%files         -n gem-em-http-request-devel
%doc README.md


%changelog
* Thu Jan 26 2023 Pavel Skrylev <majioa@altlinux.org> 1.1.7.1-alt0.1
- ^ 1.1.7 -> 1.1.7[1]

* Thu Jul 01 2021 Pavel Skrylev <majioa@altlinux.org> 1.1.7-alt1
- ^ 1.1.5 -> 1.1.7

* Sat Apr 18 2020 Andrey Cherepanov <cas@altlinux.org> 1.1.5-alt2
- Remove obsoleted requirement.
- Fix License tag according to SPDX.

* Wed Jul 11 2018 Andrey Cherepanov <cas@altlinux.org> 1.1.5-alt1.2
- Rebuild with new Ruby autorequirements.

* Sat Sep 09 2017 Andrey Cherepanov <cas@altlinux.org> 1.1.5-alt1.1
- Rebuild with Ruby 2.4.1

* Sat Jan 28 2017 Andrey Cherepanov <cas@altlinux.org> 1.1.5-alt1
- new version 1.1.5

* Fri Jun 03 2016 Andrey Cherepanov <cas@altlinux.org> 1.1.3-alt1
- New version

* Wed Mar 05 2014 Andrey Cherepanov <cas@altlinux.org> 1.1.2-alt1
- Initial build for ALT Linux
