
Name:    ruby-em-http-request
Version: 1.1.5
Release: alt1

Summary: EventMachine based, async HTTP Request client
Group:   Development/Ruby
License: MIT/Ruby
URL:     https://github.com/igrigorik/em-http-request

BuildArch: noarch

BuildRequires(pre): rpm-build-ruby
BuildRequires: ruby-test-unit
BuildRequires: ruby-tool-setup

BuildRequires: ruby-addressable
BuildRequires: ruby-cookiejar
BuildRequires: ruby-em-socksify
BuildRequires: ruby-http_parser.rb
BuildRequires: ruby-multi_json
BuildRequires: ruby-simple_oauth

Source: %name-%version.tar

%description
em-http-client is an asynchronous HTTP client based on EventMachine with
support for:

* Asynchronous HTTP API for single & parallel request execution
* Keep-Alive and HTTP pipelining support
* Auto-follow 3xx redirects with max depth
* Automatic gzip & deflate decoding
* Streaming response processing
* Streaming file uploads
* HTTP proxy and SOCKS5 support
* Basic Auth & OAuth
* Connection-level & Global middleware support

%package doc
Summary:   Documentation for %name
Group:     Development/Documentation
Requires:  %name = %version-%release
BuildArch: noarch

%description doc
Documentation for %{name}.

%prep
%setup -n %name-%version
%update_setup_rb

%build
%ruby_config
%ruby_build

%check
%ruby_test_unit -Ilib:test tests

%install
%ruby_install
%rdoc lib/
# Remove unnecessary files
rm -f %buildroot%ruby_ri_sitedir/{Object/cdesc-Object.ri,cache.ri,created.rid}

%files
%doc README.md
%ruby_sitelibdir/*

%files doc
%ruby_ri_sitedir/*

%changelog
* Sat Jan 28 2017 Andrey Cherepanov <cas@altlinux.org> 1.1.5-alt1
- new version 1.1.5

* Fri Jun 03 2016 Andrey Cherepanov <cas@altlinux.org> 1.1.3-alt1
- New version

* Wed Mar 05 2014 Andrey Cherepanov <cas@altlinux.org> 1.1.2-alt1
- Initial build for ALT Linux

