%define  pkgname record_tag_helper

Name:    ruby-%pkgname
Version: 1.0.0
Release: alt1

Summary: ActionView Record Tag Helpers
License: MIT
Group:   Development/Ruby
Url:     https://github.com/rails/record_tag_helper

Packager:  Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch: noarch

Source:  %pkgname-%version.tar

BuildRequires(pre): rpm-build-ruby
BuildRequires: ruby-tool-setup

%description
RecordTagHelper consists of code that was formerly a part of ActionView, but has
been removed from core in Rails 5. This gem is provided to ensure projects that
use functionality from ActionView::Helpers::RecordTagHelper have an appropriate
upgrade path.

This gem provides methods for generating container tags, such as div, for your
record. This is the recommended way of creating a container for your Active Record
object, as it adds appropriate class and id attributes to that container. You can
then refer to those containers easily by following that convention, instead of having
to think about which class or id attribute you should use.

%description -l ru_RU.UTF8
RecordTagHelper состоит из кода, который был частью ActionView, но был удалён из
ядра Рельс 5.0. Этот бисер позволяет увериться в том, что проекты, которые используют
функциональность из ActionView::Helpers::RecordTagHelper, будут иметь подобающий
путь обновления.

Этот бисер предоставляет методы для генерирования меток контейнеров, например, "div",
для вашей записи. Это рекоменндуемый способ создания контейнера для ваших объектов
Активной Записи, так как он добавляет подобающие атрибуты класса и знака (id) в ваш
контейнер. Дабы вы смогли ссылаться на те контейнеры легко следуя соглашению, вместо
того, чтобы думать о том, какие аттрибуты вы должны использовать.

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
#%ruby_test_unit -Ilib:test test

%files
%doc README*
%ruby_sitelibdir/*
%rubygem_specdir/*

%files doc
%ruby_ri_sitedir/*

%changelog
* Mon Sep 24 2018 Pavel Skrylev <majioa@altlinux.org> 1.0.0-alt1
- Initial gemified build for Sisyphus
