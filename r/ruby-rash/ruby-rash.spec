%define  pkgname rash

Name: 	 ruby-%pkgname
Version: 0.4.5
Release: alt1

Summary: Simple extension to Hashie::Mash for rubyified keys
License: MIT
Group:   Development/Ruby
Url:     https://github.com/shishi/rash_alt

Packager:  Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch: noarch

Source:  rash_alt-%version.tar

BuildRequires(pre): rpm-build-ruby
BuildRequires: ruby-tool-setup

%description
Simple extension to Hashie::Mash for rubyified keys. This alt version solve
problem which conflict name space and out of dependency.

%package doc
Summary: Documentation files for %name
Group: Documentation

BuildArch: noarch

%description doc
Documentation files for %{name}.

%prep
%setup -n rash_alt-%version
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
* Wed Dec 13 2017 Andrey Cherepanov <cas@altlinux.org> 0.4.5-alt1
- New version.

* Thu Oct 19 2017 Andrey Cherepanov <cas@altlinux.org> 0.4.4-alt1
- New version

* Fri Sep 01 2017 Andrey Cherepanov <cas@altlinux.org> 0.4.3-alt1
- Initial build for Sisyphus
