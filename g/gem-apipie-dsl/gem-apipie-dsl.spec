# vim: set ft=spec: -*- rpm-spec -*-
%define        gemname apipie-dsl

Name:          gem-apipie-dsl
Version:       2.5.0
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
%if_with check
BuildRequires: gem(bundler) >= 0
BuildRequires: gem(json-schema) >= 0
BuildRequires: gem(maruku) >= 0
BuildRequires: gem(minitest) >= 0
BuildRequires: gem(rake) >= 0
BuildRequires: gem(rdoc) >= 0
BuildRequires: gem(RedCloth) >= 0
BuildRequires: gem(actionview) >= 0
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
Provides:      gem(apipie-dsl) = 2.5.0


%description
Apipie-dsl is a DSL for documenting DSLs written in Ruby. Instead of traditional
use of #comments, ApipieDSL lets you describe the code, through the code.


%package       -n gem-apipie-dsl-doc
Version:       2.5.0
Release:       alt1
Summary:       Apipie-dsl is a DSL for documenting DSLs written in Ruby documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета apipie-dsl
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(apipie-dsl) = 2.5.0

%description   -n gem-apipie-dsl-doc
Apipie-dsl is a DSL for documenting DSLs written in Ruby documentation
files.

Apipie-dsl is a DSL for documenting DSLs written in Ruby. Instead of traditional
use of #comments, ApipieDSL lets you describe the code, through the code.

%description   -n gem-apipie-dsl-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета apipie-dsl.


%package       -n gem-apipie-dsl-devel
Version:       2.5.0
Release:       alt1
Summary:       Apipie-dsl is a DSL for documenting DSLs written in Ruby development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета apipie-dsl
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(apipie-dsl) = 2.5.0
Requires:      gem(bundler) >= 0
Requires:      gem(json-schema) >= 0
Requires:      gem(maruku) >= 0
Requires:      gem(minitest) >= 0
Requires:      gem(rake) >= 0
Requires:      gem(rdoc) >= 0
Requires:      gem(RedCloth) >= 0
Requires:      gem(actionview) >= 0

%description   -n gem-apipie-dsl-devel
Apipie-dsl is a DSL for documenting DSLs written in Ruby development
package.

Apipie-dsl is a DSL for documenting DSLs written in Ruby. Instead of traditional
use of #comments, ApipieDSL lets you describe the code, through the code.

%description   -n gem-apipie-dsl-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета apipie-dsl.


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

%files         -n gem-apipie-dsl-doc
%doc README.md
%ruby_gemdocdir

%files         -n gem-apipie-dsl-devel
%doc README.md


%changelog
* Fri Oct 07 2022 Pavel Skrylev <majioa@altlinux.org> 2.5.0-alt1
- ^ 2.3.0 -> 2.5.0

* Wed Dec 16 2020 Pavel Skrylev <majioa@altlinux.org> 2.3.0-alt1
- + packaged gem with usage Ruby Policy 2.0
