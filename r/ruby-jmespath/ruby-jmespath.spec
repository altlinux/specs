%define  pkgname jmespath

Name: 	 ruby-%pkgname
Version: 1.3.1 
Release: alt1

Summary: Ruby implementation of JMESPath
License: Apache-2.0
Group:   Development/Ruby
Url:     https://github.com/jmespath/jmespath.rb

Packager:  Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch: noarch

Source:  jmespath.rb-%version.tar

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

%prep
%setup -n jmespath.rb-%version
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
%_bindir/jmespath.rb
%ruby_sitelibdir/*

%files doc
%ruby_ri_sitedir/*

%changelog
* Thu Aug 31 2017 Andrey Cherepanov <cas@altlinux.org> 1.3.1-alt1
- Initial build for Sisyphus
