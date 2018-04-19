Name: 	 ruby-domain_name
Version: 0.5.20180417
Release: alt1

Summary: Domain Name manipulation library for Ruby
License: BSD and (MPLv1.1 or GPLv2+ or LGPLv2+)
Group:   Development/Ruby
Url:     https://github.com/knu/ruby-domain_name

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
* Thu Apr 19 2018 Andrey Cherepanov <cas@altlinux.org> 0.5.20180417-alt1
- New version.

* Mon Sep 11 2017 Andrey Cherepanov <cas@altlinux.org> 0.5.20170404-alt1
- Initial build for Sisyphus.
