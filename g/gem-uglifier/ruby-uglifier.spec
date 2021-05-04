%define        pkgname uglifier

Name:          gem-%pkgname
Version:       4.2.0
Release:       alt1
Summary:       Ruby wrapper for UglifyJS JavaScript compressor
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/lautis/uglifier
Vcs:           https://github.com/lautis/uglifier.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
Obsoletes:     ruby-%gemname < %EVR
Provides:      ruby-%gemname = %EVR

%description
%summary.

UglifyJS currently is extensively tested with ES5, but also includes
experimental ES6/ES2015+/Harmony support.

More stable alternatives for working with ES6 code is to first transpile to ES5
with e.g. babel-transpiler or using Closure Compiler to directly minify ES6
code.


%package       doc
Summary:       Documentation files for %gemname gem
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета %gemname
Group:         Development/Documentation
BuildArch:     noarch

%description   doc
Documentation files for %gemname gem.

%description   doc -l ru_RU.UTF8
Файлы сведений для самоцвета %gemname.


%prep
%setup

%build
%ruby_build

%install
%ruby_install

%check
%ruby_test

%files
%doc README*
%ruby_gemspec
%ruby_gemlibdir

%files         doc
%ruby_gemdocdir


%changelog
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
