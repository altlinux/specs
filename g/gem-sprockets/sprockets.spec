%define        pkgname sprockets

Name:          gem-%pkgname
Epoch:         1
Version:       4.0.2
Release:       alt1
Summary:       Rack-based asset packaging system
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/rails/sprockets
Vcs:           https://github.com/rails/sprockets.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:  %name-%version.tar
BuildRequires(pre): rpm-build-ruby

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
Obsoletes:     %gemname < %EVR

%description
Sprockets is a Ruby library for compiling and serving web assets. It features
declarative dependency management for JavaScript and CSS assets, as well as
a powerful preprocessor pipeline that allows you to write assets in languages
like CoffeeScript, Sass and SCSS.


%package       -n %pkgname
Summary:       Library files for %gemname gem
Summary(ru_RU.UTF-8): Файлы библиотеки для самоцвета %gemname
Group:         Development/Ruby
BuildArch:     noarch

%description   -n %pkgname
Library files for %gemname gem.

%description   -n %pkgname -l ru_RU.UTF8
Файлы библиотеки для самоцвета %gemname.


%package       -n gem-%pkgname-doc
Summary:       Documentation files for %gemname gem
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета %gemname
Group:         Development/Documentation
BuildArch:     noarch

%description   -n gem-%pkgname-doc
Documentation files for %gemname gem.

%description   -n gem-%pkgname-doc -l ru_RU.UTF8
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

%files         -n %pkgname
%doc README*
%_bindir/%{pkgname}*

%files         -n gem-%pkgname-doc
%ruby_gemdocdir


%changelog
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
