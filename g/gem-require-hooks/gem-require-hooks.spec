%define        _unpackaged_files_terminate_build 1
%def_enable    check
%def_enable    doc
%def_enable    devel
%define        gemname require-hooks

Name:          gem-require-hooks
Version:       0.2.2
Release:       alt1
Summary:       Require Hooks provide infrastructure for intercepting require/load calls in Ruby
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/ruby-next/ruby-next
Vcs:           https://github.com/ruby-next/ruby-next.git
Packager:      Baltix Maintaining Team <baltix@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
Autoprov:      yes,noruby
Autoreq:       yes,noruby
BuildRequires(pre): rpm-build-ruby
%if_enabled check
BuildRequires: gem(rubocop-md) >= 1.0
BuildRequires: gem(standard) >= 1.0
BuildConflicts: gem(rubocop-md) >= 3
BuildConflicts: gem(standard) >= 2
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_use_gem_dependency rubocop-md >= 2.0.2,rubocop-md < 3
Requires:      ruby >= 2.2
Provides:      gem(require-hooks) = 0.2.2

%description
Require Hooks provide infrastructure for intercepting require/load calls in Ruby


%if_enabled    doc
%package       -n gem-require-hooks-doc
Version:       0.2.2
Release:       alt1
Summary:       Require Hooks provide infrastructure for intercepting require/load calls in Ruby documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета require-hooks
Group:         Development/Documentation
BuildArch:     noarch

Autoprov:      yes,noruby
Autoreq:       yes,noruby
Requires:      gem(require-hooks) = 0.2.2

%description   -n gem-require-hooks-doc
Require Hooks provide infrastructure for intercepting require/load calls in Ruby
documentation files.

%description   -n gem-require-hooks-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета require-hooks.
%endif


%if_enabled    devel
%package       -n gem-require-hooks-devel
Version:       0.2.2
Release:       alt1
Summary:       Require Hooks provide infrastructure for intercepting require/load calls in Ruby development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета require-hooks
Group:         Development/Ruby
BuildArch:     noarch

Autoprov:      yes,noruby
Autoreq:       yes,noruby
Requires:      gem(require-hooks) = 0.2.2
Requires:      gem(rubocop-md) >= 1.0
Requires:      gem(standard) >= 1.0
Conflicts:     gem(rubocop-md) >= 3
Conflicts:     gem(standard) >= 2

%description   -n gem-require-hooks-devel
Require Hooks provide infrastructure for intercepting require/load calls in Ruby
development package.

%description   -n gem-require-hooks-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета require-hooks.
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
%files         -n gem-require-hooks-doc
%doc CHANGELOG.md LICENSE.txt README.md
%ruby_gemdocdir
%endif

%if_enabled    devel
%files         -n gem-require-hooks-devel
%doc CHANGELOG.md LICENSE.txt README.md
%endif


%changelog
* Sat Nov 29 2025 Pavel Skrylev <majioa@altlinux.org> 0.2.2-alt1
- ^ 0.2.0 -> 0.2.2

* Wed Apr 17 2024 Pavel Skrylev <majioa@altlinux.org> 0.2.0-alt1
- + packaged gem with Ruby Policy 2.0
