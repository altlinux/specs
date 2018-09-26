%define pkgname rails-i18n

Name: ruby-%pkgname
Version: 5.1.1
Release: alt1
Summary: Central point to collect locale data for use in Ruby on Rails
License: MIT
Group: Development/Ruby
Url: https://github.com/svenfuchs/rails-i18n

Source: %pkgname-%version.tar

Packager:  Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch: noarch

BuildRequires(pre): rpm-build-ruby

%description
Central point to collect locale data for use in Ruby on Rails.

%description -l ru_RU.UTF8
Основная точка сбора данных локализаций для использования их в Рельсах.

%package doc
Summary: Documentation files for %name
Group: Documentation

%description doc
Documentation files for %name

%description doc -l ru_RU.UTF8
Файлы сведений для %name

%prep
%setup -n %pkgname-%version
%update_setup_rb

%build
%ruby_config
%ruby_build

%install
%ruby_install
%rdoc lib/

%files
%doc README.md
%ruby_sitelibdir/*
%rubygem_specdir/*

%files doc
%ruby_ri_sitedir/*

%changelog
* Mon Sep 24 2018 Pavel Skrylev <majioa@altlinux.org> 5.1.1-alt1
- Initial gemified build for Sisyphus.
