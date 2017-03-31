%define  pkgname ethon
 
Name: 	 ruby-%pkgname
Version: 0.9.1 
Release: alt1
 
Summary: Very simple libcurl wrapper
License: MIT/Ruby
Group:   Development/Ruby
Url:     https://github.com/typhoeus/ethon
 
Packager:  Ruby Maintainers Team <ruby@packages.altlinux.org>
 
Source:  %pkgname-%version.tar
 
BuildRequires(pre): rpm-build-ruby
BuildRequires: ruby-tool-setup
BuildRequires: libruby-devel
BuildArch: noarch
%description
In Greek mythology, Ethon, the son of Typhoeus and Echidna, is a gigantic eagle. So much for the history. In the modern world, Ethon is a very basic libcurl wrapper using ffi.

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
* Wed Mar 29 2017 Denis Medvedev <nbr@altlinux.org> 0.9.1-alt1
- Initial sisyphus release
