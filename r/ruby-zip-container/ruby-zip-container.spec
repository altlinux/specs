%define  pkgname zip-container
 
Name: 	 ruby-%pkgname
Version: 3.0.2
Release: alt1
 
Summary: A Ruby library for working with ZIP Container Format files
License: MIT/Ruby
Group:   Development/Ruby
Url:     http://mygrid.github.io/ruby-zip-container/
# VCS:	 https://github.com/myGrid/ruby-zip-container

Packager:  Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch: noarch
 
Source:  %pkgname-%version.tar
 
BuildRequires(pre): rpm-build-ruby
BuildRequires: ruby-tool-setup
BuildRequires: rubyzip
 
%description
A Ruby library for working with ZIP Container Format files. See
http://www.idpf.org/epub/30/spec/epub30-ocf.html for the OCF
specification and
https://learn.adobe.com/wiki/display/PDFNAV/Universal+Container+Format
for the UCF specification.

%package doc
Summary: Documentation files for %name
Group: Documentation
 
BuildArch: noarch
 
%description doc
Documentation files for %{name}.

%prep
%setup -n %pkgname-%version
subst 's,\(require.*bundler/setup\),#\1,' lib/zip-container.rb

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
#ruby_test_unit -Ilib:test test
 
%files
%doc Changes.rdoc Licence.rdoc ReadMe.rdoc
%ruby_sitelibdir/*
%rubygem_specdir/*
 
%files doc
%ruby_ri_sitedir/*
 
%changelog
* Wed Sep 05 2018 Andrey Cherepanov <cas@altlinux.org> 3.0.2-alt1
- New version.

* Wed Jul 11 2018 Andrey Cherepanov <cas@altlinux.org> 3.0.1-alt1.1
- Rebuild with new Ruby autorequirements.

* Tue Feb 17 2015 Andrey Cherepanov <cas@altlinux.org> 3.0.1-alt1
- Initial build for ALT Linux (without tests)
