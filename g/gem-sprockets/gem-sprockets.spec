%define        _unpackaged_files_terminate_build 1
%define        gemname sprockets

Name:          gem-sprockets
Epoch:         1
Version:       4.2.0
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
%if_with check
BuildRequires: gem(m) >= 0
BuildRequires: gem(babel-transpiler) >= 0.6
BuildRequires: gem(closure-compiler) >= 1.1
BuildRequires: gem(coffee-script-source) >= 1.6
BuildRequires: gem(coffee-script) >= 2.2
BuildRequires: gem(eco) >= 1.0
BuildRequires: gem(ejs) >= 1.0
BuildRequires: gem(execjs) >= 2.0
BuildRequires: gem(jsminc) >= 1.1
BuildRequires: gem(timecop) >= 0.9.1
BuildRequires: gem(minitest) >= 5.0
BuildRequires: gem(nokogiri) >= 1.3
BuildRequires: gem(rack-test) >= 1.1.0
BuildRequires: gem(rake) >= 12.0
BuildRequires: gem(sass) >= 3.4
BuildRequires: gem(sassc) >= 2.0
BuildRequires: gem(uglifier) >= 2.3
BuildRequires: gem(yui-compressor) >= 0.12
BuildRequires: gem(zopfli) >= 0.0.4
BuildRequires: gem(rubocop-performance) >= 1.3
BuildRequires: gem(rack) >= 2.2.2
BuildRequires: gem(concurrent-ruby) >= 1.0
BuildConflicts: gem(babel-transpiler) >= 1
BuildConflicts: gem(closure-compiler) >= 2
BuildConflicts: gem(coffee-script-source) >= 2
BuildConflicts: gem(coffee-script) >= 3
BuildConflicts: gem(eco) >= 2
BuildConflicts: gem(ejs) >= 2
BuildConflicts: gem(execjs) >= 3
BuildConflicts: gem(jsminc) >= 2
BuildConflicts: gem(timecop) >= 0.10
BuildConflicts: gem(minitest) >= 6
BuildConflicts: gem(nokogiri) >= 2
BuildConflicts: gem(rack-test) >= 2.1
BuildConflicts: gem(rake) >= 14
BuildConflicts: gem(sass) >= 4
BuildConflicts: gem(sassc) >= 3
BuildConflicts: gem(yui-compressor) >= 1
BuildConflicts: gem(zopfli) >= 0.1
BuildConflicts: gem(rubocop-performance) >= 2
BuildConflicts: gem(rack) >= 4
BuildConflicts: gem(concurrent-ruby) >= 2
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_use_gem_dependency rack >= 2.2.2,rack < 3
%ruby_use_gem_dependency rake >= 13.0.1,rake < 14
%ruby_use_gem_dependency rack-test >= 1.1.0,rack-test < 2
Requires:      gem(rack) >= 2.2.2
Requires:      gem(concurrent-ruby) >= 1.0
Conflicts:     gem(rack) >= 4
Conflicts:     gem(concurrent-ruby) >= 2
Obsoletes:     sprockets < %EVR
Provides:      gem(sprockets) = 4.2.0


%description
Sprockets is a Ruby library for compiling and serving web assets. It features
declarative dependency management for JavaScript and CSS assets, as well as a
powerful preprocessor pipeline that allows you to write assets in languages like
CoffeeScript, Sass and SCSS.


%package       -n sprockets
Version:       4.2.0
Release:       alt1
Summary:       Rack-based asset packaging system executable(s)
Summary(ru_RU.UTF-8): Исполнямка для самоцвета sprockets
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(sprockets) = 4.2.0

%description   -n sprockets
Rack-based asset packaging system executable(s).

Sprockets is a Ruby library for compiling and serving web assets. It features
declarative dependency management for JavaScript and CSS assets, as well as a
powerful preprocessor pipeline that allows you to write assets in languages like
CoffeeScript, Sass and SCSS.

%description   -n sprockets -l ru_RU.UTF-8
Исполнямка для самоцвета sprockets.


%package       -n gem-sprockets-doc
Version:       4.2.0
Release:       alt1
Summary:       Rack-based asset packaging system documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета sprockets
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(sprockets) = 4.2.0

%description   -n gem-sprockets-doc
Rack-based asset packaging system documentation files.

Sprockets is a Ruby library for compiling and serving web assets. It features
declarative dependency management for JavaScript and CSS assets, as well as a
powerful preprocessor pipeline that allows you to write assets in languages like
CoffeeScript, Sass and SCSS.

%description   -n gem-sprockets-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета sprockets.


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

%files         -n sprockets
%doc README.md
%_bindir/sprockets

%files         -n gem-sprockets-doc
%doc README.md
%ruby_gemdocdir


%changelog
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
