%define  pkgname backports
 
Name: 	 ruby-%pkgname
Version: 3.7.0 
Release: alt1
 
Summary: The latest features of Ruby backported to older versions

License: MIT/Ruby
Group:   Development/Ruby
Url:     https://github.com/marcandre/backports
 
Packager:  Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch: noarch
 
Source:  %pkgname-%version.tar
 
BuildRequires(pre): rpm-build-ruby
BuildRequires: ruby-tool-setup
BuildRequires: libruby-devel 
 
%description
The goal of 'backports' is to make it easier to write ruby code that runs across
different versions of Ruby.

%package doc
Summary: Documentation files for %name
Group: Documentation
 

 
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
* Wed Mar 29 2017 Denis Medvedev <nbr@altlinux.org> 3.7.0-alt1
- Initial build in sisyphus
