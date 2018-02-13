%define  pkgname public_suffix
 
Name: 	 ruby-%pkgname
Version: 3.0.2
Release: alt1
 
Summary: PublicSuffix can parse and decompose a domain name into top level domain, domain and subdomains
License: MIT/Ruby
Group:   Development/Ruby
Url:     https://simonecarletti.com/code/publicsuffix-ruby/
 
Packager:  Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch: noarch
 
Source:  %pkgname-%version.tar
 
BuildRequires(pre): rpm-build-ruby
BuildRequires: ruby-tool-setup
 
%description
PublicSuffix can parse and decompose a domain name into top level
domain, domain and subdomains.

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
%doc *.md
%ruby_sitelibdir/*
 
%files doc
%ruby_ri_sitedir/*
 
%changelog
* Tue Feb 13 2018 Andrey Cherepanov <cas@altlinux.org> 3.0.2-alt1
- New version.

* Thu Nov 09 2017 Andrey Cherepanov <cas@altlinux.org> 3.0.1-alt1
- New version

* Sun Aug 06 2017 Andrey Cherepanov <cas@altlinux.org> 3.0.0-alt1
- New version

* Tue Jan 31 2017 Andrey Cherepanov <cas@altlinux.org> 2.0.5-alt1
- Initial build in Sisyphus
