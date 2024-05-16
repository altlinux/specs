%define        _unpackaged_files_terminate_build 1
%def_enable    check
%def_enable    doc
%def_enable    devel
%define        gemname rbs

Name:          gem-rbs
Version:       3.4.4
Release:       alt1
Summary:       Type signature for Ruby
License:       BSD-2-Clause or Ruby
Group:         Development/Ruby
Url:           https://github.com/ruby/rbs
Vcs:           https://github.com/ruby/rbs.git
Packager:      Pavel Skrylev <majioa@altlinux.org>

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
%if_enabled check
BuildRequires: gem(rake) >= 0
BuildRequires: gem(rake-compiler) >= 0
BuildRequires: gem(test-unit) >= 0
BuildRequires: gem(rspec) >= 0
BuildRequires: gem(rubocop) >= 0
BuildRequires: gem(rubocop-rubycw) >= 0
BuildRequires: gem(json) >= 0
BuildRequires: gem(json-schema) >= 0
BuildRequires: gem(stackprof) >= 0
BuildRequires: gem(goodcheck) >= 0
BuildRequires: gem(dbm) >= 0
BuildRequires: gem(digest) >= 0
BuildRequires: gem(tempfile) >= 0
BuildRequires: gem(rdoc) >= 0
BuildRequires: gem(net-smtp) >= 0
BuildRequires: gem(minitest) >= 0
BuildRequires: gem(abbrev) >= 0
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
Requires:      gem(abbrev) >= 0
Provides:      gem(rbs) = 3.4.4

%ruby_ignore_names steep

%description
RBS is the language for type signatures for Ruby and standard library
definitions.

RBS is a language to describe the structure of Ruby programs. You can write down
the definition of a class or module: methods defined in the class, instance
variables and their types, and inheritance/mix-in relations. It also allows
declaring constants and global variables.


%package       -n rbs
Version:       3.4.4
Release:       alt1
Summary:       Type signature for Ruby executable(s)
Summary(ru_RU.UTF-8): Исполнямка для самоцвета rbs
Group:         Other
BuildArch:     noarch

Requires:      gem(rbs) = 3.4.4

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
Version:       3.4.4
Release:       alt1
Summary:       Type signature for Ruby documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета rbs
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(rbs) = 3.4.4

%description   -n gem-rbs-doc
Type signature for Ruby documentation files.

RBS is the language for type signatures for Ruby and standard library
definitions.

RBS is a language to describe the structure of Ruby programs. You can write down
the definition of a class or module: methods defined in the class, instance
variables and their types, and inheritance/mix-in relations. It also allows
declaring constants and global variables.

%description   -n gem-rbs-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета rbs.
%endif


%if_enabled    devel
%package       -n gem-rbs-devel
Version:       3.4.4
Release:       alt1
Summary:       Type signature for Ruby development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета rbs
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(rbs) = 3.4.4
Requires:      gem(rake) >= 0
Requires:      gem(rake-compiler) >= 0
Requires:      gem(test-unit) >= 0
Requires:      gem(rspec) >= 0
Requires:      gem(rubocop) >= 0
Requires:      gem(rubocop-rubycw) >= 0
Requires:      gem(json) >= 0
Requires:      gem(json-schema) >= 0
Requires:      gem(stackprof) >= 0
Requires:      gem(goodcheck) >= 0
Requires:      gem(dbm) >= 0
Requires:      gem(digest) >= 0
Requires:      gem(tempfile) >= 0
Requires:      gem(rdoc) >= 0
Requires:      gem(net-smtp) >= 0
Requires:      gem(minitest) >= 0

%description   -n gem-rbs-devel
Type signature for Ruby development package.

RBS is the language for type signatures for Ruby and standard library
definitions.

RBS is a language to describe the structure of Ruby programs. You can write down
the definition of a class or module: methods defined in the class, instance
variables and their types, and inheritance/mix-in relations. It also allows
declaring constants and global variables.

%description   -n gem-rbs-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета rbs.
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
%ruby_gemextdir

%files         -n rbs
%doc README.md
%_bindir/rbs

%if_enabled    doc
%files         -n gem-rbs-doc
%doc README.md
%ruby_gemdocdir
%endif

%if_enabled    devel
%files         -n gem-rbs-devel
%doc README.md
%ruby_includedir/*
%endif


%changelog
* Mon Apr 15 2024 Pavel Skrylev <majioa@altlinux.org> 3.4.4-alt1
- ^ 2.4.0 -> 3.4.4

* Tue May 17 2022 Pavel Skrylev <majioa@altlinux.org> 2.4.0-alt1
- ^ 2.3.0 -> 2.4.0

* Sun Apr 03 2022 Pavel Skrylev <majioa@altlinux.org> 2.3.0-alt1
- + packaged gem with Ruby Policy 2.0
