%define source_version 5.8.35
Name:    ruby-babel-transpiler
Version: 0.7.0
Release: alt2

Summary: Ruby Babel is a bridge to the JS Babel transpiler
License: MIT
Group:   Development/Ruby
Url:     https://github.com/babel/ruby-babel-transpiler

Packager:  Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch: noarch

Source:  %name-%version.tar

BuildRequires(pre): rpm-build-ruby
BuildRequires: ruby-tool-setup

%description
%summary

%package doc
Summary: Documentation files for %name
Group: Documentation

BuildArch: noarch

%description doc
Documentation files for %{name}.

%package -n ruby-babel-source
Summary: Java script sources for JS Babel transpiler
Group: Development/Ruby
Version: %source_version
Release: alt2

BuildArch: noarch

%description -n ruby-babel-source
Java script sources for JS Babel transpiler.

%prep
%setup
%update_setup_rb

%build
%ruby_config
%ruby_build

mkdir -p "ruby-babel-source/lib/babel"
./script/eval-erb-template "babel-source.gemspec.erb" %{source_version} "$(date +%%s)" > "./ruby-babel-source/babel-source.gemspec"
./script/eval-erb-template "lib/babel/source.rb.erb" %{source_version} "$(date +%%s)" > "./ruby-babel-source/lib/babel/source.rb"
cd ruby-babel-source
%update_setup_rb
%ruby_config
%ruby_build

%install
%ruby_install
%rdoc lib/
# Remove unnecessary files
rm -f %buildroot%ruby_ri_sitedir/{Object/cdesc-Object.ri,cache.ri,created.rid}
cd ruby-babel-source
%ruby_install

%check
#%%ruby_test_unit -Ilib:test test

%files
%doc README*
%ruby_sitelibdir/babel-transpiler.rb
%ruby_sitelibdir/babel/transpiler*
%rubygem_specdir/babel-transpiler*

%files doc
%ruby_ri_sitedir/*

%files -n ruby-babel-source
%ruby_sitelibdir/babel/source.rb
%rubygem_specdir/babel-source*

%changelog
* Tue Sep 04 2018 Pavel Skrylev <majioa@altlinux.org> 0.7.0-alt2
- Split into two gems babel-transpiler and babel-source.

* Tue Jul 24 2018 Andrey Cherepanov <cas@altlinux.org> 0.7.0-alt1.1
- Rebuild with new Ruby autorequirements.
- Disable tests.

* Mon Jun 04 2018 Andrey Cherepanov <cas@altlinux.org> 0.7.0-alt1
- Initial build for Sisyphus
