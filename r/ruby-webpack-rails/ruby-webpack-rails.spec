%define  pkgname webpack-rails

Name:    ruby-%pkgname
Version: 0.9.11
Release: alt1

Summary: Integrate webpack with your Ruby on Rails application
License: MIT
Group:   Development/Ruby
Url:     https://github.com/mipearson/webpack-rails

Packager:  Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch: noarch

Source:  %pkgname-%version.tar

BuildRequires(pre): rpm-build-ruby
BuildRequires: ruby-tool-setup

%description
webpack-rails gives you tools to integrate Webpack in to an existing Ruby on Rails
application.

It will happily co-exist with sprockets but does not use it for production fingerprinting
or asset serving. webpack-rails is designed with the assumption that if you're using
Webpack you treat Javascript as a first-class citizen. This means that you control
the webpack config, package.json, and use yarn to install Webpack & its plugins.

In development mode webpack-dev-server is used to serve webpacked entry points and
offer hot module reloading. In production entry points are built in to public/webpack.
webpack-rails uses stats-webpack-plugin to translate entry points in to asset paths.

It was designed for use at Marketplacer to assist us in migrating our Javascript
(and possibly our SCSS) off of Sprockets. It first saw production use in June 2015.

Our examples show webpack-rails co-existing with sprockets (as that's how environment
works), but sprockets is not used or required for development or production use of
this gem.

This gem has been tested against Rails 4.2 and Ruby 2.2. Earlier versions of Rails
(>= 3.2) and Ruby (>= 2.0) may work, but we haven't tested them.

%description -l ru_RU.UTF8
webpack-rails даёт вам возможность интегрировать Webpack в существующее приложение Рельс.


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
* Mon Sep 24 2018 Pavel Skrylev <majioa@altlinux.org> 0.9.11-alt1
- Initial gemified build for Sisyphus
