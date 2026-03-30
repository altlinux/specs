%define        _unpackaged_files_terminate_build 1
%def_enable    check
%def_enable    doc
%def_enable    devel
%define        gemname rack-cors

Name:          gem-rack-cors
Version:       3.0.0
Release:       alt1
Summary:       Middleware that will make Rack-based apps CORS compatible
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/cyu/rack-cors
Vcs:           https://github.com/cyu/rack-cors.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
Autoprov:      yes,noruby
Autoreq:       yes,noruby
BuildRequires(pre): rpm-build-ruby
%if_enabled check
BuildRequires: gem(bundler) >= 1.16.0
BuildRequires: gem(logger) >= 0
BuildRequires: gem(minitest) >= 0
BuildRequires: gem(mocha) >= 0
BuildRequires: gem(pry) >= 0.12
BuildRequires: gem(pry-byebug) >= 3.6.0
BuildRequires: gem(rack) >= 3.0.14
BuildRequires: gem(rack-test) >= 1.1.0
BuildRequires: gem(rake) >= 12.3.0
BuildRequires: gem(rubocop) >= 0.80.1
BuildConflicts: gem(bundler) >= 3
BuildConflicts: gem(pry) >= 1
BuildConflicts: gem(pry-byebug) >= 4
BuildConflicts: gem(rake) >= 14
BuildConflicts: gem(rubocop) >= 2
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_use_gem_dependency pry-byebug >= 3.11.0,pry-byebug < 4
%ruby_use_gem_dependency rake >= 13.1.0,rake < 14
%ruby_use_gem_dependency rubocop >= 1.15.0,rubocop < 2
Requires:      gem(logger) >= 0
Requires:      gem(rack) >= 3.0.14
Provides:      gem(rack-cors) = 3.0.0

%description
Rack Middleware for handling Cross-Origin Resource Sharing (CORS), which makes
cross-origin AJAX possible.

Build Status

Rack::Cors provides support for Cross-Origin Resource Sharing (CORS) for Rack
compatible web applications.

The CORS spec allows web applications to make cross domain AJAX calls without
using workarounds such as JSONP. See Cross-domain Ajax with Cross-Origin
Resource Sharing.


%if_enabled    doc
%package       -n gem-rack-cors-doc
Version:       3.0.0
Release:       alt1
Summary:       Middleware that will make Rack-based apps CORS compatible documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета rack-cors
Group:         Development/Documentation
BuildArch:     noarch

Autoprov:      yes,noruby
Autoreq:       yes,noruby
Requires:      gem(rack-cors) = 3.0.0

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
%endif


%if_enabled    devel
%package       -n gem-rack-cors-devel
Version:       3.0.0
Release:       alt1
Summary:       Middleware that will make Rack-based apps CORS compatible development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета rack-cors
Group:         Development/Ruby
BuildArch:     noarch

Autoprov:      yes,noruby
Autoreq:       yes,noruby
Requires:      gem(rack-cors) = 3.0.0
Requires:      gem(bundler) >= 1.16.0
Requires:      gem(minitest) >= 0
Requires:      gem(mocha) >= 0
Requires:      gem(pry) >= 0.12
Requires:      gem(pry-byebug) >= 3.6.0
Requires:      gem(rack-test) >= 1.1.0
Requires:      gem(rake) >= 12.3.0
Requires:      gem(rubocop) >= 0.80.1
Conflicts:     gem(bundler) >= 3
Conflicts:     gem(pry) >= 1
Conflicts:     gem(pry-byebug) >= 4
Conflicts:     gem(rake) >= 14
Conflicts:     gem(rubocop) >= 2

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
%doc CHANGELOG.md LICENSE.txt README.md
%ruby_gemspec
%ruby_gemlibdir

%if_enabled    doc
%files         -n gem-rack-cors-doc
%doc CHANGELOG.md LICENSE.txt README.md
%ruby_gemdocdir
%endif

%if_enabled    devel
%files         -n gem-rack-cors-devel
%doc CHANGELOG.md LICENSE.txt README.md
%endif


%changelog
* Mon Mar 30 2026 Pavel Skrylev <majioa@altlinux.org> 3.0.0-alt1
- ^ 2.0[1.0] -> 3.0.0

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
