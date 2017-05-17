%define  pkgname method_source

Name: 	 ruby-%pkgname
Version: 0.8.2 
Release: alt1

Summary: return the sourcecode for a method
License: MIT
Group:   Development/Ruby
Url:     https://github.com/banister/method_source

Packager:  Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch: noarch

Source:  %pkgname-%version.tar

%filter_from_requires /^ruby(java)$/d

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
* Wed May 17 2017 Gordeev Mikhail <obirvalger@altlinux.org> 0.8.2-alt1
- Initial build in Sisyphus
