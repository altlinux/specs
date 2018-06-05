Name:    ruby-babel-transpiler
Version: 0.7.0
Release: alt1

Summary: Ruby Babel is a bridge to the JS Babel transpiler
License: MIT
Group:   Development/Ruby
Url:     https://github.com/babel/ruby-babel-transpiler

Packager:  Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch: noarch

Source:  %name-%version.tar
Source1: babel-source-5.8.35.gem

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
%setup
tar xOf %SOURCE1 data.tar.gz | tar xzf -
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
* Mon Jun 04 2018 Andrey Cherepanov <cas@altlinux.org> 0.7.0-alt1
- Initial build for Sisyphus
