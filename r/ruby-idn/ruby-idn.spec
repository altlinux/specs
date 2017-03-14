%define  pkgname idn
 
Name: 	 ruby-%pkgname
Version: 0.1.0
Release: alt3
 
Summary: Ruby Bindings for the GNU LibIDN library
License: MIT/Ruby
Group:   Development/Ruby
Url:     http://idn.rubyforge.org/
 
Packager: Andrey Cherepanov <cas@altlinux.org>
 
Source:  %pkgname-%version.tar
 
BuildRequires(pre): rpm-build-ruby
BuildRequires: ruby-test-unit ruby-tool-rdoc ruby-tool-setup 
BuildRequires: libidn-devel
BuildRequires: libruby-devel
 
%description
Ruby Bindings for the GNU LibIDN library - featuring the most important
bits of all LibIDN APIs like performing Stringprep processings, encoding
to and decoding from Punycode strings and converting entire domain names
to and from the ACE encoded form.

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
 
%files
%doc README CHANGES NOTICE
%ruby_sitearchdir/*
 
%files doc
%ruby_ri_sitedir/*
 
%changelog
* Sat Mar 11 2017 Andrey Cherepanov <cas@altlinux.org> 0.1.0-alt3
- Rebuild with new %%ruby_sitearchdir location

* Mon Sep 12 2016 Andrey Cherepanov <cas@altlinux.org> 0.1.0-alt2
- Rebuild with Ruby 2.3.1

* Mon Apr 21 2014 Andrey Cherepanov <cas@altlinux.org> 0.1.0-alt1
- Initial build for ALT Linux
