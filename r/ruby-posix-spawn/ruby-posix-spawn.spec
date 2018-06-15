%define  pkgname posix-spawn

Name:    ruby-%pkgname
Version: 0.3.13
Release: alt1

Summary: Ruby process spawning library
License: MIT
Group:   Development/Ruby
Url:     https://github.com/rtomayko/posix-spawn

Packager:  Ruby Maintainers Team <ruby@packages.altlinux.org>

Source:  %pkgname-%version.tar
Patch:   upstream-fix-build-on-i586.patch

BuildRequires(pre): rpm-build-ruby
BuildRequires: ruby-tool-setup
BuildRequires: libruby-devel

%filter_from_requires /^ruby(jruby)/d

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
#%%ruby_test_unit -Ilib:test test

%files
%doc README*
%ruby_sitelibdir/*

%files doc
%ruby_ri_sitedir/*

%changelog
* Fri Jun 15 2018 Andrey Cherepanov <cas@altlinux.org> 0.3.13-alt1
- Initial build for Sisyphus
