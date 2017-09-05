Name: 	 ruby-unf
Version: 0.1.4
Release: alt1

Summary: A wrapper library to bring Unicode Normalization Form support to Ruby/JRuby
License: BSD-2-Clause
Group:   Development/Ruby
Url:     https://github.com/knu/ruby-unf

Packager:  Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch: noarch

Source:  %name-%version.tar

BuildRequires(pre): rpm-build-ruby
BuildRequires: ruby-tool-setup

%filter_from_requires /^ruby(java)/d

%description
%summary

%package doc
Summary: Documentation files for %name
Group: Documentation

BuildArch: noarch

%description doc
Documentation files for %{name}.

%prep
%setup
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
* Mon Sep 11 2017 Andrey Cherepanov <cas@altlinux.org> 0.1.4-alt1
- Initial build for Sisyphus.
