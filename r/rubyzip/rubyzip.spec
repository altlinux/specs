Name: 	 rubyzip
Version: 1.1.7 
Release: alt2
 
Summary: rubyzip is a ruby module for reading and writing zip files
License: MIT/Ruby
Group:   Development/Ruby
Url:     https://github.com/rubyzip/rubyzip
 
Packager:  Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch: noarch
 
Source:  %name-%version.tar
 
BuildRequires(pre): rpm-build-ruby
BuildRequires: ruby-tool-setup
BuildRequires: ruby-simplecov
BuildRequires: zip

%filter_from_requires /^ruby(jruby)/d
 
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
%ruby_test_unit -Ilib:test test
 
%files
%doc README* TODO
%ruby_sitelibdir/*
 
%files doc
%ruby_ri_sitedir/*
 
%changelog
* Mon Jun 25 2018 Dmitry Terekhin <jqt4@altlinux.org> 1.1.7-alt2
- Filter the "ruby(jruby)" dependency for mipsel build

* Tue Feb 17 2015 Andrey Cherepanov <cas@altlinux.org> 1.1.7-alt1
- Initial build for ALT Linux
