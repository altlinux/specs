# vim: set ft=spec: -*- rpm-spec -*-
%define        pkgname apipie-bindings

Name:          gem-%pkgname
Version:       0.4.0
Release:       alt1
Summary:       Bindings for API calls that are documented with Apipie
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/Apipie/apipie-bindings
Vcs:           https://github.com/Apipie/apipie-bindings.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*

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


%package       doc
Summary:       Documentation files for %gemname gem
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета %gemname
Group:         Development/Documentation
BuildArch:     noarch

%description   doc
Documentation files for %gemname gem.

%description   doc -l ru_RU.UTF8
Файлы сведений для самоцвета %gemname.


%prep
%setup

%build
%ruby_build --ignore=dummy

%install
%ruby_install

%check
%ruby_test

%files
%doc README*
%ruby_gemspec
%ruby_gemlibdir

%files         doc
%ruby_gemdocdir


%changelog
* Thu Dec 10 2020 Pavel Skrylev <majioa@altlinux.org> 0.4.0-alt1
- + packaged gem with usage Ruby Policy 2.0
