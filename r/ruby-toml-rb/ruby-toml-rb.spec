%define  pkgname toml-rb

Name:    ruby-%pkgname
Version: 1.1.1
Release: alt1

Summary: A parser for TOML using Citrus library
License: MIT/Ruby
Group:   Development/Ruby
Url:     https://github.com/emancu/toml-rb

Packager:  Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch: noarch

Source:  %pkgname-%version.tar

BuildRequires(pre): rpm-build-ruby
BuildRequires: ruby-tool-setup

%description
A TomlRB parser using Citrus library.
TomlRB specs supported: 0.4.0

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
* Thu Apr 05 2018 Andrey Cherepanov <cas@altlinux.org> 1.1.1-alt1
- Initial build for Sisyphus.
