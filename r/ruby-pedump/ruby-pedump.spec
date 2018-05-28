%define  pkgname pedump

Name: 	 ruby-%pkgname
Version: 0.5.2 
Release: alt1

Summary: dump windows PE files using ruby
License: MIT
Group:   Development/Ruby
Url:     http://github.com/zed-0xff/pedump

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
%_bindir/%pkgname
%ruby_sitelibdir/*

%files doc
%ruby_ri_sitedir/*

%changelog
* Sun Sep 24 2017 Andrey Cherepanov <cas@altlinux.org> 0.5.2-alt1
- Initial build for Sisyphus
