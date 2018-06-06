Name:    sprockets
Version: 4.0.0
Release: alt0.1.beta7

Summary: Rack-based asset packaging system
License: MIT
Group:   Development/Ruby
Url:     https://github.com/rails/sprockets

Packager:  Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch: noarch

Source:  %name-%version.tar

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
%setup -q
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
%_bindir/%name
%ruby_sitelibdir/*

%files doc
%ruby_ri_sitedir/*

%changelog
* Thu May 31 2018 Andrey Cherepanov <cas@altlinux.org> 4.0.0-alt0.1.beta7
- Initial build for Sisyphus
