%define  pkgname will_paginate

Name:    ruby-%pkgname
Version: 3.1.6
Release: alt1

Summary: Pagination library for Rails, Sinatra, Merb, DataMapper, and more
License: MIT
Group:   Development/Ruby
Url:     https://github.com/mislav/will_paginate

Packager:  Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch: noarch

Source:  %pkgname-%version.tar

BuildRequires(pre): rpm-build-ruby
BuildRequires: ruby-tool-setup

%description
will_paginate is a pagination library that integrates with Ruby on Rails, Sinatra,
Merb, DataMapper and Sequel.

%description -l ru_RU.UTF8
will_paginate есть библиотека остраничивания, которая может быть состроена с Рельсами, Синатрою,
Мербом, Датамапером и Секвелом.

%package doc
Summary: Documentation files for %name
Group: Documentation

BuildArch: noarch

%description doc
Documentation files for %{name}.

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
* Mon Sep 24 2018 Pavel Skrylev <majioa@altlinux.org> 3.1.6-alt1
- Initial gemified build for Sisyphus
