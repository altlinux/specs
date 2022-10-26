%define        gemname ruby-debug-base19x

Name:          gem-ruby-debug-base19x
Version:       0.11.32
Release:       alt1
Summary:       Fast Ruby debugger - core component
License:       Unlicense
Group:         Development/Ruby
Url:           https://github.com/JetBrains/ruby-debug-base19
Vcs:           https://github.com/jetbrains/ruby-debug-base19.git
Packager:      Pavel Skrylev <majioa@altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
BuildRequires: gem(debugger-ruby_core_source) > 0
%if_with check
BuildRequires: gem(test-unit) >= 0
BuildRequires: gem(rake) >= 0.8.1
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
Requires:      gem(debugger-ruby_core_source) > 0
Requires:      gem(rake) >= 0.8.1
Provides:      gem(ruby-debug-base19x) = 0.11.32


%description
ruby-debug is a fast implementation of the standard Ruby debugger debug.rb. It
is implemented by utilizing a new Ruby C API hook. The core component provides
support that front-ends can build on. It provides breakpoint handling, bindings
for stack frames among other things.


%package       -n gem-ruby-debug-base19x-doc
Version:       0.11.32
Release:       alt1
Summary:       Fast Ruby debugger - core component documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета ruby-debug-base19x
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(ruby-debug-base19x) = 0.11.32

%description   -n gem-ruby-debug-base19x-doc
Fast Ruby debugger - core component documentation files.

ruby-debug is a fast implementation of the standard Ruby debugger debug.rb. It
is implemented by utilizing a new Ruby C API hook. The core component provides
support that front-ends can build on. It provides breakpoint handling, bindings
for stack frames among other things.

%description   -n gem-ruby-debug-base19x-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета ruby-debug-base19x.


%package       -n gem-ruby-debug-base19x-devel
Version:       0.11.32
Release:       alt1
Summary:       Fast Ruby debugger - core component development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета ruby-debug-base19x
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(ruby-debug-base19x) = 0.11.32
Requires:      gem(test-unit) >= 0

%description   -n gem-ruby-debug-base19x-devel
Fast Ruby debugger - core component development package.

ruby-debug is a fast implementation of the standard Ruby debugger debug.rb. It
is implemented by utilizing a new Ruby C API hook. The core component provides
support that front-ends can build on. It provides breakpoint handling, bindings
for stack frames among other things.

%description   -n gem-ruby-debug-base19x-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета ruby-debug-base19x.


%prep
%setup

%build
%ruby_build

%install
%ruby_install

%check
%ruby_test

%files
%doc README
%ruby_gemspec
%ruby_gemlibdir
# %ruby_gemextdir

%files         -n gem-ruby-debug-base19x-doc
%doc README
%ruby_gemdocdir

%files         -n gem-ruby-debug-base19x-devel
%doc README
%ruby_includedir/*


%changelog
* Tue Oct 18 2022 Pavel Skrylev <majioa@altlinux.org> 0.11.32-alt1
- + packaged gem with Ruby Policy 2.0
