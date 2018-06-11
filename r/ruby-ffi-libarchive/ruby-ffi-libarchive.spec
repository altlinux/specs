%define  pkgname ffi-libarchive

Name:    ruby-%pkgname
Version: 0.4.1
Release: alt1

Summary: A Ruby FFI binding to libarchive.
License: GPL-3.0
Group:   Development/Ruby
Url:     https://github.com/johnbellone/ffi-libarchive

Packager:  Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch: noarch

Source:  %pkgname-%version.tar

BuildRequires(pre): rpm-build-ruby
BuildRequires: ruby-tool-setup
# For tests
BuildRequires: ruby-ffi

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
#%%ruby_test_unit -Ilib:test test

%files
%doc README*
%ruby_sitelibdir/*

%files doc
%ruby_ri_sitedir/*

%changelog
* Mon Jun 11 2018 Andrey Cherepanov <cas@altlinux.org> 0.4.1-alt1
- New version.
- Disable tests.

* Tue May 29 2018 Andrey Cherepanov <cas@altlinux.org> 0.2.0-alt1
- Initial build for Sisyphus
