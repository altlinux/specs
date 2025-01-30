%define        _unpackaged_files_terminate_build 1
%def_disable   check
%def_enable    doc
%def_disable   devel
%define        gemname sprockets

Name:          gem-sprockets
Epoch:         1
Version:       4.2.1
Release:       alt1
Summary:       Rack-based asset packaging system
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/rails/sprockets
Vcs:           https://github.com/rails/sprockets.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
%if_enabled check
BuildRequires: gem(babel-transpiler) >= 0.6
BuildRequires: gem(closure-compiler) >= 1.1
BuildRequires: gem(coffee-script) >= 2.2
BuildRequires: gem(coffee-script-source) >= 1.6
BuildRequires: gem(concurrent-ruby) >= 1.0
BuildRequires: gem(eco) >= 1.0
BuildRequires: gem(ejs) >= 1.0
BuildRequires: gem(execjs) >= 2.0
BuildRequires: gem(jsminc) >= 1.1
BuildRequires: gem(m) >= 0
BuildRequires: gem(minitest) >= 5.0
BuildRequires: gem(nokogiri) >= 1.3
BuildRequires: gem(rack) >= 2.2.4
BuildRequires: gem(rack-test) >= 1.1.0
BuildRequires: gem(rake) >= 13.1.0
BuildRequires: gem(rubocop-performance) >= 1.3
BuildRequires: gem(sass) >= 3.4
BuildRequires: gem(sassc) >= 2.0
BuildRequires: gem(timecop) >= 0.9.1
BuildRequires: gem(uglifier) >= 2.3
BuildRequires: gem(yui-compressor) >= 0.12
BuildRequires: gem(zopfli) >= 0.0.4
BuildConflicts: gem(babel-transpiler) >= 1
BuildConflicts: gem(closure-compiler) >= 2
BuildConflicts: gem(coffee-script) >= 3
BuildConflicts: gem(coffee-script-source) >= 2
BuildConflicts: gem(concurrent-ruby) >= 2
BuildConflicts: gem(eco) >= 2
BuildConflicts: gem(ejs) >= 2
BuildConflicts: gem(execjs) >= 3
BuildConflicts: gem(jsminc) >= 2
BuildConflicts: gem(minitest) >= 6
BuildConflicts: gem(nokogiri) >= 2
BuildConflicts: gem(rack) >= 4
BuildConflicts: gem(rack-test) >= 2.1
BuildConflicts: gem(rake) >= 14
BuildConflicts: gem(rubocop-performance) >= 2
BuildConflicts: gem(sass) >= 4
BuildConflicts: gem(sassc) >= 3
BuildConflicts: gem(timecop) >= 0.10
BuildConflicts: gem(yui-compressor) >= 1
BuildConflicts: gem(zopfli) >= 0.1
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_use_gem_dependency rake >= 13.1.0,rake < 14
%ruby_use_gem_dependency rack-test >= 1.1.0,rack-test < 2
Requires:      ruby >= 2.5.0
Requires:      gem(concurrent-ruby) >= 1.0
Requires:      gem(rack) >= 2.2.4
Conflicts:     gem(concurrent-ruby) >= 2
Conflicts:     gem(rack) >= 4
Obsoletes:     sprockets < %EVR
Provides:      gem(sprockets) = 4.2.1

%description
Sprockets is a Ruby library for compiling and serving web assets. It features
declarative dependency management for JavaScript and CSS assets, as well as a
powerful preprocessor pipeline that allows you to write assets in languages like
CoffeeScript, Sass and SCSS.


%package       -n sprockets
Version:       4.2.1
Release:       alt1
Summary:       Rack-based asset packaging system executable(s)
Summary(ru_RU.UTF-8): Исполнямка для самоцвета sprockets
Group:         Other
BuildArch:     noarch

Requires:      gem(sprockets) = 4.2.1

%description   -n sprockets
Rack-based asset packaging system executable(s).

Sprockets is a Ruby library for compiling and serving web assets. It features
declarative dependency management for JavaScript and CSS assets, as well as a
powerful preprocessor pipeline that allows you to write assets in languages like
CoffeeScript, Sass and SCSS.

%description   -n sprockets -l ru_RU.UTF-8
Исполнямка для самоцвета sprockets.


%if_enabled    doc
%package       -n gem-sprockets-doc
Version:       4.2.1
Release:       alt1
Summary:       Rack-based asset packaging system documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета sprockets
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(sprockets) = 4.2.1

%description   -n gem-sprockets-doc
Rack-based asset packaging system documentation files.

Sprockets is a Ruby library for compiling and serving web assets. It features
declarative dependency management for JavaScript and CSS assets, as well as a
powerful preprocessor pipeline that allows you to write assets in languages like
CoffeeScript, Sass and SCSS.

%description   -n gem-sprockets-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета sprockets.
%endif


%if_enabled    devel
%package       -n gem-sprockets-devel
Version:       4.2.1
Release:       alt1
Summary:       Rack-based asset packaging system development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета sprockets
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(sprockets) = 4.2.1
Requires:      gem(babel-transpiler) >= 0.6
Requires:      gem(closure-compiler) >= 1.1
Requires:      gem(coffee-script) >= 2.2
Requires:      gem(coffee-script-source) >= 1.6
Requires:      gem(eco) >= 1.0
Requires:      gem(ejs) >= 1.0
Requires:      gem(execjs) >= 2.0
Requires:      gem(jsminc) >= 1.1
Requires:      gem(m) >= 0
Requires:      gem(minitest) >= 5.0
Requires:      gem(nokogiri) >= 1.3
Requires:      gem(rack-test) >= 1.1.0
Requires:      gem(rake) >= 13.1.0
Requires:      gem(rubocop-performance) >= 1.3
Requires:      gem(sass) >= 3.4
Requires:      gem(sassc) >= 2.0
Requires:      gem(timecop) >= 0.9.1
Requires:      gem(uglifier) >= 2.3
Requires:      gem(yui-compressor) >= 0.12
Requires:      gem(zopfli) >= 0.0.4
Conflicts:     gem(babel-transpiler) >= 1
Conflicts:     gem(closure-compiler) >= 2
Conflicts:     gem(coffee-script) >= 3
Conflicts:     gem(coffee-script-source) >= 2
Conflicts:     gem(eco) >= 2
Conflicts:     gem(ejs) >= 2
Conflicts:     gem(execjs) >= 3
Conflicts:     gem(jsminc) >= 2
Conflicts:     gem(minitest) >= 6
Conflicts:     gem(nokogiri) >= 2
Conflicts:     gem(rack-test) >= 2.1
Conflicts:     gem(rake) >= 14
Conflicts:     gem(rubocop-performance) >= 2
Conflicts:     gem(sass) >= 4
Conflicts:     gem(sassc) >= 3
Conflicts:     gem(timecop) >= 0.10
Conflicts:     gem(yui-compressor) >= 1
Conflicts:     gem(zopfli) >= 0.1

%description   -n gem-sprockets-devel
Rack-based asset packaging system development package.

Sprockets is a Ruby library for compiling and serving web assets. It features
declarative dependency management for JavaScript and CSS assets, as well as a
powerful preprocessor pipeline that allows you to write assets in languages like
CoffeeScript, Sass and SCSS.

%description   -n gem-sprockets-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета sprockets.
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
%doc CHANGELOG.md MIT-LICENSE README.md CODE_OF_CONDUCT.md CONTRIBUTING.md
%ruby_gemspec
%ruby_gemlibdir

%files         -n sprockets
%doc CHANGELOG.md MIT-LICENSE README.md CODE_OF_CONDUCT.md CONTRIBUTING.md
%_bindir/sprockets

%if_enabled    doc
%files         -n gem-sprockets-doc
%doc CHANGELOG.md MIT-LICENSE README.md CODE_OF_CONDUCT.md CONTRIBUTING.md
%ruby_gemdocdir
%endif

%if_enabled    devel
%files         -n gem-sprockets-devel
%doc CHANGELOG.md MIT-LICENSE README.md CODE_OF_CONDUCT.md CONTRIBUTING.md
%endif


%changelog
* Fri Jan 10 2025 Pavel Skrylev <majioa@altlinux.org> 1:4.2.1-alt1
- ^ 4.2.0 -> 4.2.1

* Tue Apr 23 2024 Pavel Skrylev <majioa@altlinux.org> 1:4.2.0-alt1.1
- ! fixed dep to rack

* Fri Mar 10 2023 Pavel Skrylev <majioa@altlinux.org> 1:4.2.0-alt1
- ^ 4.0.2.1 -> 4.2.0 (no devel)

* Tue Dec 08 2020 Pavel Skrylev <majioa@altlinux.org> 1:4.0.2.1-alt1
- ^ 4.0.2 -> 4.0.2[1]
- + finding all asset by a regexp filemask

* Tue Dec 08 2020 Pavel Skrylev <majioa@altlinux.org> 1:4.0.2-alt1
- ^ 4.0.0 -> 4.0.2

* Wed Mar 04 2020 Pavel Skrylev <majioa@altlinux.org> 1:4.0.0-alt1
- updated (^) 3.7.2 -> 4.0.0
- fixed (-) spec

* Tue Sep 10 2019 Pavel Skrylev <majioa@altlinux.org> 1:3.7.2-alt2
- used (>) Ruby Policy 2.0

* Thu Aug 30 2018 Andrey Cherepanov <cas@altlinux.org> 1:3.7.2-alt1
- Build stable version.

* Wed Jul 11 2018 Andrey Cherepanov <cas@altlinux.org> 4.0.0-alt0.1.beta7.1
- Rebuild with new Ruby autorequirements.
- Disable tests.

* Thu May 31 2018 Andrey Cherepanov <cas@altlinux.org> 4.0.0-alt0.1.beta7
- Initial build for Sisyphus
