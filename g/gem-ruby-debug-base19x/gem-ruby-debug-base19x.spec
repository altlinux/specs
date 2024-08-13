%define        _unpackaged_files_terminate_build 1
%def_enable    check
%def_enable    doc
%def_enable    devel
%define        gemname ruby-debug-base19x

Name:          gem-ruby-debug-base19x
Version:       0.11.32.3
Release:       alt1
Summary:       Fast Ruby debugger - core component
License:       Unlicense
Group:         Development/Ruby
Url:           https://github.com/JetBrains/ruby-debug-base19
Vcs:           https://github.com/jetbrains/ruby-debug-base19.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
%if_enabled check
BuildRequires: gem(debugger-ruby_core_source) > 0
BuildRequires: gem(rake) >= 0.8.1
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
Requires:      gem(test-unit) >= 0
Requires:      gem(debugger-ruby_core_source) > 0
Requires:      gem(rake) >= 0.8.1
Provides:      gem(ruby-debug-base19x) = 0.11.32.3

%ruby_use_gem_version ruby-debug-base19x:0.11.32.3

%description
ruby-debug is a fast implementation of the standard Ruby debugger debug.rb. It
is implemented by utilizing a new Ruby C API hook. The core component provides
support that front-ends can build on. It provides breakpoint handling, bindings
for stack frames among other things.


%if_enabled    doc
%package       -n gem-ruby-debug-base19x-doc
Version:       0.11.32.3
Release:       alt1
Summary:       Fast Ruby debugger - core component documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета ruby-debug-base19x
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(ruby-debug-base19x) = 0.11.32.3

%description   -n gem-ruby-debug-base19x-doc
Fast Ruby debugger - core component documentation files.

ruby-debug is a fast implementation of the standard Ruby debugger debug.rb. It
is implemented by utilizing a new Ruby C API hook. The core component provides
support that front-ends can build on. It provides breakpoint handling, bindings
for stack frames among other things.

%description   -n gem-ruby-debug-base19x-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета ruby-debug-base19x.
%endif


%if_enabled    devel
%package       -n gem-ruby-debug-base19x-devel
Version:       0.11.32.3
Release:       alt1
Summary:       Fast Ruby debugger - core component development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета ruby-debug-base19x
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(ruby-debug-base19x) = 0.11.32.3

%description   -n gem-ruby-debug-base19x-devel
Fast Ruby debugger - core component development package.

ruby-debug is a fast implementation of the standard Ruby debugger debug.rb. It
is implemented by utilizing a new Ruby C API hook. The core component provides
support that front-ends can build on. It provides breakpoint handling, bindings
for stack frames among other things.

%description   -n gem-ruby-debug-base19x-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета ruby-debug-base19x.
%endif


%prep
%setup
%autopatch

%build
%ruby_build

%install
%ruby_install

%check
%ruby_test

%files
%doc LICENSE README
%ruby_gemspec
%ruby_gemlibdir
%ruby_gemextdir

%if_enabled    doc
%files         -n gem-ruby-debug-base19x-doc
%doc LICENSE README
%ruby_gemdocdir
%endif

%if_enabled    devel
%files         -n gem-ruby-debug-base19x-devel
%doc LICENSE README
%ruby_includedir/*
%endif


%changelog
* Mon Aug 12 2024 Pavel Skrylev <majioa@altlinux.org> 0.11.32.3-alt1
- ^ 0.11.32 -> 0.11.32.3

* Tue Oct 18 2022 Pavel Skrylev <majioa@altlinux.org> 0.11.32-alt1
- + packaged gem with Ruby Policy 2.0
