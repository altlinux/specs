%define  pkgname polyglot
 
Name: 	 ruby-%pkgname
Version: 0.3.5
Release: alt1
 
Summary: Augment 'require' to load non-ruby file types
License: MIT/Ruby
Group:   Development/Ruby
Url:     http://polyglot.rubyforge.org/
 
Packager: Andrey Cherepanov <cas@altlinux.org>
BuildArch: noarch
 
Source:  %pkgname-%version.tar
 
BuildRequires(pre): rpm-build-ruby
BuildRequires: ruby-tool-setup
 
%description
The Polyglot library allows a Ruby module to register a loader
for the file type associated with a filename extension, and it
augments 'require' to find and load matching files.

This supports the creation of DSLs having a syntax that is most
appropriate to their purpose, instead of abusing the Ruby syntax.

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
* Fri Jun 03 2016 Andrey Cherepanov <cas@altlinux.org> 0.3.5-alt1
- New version

* Thu Apr 24 2014 Andrey Cherepanov <cas@altlinux.org> 0.3.4-alt1
- Initial build for ALT Linux
