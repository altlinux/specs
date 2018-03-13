%define  pkgname hiredis-rb

Name: 	 ruby-hiredis
Version: 0.6.1 
Release: alt1.1

Summary: Ruby wrapper for hiredis
License: BSD-3-Clause
Group:   Development/Ruby
Url:     http://github.com/redis/hiredis-rb

Packager:  Ruby Maintainers Team <ruby@packages.altlinux.org>

Source:  %pkgname-%version.tar
Patch:   %name-%version-%release.patch

BuildRequires(pre): rpm-build-ruby
BuildRequires: ruby-tool-setup
BuildRequires: libruby-devel
BuildRequires: libhiredis-devel

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
%patch -p1
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
* Tue Mar 13 2018 Andrey Cherepanov <cas@altlinux.org> 0.6.1-alt1.1
- Rebuild with Ruby 2.5.0

* Sat Oct 28 2017 Andrey Cherepanov <cas@altlinux.org> 0.6.1-alt1
- Initial build for Sisyphus
