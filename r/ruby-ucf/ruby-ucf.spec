%define  pkgname ucf
 
Name: 	 ruby-%pkgname
Version: 2.0.0 
Release: alt1.1
 
Summary: This is a Ruby library for working with UCF documents
License: MIT/Ruby
Group:   Development/Ruby
Url:     http://mygrid.github.io/ruby-ucf/
# VCS:   https://github.com/myGrid/ruby-ucf

Packager:  Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch: noarch
 
Source:  %pkgname-%version.tar
 
BuildRequires(pre): rpm-build-ruby
BuildRequires: ruby-tool-setup
BuildRequires: ruby-nokogiri
BuildRequires: ruby-zip-container
 
%description
This is a Ruby library for working with UCF documents. See the
specification at
https://learn.adobe.com/wiki/display/PDFNAV/Universal+Container+Format
for more details. UCF is a type of EPUB and very similar to the EPUB
Open Container Format (OCF).

%package doc
Summary: Documentation files for %name
Group: Documentation
 
BuildArch: noarch
 
%description doc
Documentation files for %{name}.

%prep
%setup -n %pkgname-%version
subst 's,\(require.*bundler/setup\),#\1,' lib/%pkgname.rb

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
* Wed Jul 11 2018 Andrey Cherepanov <cas@altlinux.org> 2.0.0-alt1.1
- Rebuild with new Ruby autorequirements.

* Tue Feb 17 2015 Andrey Cherepanov <cas@altlinux.org> 2.0.0-alt1
- Initial build for ALT Linux (without tests)
