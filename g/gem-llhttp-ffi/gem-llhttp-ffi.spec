%define        _unpackaged_files_terminate_build 0
%def_enable    check
%def_enable    doc
%def_enable    devel
%define        gemname llhttp-ffi

Name:          gem-llhttp-ffi
Version:       0.5.1.16
Release:       alt0.1
Summary:       Ruby FFI bindings for llhttp
License:       MPL-2.0
Group:         Development/Ruby
Url:           https://github.com/bryanp/llhttp/
Vcs:           https://github.com/bryanp/llhttp.git
Packager:      Baltix Maintaining Team <baltix@packages.altlinux.org>

Source:        %name-%version.tar
Autoprov:      yes,noruby
Autoreq:       yes,noruby
BuildRequires(pre): rpm-build-ruby
%if_enabled check
BuildRequires: gem(async) >= 0
BuildRequires: gem(ffi-compiler) >= 1.0
BuildRequires: gem(io-endpoint) >= 0
BuildRequires: gem(rake) >= 0
BuildRequires: gem(rake-compiler) >= 0
BuildRequires: gem(rspec) >= 0
BuildRequires: gem(standardrb) >= 0
BuildConflicts: gem(ffi-compiler) >= 2
BuildConflicts: gem(rake) >= 14
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_ignore_names gem-llhttp-ffi
Requires:      ruby >= 2.5.0
Requires:      gem(ffi-compiler) >= 1.0
Requires:      gem(rake) >= 13.0
Conflicts:     gem(ffi-compiler) >= 2
Conflicts:     gem(rake) >= 14
Provides:      gem(llhttp-ffi) = 0.5.1.16

%ruby_use_gem_version llhttp:0.6.1.16
%ruby_use_gem_version llhttp-ffi:0.5.1.16

%description
Ruby FFI bindings for llhttp.


%package       -n gem-llhttp
Version:       0.6.1.16
Release:       alt0.1
Summary:       Ruby bindings for llhttp
Group:         Development/Ruby

Autoprov:      yes,noruby
Autoreq:       yes,noruby
Requires:      ruby >= 2.6.7
Provides:      gem(llhttp) = 0.6.1.16

%description   -n gem-llhttp
Ruby bindings for llhttp.


%if_enabled    doc
%package       -n gem-llhttp-doc
Version:       0.6.1.16
Release:       alt0.1
Summary:       Ruby bindings for llhttp documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета llhttp
Group:         Development/Documentation
BuildArch:     noarch

Autoprov:      yes,noruby
Autoreq:       yes,noruby
Requires:      gem(llhttp) = 0.6.1.16

%description   -n gem-llhttp-doc
Ruby bindings for llhttp documentation files.

%description   -n gem-llhttp-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета llhttp.
%endif


%if_enabled    devel
%package       -n gem-llhttp-devel
Version:       0.6.1.16
Release:       alt0.1
Summary:       Ruby bindings for llhttp development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета llhttp
Group:         Development/Ruby
BuildArch:     noarch

Autoprov:      yes,noruby
Autoreq:       yes,noruby
Requires:      gem(llhttp) = 0.6.1.16
Requires:      gem(async) >= 0
Requires:      gem(io-endpoint) >= 0
Requires:      gem(rake) >= 0
Requires:      gem(rake-compiler) >= 0
Requires:      gem(rspec) >= 0

%description   -n gem-llhttp-devel
Ruby bindings for llhttp development package.

%description   -n gem-llhttp-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета llhttp.
%endif


%if_enabled    devel
%package       -n gem-llhttp-ffi-devel
Version:       0.5.1.16
Release:       alt0.1
Summary:       Ruby FFI bindings for llhttp development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета llhttp-ffi
Group:         Development/Ruby
BuildArch:     noarch

Autoprov:      yes,noruby
Autoreq:       yes,noruby
Requires:      gem(llhttp-ffi) = 0.5.1.16
Requires:      gem(async) >= 0
Requires:      gem(ffi-compiler) >= 1.0
Requires:      gem(io-endpoint) >= 0
Requires:      gem(rake) >= 0
Requires:      gem(rake-compiler) >= 0
Requires:      gem(rspec) >= 0
Requires:      gem(standardrb) >= 0
Conflicts:     gem(ffi-compiler) >= 2
Conflicts:     gem(rake) >= 14

%description   -n gem-llhttp-ffi-devel
Ruby FFI bindings for llhttp development package.

%description   -n gem-llhttp-ffi-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета llhttp-ffi.
%endif


%if_enabled    doc
%package       -n gem-llhttp-ffi-doc
Version:       0.5.1.16
Release:       alt0.1
Summary:       Ruby FFI bindings for llhttp documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета llhttp-ffi
Group:         Development/Documentation
BuildArch:     noarch

Autoprov:      yes,noruby
Autoreq:       yes,noruby
Requires:      gem(llhttp-ffi) = 0.5.1.16

%description   -n gem-llhttp-ffi-doc
Ruby FFI bindings for llhttp documentation files.

%description   -n gem-llhttp-ffi-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета llhttp-ffi.
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

%files         -n gem-llhttp
%doc README.md
%ruby_gemspecdir/llhttp-0.6.1.16.gemspec
%ruby_gemslibdir/llhttp-0.6.1.16
%ruby_gemsextdir/llhttp-0.6.1.16

%if_enabled    doc
%files         -n gem-llhttp-doc
%doc README.md
%ruby_gemsdocdir/llhttp-0.6.1.16
%endif

%if_enabled    devel
%files         -n gem-llhttp-devel
%doc README.md
%ruby_includedir/*
%endif

%if_enabled    doc
%files         -n gem-llhttp-ffi-doc
%doc README.md
%ruby_gemsdocdir/llhttp-ffi-0.5.1.16
%endif

%if_enabled    devel
%files         -n gem-llhttp-ffi-devel
%doc README.md
%ruby_includedir/*
%endif


%changelog
* Tue Nov 18 2025 Pavel Skrylev <majioa@altlinux.org> 0.5.1.16-alt0.1
- ^ 0.5.0 -> 0.5.1.16

* Wed Apr 17 2024 Pavel Skrylev <majioa@altlinux.org> 0.5.0-alt1
- + packaged gem with Ruby Policy 2.0
