%define  pkgname activerecord-session_store

Name:    ruby-%pkgname
Version: 1.1.1
Release: alt1

Summary: Active Record's Session Store extracted from Rails
License: MIT
Group:   Development/Ruby
Url:     https://github.com/rails/activerecord-session_store

Packager:  Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch: noarch

Source:  %pkgname-%version.tar

BuildRequires(pre): rpm-build-ruby
BuildRequires: ruby-tool-setup

%description
%summary

%description -l ru_RU.UTF8
Хранилище сессий для Активной Записи извлечённое из Рельс.

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
* Fri Sep 21 2018 Pavel Skrylev <majioa@altlinux.org> 1.1.1-alt1
- Initial gemified build for Sisyphus
