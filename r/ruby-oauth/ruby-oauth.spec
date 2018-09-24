%define pkgname oauth

Name: ruby-%pkgname
Version: 0.5.4
Release: alt1
Summary: OAuth Core Ruby implementation
License: Distributed
Group: Development/Ruby

Source: %pkgname-%version.tar

Packager:  Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch: noarch

BuildRequires(pre): rpm-build-ruby
Provides: /usr/bin/oauth

%description
%summary

%description -l ru_RU.UTF8
Ядро OAuth для Рубина.

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
%_bindir/*
%doc README* LICENSE
%ruby_sitelibdir/*
%rubygem_specdir/*

%files doc
%ruby_ri_sitedir/*

%changelog
* Mon Sep 24 2018 Pavel Skrylev <majioa@altlinux.org> 0.5.4-alt1
- Initial gemified build for Sisyphus.
