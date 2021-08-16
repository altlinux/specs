# vim: set ft=spec: -*- rpm-spec -*-
%define        pkgname apipie-dsl

Name:          gem-%pkgname
Version:       2.3.0
Release:       alt1
Summary:       Apipie-dsl is a DSL for documenting DSLs written in Ruby
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/ofedoren/apipie-dsl
Vcs:           https://github.com/ofedoren/apipie-dsl.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
BuildRequires: gem(actionview)
BuildRequires: gem(bundler)
BuildRequires: gem(json-schema)
BuildRequires: gem(maruku)
BuildRequires: gem(minitest)
BuildRequires: gem(rake)
BuildRequires: gem(rdoc)
BuildRequires: gem(RedCloth)

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*

%description
Apipie-dsl is a DSL for documenting DSLs written in Ruby. Instead of
traditional use of #comments, ApipieDSL lets you describe the code, through the
code.


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
%ruby_build

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
* Wed Dec 16 2020 Pavel Skrylev <majioa@altlinux.org> 2.3.0-alt1
- + packaged gem with usage Ruby Policy 2.0
