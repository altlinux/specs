%define        _unpackaged_files_terminate_build 1
%def_disable   check
%def_enable    doc
%def_enable    devel
%define        gemname fiber-local

Name:          gem-fiber-local
Version:       1.1.0
Release:       alt1
Summary:       Provides a class-level mixin to make fiber local state easy
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/socketry/fiber-local
Vcs:           https://github.com/socketry/fiber-local.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
%if_enabled check
BuildRequires: gem(fiber-storage) >= 0
BuildRequires: gem(bundler) >= 0
BuildRequires: gem(covered) >= 0
BuildRequires: gem(rspec) >= 0
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
Requires:      gem(fiber-storage) >= 0
Provides:      gem(fiber-local) = 1.1.0


%description
A module to simplify fiber-local state. This provides a convenient interface for
providing a default per-thread instance, while allowing per-fiber overrides
(e.g. per-request state handling).


%if_enabled    doc
%package       -n gem-fiber-local-doc
Version:       1.1.0
Release:       alt1
Summary:       Provides a class-level mixin to make fiber local state easy documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета fiber-local
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(fiber-local) = 1.1.0

%description   -n gem-fiber-local-doc
Provides a class-level mixin to make fiber local state easy documentation files.

A module to simplify fiber-local state. This provides a convenient interface for
providing a default per-thread instance, while allowing per-fiber overrides
(e.g. per-request state handling).

%description   -n gem-fiber-local-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета fiber-local.
%endif


%if_enabled    devel
%package       -n gem-fiber-local-devel
Version:       1.1.0
Release:       alt1
Summary:       Provides a class-level mixin to make fiber local state easy development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета fiber-local
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(fiber-local) = 1.1.0
Requires:      gem(bundler) >= 0
Requires:      gem(covered) >= 0
Requires:      gem(rspec) >= 0


%description   -n gem-fiber-local-devel
Provides a class-level mixin to make fiber local state easy development package.

A module to simplify fiber-local state. This provides a convenient interface for
providing a default per-thread instance, while allowing per-fiber overrides
(e.g. per-request state handling).

%description   -n gem-fiber-local-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета fiber-local.
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
%doc readme.md
%ruby_gemspec
%ruby_gemlibdir

%if_enabled    doc
%files         -n gem-fiber-local-doc
%doc readme.md
%ruby_gemdocdir
%endif

%if_enabled    devel
%files         -n gem-fiber-local-devel
%doc readme.md
%endif


%changelog
* Wed Jul 24 2024 Pavel Skrylev <majioa@altlinux.org> 1.1.0-alt1
- ^ 1.0.0 -> 1.1.0

* Wed Oct 12 2022 Pavel Skrylev <majioa@altlinux.org> 1.0.0-alt1.1
- ! closes gem build required into check condition

* Fri Sep 03 2021 Pavel Skrylev <majioa@altlinux.org> 1.0.0-alt1
- + packaged gem with Ruby Policy 2.0
