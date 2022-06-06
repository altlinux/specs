%define        gemname ruby-debug-ide

Name:          gem-debug-ide
Version:       0.7.3
Release:       alt1
Summary:       IDE interface for ruby-debug
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/ruby-debug/ruby-debug-ide
Vcs:           https://github.com/ruby-debug/ruby-debug-ide.git
Packager:      Pavel Skrylev <majioa@altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
BuildRequires: gem(rake) >= 0.8.1

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
#ruby_alias_names ruby-debug-ide,debug-ide
Requires:      gem(rake) >= 0.8.1
Provides:      gem(ruby-debug-ide) = 0.7.3


%description
An interface which glues ruby-debug to IDEs like Eclipse (RDT), NetBeans and
RubyMine.


%package       -n debug-ide
Version:       0.7.3
Release:       alt1
Summary:       IDE interface for ruby-debug executable(s)
Summary(ru_RU.UTF-8): Исполнямка для самоцвета ruby-debug-ide
Group:         Other
BuildArch:     noarch

Requires:      gem(ruby-debug-ide) = 0.7.3

%description   -n debug-ide
IDE interface for ruby-debug executable(s).

An interface which glues ruby-debug to IDEs like Eclipse (RDT), NetBeans and
RubyMine.

%description   -n debug-ide -l ru_RU.UTF-8
Исполнямка для самоцвета ruby-debug-ide.


%package       -n gem-debug-ide-doc
Version:       0.7.3
Release:       alt1
Summary:       IDE interface for ruby-debug documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета ruby-debug-ide
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(ruby-debug-ide) = 0.7.3

%description   -n gem-debug-ide-doc
IDE interface for ruby-debug documentation files.

An interface which glues ruby-debug to IDEs like Eclipse (RDT), NetBeans and
RubyMine.

%description   -n gem-debug-ide-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета ruby-debug-ide.


%package       -n gem-debug-ide-devel
Version:       0.7.3
Release:       alt1
Summary:       IDE interface for ruby-debug development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета ruby-debug-ide
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(ruby-debug-ide) = 0.7.3

%description   -n gem-debug-ide-devel
IDE interface for ruby-debug development package.

An interface which glues ruby-debug to IDEs like Eclipse (RDT), NetBeans and
RubyMine.

%description   -n gem-debug-ide-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета ruby-debug-ide.


%prep
%setup

%build
%ruby_build

%install
%ruby_install

%check
%ruby_test

%files
%ruby_gemspec
%ruby_gemlibdir

%files         -n debug-ide
%_bindir/rdebug-ide
%_bindir/gdb_wrapper

%files         -n gem-debug-ide-doc
%ruby_gemdocdir

%files         -n gem-debug-ide-devel


%changelog
* Mon May 16 2022 Pavel Skrylev <majioa@altlinux.org> 0.7.3-alt1
- + packaged gem with Ruby Policy 2.0
