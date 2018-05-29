%define  pkgname deep_cloneable

Name:    ruby-deep-cloneable
Version: 2.3.2
Release: alt1

Summary: This gem gives every ActiveRecord::Base object the possibility to do a deep clone that includes user specified associations.
License: MIT
Group:   Development/Ruby
Url:     http://github.com/moiristo/deep_cloneable

Packager:  Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch: noarch

Source:  %pkgname-%version.tar

BuildRequires(pre): rpm-build-ruby
BuildRequires: ruby-tool-setup

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
%doc readme.md
%ruby_sitelibdir/*

%files doc
%ruby_ri_sitedir/*

%changelog
* Tue May 29 2018 Andrey Cherepanov <cas@altlinux.org> 2.3.2-alt1
- Initial build for Sisyphus
