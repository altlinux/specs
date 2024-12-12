%define        _unpackaged_files_terminate_build 1
%def_enable    check
%def_enable    doc
%def_enable    devel
%define        gemname wasmtime

Name:          gem-wasmtime
Version:       27.0.0
Release:       alt1
Summary:       Wasmtime bindings for Ruby
License:       Apache-2.0
Group:         Development/Ruby
Url:           https://github.com/BytecodeAlliance/wasmtime-rb
Vcs:           https://github.com/bytecodealliance/wasmtime-rb.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
BuildRequires: gem(get_process_mem) >= 0
BuildRequires: gem(rake) >= 13.1.0
BuildRequires: gem(rake-compiler) >= 0
BuildRequires: gem(standard) >= 1.40
BuildRequires: gem(yard) >= 0
BuildRequires: gem(yard-rustdoc) >= 0.4.0
BuildConflicts: gem(rake) >= 14
BuildConflicts: gem(standard) >= 2
BuildConflicts: gem(yard-rustdoc) >= 0.5
%if_enabled check
BuildRequires: gem(benchmark-ips) >= 0
BuildRequires: gem(rb_sys) >= 0.9.97
BuildRequires: gem(rspec) >= 3.10.0
BuildConflicts: gem(rb_sys) >= 0.10
BuildConflicts: gem(rspec) >= 4
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_use_gem_dependency rake >= 13.1.0,rake < 14
%ruby_use_gem_dependency rspec >= 3.10.0,rspec < 4
Requires:      ruby >= 3.1.0
Requires:      gem(rb_sys) >= 0.9.97
Conflicts:     gem(rb_sys) >= 0.10
Provides:      gem(wasmtime) = 27.0.0

%description
A Ruby binding for Wasmtime, a WebAssembly runtime.

wasmtime-rb's goal is to expose the full power of Wasmtime in Ruby with minimal
overhead, serving as a foundation layer for other projects or gems.


%if_enabled    doc
%package       -n gem-wasmtime-doc
Version:       27.0.0
Release:       alt1
Summary:       Wasmtime bindings for Ruby documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета wasmtime
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(wasmtime) = 27.0.0

%description   -n gem-wasmtime-doc
Wasmtime bindings for Ruby documentation files.

A Ruby binding for Wasmtime, a WebAssembly runtime.

wasmtime-rb's goal is to expose the full power of Wasmtime in Ruby with minimal
overhead, serving as a foundation layer for other projects or gems.

%description   -n gem-wasmtime-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета wasmtime.
%endif


%if_enabled    devel
%package       -n gem-wasmtime-devel
Version:       27.0.0
Release:       alt1
Summary:       Wasmtime bindings for Ruby development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета wasmtime
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(wasmtime) = 27.0.0
Requires:      gem(benchmark-ips) >= 0
Requires:      gem(get_process_mem) >= 0
Requires:      gem(rake) >= 13.1.0
Requires:      gem(rake-compiler) >= 0
Requires:      gem(rspec) >= 3.10.0
Requires:      gem(standard) >= 1.40
Requires:      gem(yard) >= 0
Requires:      gem(yard-rustdoc) >= 0.4.0
Conflicts:     gem(rake) >= 14
Conflicts:     gem(rspec) >= 4
Conflicts:     gem(standard) >= 2
Conflicts:     gem(yard-rustdoc) >= 0.5

%description   -n gem-wasmtime-devel
Wasmtime bindings for Ruby development package.

A Ruby binding for Wasmtime, a WebAssembly runtime.

wasmtime-rb's goal is to expose the full power of Wasmtime in Ruby with minimal
overhead, serving as a foundation layer for other projects or gems.

%description   -n gem-wasmtime-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета wasmtime.
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
%doc LICENSE README.md CHANGELOG.md CONTRIBUTING.md
%ruby_gemspec
%ruby_gemlibdir
#ruby_gemextdir

%if_enabled    doc
%files         -n gem-wasmtime-doc
%doc LICENSE README.md CHANGELOG.md CONTRIBUTING.md
%ruby_gemdocdir
%endif

%if_enabled    devel
%files         -n gem-wasmtime-devel
%doc LICENSE README.md CHANGELOG.md CONTRIBUTING.md
%endif


%changelog
* Wed Dec 11 2024 Pavel Skrylev <majioa@altlinux.org> 27.0.0-alt1
- + packaged gem with Ruby Policy 2.0
- * define explicit dependencies
