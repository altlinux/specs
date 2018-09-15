%define  pkgname sass-rails

Name:    ruby-%pkgname
Version: 5.0.7
Release: alt1.1

Summary: Ruby on Rails stylesheet engine for Sass
License: MIT
Group:   Development/Ruby
Url:     https://github.com/rails/sass-rails

Packager:  Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch: noarch

Source:  %pkgname-%version.tar

BuildRequires(pre): rpm-build-ruby
BuildRequires: ruby-tool-setup

%description
This gem provides official integration for Ruby on Rails projects with
the Sass stylesheet language.

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
#%%ruby_test_unit -Ilib:test test

%files
%doc README*
%ruby_sitelibdir/*
%rubygem_specdir/*

%files doc
%ruby_ri_sitedir/*

%changelog
* Thu Jul 26 2018 Andrey Cherepanov <cas@altlinux.org> 5.0.7-alt1.1
- Rebuild with new Ruby autorequirements.

* Sun Jul 08 2018 Andrey Cherepanov <cas@altlinux.org> 5.0.7-alt1
- Initial build for Sisyphus
