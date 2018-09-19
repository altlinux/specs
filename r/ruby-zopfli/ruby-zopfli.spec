%define  pkgname zopfli

Name:    ruby-%pkgname
Version: 0.0.7
Release: alt2

Summary: Ruby wrapper for zopfli
License: MIT
Group:   Development/Ruby
Url:     https://github.com/miyucy/zopfli

Packager:  Ruby Maintainers Team <ruby@packages.altlinux.org>

Source:  %pkgname-%version.tar

BuildRequires(pre): rpm-build-ruby
BuildRequires: libruby-devel
BuildRequires: libzopfli-devel

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
%ruby_test_unit -Ilib:test test

%files
%doc README*
%ruby_sitelibdir/*
%rubygem_specdir/*

%files doc
%ruby_ri_sitedir/*

%changelog
* Sat Jun 09 2018 Andrey Cherepanov <cas@altlinux.org> 0.0.7-alt2
- Rebuild for aarch64.
- Package as gem.

* Tue Jun 05 2018 Andrey Cherepanov <cas@altlinux.org> 0.0.7-alt1
- Initial build for Sisyphus
