# vim: set ft=spec: -*- rpm-spec -*-
%define        gemname apipie-bindings

Name:          gem-apipie-bindings
Version:       0.5.0
Release:       alt1.1
Summary:       Bindings for API calls that are documented with Apipie
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/Apipie/apipie-bindings
Vcs:           https://github.com/apipie/apipie-bindings.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
%if_with check
BuildRequires: gem(rake) >= 12.3.3
BuildRequires: gem(thor) >= 0
BuildRequires: gem(minitest) >= 4.7.4
BuildRequires: gem(minitest-spec-context) >= 0
BuildRequires: gem(simplecov) >= 0
BuildRequires: gem(mocha) >= 0
BuildRequires: gem(ci_reporter) >= 1.6.3
BuildRequires: gem(rest-client) >= 1.6.5
BuildRequires: gem(json) >= 1.2.1
BuildRequires: gem(oauth) >= 0
BuildRequires: gem(gssapi) >= 0
BuildConflicts: gem(minitest) >= 6
BuildConflicts: gem(ci_reporter) >= 3
BuildConflicts: gem(rest-client) >= 3.0
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_use_gem_dependency minitest >= 5.17.0,minitest < 6
%ruby_use_gem_dependency ci_reporter >= 2.0,ci_reporter < 3
Requires:      gem(rest-client) >= 1.6.5
Requires:      gem(json) >= 1.2.1
Requires:      gem(oauth) >= 0
Requires:      gem(gssapi) >= 0
Conflicts:     gem(rest-client) >= 3.0
Provides:      gem(apipie-bindings) = 0.5.0


%description
Bindings for API calls that are documented with Apipie. Bindings are generated
on the fly.

The bindings cache the apidoc from the server. It has separated caches for each
server it connects to. If the server sends the apipie checksum in the headers
Apipie-Checksum: <md5> , the bindings can expire the cache and reload updated
version before next request. If the server does not send the hashes, the cache
does not expire and has to be deleted manually when necessary.

The ability to send checksums comes with Apipie 0.1.1, see the docs on how to
set it up.


%package       -n gem-apipie-bindings-doc
Version:       0.5.0
Release:       alt1.1
Summary:       Bindings for API calls that are documented with Apipie documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета apipie-bindings
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(apipie-bindings) = 0.5.0

%description   -n gem-apipie-bindings-doc
Bindings for API calls that are documented with Apipie documentation
files.

Bindings for API calls that are documented with Apipie. Bindings are generated
on the fly.

The bindings cache the apidoc from the server. It has separated caches for each
server it connects to. If the server sends the apipie checksum in the headers
Apipie-Checksum: <md5> , the bindings can expire the cache and reload updated
version before next request. If the server does not send the hashes, the cache
does not expire and has to be deleted manually when necessary.

The ability to send checksums comes with Apipie 0.1.1, see the docs on how to
set it up.

%description   -n gem-apipie-bindings-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета apipie-bindings.


%package       -n gem-apipie-bindings-devel
Version:       0.5.0
Release:       alt1.1
Summary:       Bindings for API calls that are documented with Apipie development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета apipie-bindings
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(apipie-bindings) = 0.5.0
Requires:      gem(rake) >= 12.3.3
Requires:      gem(thor) >= 0
Requires:      gem(minitest) >= 4.7.4
Requires:      gem(minitest-spec-context) >= 0
Requires:      gem(simplecov) >= 0
Requires:      gem(mocha) >= 0
Requires:      gem(ci_reporter) >= 1.6.3
Conflicts:     gem(minitest) >= 6
Conflicts:     gem(ci_reporter) >= 3

%description   -n gem-apipie-bindings-devel
Bindings for API calls that are documented with Apipie development
package.

Bindings for API calls that are documented with Apipie. Bindings are generated
on the fly.

The bindings cache the apidoc from the server. It has separated caches for each
server it connects to. If the server sends the apipie checksum in the headers
Apipie-Checksum: <md5> , the bindings can expire the cache and reload updated
version before next request. If the server does not send the hashes, the cache
does not expire and has to be deleted manually when necessary.

The ability to send checksums comes with Apipie 0.1.1, see the docs on how to
set it up.

%description   -n gem-apipie-bindings-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета apipie-bindings.


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

%files         -n gem-apipie-bindings-doc
%doc README.md
%ruby_gemdocdir

%files         -n gem-apipie-bindings-devel
%doc README.md


%changelog
* Sat Jan 28 2023 Pavel Skrylev <majioa@altlinux.org> 0.5.0-alt1.1
- ! closes build deps under check condition

* Fri Sep 23 2022 Pavel Skrylev <majioa@altlinux.org> 0.5.0-alt1
- ^ 0.4.0 -> 0.5.0

* Mon Apr 18 2022 Pavel Skrylev <majioa@altlinux.org> 0.4.0-alt1.1
- ! spec

* Thu Dec 10 2020 Pavel Skrylev <majioa@altlinux.org> 0.4.0-alt1
- + packaged gem with usage Ruby Policy 2.0
