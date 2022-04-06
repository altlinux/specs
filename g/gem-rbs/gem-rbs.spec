%define        gemname rbs

Name:          gem-rbs
Version:       2.3.0
Release:       alt1
Summary:       Type signature for Ruby
License:       BSD-2-Clause or Ruby
Group:         Development/Ruby
Url:           https://github.com/ruby/rbs
Vcs:           https://github.com/ruby/rbs.git
Packager:      Pavel Skrylev <majioa@altlinux.org>

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_ignore_names rbs-amber,steep
Provides:      gem(rbs) = 2.3.0


%description
RBS is the language for type signatures for Ruby and standard library
definitions.

RBS is a language to describe the structure of Ruby programs. You can write
down the definition of a class or module: methods defined in the class,
instance variables and their types, and inheritance/mix-in relations. It
also allows declaring constants and global variables.


%package       -n rbs
Version:       2.3.0
Release:       alt1
Summary:       Type signature for Ruby executable(s)
Summary(ru_RU.UTF-8): Исполнямка для самоцвета rbs
Group:         Other
BuildArch:     noarch

Requires:      gem(rbs) = 2.3.0

%description   -n rbs
Type signature for Ruby executable(s).

RBS is the language for type signatures for Ruby and standard library
definitions.

RBS is a language to describe the structure of Ruby programs. You can write
down the definition of a class or module: methods defined in the class,
instance variables and their types, and inheritance/mix-in relations. It
also allows declaring constants and global variables.

%description   -n rbs -l ru_RU.UTF-8
Исполнямка для самоцвета rbs.


%package       -n gem-rbs-doc
Version:       2.3.0
Release:       alt1
Summary:       Type signature for Ruby documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета rbs
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(rbs) = 2.3.0

%description   -n gem-rbs-doc
Type signature for Ruby documentation files.

RBS is the language for type signatures for Ruby and standard library
definitions.

RBS is a language to describe the structure of Ruby programs. You can write
down the definition of a class or module: methods defined in the class,
instance variables and their types, and inheritance/mix-in relations. It
also allows declaring constants and global variables.

%description   -n gem-rbs-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета rbs.


%package       -n gem-rbs-devel
Version:       2.3.0
Release:       alt1
Summary:       Type signature for Ruby development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета rbs
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(rbs) = 2.3.0

%description   -n gem-rbs-devel
Type signature for Ruby development package.

RBS is the language for type signatures for Ruby and standard library
definitions.

RBS is a language to describe the structure of Ruby programs. You can write
down the definition of a class or module: methods defined in the class,
instance variables and their types, and inheritance/mix-in relations. It
also allows declaring constants and global variables.

%description   -n gem-rbs-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета rbs.


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

%files         -n gem-rbs-doc
%doc README.md
%ruby_gemdocdir

%files         -n gem-rbs-devel
%doc README.md
%ruby_includedir/*


%changelog
* Sun Apr 03 2022 Pavel Skrylev <majioa@altlinux.org> 2.3.0-alt1
- + packaged gem with Ruby Policy 2.0
