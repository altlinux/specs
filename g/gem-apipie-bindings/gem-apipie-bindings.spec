# vim: set ft=spec: -*- rpm-spec -*-
%define        _unpackaged_files_terminate_build 1
%def_enable    check
%def_enable    doc
%def_enable    devel
%define        gemname apipie-bindings

Name:          gem-apipie-bindings
Version:       0.7.1
Release:       alt1
Summary:       Bindings for API calls that are documented with Apipie
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/Apipie/apipie-bindings
Vcs:           https://github.com/apipie/apipie-bindings.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
Autoprov:      yes,noruby
Autoreq:       yes,noruby
BuildRequires(pre): rpm-build-ruby
%if_enabled check
BuildRequires: gem(gssapi) >= 1.2
BuildRequires: gem(minitest) >= 4.7
BuildRequires: gem(minitest-spec-context) >= 0.0.5
BuildRequires: gem(mocha) >= 2.7
BuildRequires: gem(oauth) >= 1.1
BuildRequires: gem(rake) >= 13.0
BuildRequires: gem(rest-client) >= 2.0
BuildRequires: gem(simplecov) >= 0.22
BuildConflicts: gem(gssapi) >= 2
BuildConflicts: gem(minitest) >= 6
BuildConflicts: gem(minitest-spec-context) >= 0.1
BuildConflicts: gem(mocha) >= 3
BuildConflicts: gem(oauth) >= 2
BuildConflicts: gem(rake) >= 14
BuildConflicts: gem(rest-client) >= 3
BuildConflicts: gem(simplecov) >= 1
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_use_gem_dependency minitest >= 5.17.0,minitest < 6
Requires:      ruby >= 2.7.0
Requires:      gem(gssapi) >= 1.2
Requires:      gem(oauth) >= 1.1
Requires:      gem(rest-client) >= 2.0
Conflicts:     gem(gssapi) >= 2
Conflicts:     gem(oauth) >= 2
Conflicts:     gem(rest-client) >= 3
Provides:      gem(apipie-bindings) = 0.7.1

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


%if_enabled    doc
%package       -n gem-apipie-bindings-doc
Version:       0.7.1
Release:       alt1
Summary:       Bindings for API calls that are documented with Apipie documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета apipie-bindings
Group:         Development/Documentation
BuildArch:     noarch

Autoprov:      yes,noruby
Autoreq:       yes,noruby
Requires:      gem(apipie-bindings) = 0.7.1

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
%endif


%if_enabled    devel
%package       -n gem-apipie-bindings-devel
Version:       0.7.1
Release:       alt1
Summary:       Bindings for API calls that are documented with Apipie development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета apipie-bindings
Group:         Development/Ruby
BuildArch:     noarch

Autoprov:      yes,noruby
Autoreq:       yes,noruby
Requires:      gem(apipie-bindings) = 0.7.1
Requires:      gem(minitest) >= 4.7
Requires:      gem(minitest-spec-context) >= 0.0.5
Requires:      gem(mocha) >= 2.7
Requires:      gem(rake) >= 13.0
Requires:      gem(simplecov) >= 0.22
Conflicts:     gem(minitest) >= 6
Conflicts:     gem(minitest-spec-context) >= 0.1
Conflicts:     gem(mocha) >= 3
Conflicts:     gem(rake) >= 14
Conflicts:     gem(simplecov) >= 1

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
%doc LICENSE README.md
%ruby_gemspec
%ruby_gemlibdir

%if_enabled    doc
%files         -n gem-apipie-bindings-doc
%doc LICENSE README.md
%ruby_gemdocdir
%endif

%if_enabled    devel
%files         -n gem-apipie-bindings-devel
%doc LICENSE README.md
%endif


%changelog
* Sat Mar 21 2026 Pavel Skrylev <majioa@altlinux.org> 0.7.1-alt1
- ^ 0.5.0 -> 0.7.1

* Sat Jan 28 2023 Pavel Skrylev <majioa@altlinux.org> 0.5.0-alt1.1
- ! closes build deps under check condition

* Fri Sep 23 2022 Pavel Skrylev <majioa@altlinux.org> 0.5.0-alt1
- ^ 0.4.0 -> 0.5.0

* Mon Apr 18 2022 Pavel Skrylev <majioa@altlinux.org> 0.4.0-alt1.1
- ! spec

* Thu Dec 10 2020 Pavel Skrylev <majioa@altlinux.org> 0.4.0-alt1
- + packaged gem with usage Ruby Policy 2.0
