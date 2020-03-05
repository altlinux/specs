%define        pkgname ancestry

Name:          gem-%pkgname
Version:       3.0.7
Release:       alt1.1
Summary:       Organise ActiveRecord model into a tree structure
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/stefankroes/ancestry
Vcs:           https://github.com/stefankroes/ancestry.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby

%add_findreq_skiplist %ruby_gemslibdir/**/*
Obsoletes:     ruby-%pkgname
Provides:      ruby-%pkgname

%description
%summary

%description -l ru_RU.UTF8
Упорядочивание модели ActiveRecord в виде древовидной структуры

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
* Thu Mar 05 2020 Pavel Skrylev <majioa@altlinux.org> 3.0.7-alt1.1
- fixed (!) spec

* Mon Sep 16 2019 Pavel Skrylev <majioa@altlinux.org> 3.0.7-alt1
- updated (^) 3.0.5 -> v3.0.7

* Wed Apr 03 2019 Pavel Skrylev <majioa@altlinux.org> 3.0.5-alt1
- updated (^) 3.0.3 -> 3.0.5
- used (>) Ruby Policy 2.0

* Mon Oct 29 2018 Pavel Skrylev <majioa@altlinux.org> 3.0.3-alt1
- updated (^) 3.0.2 -> 3.0.3

* Fri Sep 21 2018 Pavel Skrylev <majioa@altlinux.org> 3.0.2-alt2
- fixed (!) gemify the package.

* Tue May 29 2018 Andrey Cherepanov <cas@altlinux.org> 3.0.2-alt1
- adeed (+) initial build for Sisyphus
