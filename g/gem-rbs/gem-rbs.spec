%define        _unpackaged_files_terminate_build 1
%def_disable   check
%def_enable    doc
%def_enable    devel

Name:          gem-rbs
Version:       4.2.0
Release:       alt1
Summary:       Type signature for Ruby
License:       BSD-2-Clause or Ruby or MIT
Group:         Development/Ruby
Url:           https://github.com/ruby/rbs
Vcs:           https://github.com/ruby/rbs.git
Packager:      Baltix Maintaining Team <baltix@packages.altlinux.org>

Source:        %name-%version.tar
BuildRequires(pre): rpm-macros-ruby
BuildRequires(pre): setup-rb
BuildRequires(pre): rake
BuildRequires(pre): libruby-devel
%if_enabled check
BuildRequires: gem(activesupport) >= 7.0
BuildRequires: gem(csv) >= 0
BuildRequires: gem(digest) >= 0
BuildRequires: gem(extconf_compile_commands_json) >= 0
BuildRequires: gem(fileutils) >= 0
BuildRequires: gem(goodcheck) >= 0
BuildRequires: gem(irb) >= 0
BuildRequires: gem(json) >= 0
BuildRequires: gem(json-schema) >= 0
BuildRequires: gem(net-smtp) >= 0
BuildRequires: gem(ostruct) >= 0
BuildRequires: gem(pstore) >= 0
BuildRequires: gem(raap) >= 0
BuildRequires: gem(rake) >= 0
BuildRequires: gem(rake-compiler) >= 0
BuildRequires: gem(rbs) >= 0
BuildRequires: gem(rdoc) >= 0
BuildRequires: gem(rspec) >= 0
BuildRequires: gem(rubocop) >= 0
BuildRequires: gem(rubocop-on-rbs) >= 0
BuildRequires: gem(rubocop-rubycw) >= 0
BuildRequires: gem(tempfile) >= 0
BuildRequires: gem(test-unit) >= 0
BuildRequires: gem(timeout) >= 0
BuildConflicts: gem(activesupport) >= 8
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
Requires:      ruby >= 3.2
Requires:      gem(logger) >= 0
Requires:      gem(prism) >= 1.6.0
Requires:      gem(tsort) >= 0
Provides:      gem(rbs) = 4.2.0

%description
RBS is the language for type signatures for Ruby and standard library
definitions.

RBS is a language to describe the structure of Ruby programs. You can write down
the definition of a class or module: methods defined in the class, instance
variables and their types, and inheritance/mix-in relations. It also allows
declaring constants and global variables.


%package       -n rbs
Version:       4.2.0
Release:       alt1
Summary:       Type signature for Ruby executable(s)
Summary(ru_RU.UTF-8): Исполнямка для самоцвета rbs
Group:         Other
BuildArch:     noarch

Requires:      gem(rbs) = 4.2.0
Requires:      gem(activesupport) >= 7.0
Requires:      gem(ostruct) >= 0
Requires:      gem(pstore) >= 0
Conflicts:     gem(activesupport) >= 8

%description   -n rbs
Type signature for Ruby executable(s).

RBS is the language for type signatures for Ruby and standard library
definitions.

RBS is a language to describe the structure of Ruby programs. You can write down
the definition of a class or module: methods defined in the class, instance
variables and their types, and inheritance/mix-in relations. It also allows
declaring constants and global variables.

%description   -n rbs -l ru_RU.UTF-8
Исполнямка для самоцвета rbs.


%if_enabled    doc
%package       -n gem-rbs-doc
Version:       4.2.0
Release:       alt1
Summary:       Type signature for Ruby
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета rbs
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem-rbs = 4.2.0-alt1

%description   -n gem-rbs-doc
Type signature for Ruby documentation files.

RBS is the language for type signatures for Ruby and standard library
definitions.

RBS is a language to describe the structure of Ruby programs. You can write down
the definition of a class or module: methods defined in the class, instance
variables and their types, and inheritance/mix-in relations. It also allows
declaring constants and global variables.

%description   -n gem-rbs-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета rbs. %endif
%endif


%if_enabled    devel
%package       -n gem-rbs-devel
Version:       4.2.0
Release:       alt1
Summary:       Type signature for Ruby
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета rbs
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem-rbs = 4.2.0-alt1
Requires:      gem(activesupport) >= 7.0
Requires:      gem(csv) >= 0
Requires:      gem(digest) >= 0
Requires:      gem(extconf_compile_commands_json) >= 0
Requires:      gem(fileutils) >= 0
Requires:      gem(goodcheck) >= 0
Requires:      gem(irb) >= 0
Requires:      gem(json) >= 0
Requires:      gem(json-schema) >= 0
Requires:      gem(logger) >= 0
Requires:      gem(net-smtp) >= 0
Requires:      gem(ostruct) >= 0
Requires:      gem(prism) >= 1.6.0
Requires:      gem(pstore) >= 0
Requires:      gem(raap) >= 0
Requires:      gem(rake) >= 0
Requires:      gem(rake-compiler) >= 0
Requires:      gem(rbs) >= 0
Requires:      gem(rdoc) >= 0
Requires:      gem(rspec) >= 0
Requires:      gem(rubocop) >= 0
Requires:      gem(rubocop-on-rbs) >= 0
Requires:      gem(rubocop-rubycw) >= 0
Requires:      gem(tempfile) >= 0
Requires:      gem(test-unit) >= 0
Requires:      gem(timeout) >= 0
Requires:      gem(tsort) >= 0
Conflicts:     gem(activesupport) >= 8

%description   -n gem-rbs-devel
Type signature for Ruby development package.

RBS is the language for type signatures for Ruby and standard library
definitions.

RBS is a language to describe the structure of Ruby programs. You can write down
the definition of a class or module: methods defined in the class, instance
variables and their types, and inheritance/mix-in relations. It also allows
declaring constants and global variables.

%description   -n gem-rbs-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета rbs. %endif
%endif


%prep
%setup
sed 's,gem "rbs-amber",# gem "rbs-amber",' -i Gemfile

%build
%ruby_build

%install
%ruby_install

%check
%ruby_test

%files
%ruby_gemspec
%ruby_gemlibdir
%ruby_gemextdir

%files         -n rbs
%_bindir/rbs

%if_enabled    doc
%files         -n gem-rbs-doc
%ruby_gemdocdir
%endif

%if_enabled    devel
%files         -n gem-rbs-devel
%_includedir/rbs_extension
%endif


%changelog
* Wed Aug 26 2026 Pavel Skrylev <majioa@altlinux.org> 4.2.0-alt1
- ^ 3.9.4 -> 4.2.0

* Wed Oct 22 2025 Pavel Skrylev <majioa@altlinux.org> 3.9.4-alt1
- ^ 3.5.2 -> 3.9.4

* Wed Jul 24 2024 Pavel Skrylev <majioa@altlinux.org> 3.5.2-alt1
- ^ 3.4.4 -> 3.5.2

* Mon Apr 15 2024 Pavel Skrylev <majioa@altlinux.org> 3.4.4-alt1
- ^ 2.4.0 -> 3.4.4

* Tue May 17 2022 Pavel Skrylev <majioa@altlinux.org> 2.4.0-alt1
- ^ 2.3.0 -> 2.4.0

* Sun Apr 03 2022 Pavel Skrylev <majioa@altlinux.org> 2.3.0-alt1
- + packaged gem with Ruby Policy 2.0
