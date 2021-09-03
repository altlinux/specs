%define        gemname rack-cors

Name:          gem-rack-cors
Version:       1.1.1
Release:       alt1
Summary:       Middleware that will make Rack-based apps CORS compatible
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/cyu/rack-cors
Vcs:           https://github.com/cyu/rack-cors.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
BuildRequires: gem(rack) >= 2.0.0 gem(rack) < 3
BuildRequires: gem(bundler) >= 1.16.0 gem(bundler) < 3
BuildRequires: gem(rake) >= 12.3.0 gem(rake) < 14
BuildRequires: gem(minitest) >= 5.11.0 gem(minitest) < 6
BuildRequires: gem(mocha) >= 1.6.0 gem(mocha) < 2
BuildRequires: gem(rack-test) >= 1.1.0 gem(rack-test) < 2

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_use_gem_dependency bundler >= 2.1.4,bundler < 3
%ruby_use_gem_dependency rake >= 13.0.1,rake < 14
%ruby_ignore_names rails5,rack
Requires:      gem(rack) >= 2.0.0 gem(rack) < 3
Provides:      gem(rack-cors) = 1.1.1


%description
Rack Middleware for handling Cross-Origin Resource Sharing (CORS), which makes
cross-origin AJAX possible.

Build Status

Rack::Cors provides support for Cross-Origin Resource Sharing (CORS) for Rack
compatible web applications.

The CORS spec allows web applications to make cross domain AJAX calls without
using workarounds such as JSONP. See Cross-domain Ajax with Cross-Origin
Resource Sharing.


%package       -n gem-rack-cors-doc
Version:       1.1.1
Release:       alt1
Summary:       Middleware that will make Rack-based apps CORS compatible documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета rack-cors
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(rack-cors) = 1.1.1

%description   -n gem-rack-cors-doc
Middleware that will make Rack-based apps CORS compatible documentation
files.

Rack Middleware for handling Cross-Origin Resource Sharing (CORS), which makes
cross-origin AJAX possible.

Build Status

Rack::Cors provides support for Cross-Origin Resource Sharing (CORS) for Rack
compatible web applications.

The CORS spec allows web applications to make cross domain AJAX calls without
using workarounds such as JSONP. See Cross-domain Ajax with Cross-Origin
Resource Sharing.

%description   -n gem-rack-cors-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета rack-cors.


%package       -n gem-rack-cors-devel
Version:       1.1.1
Release:       alt1
Summary:       Middleware that will make Rack-based apps CORS compatible development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета rack-cors
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(rack-cors) = 1.1.1
Requires:      gem(bundler) >= 1.16.0 gem(bundler) < 3
Requires:      gem(rake) >= 12.3.0 gem(rake) < 14
Requires:      gem(minitest) >= 5.11.0 gem(minitest) < 6
Requires:      gem(mocha) >= 1.6.0 gem(mocha) < 2
Requires:      gem(rack-test) >= 1.1.0 gem(rack-test) < 2

%description   -n gem-rack-cors-devel
Middleware that will make Rack-based apps CORS compatible development
package.

Rack Middleware for handling Cross-Origin Resource Sharing (CORS), which makes
cross-origin AJAX possible.

Build Status

Rack::Cors provides support for Cross-Origin Resource Sharing (CORS) for Rack
compatible web applications.

The CORS spec allows web applications to make cross domain AJAX calls without
using workarounds such as JSONP. See Cross-domain Ajax with Cross-Origin
Resource Sharing.

%description   -n gem-rack-cors-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета rack-cors.


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

%files         -n gem-rack-cors-doc
%doc README.md
%ruby_gemdocdir

%files         -n gem-rack-cors-devel
%doc README.md


%changelog
* Thu Sep 02 2021 Pavel Skrylev <majioa@altlinux.org> 1.1.1-alt1
- ^ 1.0.3 -> 1.1.1

* Wed Sep 11 2019 Pavel Skrylev <majioa@altlinux.org> 1.0.3-alt1.1
- ! spec according to changelog rules

* Wed Aug 21 2019 Pavel Skrylev <majioa@altlinux.org> 1.0.3-alt1
- + packaged gem with usage Ruby Policy 2.0
