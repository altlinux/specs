# vim: set ft=spec: -*- rpm-spec -*-
%define        _unpackaged_files_terminate_build 1
%def_enable    check
%def_enable    doc
%def_enable    devel
%define        gemname apipie-dsl

Name:          gem-apipie-dsl
Version:       2.6.2.1
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
BuildRequires: gem(RedCloth) >= 0
BuildRequires: gem(actionview) >= 0
BuildRequires: gem(bundler) >= 0
BuildRequires: gem(json-schema) >= 0
BuildRequires: gem(maruku) >= 0
BuildRequires: gem(minitest) >= 0
BuildRequires: gem(rake) >= 0
BuildRequires: gem(rdoc) >= 0

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
Requires:      ruby >= 2.5.0
Provides:      apipie-dsl = %EVR
Provides:      gem(apipie-dsl) = 2.6.2.1

%ruby_use_gem_version apipie-dsl:2.6.2.1

%description
Apipie-dsl is a DSL for documenting DSLs written in Ruby. Instead of traditional
use of #comments, ApipieDSL lets you describe the code, through the code.


%if_enabled    doc
%package       -n gem-apipie-dsl-doc
Version:       2.6.2.1
Release:       alt1
Summary:       Apipie-dsl is a DSL for documenting DSLs written in Ruby documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета apipie-dsl
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(apipie-dsl) = 2.6.2.1

%description   -n gem-apipie-dsl-doc
Apipie-dsl is a DSL for documenting DSLs written in Ruby documentation
files.

Apipie-dsl is a DSL for documenting DSLs written in Ruby. Instead of traditional
use of #comments, ApipieDSL lets you describe the code, through the code.

%description   -n gem-apipie-dsl-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета apipie-dsl.
%endif


%if_enabled    devel
%package       -n gem-apipie-dsl-devel
Version:       2.6.2.1
Release:       alt1
Summary:       Apipie-dsl is a DSL for documenting DSLs written in Ruby development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета apipie-dsl
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(apipie-dsl) = 2.6.2.1
Requires:      gem(RedCloth) >= 0
Requires:      gem(actionview) >= 0
Requires:      gem(bundler) >= 0
Requires:      gem(json-schema) >= 0
Requires:      gem(maruku) >= 0
Requires:      gem(minitest) >= 0
Requires:      gem(rake) >= 0
Requires:      gem(rdoc) >= 0

%description   -n gem-apipie-dsl-devel
Apipie-dsl is a DSL for documenting DSLs written in Ruby development
package.

Apipie-dsl is a DSL for documenting DSLs written in Ruby. Instead of traditional
use of #comments, ApipieDSL lets you describe the code, through the code.

%description   -n gem-apipie-dsl-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета apipie-dsl.
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
%doc APACHE-LICENSE-2.0 MIT-LICENSE README.md
%ruby_gemspec
%ruby_gemlibdir

%if_enabled    doc
%files         -n gem-apipie-dsl-doc
%doc APACHE-LICENSE-2.0 MIT-LICENSE README.md
%ruby_gemdocdir
%endif

%if_enabled    devel
%files         -n gem-apipie-dsl-devel
%doc APACHE-LICENSE-2.0 MIT-LICENSE README.md
%endif


%changelog
* Fri Jan 10 2025 Pavel Skrylev <majioa@altlinux.org> 2.6.2.1-alt1
- ^ 2.5.0 -> 2.6.2p1

* Fri Oct 07 2022 Pavel Skrylev <majioa@altlinux.org> 2.5.0-alt1
- ^ 2.3.0 -> 2.5.0

* Wed Dec 16 2020 Pavel Skrylev <majioa@altlinux.org> 2.3.0-alt1
- + packaged gem with usage Ruby Policy 2.0
