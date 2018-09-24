%define  pkgname responders

Name:    ruby-%pkgname
Version: 2.4.0
Release: alt1

Summary: A set of Rails responders to dry up your application
License: MIT
Group:   Development/Ruby
Url:     https://github.com/plataformatec/responders

Packager:  Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch: noarch

Source:  %pkgname-%version.tar

BuildRequires(pre): rpm-build-ruby
BuildRequires: ruby-tool-setup

%description
A set of responders modules to dry up your Rails 4.2+ app.

%description -l ru_RU.UTF8
Наборы модулей отвечиков для очистки коджа вашего приложения для Рельс 4.2+.

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
* Mon Sep 24 2018 Pavel Skrylev <majioa@altlinux.org> 2.4.0-alt1
- Initial gemified build for Sisyphus
