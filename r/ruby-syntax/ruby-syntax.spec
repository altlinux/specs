%define  pkgname syntax

Name:    ruby-%pkgname
Version: 1.2.2
Release: alt1

Summary: Syntax is a Ruby library for simple syntax highlighting.
License: BSD
Group:   Development/Ruby
Url:     https://github.com/dblock/syntax

Packager:  Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch: noarch

Source:  %pkgname-%version.tar

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
%ruby_test_unit -Ilib:test test/ALL-TESTS.rb

%files
%doc README*
%ruby_sitelibdir/*

%files doc
%ruby_ri_sitedir/*

%changelog
* Sat Jun 09 2018 Andrey Cherepanov <cas@altlinux.org> 1.2.2-alt1
- Initial build for Sisyphus
