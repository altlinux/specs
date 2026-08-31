%define        _unpackaged_files_terminate_build 1
%def_enable    check
%def_enable    doc
%def_enable    devel
%define        gemname rb_sys

Name:          gem-rb-sys
Version:       0.9.128
Release:       alt1.1
Summary:       Helpers for compiling Rust extensions for ruby
License:       MIT or Apache-2.0
Group:         Other
Url:           https://oxidize-rb.github.io/rb-sys/
Vcs:           https://github.com/oxidize-rb/rb-sys.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
Patch:         no_rust.patch
BuildRequires(pre): rpm-macros-ruby setup-rb rake
%if_enabled check
BuildRequires: gem(base64) >= 0
BuildRequires: gem(minitest) >= 5
BuildRequires: gem(mutex_m) >= 0
BuildRequires: gem(ostruct) >= 0.6.3
BuildRequires: gem(racc) >= 0
BuildRequires: gem(rake) >= 0
BuildRequires: gem(rake-compiler) >= 0
BuildRequires: gem(rake-compiler-dock) >= 1.2.1
BuildRequires: gem(standard) >= 1.54.0
BuildRequires: gem(tsort) >= 0
BuildRequires: gem(yard) >= 0
BuildConflicts: gem(ostruct) >= 0.7
BuildConflicts: gem(rake-compiler-dock) >= 2
BuildConflicts: gem(standard) >= 2
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_use_gem_dependency rake-compiler-dock >= 1.2.1,rake-compiler-dock < 2
%ruby_use_gem_dependency standard >= 1.56.0,standard < 2
%ruby_use_gem_dependency minitest >= 5.0
%ruby_alias_names rb_sys,rb-sys
Requires:      ruby >= 2.7.0
Requires:      gem(rake-compiler-dock) >= 1.2.1
Conflicts:     gem(rake-compiler-dock) >= 2
Provides:      gem(rb_sys) = 0.9.128

%ruby_ignore_names gem-rb-sys

%description
Helpers for compiling Rust extensions for ruby


%package       -n rb-sys-dock
Version:       0.9.128
Release:       alt1.1
Summary:       Helpers for compiling Rust extensions for ruby executable(s)
Summary(ru_RU.UTF-8): Исполнямка для самоцвета rb_sys
Group:         Other
BuildArch:     noarch

Requires:      gem(rb_sys) = 0.9.128

%description   -n rb-sys-dock
Helpers for compiling Rust extensions for ruby executable(s).

%description   -n rb-sys-dock -l ru_RU.UTF-8
Исполнямка для самоцвета rb_sys.


%if_enabled    doc
%package       -n gem-rb-sys-doc
Version:       0.9.128
Release:       alt1.1
Summary:       Helpers for compiling Rust extensions for ruby documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета rb_sys
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(rb_sys) = 0.9.128

%description   -n gem-rb-sys-doc
Helpers for compiling Rust extensions for ruby documentation files.

%description   -n gem-rb-sys-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета rb_sys.
%endif


%if_enabled    devel
%package       -n gem-rb-sys-devel
Version:       0.9.128
Release:       alt1.1
Summary:       Helpers for compiling Rust extensions for ruby development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета rb_sys
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(rb_sys) = 0.9.128
Requires:      gem(base64) >= 0
Requires:      gem(minitest) >= 5
Requires:      gem(mutex_m) >= 0
Requires:      gem(ostruct) >= 0.6.3
Requires:      gem(racc) >= 0
Requires:      gem(rake) >= 0
Requires:      gem(rake-compiler) >= 0
Requires:      gem(rake-compiler-dock) >= 1.2.1
Requires:      gem(standard) >= 1.54.0
Requires:      gem(tsort) >= 0
Requires:      gem(yard) >= 0
Conflicts:     gem(ostruct) >= 0.7
Conflicts:     gem(rake-compiler-dock) >= 2
Conflicts:     gem(standard) >= 2

%description   -n gem-rb-sys-devel
Helpers for compiling Rust extensions for ruby development package.

%description   -n gem-rb-sys-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета rb_sys.
%endif


%prep
%setup
%autopatch -p1

%build
%ruby_build

%install
%ruby_install

%check
%ruby_test

%files
%doc LICENSE-APACHE LICENSE-MIT readme.md
%ruby_gemspec
%ruby_gemlibdir

%files         -n rb-sys-dock
%doc LICENSE-APACHE LICENSE-MIT readme.md
%_bindir/rb-sys-dock

%if_enabled    doc
%files         -n gem-rb-sys-doc
%doc LICENSE-APACHE LICENSE-MIT readme.md
%ruby_gemdocdir
%endif

%if_enabled    devel
%files         -n gem-rb-sys-devel
%doc LICENSE-APACHE LICENSE-MIT readme.md
%endif


%changelog
* Mon Aug 31 2026 Pavel Skrylev <majioa@altlinux.org> 0.9.128-alt1.1
- ! fixed dep to minitest gem

* Mon Aug 10 2026 Pavel Skrylev <majioa@altlinux.org> 0.9.128-alt1
- ^ 0.9.98 -> 0.9.128

* Wed Jul 24 2024 Pavel Skrylev <majioa@altlinux.org> 0.9.98-alt1
- + packaged gem with Ruby Policy 2.0
