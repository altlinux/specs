%define  pkgname escape_utils

Name: 	 ruby-%pkgname
Version: 1.2.1 
Release: alt1

Summary: Faster string escaping routines for your ruby apps
License: MIT
Group:   Development/Ruby
Url:     https://github.com/brianmario/escape_utils

Packager:  Ruby Maintainers Team <ruby@packages.altlinux.org>

Source:  %pkgname-%version.tar

BuildRequires(pre): rpm-build-ruby
BuildRequires: ruby-tool-setup
BuildRequires: libruby-devel

%description
%summary

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
%ruby_sitelibdir/%pkgname.rb
%ruby_sitelibdir/%pkgname
%ruby_sitearchdir/*

%files doc
%ruby_ri_sitedir/*

%changelog
* Wed Jun 14 2017 Andrey Cherepanov <cas@altlinux.org> 1.2.1-alt1
- Initial build for Sisyphus
