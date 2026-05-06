%define        _unpackaged_files_terminate_build 0
%def_enable    check
%def_enable    doc
%def_enable    devel
%define        gemname apipie-rails

Name:          gem-apipie-rails
Version:       1.5.0
Release:       alt1.1
Summary:       Ruby on Rails API documentation tool
License:       Apache-2.0
Group:         Development/Ruby
Url:           https://github.com/Apipie/apipie-rails
Vcs:           https://github.com/apipie/apipie-rails.git
Packager:      Baltix Maintaining Team <baltix@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
Patch:         no-dummy.patch
BuildRequires(pre): rpm-build-ruby setup-rb rake
%if_enabled check
BuildRequires: gem(RedCloth) >= 0
BuildRequires: gem(actionpack) >= 7.1.0
BuildRequires: gem(activesupport) >= 7.1
BuildRequires: gem(json-schema) >= 2.8
BuildRequires: gem(maruku) >= 0
BuildRequires: gem(mime-types) >= 0
BuildRequires: gem(net-smtp) >= 0
BuildRequires: gem(rails-controller-testing) >= 0
BuildRequires: gem(rake) >= 0
BuildRequires: gem(rspec-rails) >= 3.0
BuildRequires: gem(rubocop-performance) >= 0
BuildRequires: gem(rubocop-rails) >= 0
BuildRequires: gem(rubocop-rspec) >= 0
BuildRequires: gem(rubocop-rspec_rails) >= 0
BuildRequires: gem(rubocop_challenger) >= 0
BuildRequires: gem(simplecov) >= 0
BuildRequires: gem(sqlite3) >= 0
BuildConflicts: gem(actionpack) >= 7.2
BuildConflicts: gem(activesupport) >= 8
BuildConflicts: gem(json-schema) >= 3
BuildConflicts: gem(rspec-rails) >= 6
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_use_gem_dependency rspec-rails >= 5.0.1,rspec-rails < 6
%ruby_use_gem_dependency activesupport >= 7.1,activesupport < 8
Requires:      ruby >= 2.6.0
Requires:      gem(actionpack) >= 7.1.0
Requires:      gem(activesupport) >= 7.1
Requires:      gem(rspec-rails) >= 3.0
Conflicts:     gem(actionpack) >= 7.2
Conflicts:     gem(activesupport) >= 8
Conflicts:     gem(rspec-rails) >= 6
Obsoletes:     ruby-apipie-rails < %EVR
Provides:      ruby-apipie-rails = %EVR
Provides:      gem(apipie-rails) = 1.5.0

%description
Apipie-rails is a DSL and Rails engine for documenting your RESTful API. Instead
of traditional use of #comments, Apipie lets you describe the code, through the
code. This brings advantages like:

* No need to learn yet another syntax, you already know Ruby, right?
* Possibility of reusing the docs for other purposes (such as validation)
* Easier to extend and maintain (no string parsing involved)
* Possibility of reusing other sources for documentation purposes (such as
routes etc.)

The documentation is available from within your app (by default under the
/apipie path.) In development mode, you can see the changes as you go. It's
markup language agnostic, and even provides an API for reusing the documentation
data in JSON.


%if_enabled    doc
%package       -n gem-apipie-rails-doc
Version:       1.5.0
Release:       alt1
Summary:       Ruby on Rails API documentation tool documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета apipie-rails
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(apipie-rails) = 1.5.0

%description   -n gem-apipie-rails-doc
Ruby on Rails API documentation tool documentation files.

Apipie-rails is a DSL and Rails engine for documenting your RESTful API. Instead
of traditional use of #comments, Apipie lets you describe the code, through the
code. This brings advantages like:

* No need to learn yet another syntax, you already know Ruby, right?
* Possibility of reusing the docs for other purposes (such as validation)
* Easier to extend and maintain (no string parsing involved)
* Possibility of reusing other sources for documentation purposes (such as
routes etc.)

The documentation is available from within your app (by default under the
/apipie path.) In development mode, you can see the changes as you go. It's
markup language agnostic, and even provides an API for reusing the documentation
data in JSON.

%description   -n gem-apipie-rails-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета apipie-rails.
%endif


%if_enabled    devel
%package       -n gem-apipie-rails-devel
Version:       1.5.0
Release:       alt1
Summary:       Ruby on Rails API documentation tool development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета apipie-rails
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(apipie-rails) = 1.5.0
Requires:      gem(RedCloth) >= 0
Requires:      gem(json-schema) >= 2.8
Requires:      gem(maruku) >= 0
Requires:      gem(rake) >= 0
Requires:      gem(rubocop-performance) >= 0
Requires:      gem(rubocop-rails) >= 0
Requires:      gem(rubocop-rspec) >= 0
Requires:      gem(rubocop-rspec_rails) >= 0
Requires:      gem(rubocop_challenger) >= 0
Requires:      gem(simplecov) >= 0
Requires:      gem(sqlite3) >= 0
Conflicts:     gem(json-schema) >= 3

%description   -n gem-apipie-rails-devel
Ruby on Rails API documentation tool development package.

Apipie-rails is a DSL and Rails engine for documenting your RESTful API. Instead
of traditional use of #comments, Apipie lets you describe the code, through the
code. This brings advantages like:

* No need to learn yet another syntax, you already know Ruby, right?
* Possibility of reusing the docs for other purposes (such as validation)
* Easier to extend and maintain (no string parsing involved)
* Possibility of reusing other sources for documentation purposes (such as
routes etc.)

The documentation is available from within your app (by default under the
/apipie path.) In development mode, you can see the changes as you go. It's
markup language agnostic, and even provides an API for reusing the documentation
data in JSON.

%description   -n gem-apipie-rails-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета apipie-rails.
%endif


%prep
%setup
%autopatch -p1

%build
%ruby_build

%install
%ruby_install

%check
%ruby_test

%files
%doc APACHE-LICENSE-2.0 CHANGELOG.md MIT-LICENSE README.md
%ruby_gemspec
%ruby_gemlibdir

%if_enabled    doc
%files         -n gem-apipie-rails-doc
%doc APACHE-LICENSE-2.0 CHANGELOG.md MIT-LICENSE README.md
%ruby_gemdocdir
%endif

%if_enabled    devel
%files         -n gem-apipie-rails-devel
%doc APACHE-LICENSE-2.0 CHANGELOG.md MIT-LICENSE README.md
%endif


%changelog
* Thu Apr 30 2026 Pavel Skrylev <majioa@altlinux.org> 1.5.0-alt1.1
- ! fixed to ignore fake package, and enable dep

* Wed Nov 05 2025 Pavel Skrylev <majioa@altlinux.org> 1.5.0-alt1
- ^ 1.4.2p5 -> 1.5.0

* Tue Jan 14 2025 Pavel Skrylev <majioa@altlinux.org> 1.4.2.5-alt0.1
- ^ 0.8.2 -> 1.4.2p5

* Mon Oct 10 2022 Pavel Skrylev <majioa@altlinux.org> 0.8.2-alt1.1
- ! closes gem build requires into check enable condition

* Thu Sep 29 2022 Pavel Skrylev <majioa@altlinux.org> 0.8.2-alt1
- ^ 0.5.19 -> 0.8.2

* Sat Oct 23 2021 Pavel Skrylev <majioa@altlinux.org> 0.5.19-alt1
- ^ 0.5.17 -> 0.5.19

* Thu Mar 05 2020 Pavel Skrylev <majioa@altlinux.org> 0.5.17-alt1
- updated (^) 0.5.16 -> 0.5.17
- fixed (!) spec

* Mon Sep 16 2019 Pavel Skrylev <majioa@altlinux.org> 0.5.16-alt1
- updated (^) 0.5.15 -> 0.5.16

* Wed Apr 03 2019 Pavel Skrylev <majioa@altlinux.org> 0.5.15-alt1
- updated (^) 0.5.13 -> 0.5.15
- used (>) Ruby Policy 2.0

* Wed Oct 24 2018 Pavel Skrylev <majioa@altlinux.org> 0.5.13-alt1
- updated (^) 0.5.12 -> 0.5.13

* Wed Oct 17 2018 Andrey Cherepanov <cas@altlinux.org> 0.5.12-alt1
- New version.

* Mon Oct 15 2018 Andrey Cherepanov <cas@altlinux.org> 0.5.11-alt1
- New version.

* Fri Sep 21 2018 Pavel Skrylev <majioa@altlinux.org> 0.5.10-alt2
- Gemify the package.

* Mon Sep 17 2018 Andrey Cherepanov <cas@altlinux.org> 0.5.10-alt1
- New version.

* Wed Jul 04 2018 Andrey Cherepanov <cas@altlinux.org> 0.5.9-alt1
- New version.
- Package as gem.

* Fri Jun 01 2018 Andrey Cherepanov <cas@altlinux.org> 0.5.8-alt1
- Initial build for Sisyphus
