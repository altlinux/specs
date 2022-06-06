%define        gemname debase

Name:          gem-debase
Version:       0.2.5.beta2
Release:       alt1
Summary:       debase is a fast implementation of the standard Ruby debugger debug.rb for Ruby 2.0
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/ruby-debug/debase
Vcs:           https://github.com/ruby-debug/debase.git
Packager:      Pavel Skrylev <majioa@altlinux.org>

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
BuildRequires: gem(debase-ruby_core_source) >= 0.10.12
BuildRequires: gem(test-unit) >= 0
BuildRequires: gem(rake) >= 0

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
Requires:      gem(debase-ruby_core_source) >= 0.10.12
Provides:      gem(debase) = 0.2.5.beta2


%description
debase is a fast implementation of the standard Ruby debugger debug.rb for Ruby
2.0+. It is implemented by utilizing a new Ruby TracePoint class. The core
component provides support that front-ends can build on. It provides breakpoint
handling, bindings for stack frames among other things.


%package       -n gem-debase-doc
Version:       0.2.5.beta2
Release:       alt1
Summary:       debase is a fast implementation of the standard Ruby debugger debug.rb for Ruby 2.0 documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета debase
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(debase) = 0.2.5.beta2

%description   -n gem-debase-doc
debase is a fast implementation of the standard Ruby debugger debug.rb for Ruby
2.0 documentation files.

debase is a fast implementation of the standard Ruby debugger debug.rb for Ruby
2.0+. It is implemented by utilizing a new Ruby TracePoint class. The core
component provides support that front-ends can build on. It provides breakpoint
handling, bindings for stack frames among other things.

%description   -n gem-debase-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета debase.


%package       -n gem-debase-devel
Version:       0.2.5.beta2
Release:       alt1
Summary:       debase is a fast implementation of the standard Ruby debugger debug.rb for Ruby 2.0 development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета debase
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(debase) = 0.2.5.beta2
Requires:      gem(test-unit) >= 0
Requires:      gem(rake) >= 0

%description   -n gem-debase-devel
debase is a fast implementation of the standard Ruby debugger debug.rb for Ruby
2.0 development package.

debase is a fast implementation of the standard Ruby debugger debug.rb for Ruby
2.0+. It is implemented by utilizing a new Ruby TracePoint class. The core
component provides support that front-ends can build on. It provides breakpoint
handling, bindings for stack frames among other things.

%description   -n gem-debase-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета debase.


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

%files         -n gem-debase-doc
%doc README.md
%ruby_gemdocdir

%files         -n gem-debase-devel
%doc README.md
%ruby_includedir/*


%changelog
* Mon May 16 2022 Pavel Skrylev <majioa@altlinux.org> 0.2.5.beta2-alt1
- + packaged gem with Ruby Policy 2.0
