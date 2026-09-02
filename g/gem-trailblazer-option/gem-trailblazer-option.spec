%define        _unpackaged_files_terminate_build 1
%def_enable    check
%def_enable    doc
%def_enable    devel
%define        gemname trailblazer-option

Name:          gem-trailblazer-option
Version:       0.1.2
Release:       alt1
Summary:       Callable patterns for options in Trailblazer
License:       MIT
Group:         Development/Ruby
Url:           https://trailblazer.to/
Vcs:           https://github.com/trailblazer/trailblazer-option.git
Packager:      Pavel Skrylev <majioa@altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-macros-ruby setup-rb rake
%if_enabled check
BuildRequires: gem(minitest) >= 5.0
BuildRequires: gem(minitest-line) >= 0.6.5
BuildRequires: gem(rake) >= 13.0
BuildConflicts: gem(minitest) >= 7
BuildConflicts: gem(minitest-line) >= 0.7
BuildConflicts: gem(rake) >= 14
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_use_gem_dependency minitest >= 6.0,minitest < 7
Requires:      ruby >= 2.1.0
Requires:      gem(minitest) >= 5.0
Requires:      gem(minitest-line) >= 0.6.5
Requires:      gem(rake) >= 13.0
Conflicts:     gem(minitest) >= 7
Conflicts:     gem(minitest-line) >= 0.7
Conflicts:     gem(rake) >= 14
Provides:      gem(trailblazer-option) = 0.1.2

%description
Wrap an option at compile-time and `call` it at runtime, which allows to have
the common `-> ()`, `:method` or `Callable` pattern used for most options.


%if_enabled    doc
%package       -n gem-trailblazer-option-doc
Version:       0.1.2
Release:       alt1
Summary:       Callable patterns for options in Trailblazer documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета trailblazer-option
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(trailblazer-option) = 0.1.2

%description   -n gem-trailblazer-option-doc
Callable patterns for options in Trailblazer documentation files.

Wrap an option at compile-time and `call` it at runtime, which allows to have
the common `-> ()`, `:method` or `Callable` pattern used for most options.

%description   -n gem-trailblazer-option-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета trailblazer-option.
%endif


%if_enabled    devel
%package       -n gem-trailblazer-option-devel
Version:       0.1.2
Release:       alt1
Summary:       Callable patterns for options in Trailblazer development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета trailblazer-option
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(trailblazer-option) = 0.1.2

%description   -n gem-trailblazer-option-devel
Callable patterns for options in Trailblazer development package.

Wrap an option at compile-time and `call` it at runtime, which allows to have
the common `-> ()`, `:method` or `Callable` pattern used for most options.

%description   -n gem-trailblazer-option-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета trailblazer-option.
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
%doc LICENSE README.md
%ruby_gemspec
%ruby_gemlibdir

%if_enabled    doc
%files         -n gem-trailblazer-option-doc
%doc LICENSE README.md
%ruby_gemdocdir
%endif

%if_enabled    devel
%files         -n gem-trailblazer-option-devel
%doc LICENSE README.md
%endif


%changelog
* Mon Aug 31 2026 Pavel Skrylev <majioa@altlinux.org> 0.1.2-alt1
- ^ 0.1.1 -> 0.1.2

* Wed Jun 02 2021 Pavel Skrylev <majioa@altlinux.org> 0.1.1-alt1
- + packaged gem with Ruby Policy 2.0
