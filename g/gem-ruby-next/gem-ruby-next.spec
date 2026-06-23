%define        _unpackaged_files_terminate_build 1
%def_enable    check
%def_enable    doc
%def_enable    devel
%define        gemname ruby-next

Name:          gem-ruby-next
Version:       1.2.0
Release:       alt1
Summary:       Make older Rubies quack like edge Ruby
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/ruby-next/ruby-next
Vcs:           https://github.com/ruby-next/ruby-next.git
Packager:      Baltix Maintaining Team <baltix@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-macros-ruby setup-rb rake
%if_enabled check
BuildRequires: gem(benchmark_driver) >= 0
BuildRequires: gem(bootsnap) >= 0
BuildRequires: gem(paco) >= 0.2
BuildRequires: gem(pry-byebug) >= 0
BuildRequires: gem(require-hooks) >= 0.2
BuildRequires: gem(rubocop-md) >= 1.0
BuildRequires: gem(ruby-next-parser) >= 3.4.0.2
BuildRequires: gem(standard) >= 1.0
BuildRequires: gem(unparser) >= 0.6.0
BuildRequires: gem(zeitwerk) >= 0
BuildConflicts: gem(paco) >= 1
BuildConflicts: gem(require-hooks) >= 1
BuildConflicts: gem(rubocop-md) >= 3
BuildConflicts: gem(standard) >= 2
BuildConflicts: gem(unparser) >= 1
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_use_gem_dependency pry >= 0.13.1,pry < 1
%ruby_use_gem_dependency unparser >= 0.9,unparser < 1
%ruby_use_gem_dependency rubocop-md >= 2.0.2,rubocop-md < 3
Requires:      ruby >= 2.2.0
Requires:      gem(benchmark_driver) >= 0
Requires:      gem(paco) >= 0.2
Requires:      gem(require-hooks) >= 0.2
Requires:      gem(ruby-next-parser) >= 3.4.0.2
Requires:      gem(unparser) >= 0.6.0
Requires:      gem(zeitwerk) >= 0
Conflicts:     gem(paco) >= 1
Conflicts:     gem(require-hooks) >= 1
Conflicts:     gem(unparser) >= 1
Provides:      gem(ruby-next) = 1.2.0

%description
Ruby Next is a collection of polyfills and a transpiler for supporting latest
and upcoming edge CRuby features in older versions and alternative
implementations (such as mruby, JRuby, Opal, Artichoke, RubyMotion, etc.).


%package       -n gem-ruby-next-core
Version:       1.2.0
Release:       alt1
Summary:       Ruby Next core functionality
Group:         Development/Ruby
BuildArch:     noarch

Requires:      ruby >= 2.2.0
Provides:      gem(ruby-next-core) = 1.2.0

%description   -n gem-ruby-next-core
Ruby Next Core is a zero deps version of Ruby Next meant to be used as as
dependency in your gems.

It contains all the polyfills and utility files but doesn't require transpiler
dependencies to be install.


%package       -n ruby-next
Version:       1.2.0
Release:       alt1
Summary:       Ruby Next core functionality executable(s)
Summary(ru_RU.UTF-8): Исполнямка для самоцвета ruby-next-core
Group:         Other
BuildArch:     noarch

Requires:      gem(ruby-next-core) = 1.2.0
Requires:      gem(benchmark_driver) >= 0
Requires:      gem(ruby-next-parser) >= 3.4.0.2
Requires:      gem(zeitwerk) >= 0

%description   -n ruby-next
Ruby Next core functionality executable(s).

Ruby Next Core is a zero deps version of Ruby Next meant to be used as as
dependency in your gems.

It contains all the polyfills and utility files but doesn't require transpiler
dependencies to be install.

%description   -n ruby-next -l ru_RU.UTF-8
Исполнямка для самоцвета ruby-next-core.


%if_enabled    doc
%package       -n gem-ruby-next-core-doc
Version:       1.2.0
Release:       alt1
Summary:       Ruby Next core functionality documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета ruby-next-core
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(ruby-next-core) = 1.2.0

%description   -n gem-ruby-next-core-doc
Ruby Next core functionality documentation files.

Ruby Next Core is a zero deps version of Ruby Next meant to be used as as
dependency in your gems.

It contains all the polyfills and utility files but doesn't require transpiler
dependencies to be install.

%description   -n gem-ruby-next-core-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета ruby-next-core.
%endif


%if_enabled    devel
%package       -n gem-ruby-next-core-devel
Version:       1.2.0
Release:       alt1
Summary:       Ruby Next core functionality development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета ruby-next-core
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(ruby-next-core) = 1.2.0
Requires:      gem(benchmark_driver) >= 0
Requires:      gem(pry) > 0.13.1
Requires:      gem(paco) >= 0.2
Requires:      gem(require-hooks) >= 0.2
Requires:      gem(ruby-next-core) >= 0
Requires:      gem(ruby-next-parser) >= 3.4.0.2
Requires:      gem(unparser) >= 0.6.0
Requires:      gem(zeitwerk) >= 0
Conflicts:     gem(paco) >= 1
Conflicts:     gem(require-hooks) >= 1
Conflicts:     gem(unparser) >= 1

%description   -n gem-ruby-next-core-devel
Ruby Next core functionality development package.

Ruby Next Core is a zero deps version of Ruby Next meant to be used as as
dependency in your gems.

It contains all the polyfills and utility files but doesn't require transpiler
dependencies to be install.

%description   -n gem-ruby-next-core-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета ruby-next-core.
%endif


%if_enabled    doc
%package       -n gem-ruby-next-doc
Version:       1.2.0
Release:       alt1
Summary:       Make older Rubies quack like edge Ruby documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета ruby-next
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(ruby-next) = 1.2.0

%description   -n gem-ruby-next-doc
Make older Rubies quack like edge Ruby documentation files.

Ruby Next is a collection of polyfills and a transpiler for supporting latest
and upcoming edge CRuby features in older versions and alternative
implementations (such as mruby, JRuby, Opal, Artichoke, RubyMotion, etc.).

%description   -n gem-ruby-next-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета ruby-next.
%endif


%if_enabled    devel
%package       -n gem-ruby-next-devel
Version:       1.2.0
Release:       alt1
Summary:       Make older Rubies quack like edge Ruby development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета ruby-next
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(ruby-next) = 1.2.0
Requires:      gem(benchmark_driver) >= 0
Requires:      gem(bootsnap) >= 0
Requires:      gem(paco) >= 0.2
Requires:      gem(pry-byebug) >= 0
Requires:      gem(require-hooks) >= 0.2
Requires:      gem(rubocop-md) >= 1.0
Requires:      gem(ruby-next-parser) >= 3.4.0.2
Requires:      gem(standard) >= 1.0
Requires:      gem(unparser) >= 0.6.0
Requires:      gem(zeitwerk) >= 0
Conflicts:     gem(paco) >= 1
Conflicts:     gem(require-hooks) >= 1
Conflicts:     gem(rubocop-md) >= 3
Conflicts:     gem(standard) >= 2
Conflicts:     gem(unparser) >= 1

%description   -n gem-ruby-next-devel
Make older Rubies quack like edge Ruby development package.

Ruby Next is a collection of polyfills and a transpiler for supporting latest
and upcoming edge CRuby features in older versions and alternative
implementations (such as mruby, JRuby, Opal, Artichoke, RubyMotion, etc.).

%description   -n gem-ruby-next-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета ruby-next.
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

%files         -n gem-ruby-next-core
%doc CHANGELOG.md LICENSE.txt README.md
%ruby_gemspecdir/ruby-next-core-1.2.0.gemspec
%ruby_gemslibdir/ruby-next-core-1.2.0

%files         -n ruby-next
%doc CHANGELOG.md LICENSE.txt README.md
%_bindir/ruby-next

%if_enabled    doc
%files         -n gem-ruby-next-core-doc
%doc CHANGELOG.md LICENSE.txt README.md
%ruby_gemsdocdir/ruby-next-core-1.2.0
%endif

%if_enabled    devel
%files         -n gem-ruby-next-core-devel
%doc CHANGELOG.md LICENSE.txt README.md
%endif

%if_enabled    doc
%files         -n gem-ruby-next-doc
%doc CHANGELOG.md LICENSE.txt README.md
%ruby_gemdocdir
%endif

%if_enabled    devel
%files         -n gem-ruby-next-devel
%doc CHANGELOG.md LICENSE.txt README.md
%endif


%changelog
* Mon Jun 22 2026 Pavel Skrylev <majioa@altlinux.org> 1.2.0-alt1
- ^ 1.1.2 -> 1.2.0

* Tue Dec 09 2025 Pavel Skrylev <majioa@altlinux.org> 1.1.2-alt1
- ^ 1.0.2 -> 1.1.2

* Wed Apr 17 2024 Pavel Skrylev <majioa@altlinux.org> 1.0.2-alt1
- + packaged gem with Ruby Policy 2.0
