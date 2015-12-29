%define  pkgname semantic
 
Name: 	 ruby-%pkgname
Version: 1.4.1 
Release: alt1
 
Summary: Semantic Version utility class for parsing, storing, and comparing versions
License: MIT/Ruby
Group:   Development/Ruby
Url:     https://github.com/jlindsey/semantic
 
Packager:  Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch: noarch
 
Source:  %pkgname-%version.tar
 
BuildRequires(pre): rpm-build-ruby
BuildRequires: ruby-tool-setup
 
%description
A small Ruby utility class to aid in the storage, parsing, and
comparison of SemVer-style Version strings.

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
* Tue Dec 22 2015 Andrey Cherepanov <cas@altlinux.org> 1.4.1-alt1
- Initial build for ALT Linux
