%define  pkgname fog-aws

Name:    ruby-%pkgname
Version: 2.0.1
Release: alt1
Epoch:   1

Summary: Module for the 'fog' gem to support Amazon Web Services http://aws.amazon.com/
License: MIT
Group:   Development/Ruby
Url:     https://github.com/fog/fog-aws

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
%rubygem_specdir/*

%files doc
%ruby_ri_sitedir/*

%changelog
* Tue Sep 04 2018 Andrey Cherepanov <cas@altlinux.org> 1:2.0.1-alt1
- Use old version for fog-core.

* Wed Jul 11 2018 Andrey Cherepanov <cas@altlinux.org> 3.0.0-alt1.1
- Rebuild with new Ruby autorequirements.

* Thu May 24 2018 Andrey Cherepanov <cas@altlinux.org> 3.0.0-alt1
- Initial build for Sisyphus
