%define        _unpackaged_files_terminate_build 1
%def_enable    check
%def_enable    doc
%def_enable    devel
%define        gemname rb_sys

Name:          gem-rb-sys
Version:       0.9.98
Release:       alt1
Summary:       Helpers for compiling Rust extensions for ruby
License:       MIT or Apache-2.0
Group:         Other
Url:           https://oxidize-rb.github.io/rb-sys/
Vcs:           https://github.com/oxidize-rb/rb-sys.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_ignore_names gem-rb-sys
Provides:      gem(rb_sys) = 0.9.98

%description
Helpers for compiling Rust extensions for ruby


%package       -n rb-sys-dock
Version:       0.9.98
Release:       alt1
Summary:       Helpers for compiling Rust extensions for ruby executable(s)
Summary(ru_RU.UTF-8): Исполнямка для самоцвета rb_sys
Group:         Other
BuildArch:     noarch

Requires:      gem(rb_sys) = 0.9.98

%description   -n rb-sys-dock
Helpers for compiling Rust extensions for ruby executable(s).

%description   -n rb-sys-dock -l ru_RU.UTF-8
Исполнямка для самоцвета rb_sys.


%if_enabled    doc
%package       -n gem-rb-sys-doc
Version:       0.9.98
Release:       alt1
Summary:       Helpers for compiling Rust extensions for ruby documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета rb_sys
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(rb_sys) = 0.9.98

%description   -n gem-rb-sys-doc
Helpers for compiling Rust extensions for ruby documentation files.

%description   -n gem-rb-sys-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета rb_sys.
%endif


%if_enabled    devel
%package       -n gem-rb-sys-devel
Version:       0.9.98
Release:       alt1
Summary:       Helpers for compiling Rust extensions for ruby development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета rb_sys
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(rb_sys) = 0.9.98

%description   -n gem-rb-sys-devel
Helpers for compiling Rust extensions for ruby development package.

%description   -n gem-rb-sys-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета rb_sys.
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
%doc readme.md
%ruby_gemspec
%ruby_gemlibdir

%files         -n rb-sys-dock
%doc readme.md
%_bindir/rb-sys-dock

%if_enabled    doc
%files         -n gem-rb-sys-doc
%doc readme.md
%ruby_gemsdocdir/rb_sys-0.9.98
%endif

%if_enabled    devel
%files         -n gem-rb-sys-devel
%doc readme.md
%endif


%changelog
* Wed Jul 24 2024 Pavel Skrylev <majioa@altlinux.org> 0.9.98-alt1
- + packaged gem with Ruby Policy 2.0
