%define        _unpackaged_files_terminate_build 1
%def_enable    check
%def_enable    doc
%def_enable    devel
%define        gemname debase

Name:          gem-debase
Version:       0.2.9
Release:       alt1
Summary:       debase is a fast implementation of the standard Ruby debugger debug.rb for Ruby 2.0
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/ruby-debug/debase
Vcs:           https://github.com/ruby-debug/debase.git
Packager:      Pavel Skrylev <majioa@altlinux.org>

Source:        %name-%version.tar
BuildRequires(pre): rpm-macros-ruby setup-rb rake
BuildRequires(pre): rpm-build-ruby
BuildRequires: gem(debase-ruby_core_source) >= 3.4.1
%if_enabled check
BuildRequires: gem(rake) >= 0
BuildRequires: gem(test-unit) >= 0
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
Requires:      ruby >= 2.0
Requires:      gem(debase-ruby_core_source) >= 3.4.1
Provides:      debase = %EVR
Provides:      gem(debase) = 0.2.9

%description
debase is a fast implementation of the standard Ruby debugger debug.rb for Ruby
2.0+. It is implemented by utilizing a new Ruby TracePoint class. The core
component provides support that front-ends can build on. It provides breakpoint
handling, bindings for stack frames among other things.


%if_enabled    doc
%package       -n gem-debase-doc
Version:       0.2.9
Release:       alt1
Summary:       debase is a fast implementation of the standard Ruby debugger debug.rb for Ruby 2.0 documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета debase
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(debase) = 0.2.9

%description   -n gem-debase-doc
debase is a fast implementation of the standard Ruby debugger debug.rb for Ruby
2.0 documentation files.

debase is a fast implementation of the standard Ruby debugger debug.rb for Ruby
2.0+. It is implemented by utilizing a new Ruby TracePoint class. The core
component provides support that front-ends can build on. It provides breakpoint
handling, bindings for stack frames among other things.

%description   -n gem-debase-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета debase.
%endif


%if_enabled    devel
%package       -n gem-debase-devel
Version:       0.2.9
Release:       alt1
Summary:       debase is a fast implementation of the standard Ruby debugger debug.rb for Ruby 2.0 development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета debase
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(debase) = 0.2.9
Requires:      gem(rake) >= 0
Requires:      gem(test-unit) >= 0

%description   -n gem-debase-devel
debase is a fast implementation of the standard Ruby debugger debug.rb for Ruby
2.0 development package.

debase is a fast implementation of the standard Ruby debugger debug.rb for Ruby
2.0+. It is implemented by utilizing a new Ruby TracePoint class. The core
component provides support that front-ends can build on. It provides breakpoint
handling, bindings for stack frames among other things.

%description   -n gem-debase-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета debase.
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
%doc LICENSE MIT_LICENSE README.md
%ruby_gemspec
%ruby_gemlibdir
%ruby_gemextdir

%if_enabled    doc
%files         -n gem-debase-doc
%doc LICENSE MIT_LICENSE README.md
%ruby_gemdocdir
%endif

%if_enabled    devel
%files         -n gem-debase-devel
%doc LICENSE MIT_LICENSE README.md
%ruby_includedir/*
%endif


%changelog
* Tue Sep 08 2026 Pavel Skrylev <majioa@altlinux.org> 0.2.9-alt1
- ^ 0.2.6 -> 0.2.9

* Wed Jul 24 2024 Pavel Skrylev <majioa@altlinux.org> 0.2.6-alt0.1
- ^ 0.2.5.beta2 -> 0.2.6.pre

* Mon May 16 2022 Pavel Skrylev <majioa@altlinux.org> 0.2.5.beta2-alt1
- + packaged gem with Ruby Policy 2.0
