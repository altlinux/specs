%define  pkgname generator
 
Name: 	 ruby-%pkgname
Version: 0.0.1 
Release: alt1
 
Summary: Generator gem help to create and use generators like rails 3 
License: MIT/Ruby
Group:   Development/Ruby
Url:     https://github.com/maxkazar/generator
 
Packager:  Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch: noarch
 
Source:  %pkgname-%version.tar
 
BuildRequires(pre): rpm-build-ruby
BuildRequires: ruby-tool-setup
 
%description
Generator gem is designed for use in ruby projects and provides templates generators like rails 3.

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
* Wed Mar 29 2017 Denis Medvedev <nbr@altlinux.org> 0.0.1-alt1
- Initial sisyphus release
