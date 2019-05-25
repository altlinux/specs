Name: 	 rubyzip
Version: 1.2.3
Release: alt1
 
Summary: rubyzip is a ruby module for reading and writing zip files
License: MIT/Ruby
Group:   Development/Ruby
Url:     https://github.com/rubyzip/rubyzip
 
Packager:  Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch: noarch
 
Source:  %name-%version.tar
 
BuildRequires(pre): rpm-build-ruby
BuildRequires: ruby-simplecov
BuildRequires: zip

%description
rubyzip is a ruby module for reading and writing zip files.

%package doc
Summary: Documentation files for %name
Group: Documentation
 
BuildArch: noarch
 
%description doc
Documentation files for %{name}.

%prep
%setup
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
#%%ruby_test_unit -Ilib:test test
 
%files
%doc README* TODO
%ruby_sitelibdir/*
%rubygem_specdir/*
 
%files doc
%ruby_ri_sitedir/*
 
%changelog
* Sat May 25 2019 Andrey Cherepanov <cas@altlinux.org> 1.2.3-alt1
- New version.

* Tue Sep 04 2018 Andrey Cherepanov <cas@altlinux.org> 1.2.2-alt1
- New version.

* Wed Jul 11 2018 Andrey Cherepanov <cas@altlinux.org> 1.1.7-alt2.1
- Rebuild with new Ruby autorequirements.

* Mon Jun 25 2018 Dmitry Terekhin <jqt4@altlinux.org> 1.1.7-alt2
- Filter the "ruby(jruby)" dependency for mipsel build

* Tue Feb 17 2015 Andrey Cherepanov <cas@altlinux.org> 1.1.7-alt1
- Initial build for ALT Linux
