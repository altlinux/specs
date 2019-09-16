%define        pkgname ancestry

Name:          ruby-%pkgname
Version:       3.0.7
Release:       alt1
Summary:       Organise ActiveRecord model into a tree structure
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/stefankroes/ancestry
# VCS:         https://github.com/stefankroes/ancestry.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby

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
* Mon Sep 16 2019 Pavel Skrylev <majioa@altlinux.org> 3.0.7-alt1
- ^ v3.0.7

* Wed Apr 03 2019 Pavel Skrylev <majioa@altlinux.org> 3.0.5-alt1
- ^ v3.0.5
- ^ Ruby Policy 2.0

* Mon Oct 29 2018 Pavel Skrylev <majioa@altlinux.org> 3.0.3-alt1
- ^ v3.0.3

* Fri Sep 21 2018 Pavel Skrylev <majioa@altlinux.org> 3.0.2-alt2
- ! gemify the package.

* Tue May 29 2018 Andrey Cherepanov <cas@altlinux.org> 3.0.2-alt1
- + initial build for Sisyphus
