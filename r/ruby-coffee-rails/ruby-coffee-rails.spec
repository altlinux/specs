%define  pkgname coffee-rails

Name:    ruby-%pkgname
Version: 4.2.2
Release: alt1

Summary: CoffeeScript adapter for the Rails asset pipeline. Also adds support for .coffee views.
License: MIT
Group:   Development/Ruby
Url:     https://github.com/rails/coffee-rails

Packager:  Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch: noarch

Source:  %pkgname-%version.tar

BuildRequires(pre): rpm-build-ruby
BuildRequires: ruby-tool-setup

%description
CoffeeScript adapter for the Rails asset pipeline. Also adds support to
use CoffeeScript to respond to JavaScript requests (use .coffee views).

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
* Thu Jul 26 2018 Andrey Cherepanov <cas@altlinux.org> 4.2.2-alt1
- Initial build for Sisyphus
