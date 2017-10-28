%define  pkgname em-hiredis

Name: 	 ruby-%pkgname
Version: 0.3.1 
Release: alt1

Summary: Eventmachine redis client
License: MIT
Group:   Development/Ruby
Url:     https://github.com/mloughran/em-hiredis

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
%doc README*
%ruby_sitelibdir/*

%files doc
%ruby_ri_sitedir/*

%changelog
* Wed Sep 20 2017 Andrey Cherepanov <cas@altlinux.org> 0.3.1-alt1
- Initial build for Sisyphus
