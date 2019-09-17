%define        pkgname rails-i18n

Name:          ruby-%pkgname
Version:       5.1.3
Release:       alt1
Summary:       Central point to collect locale data for use in Ruby on Rails
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/svenfuchs/rails-i18n
%vcs           https://github.com/svenfuchs/rails-i18n.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
%add_findreq_skiplist %ruby_gemslibdir/**/*

%description
Central point to collect locale data for use in Ruby on Rails.

%description -l ru_RU.UTF8
Основная точка сбора данных локализаций для использования их в Рельсах.


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
* Mon Sep 16 2019 Pavel Skrylev <majioa@altlinux.org> 5.1.3-alt1
- ^ v5.1.3
- ^ Ruby Policy 2.0

* Mon Sep 24 2018 Pavel Skrylev <majioa@altlinux.org> 5.1.1-alt1
- + initial gemified build for Sisyphus.
