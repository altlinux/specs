%define  pkgname gettext_i18n_rails

Name:    ruby-%pkgname
Version: 1.8.0
Release: alt1

Summary: Rails: FastGettext, I18n integration -- simple, threadsafe and fast!
License: MIT
Group:   Development/Ruby
Url:     https://github.com/grosser/gettext_i18n_rails

Packager:  Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch: noarch

Source:  %pkgname-%version.tar

BuildRequires(pre): rpm-build-ruby
BuildRequires: ruby-tool-setup

%description
FastGettext / Rails integration.

Translate via FastGettext, use any other I18n backend as extension/fallback.

Rails does: I18n.t('syntax.with.lots.of.dots') with nested yml files
We do: _('Just translate my damn text!') with simple, flat mo/po/yml files or
directly from db. To use I18n calls add a syntax.with.lots.of.dots translation.

%description -l ru_RU.UTF8
Сопряжение Рельс и FastGettext.

Перевод через FastGettext с использованием любый иных I18n приклёпок в качестве расширений.

В Рельсах делаюется: I18n.t('syntax.with.lots.of.dots'), используя вложенные ямл-файлы.
У нас делается: _('Just translate my damn text!'), используя простые, прямые mo/po/yml файлы
или напрямую из БД. А чтобы использовать вызовы к I18n добавьте перевод строки
вида "syntax.with.lots.of.dots".

%package doc
Summary: Documentation files for %name
Group: Documentation

BuildArch: noarch

%description doc
Documentation files for %{name}.

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
# Remove unnecessary files
rm -f %buildroot%ruby_ri_sitedir/{Object/cdesc-Object.ri,cache.ri,created.rid}

%check
%ruby_test_unit -Ilib:test test

%files
%doc Readme*
%ruby_sitelibdir/*
%rubygem_specdir/*

%files doc
%ruby_ri_sitedir/*

%changelog
* Mon Sep 24 2018 Pavel Skrylev <majioa@altlinux.org> 1.8.0-alt1
- Initial gemified build for Sisyphus
