%define        gemname webmock

Name:          gem-webmock
Version:       3.13.0
Release:       alt1
Summary:       Library for stubbing and setting expectations on HTTP requests in Ruby
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/bblimke/webmock
Vcs:           https://github.com/bblimke/webmock/tree/v3.13.0.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
BuildRequires: gem(addressable) >= 2.3.6
BuildRequires: gem(crack) >= 0.3.2
BuildRequires: gem(hashdiff) >= 0.4.0 gem(hashdiff) < 2.0.0
BuildRequires: gem(patron) >= 0.4.18
BuildRequires: gem(curb) >= 0.7.16
BuildRequires: gem(typhoeus) >= 0.5.0
# BuildRequires: gem(http) >= 0.8.0
BuildRequires: gem(rack) > 1.6
BuildRequires: gem(rspec) >= 3.1.0
BuildRequires: gem(httpclient) >= 2.2.4
BuildRequires: gem(em-http-request) >= 1.0.2
BuildRequires: gem(em-synchrony) >= 1.0.0
BuildRequires: gem(excon) >= 0.27.5
# BuildRequires: gem(async-http) >= 0.48.0
BuildRequires: gem(minitest) >= 5.0.0
BuildRequires: gem(test-unit) >= 3.0.0
BuildRequires: gem(rdoc) > 3.5.0
BuildRequires: gem(webrick) >= 0

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
Requires:      gem(addressable) >= 2.3.6
Requires:      gem(crack) >= 0.3.2
Requires:      gem(hashdiff) >= 0.4.0
Provides:      gem(webmock) = 3.13.0


%description
Library for stubbing and setting expectations on HTTP requests in Ruby.

* Stubbing HTTP requests at low http client lib level (no need to change tests
when you change HTTP library)
* Setting and verifying expectations on HTTP requests
* Matching requests based on method, URI, headers and body
* Smart matching of the same URIs in different representations (also encoded and
non encoded forms)
* Smart matching of the same headers in different representations.
* Support for Test::Unit
* Support for RSpec
* Support for MiniTest


%package       -n gem-webmock-doc
Version:       3.13.0
Release:       alt1
Summary:       Library for stubbing and setting expectations on HTTP requests in Ruby documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета webmock
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(webmock) = 3.13.0

%description   -n gem-webmock-doc
Library for stubbing and setting expectations on HTTP requests in Ruby
documentation files.

* Stubbing HTTP requests at low http client lib level (no need to change tests
when you change HTTP library)
* Setting and verifying expectations on HTTP requests
* Matching requests based on method, URI, headers and body
* Smart matching of the same URIs in different representations (also encoded and
non encoded forms)
* Smart matching of the same headers in different representations.
* Support for Test::Unit
* Support for RSpec
* Support for MiniTest

%description   -n gem-webmock-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета webmock.


%package       -n gem-webmock-devel
Version:       3.13.0
Release:       alt1
Summary:       Library for stubbing and setting expectations on HTTP requests in Ruby development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета webmock
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(webmock) = 3.13.0
Requires:      gem(patron) >= 0.4.18
Requires:      gem(curb) >= 0.7.16
Requires:      gem(typhoeus) >= 0.5.0
# Requires:      gem(http) >= 0.8.0
Requires:      gem(rack) > 1.6
Requires:      gem(rspec) >= 3.1.0 gem(rspec) < 4
Requires:      gem(httpclient) >= 2.2.4
Requires:      gem(em-http-request) >= 1.0.2
Requires:      gem(em-synchrony) >= 1.0.0
Requires:      gem(excon) >= 0.27.5
# Requires:      gem(async-http) >= 0.48.0
Requires:      gem(minitest) >= 5.0.0 gem(minitest) < 6
Requires:      gem(test-unit) >= 3.0.0 gem(test-unit) < 4
Requires:      gem(rdoc) > 3.5.0 gem(rdoc) < 7
Requires:      gem(webrick) >= 0

%description   -n gem-webmock-devel
Library for stubbing and setting expectations on HTTP requests in Ruby
development package.

* Stubbing HTTP requests at low http client lib level (no need to change tests
when you change HTTP library)
* Setting and verifying expectations on HTTP requests
* Matching requests based on method, URI, headers and body
* Smart matching of the same URIs in different representations (also encoded and
non encoded forms)
* Smart matching of the same headers in different representations.
* Support for Test::Unit
* Support for RSpec
* Support for MiniTest

%description   -n gem-webmock-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета webmock.


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

%files         -n gem-webmock-doc
%doc README.md
%ruby_gemdocdir

%files         -n gem-webmock-devel
%doc README.md


%changelog
* Thu Jul 01 2021 Pavel Skrylev <majioa@altlinux.org> 3.13.0-alt1
- ^ 3.7.5 -> 3.13.0

* Tue Sep 24 2019 Pavel Skrylev <majioa@altlinux.org> 3.7.5-alt1
- ^ 3.6.0 -> 3.7.5
- ! spec

* Thu Jul 11 2019 Pavel Skrylev <majioa@altlinux.org> 3.6.0-alt1
- ̈added (+) initial build for Sisyphus, packaged as a gem with usage Ruby Policy 2.0
