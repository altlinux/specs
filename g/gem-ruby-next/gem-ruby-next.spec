%define        _unpackaged_files_terminate_build 1
%def_enable    check
%def_enable    doc
%def_enable    devel
%define        gemname ruby-next

Name:          gem-ruby-next
Version:       1.0.2
Release:       alt1
Summary:       Make older Rubies quack like edge Ruby
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/ruby-next/ruby-next
Vcs:           https://github.com/ruby-next/ruby-next.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
%if_enabled check
BuildRequires: gem(require-hooks) >= 0.2
BuildRequires: gem(unparser) >= 0.6.0
BuildRequires: gem(paco) >= 0.2
BuildRequires: gem(benchmark_driver) >= 0
BuildRequires: gem(pry-byebug) >= 0
BuildRequires: gem(rubocop-md) >= 1.0
BuildRequires: gem(standard) >= 1.0
BuildRequires: gem(ruby-next-parser) >= 3.2.2.0
BuildRequires: gem(zeitwerk) >= 0
BuildRequires: gem(bootsnap) >= 0
BuildConflicts: gem(require-hooks) >= 1
BuildConflicts: gem(unparser) >= 0.7
BuildConflicts: gem(paco) >= 1
BuildConflicts: gem(rubocop-md) >= 2
BuildConflicts: gem(standard) >= 2
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_use_gem_dependency pry >= 0.13.1,pry < 1
Requires:      gem(require-hooks) >= 0.2
Requires:      gem(unparser) >= 0.6.0
Requires:      gem(paco) >= 0.2
Requires:      gem(ruby-next-parser) >= 3.2.2.0
Requires:      gem(ruby-next-core) = 1.0.2
Conflicts:     gem(require-hooks) >= 1
Conflicts:     gem(unparser) >= 0.7
Conflicts:     gem(paco) >= 1
Provides:      gem(ruby-next) = 1.0.2


%description
Ruby Next is a collection of polyfills and a transpiler for supporting latest
and upcoming edge CRuby features in older versions and alternative
implementations (such as mruby, JRuby, Opal, Artichoke, RubyMotion, etc.).


%package       -n gem-ruby-next-core
Version:       1.0.2
Release:       alt1
Summary:       Ruby Next core functionality
Group:         Development/Ruby
BuildArch:     noarch

Provides:      gem(ruby-next-core) = 1.0.2

%description   -n gem-ruby-next-core
Ruby Next Core is a zero deps version of Ruby Next meant to be used as as
dependency in your gems.

It contains all the polyfills and utility files but doesn't require transpiler
dependencies to be install.


%package       -n ruby-next
Version:       1.0.2
Release:       alt1
Summary:       Ruby Next core functionality executable(s)
Summary(ru_RU.UTF-8): Исполнямка для самоцвета ruby-next-core
Group:         Other
BuildArch:     noarch

Requires:      gem(ruby-next-core) = 1.0.2

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
Version:       1.0.2
Release:       alt1
Summary:       Ruby Next core functionality documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета ruby-next-core
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(ruby-next-core) = 1.0.2

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
Version:       1.0.2
Release:       alt1
Summary:       Ruby Next core functionality development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета ruby-next-core
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(ruby-next-core) = 1.0.2
Requires:      gem(require-hooks) >= 0.2
Requires:      gem(unparser) >= 0.6.0
Requires:      gem(paco) >= 0.2
Requires:      gem(benchmark_driver) >= 0
Requires:      gem(pry-byebug) >= 0
Requires:      gem(rubocop-md) >= 1.0
Requires:      gem(standard) >= 1.0
Requires:      gem(ruby-next-parser) >= 3.2.2.0
Requires:      gem(zeitwerk) >= 0
Requires:      gem(bootsnap) >= 0
Conflicts:     gem(require-hooks) >= 1
Conflicts:     gem(unparser) >= 0.7
Conflicts:     gem(paco) >= 1
Conflicts:     gem(rubocop-md) >= 2
Conflicts:     gem(standard) >= 2

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
Version:       1.0.2
Release:       alt1
Summary:       Make older Rubies quack like edge Ruby documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета ruby-next
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(ruby-next) = 1.0.2

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
Version:       1.0.2
Release:       alt1
Summary:       Make older Rubies quack like edge Ruby development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета ruby-next
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(ruby-next) = 1.0.2
Requires:      gem(benchmark_driver) >= 0
Requires:      gem(pry-byebug) >= 0
Requires:      gem(rubocop-md) >= 1.0
Requires:      gem(standard) >= 1.0
Requires:      gem(zeitwerk) >= 0
Requires:      gem(bootsnap) >= 0
Conflicts:     gem(rubocop-md) >= 2
Conflicts:     gem(standard) >= 2

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
%doc README.md
%ruby_gemspec
%ruby_gemlibdir

%files         -n gem-ruby-next-core
%doc README.md
%ruby_gemspecdir/ruby-next-core-1.0.2.gemspec
%ruby_gemslibdir/ruby-next-core-1.0.2

%files         -n ruby-next
%doc README.md
%_bindir/ruby-next

%if_enabled    doc
%files         -n gem-ruby-next-core-doc
%doc README.md
%ruby_gemsdocdir/ruby-next-core-1.0.2
%endif

%if_enabled    devel
%files         -n gem-ruby-next-core-devel
%doc README.md
%endif

%if_enabled    doc
%files         -n gem-ruby-next-doc
%doc README.md
%ruby_gemdocdir
%endif

%if_enabled    devel
%files         -n gem-ruby-next-devel
%doc README.md
%endif


%changelog
* Wed Apr 17 2024 Pavel Skrylev <majioa@altlinux.org> 1.0.2-alt1
- + packaged gem with Ruby Policy 2.0
