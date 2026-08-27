%define        _unpackaged_files_terminate_build 1
%def_enable    check
%def_enable    doc
%def_enable    devel
%define        gemname coffee-script

Name:          gem-coffee-script
Version:       2.4.1.1
Release:       alt2
Summary:       Ruby CoffeeScript Compiler
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/rails/ruby-coffee-script
Vcs:           https://github.com/rails/ruby-coffee-script.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-macros-ruby setup-rb rake
%if_enabled check
BuildRequires: gem(coffee-script-source) >= 0
BuildRequires: gem(execjs) >= 0
BuildRequires: gem(json) >= 0
BuildRequires: gem(minitest) >= 0
BuildRequires: gem(rake) >= 0
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
Requires:      gem(coffee-script-source) >= 0
Requires:      gem(execjs) >= 0
Obsoletes:     ruby-coffee-script < %EVR
Provides:      ruby-coffee-script = %EVR
Provides:      gem(coffee-script) = 2.4.1.1

%ruby_use_gem_version coffee-script:2.4.1.1

%description
Ruby CoffeeScript Compiler.


%if_enabled    doc
%package       -n gem-coffee-script-doc
Version:       2.4.1.1
Release:       alt2
Summary:       Ruby CoffeeScript Compiler documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета coffee-script
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(coffee-script) = 2.4.1.1

%description   -n gem-coffee-script-doc
Ruby CoffeeScript Compiler documentation files.

%description   -n gem-coffee-script-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета coffee-script.
%endif


%if_enabled    devel
%package       -n gem-coffee-script-devel
Version:       2.4.1.1
Release:       alt2
Summary:       Ruby CoffeeScript Compiler development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета coffee-script
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(coffee-script) = 2.4.1.1
Requires:      gem(json) >= 0
Requires:      gem(minitest) >= 0
Requires:      gem(rake) >= 0

%description   -n gem-coffee-script-devel
Ruby CoffeeScript Compiler development package.

%description   -n gem-coffee-script-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета coffee-script.
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
%files         -n gem-coffee-script-doc
%doc LICENSE README.md
%ruby_gemdocdir
%endif

%if_enabled    devel
%files         -n gem-coffee-script-devel
%doc LICENSE README.md
%endif


%changelog
* Wed Aug 19 2026 Pavel Skrylev <majioa@altlinux.org> 2.4.1.1-alt2
- * rebased to upstream
- ! fixed dep to minitest gem

* Thu Sep 02 2021 Pavel Skrylev <majioa@altlinux.org> 2.4.1.1-alt1
- ^ 2.4.1 -> 2.4.1p1

* Wed Jul 10 2019 Pavel Skrylev <majioa@altlinux.org> 2.4.1-alt3
^ Ruby Policy 2.0
- coffee-script-source gem

* Wed Sep 05 2018 Pavel Skrylev <majioa@altlinux.org> 2.4.1-alt2
- Split into two gems coffee-script-transpiler and coffee-script-source.

* Tue Jul 24 2018 Andrey Cherepanov <cas@altlinux.org> 2.4.1-alt1.1
- Rebuild with new Ruby autorequirements.
- Disable tests.

* Tue Jun 05 2018 Andrey Cherepanov <cas@altlinux.org> 2.4.1-alt1
- Initial build for Sisyphus
