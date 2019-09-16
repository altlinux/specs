%define        pkgname activerecord-session-store
%define        gemname activerecord-session_store

Name:          ruby-%gemname
Version:       1.1.3
Release:       alt1
Summary:       Active Record's Session Store extracted from Rails
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/rails/activerecord-session_store
%vcs           https://github.com/rails/activerecord-session_store.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby

%description
A session store backed by an Active Record class. A default class is provided,
but any object duck-typing to an Active Record Session class with text
session_id and data attributes is sufficient.


%description -l ru_RU.UTF8
Хранилище сессий для Активной Записи извлечённое из Рельс.


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
* Mon Sep 16 2019 Pavel Skrylev <majioa@altlinux.org> 1.1.3-alt1
- ^ v1.1.3
- ^ Ruby Policy 2.0

* Fri Sep 21 2018 Pavel Skrylev <majioa@altlinux.org> 1.1.1-alt1
- Initial gemified build for Sisyphus
