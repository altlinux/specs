%define        _unpackaged_files_terminate_build 1
%def_enable    check
%def_enable    doc
%def_enable    devel
%define        gemname duktape

Name:          gem-duktape
Version:       2.7.0.0
Release:       alt1
Summary:       Bindings to the Duktape JavaScript interpreter
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/judofyr/duktape.rb
Vcs:           https://github.com/judofyr/duktape.rb.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
%if_enabled check
BuildRequires: gem(rake) >= 0
BuildRequires: gem(rake-compiler) >= 0
BuildRequires: gem(sdoc) >= 0
BuildRequires: gem(minitest) >= 5.2
BuildConflicts: gem(minitest) >= 6
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
Provides:      gem(duktape) = 2.7.0.0


%description
Bindings to the Duktape JavaScript interpreter


%if_enabled    doc
%package       -n gem-duktape-doc
Version:       2.7.0.0
Release:       alt1
Summary:       Bindings to the Duktape JavaScript interpreter documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета duktape
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(duktape) = 2.7.0.0

%description   -n gem-duktape-doc
Bindings to the Duktape JavaScript interpreter documentation files.

%description   -n gem-duktape-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета duktape.
%endif


%if_enabled    devel
%package       -n gem-duktape-devel
Version:       2.7.0.0
Release:       alt1
Summary:       Bindings to the Duktape JavaScript interpreter development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета duktape
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(duktape) = 2.7.0.0
Requires:      gem(rake) >= 0
Requires:      gem(rake-compiler) >= 0
Requires:      gem(sdoc) >= 0
Requires:      gem(minitest) >= 5.2
Conflicts:     gem(minitest) >= 6

%description   -n gem-duktape-devel
Bindings to the Duktape JavaScript interpreter development package.

%description   -n gem-duktape-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета duktape.
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

%if_enabled    doc
%files         -n gem-duktape-doc
%doc README.md
%ruby_gemdocdir
%endif

%if_enabled    devel
%files         -n gem-duktape-devel
%doc README.md
%ruby_includedir/*
%endif


%changelog
* Wed Jul 24 2024 Pavel Skrylev <majioa@altlinux.org> 2.7.0.0-alt1
- ^ 2.3.0.0 -> 2.7.0.0

* Mon Jan 30 2023 Pavel Skrylev <majioa@altlinux.org> 2.3.0.0-alt1
- + packaged gem with Ruby Policy 2.0
