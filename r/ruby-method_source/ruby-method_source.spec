%define  pkgname method_source

Name: 	 ruby-%pkgname
Version: 0.9.0
Release: alt1

Summary: return the sourcecode for a method
License: MIT
Group:   Development/Ruby
Url:     https://github.com/banister/method_source

Packager:  Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch: noarch

Source:  %pkgname-%version.tar
Patch:   alt-fix-version-in-gemspec.patch

BuildRequires(pre): rpm-build-ruby
BuildRequires: ruby-tool-setup

%description
Retrieve the sourcecode for a method.

%package doc
Summary: Documentation files for %name
Group: Documentation

BuildArch: noarch

%description doc
Documentation files for %{name}.

%prep
%setup -n %pkgname-%version
%patch -p1
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
* Thu Aug 23 2018 Andrey Cherepanov <cas@altlinux.org> 0.9.0-alt1
- New version.

* Thu Aug 23 2018 Andrey Cherepanov <cas@altlinux.org> 0.8.2-alt1.1
- Rebuild for new Ruby autorequirements.
- Disable tests.

* Wed May 17 2017 Gordeev Mikhail <obirvalger@altlinux.org> 0.8.2-alt1
- Initial build in Sisyphus
