%define  pkgname ancestry

Name:    ruby-%pkgname
Version: 3.0.2
Release: alt2

Summary: Organise ActiveRecord model into a tree structure
License: MIT
Group:   Development/Ruby
Url:     https://github.com/stefankroes/ancestry

Packager:  Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch: noarch

Source:  %pkgname-%version.tar

BuildRequires(pre): rpm-build-ruby
BuildRequires: ruby-tool-setup

%description
%summary

%description -l ru_RU.UTF8
Упорядочивание модели ActiveRecord в виде древовидной структуры

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
* Fri Sep 21 2018 Pavel Skrylev <majioa@altlinux.org> 3.0.2-alt2
- Gemify the package.

* Tue May 29 2018 Andrey Cherepanov <cas@altlinux.org> 3.0.2-alt1
- Initial build for Sisyphus
