%define        gemname uglifier

Name:          gem-uglifier
Version:       4.2.0.11
Release:       alt0.1
Summary:       Ruby wrapper for UglifyJS JavaScript compressor
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/lautis/uglifier
Vcs:           https://github.com/lautis/uglifier.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
%if_with check
BuildRequires: gem(rspec) >= 3.0
BuildRequires: gem(rake) >= 12.0
BuildRequires: gem(bundler) >= 1.3
BuildRequires: gem(sourcemap) >= 0.1.1
BuildRequires: gem(rubocop) >= 1.7.0
BuildRequires: gem(execjs) >= 0.3.0
BuildConflicts: gem(rspec) >= 4
BuildConflicts: gem(rake) >= 14
BuildConflicts: gem(sourcemap) >= 0.2
BuildConflicts: gem(rubocop) >= 2
BuildConflicts: gem(execjs) >= 3
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_use_gem_dependency rake >= 13.0.1,rake < 14
%ruby_use_gem_dependency rubocop >= 1.15.0,rubocop < 2
Requires:      gem(execjs) >= 0.3.0
Conflicts:     gem(execjs) >= 3
Obsoletes:     ruby-uglifier < %EVR
Provides:      ruby-uglifier = %EVR
Provides:      gem(uglifier) = 4.2.0.11

%ruby_use_gem_version uglifier:4.2.0.11

%description
Ruby wrapper for UglifyJS JavaScript compressor.

UglifyJS currently is extensively tested with ES5, but also includes
experimental ES6/ES2015+/Harmony support.

More stable alternatives for working with ES6 code is to first transpile to ES5
with e.g. babel-transpiler or using Closure Compiler to directly minify ES6
code.


%package       -n gem-uglifier-doc
Version:       4.2.0.11
Release:       alt0.1
Summary:       Ruby wrapper for UglifyJS JavaScript compressor documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета uglifier
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(uglifier) = 4.2.0.11

%description   -n gem-uglifier-doc
Ruby wrapper for UglifyJS JavaScript compressor documentation files.

%description   -n gem-uglifier-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета uglifier.


%package       -n gem-uglifier-devel
Version:       4.2.0.11
Release:       alt0.1
Summary:       Ruby wrapper for UglifyJS JavaScript compressor development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета uglifier
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(uglifier) = 4.2.0.11
Requires:      gem(rspec) >= 3.0
Requires:      gem(rake) >= 12.0
Requires:      gem(bundler) >= 1.3
Requires:      gem(sourcemap) >= 0.1.1
Requires:      gem(rubocop) >= 1.7.0
Conflicts:     gem(rspec) >= 4
Conflicts:     gem(rake) >= 14
Conflicts:     gem(sourcemap) >= 0.2
Conflicts:     gem(rubocop) >= 2

%description   -n gem-uglifier-devel
Ruby wrapper for UglifyJS JavaScript compressor development package.

%description   -n gem-uglifier-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета uglifier.


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

%files         -n gem-uglifier-doc
%doc README.md
%ruby_gemdocdir

%files         -n gem-uglifier-devel
%doc README.md


%changelog
* Sat Feb 04 2023 Pavel Skrylev <majioa@altlinux.org> 4.2.0.11-alt0.1
- ^ 4.2.0 -> 4.2.0p11

* Tue Dec 15 2020 Pavel Skrylev <majioa@altlinux.org> 4.2.0-alt1
- ^ 4.1.20 -> 4.2.0
- * policied name

* Thu Jun 06 2019 Pavel Skrylev <majioa@altlinux.org> 4.1.20-alt1
- ^ 4.1.19 -> 4.1.20
- > Ruby Police 2.0

* Mon Sep 17 2018 Andrey Cherepanov <cas@altlinux.org> 4.1.19-alt1
- New version.

* Fri Jul 06 2018 Andrey Cherepanov <cas@altlinux.org> 4.1.14-alt2
- Rebuild ro correct gemspec name.

* Wed Jul 04 2018 Andrey Cherepanov <cas@altlinux.org> 4.1.14-alt1
- New version.
- Package as gem.

* Thu Jun 21 2018 Andrey Cherepanov <cas@altlinux.org> 4.1.12-alt1
- New version.

* Mon Jun 04 2018 Andrey Cherepanov <cas@altlinux.org> 4.1.11-alt1
- Initial build for Sisyphus
