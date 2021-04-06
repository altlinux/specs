%define _unpackaged_files_terminate_build 1

Name:    gem-jekyll
Version: 4.2.0
Release: alt1

Summary: Jekyll is a simple, blog-aware, static site generator.
License: MIT
Group:   Development/Ruby
Url:     https://github.com/jekyll/jekyll.git

Packager:  Dmitriy Voropaev <voropaevdmtr@altlinux.org>
BuildArch: noarch

Source:  %name-%version.tar
Patch: %name-%version-%release.patch

BuildRequires(pre): rpm-build-ruby
BuildRequires: ruby-addressable
BuildRequires: gem-rubocop
BuildRequires: gem-pathutil
BuildRequires: gem-liquid
BuildRequires: gem-kramdown
BuildRequires: ruby-i18n
BuildRequires: gem-jekyll-sass-converter
BuildRequires: ruby-safe_yaml
BuildRequires: gem-colorator
BuildRequires: gem-sassc



%description
Jekyll is a simple, blog aware, static site generator.

%package doc
Summary: Documentation files for %name
Group: Documentation

BuildArch: noarch

%description doc
Documentation files for %name.

%prep
%setup -n %name-%version
%autopatch -p1
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
%_bindir/jekyll
%ruby_sitelibdir/*
%rubygem_specdir/*
%exclude %ruby_sitelibdir/*/script

%files doc
%ruby_ri_sitedir/*

%changelog
* Wed Mar 03 2021 Dmitriy Voropaev <voropaevdmtr@altlinux.org> 4.2.0-alt1
- initial build
