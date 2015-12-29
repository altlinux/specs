%define  pkgname deep_merge
 
Name: 	 ruby-%pkgname
Version: 1.0.1 
Release: alt1
 
Summary: Recursive merging for Ruby hashes
License: MIT/Ruby
Group:   Development/Ruby
Url:     https://github.com/danielsdeleo/deep_merge
 
Packager:  Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch: noarch
 
Source:  %pkgname-%version.tar
 
BuildRequires(pre): rpm-build-ruby
BuildRequires: ruby-tool-setup
 
%description
Deep Merge is a simple set of utility functions for Hash. It permits you
to merge elements inside a hash together recursively. The manner by
which it does this is somewhat arbitrary (since there is no defining
standard for this) but it should end up being pretty intuitive and do
what you expect.

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
* Tue Dec 22 2015 Andrey Cherepanov <cas@altlinux.org> 1.0.1-alt1
- Initial build for ALT Linux
