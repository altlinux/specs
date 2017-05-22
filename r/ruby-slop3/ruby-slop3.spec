%define  pkgname slop3

Name: 	 ruby-%pkgname
Version: 3.6.0 
Release: alt1

Summary: Simple Lightweight Option Parsing
License: MIT
Group:   Development/Ruby
Url:     https://github.com/leejarvis/slop

Packager:  Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch: noarch

Source:  %pkgname-%version.tar

BuildRequires(pre): rpm-build-ruby
BuildRequires: ruby-tool-setup

Conflicts: ruby-slop

%description
Slop is a simple option parser with an easy to remember syntax and friendly API.

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
%ruby_test_unit -Ilib:test test

%files
%doc README*
%ruby_sitelibdir/*

%files doc
%ruby_ri_sitedir/*

%changelog
* Sun May 21 2017 Gordeev Mikhail <obirvalger@altlinux.org> 3.6.0-alt1
- Initial build in Sisyphus
