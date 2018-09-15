%define source_version 1.12.2
%define gem_version 2.4.1
Name:    ruby-coffee-script
Version: %gem_version
Release: alt2

Summary: Ruby CoffeeScript Compiler
License: MIT
Group:   Development/Ruby
Url:     https://github.com/rails/ruby-coffee-script

Packager:  Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch: noarch

Source:  %name-%version.tar
Source1: coffee-script-source.gemspec
Source2: source.rb

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

%package -n ruby-coffee-script-source
Summary: Ruby CoffeeScript Compiler sources
Group: Development/Ruby
Version: %source_version
Release: alt2

BuildArch: noarch

%description -n ruby-coffee-script-source
%summary

%prep
%setup
%update_setup_rb

%build
%ruby_config
%ruby_build

mkdir -p ruby-coffee-script-source/lib/coffee-script
cp %SOURCE1 ./ruby-coffee-script-source/coffee-script-source.gemspec
cp %SOURCE2 ./ruby-coffee-script-source/lib/coffee-script/source.rb
cd ruby-coffee-script-source
%update_setup_rb
%ruby_config
%ruby_build

%install
%ruby_install
%rdoc lib/
# Remove unnecessary files
rm -f %buildroot%ruby_ri_sitedir/{Object/cdesc-Object.ri,cache.ri,created.rid}
cd ruby-coffee-script-source
%ruby_install

%check
#%%ruby_test_unit -Ilib:test test

%files
%doc README*
%ruby_sitelibdir/coffee-script.rb
%ruby_sitelibdir/coffee_script.rb
%rubygem_specdir/coffee-script-%{gem_version}*

%files doc
%ruby_ri_sitedir/*

%files -n ruby-coffee-script-source
%ruby_sitelibdir/coffee-script/source.rb
%rubygem_specdir/coffee-script-source*

%changelog
* Wed Sep 05 2018 Pavel Skrylev <majioa@altlinux.org> 2.4.1-alt2
- Split into two gems coffee-script-transpiler and coffee-script-source.

* Tue Jul 24 2018 Andrey Cherepanov <cas@altlinux.org> 2.4.1-alt1.1
- Rebuild with new Ruby autorequirements.
- Disable tests.

* Tue Jun 05 2018 Andrey Cherepanov <cas@altlinux.org> 2.4.1-alt1
- Initial build for Sisyphus
