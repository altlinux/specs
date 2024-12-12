%define        _unpackaged_files_terminate_build 1
%def_enable    check
%def_enable    doc
%def_enable    devel
%define        gemname onigmo

Name:          gem-onigmo
Version:       1.0.0
Release:       alt1
Summary:       The Onigmo regular expression engine compiled to WASM and wrapped in a Ruby embrace
License:       Unlicense
Group:         Development/Ruby
Url:           http://github.com/camertron/onigmo-ruby
Vcs:           https://github.com/camertron/onigmo-ruby.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
BuildRequires: gem(rake) >= 0
%if_enabled check
BuildRequires: gem(debug) >= 0
BuildRequires: gem(minitest) >= 0
BuildRequires: gem(wasmtime) >= 20.0
BuildConflicts: gem(wasmtime) >= 28
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_use_gem_dependency wasmtime >= 27,wasmtime < 28
Requires:      gem(wasmtime) >= 20.0
Conflicts:     gem(wasmtime) >= 28
Provides:      gem(onigmo) = 1.0.0

%description
The Onigmo regular expression engine compiled to WASM and wrapped in a Ruby
embrace.


%if_enabled    doc
%package       -n gem-onigmo-doc
Version:       1.0.0
Release:       alt1
Summary:       The Onigmo regular expression engine compiled to WASM and wrapped in a Ruby embrace documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета onigmo
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(onigmo) = 1.0.0

%description   -n gem-onigmo-doc
The Onigmo regular expression engine compiled to WASM and wrapped in a Ruby
embrace documentation files.

%description   -n gem-onigmo-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета onigmo.
%endif


%if_enabled    devel
%package       -n gem-onigmo-devel
Version:       1.0.0
Release:       alt1
Summary:       The Onigmo regular expression engine compiled to WASM and wrapped in a Ruby embrace development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета onigmo
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(onigmo) = 1.0.0
Requires:      gem(debug) >= 0
Requires:      gem(minitest) >= 0
Requires:      gem(rake) >= 0

%description   -n gem-onigmo-devel
The Onigmo regular expression engine compiled to WASM and wrapped in a Ruby
embrace development package.

%description   -n gem-onigmo-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета onigmo.
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
%doc CHANGELOG.md LICENSE README.md
%ruby_gemspec
%ruby_gemlibdir

%if_enabled    doc
%files         -n gem-onigmo-doc
%doc CHANGELOG.md LICENSE README.md
%ruby_gemdocdir
%endif

%if_enabled    devel
%files         -n gem-onigmo-devel
%doc CHANGELOG.md LICENSE README.md
%endif


%changelog
* Wed Dec 11 2024 Pavel Skrylev <majioa@altlinux.org> 1.0.0-alt1
- + packaged gem with Ruby Policy 2.0
- * define explicit dependencies
