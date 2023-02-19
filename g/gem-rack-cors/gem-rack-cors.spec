%define        gemname rack-cors

Name:          gem-rack-cors
Version:       2.0.1.0
Release:       alt0.1
Summary:       Middleware that will make Rack-based apps CORS compatible
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/cyu/rack-cors
Vcs:           https://github.com/cyu/rack-cors.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
%if_with check
BuildRequires: gem(bundler) >= 1.16.0
BuildRequires: gem(minitest) >= 5.11.0
BuildRequires: gem(mocha) >= 1.6.0
BuildRequires: gem(pry) >= 0.12
BuildRequires: gem(rack-test) >= 1.1.0
BuildRequires: gem(rake) >= 12.3.0
BuildRequires: gem(rubocop) >= 0.80.1
BuildRequires: gem(pry-byebug) >= 3.6.0
BuildRequires: gem(rack) >= 2.0.0
BuildConflicts: gem(bundler) >= 3
BuildConflicts: gem(minitest) >= 6
BuildConflicts: gem(mocha) >= 2
BuildConflicts: gem(pry) >= 1
BuildConflicts: gem(rack-test) >= 3
BuildConflicts: gem(rake) >= 14
BuildConflicts: gem(rubocop) >= 2
BuildConflicts: gem(pry-byebug) >= 4
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_use_gem_dependency mocha >= 1.11.2,mocha < 2
%ruby_use_gem_dependency rake >= 13.0.1,rake < 14
%ruby_use_gem_dependency rubocop >= 1.15.0,rubocop < 2
%ruby_use_gem_dependency minitest >= 5.17.0,minitest < 6
%ruby_use_gem_dependency rack-test >= 1.1.0,rack-test < 3
%ruby_use_gem_dependency pry-byebug >= 3.9.0,pry-byebug < 4
Requires:      gem(rack) >= 2.0.0
Provides:      gem(rack-cors) = 2.0.1.0

%ruby_use_gem_version rack-cors:2.0.1.0

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
Version:       2.0.1.0
Release:       alt0.1
Summary:       Middleware that will make Rack-based apps CORS compatible documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета rack-cors
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(rack-cors) = 2.0.1.0

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
Version:       2.0.1.0
Release:       alt0.1
Summary:       Middleware that will make Rack-based apps CORS compatible development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета rack-cors
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(rack-cors) = 2.0.1.0
Requires:      gem(bundler) >= 1.16.0
Requires:      gem(minitest) >= 5.11.0
Requires:      gem(mocha) >= 1.6.0
Requires:      gem(pry) >= 0.12
Requires:      gem(rack-test) >= 1.1.0
Requires:      gem(rake) >= 12.3.0
Requires:      gem(rubocop) >= 0.80.1
Requires:      gem(pry-byebug) >= 3.6.0
Conflicts:     gem(bundler) >= 3
Conflicts:     gem(minitest) >= 6
Conflicts:     gem(mocha) >= 2
Conflicts:     gem(pry) >= 1
Conflicts:     gem(rack-test) >= 3
Conflicts:     gem(rake) >= 14
Conflicts:     gem(rubocop) >= 2
Conflicts:     gem(pry-byebug) >= 4

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
* Mon Jan 30 2023 Pavel Skrylev <majioa@altlinux.org> 2.0.1.0-alt0.1
- ^ 2.0.0.rc1 -> 2.0[1.0]

* Sat Oct 08 2022 Pavel Skrylev <majioa@altlinux.org> 2.0.0.rc1-alt1
- ^ 1.1.1 -> 2.0.0.rc1

* Thu Sep 02 2021 Pavel Skrylev <majioa@altlinux.org> 1.1.1-alt1
- ^ 1.0.3 -> 1.1.1

* Wed Sep 11 2019 Pavel Skrylev <majioa@altlinux.org> 1.0.3-alt1.1
- ! spec according to changelog rules

* Wed Aug 21 2019 Pavel Skrylev <majioa@altlinux.org> 1.0.3-alt1
- + packaged gem with usage Ruby Policy 2.0
