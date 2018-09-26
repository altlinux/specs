%define  pkgname validates_lengths_from_database

Name:    ruby-%pkgname
Version: 0.7.0
Release: alt1

Summary: Introspects your database string field maximum lengths and automatically defines length validations.
License: MIT
Group:   Development/Ruby
Url:     https://github.com/rubiety/validates_lengths_from_database

Packager:  Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch: noarch

Source:  %pkgname-%version.tar

BuildRequires(pre): rpm-build-ruby
BuildRequires: ruby-tool-setup

%description
Few people add length validations to fields in their database, and when saving
such fields that have exhausted their length, an SQL error occurs. This gem
introspects your table schema for maximum lengths on string and text fields and
automatically adds length validations to the model.

%description -l ru_RU.UTF8
Некоторые люди добавляют проверки длины для полей в своих базах данных, но затем
сохранение в такие поля данных, длина которых превышает ограничение, вызывает ошибки
SQL. Сей бисер наблюдает за схемой таблицы в части превышения длины строк и текста таких полей,
и автоматически добавляет проверки длины для таких полей в модель.

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
%doc README*
%ruby_sitelibdir/*
%rubygem_specdir/*

%files doc
%ruby_ri_sitedir/*

%changelog
* Mon Sep 24 2018 Pavel Skrylev <majioa@altlinux.org> 0.7.0-alt1
- Initial gemified build for Sisyphus
