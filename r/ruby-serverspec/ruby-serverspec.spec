%define  pkgname serverspec

Name:    ruby-%pkgname
Version: 2.41.3
Release: alt1

Summary: RSpec tests for your servers configured by CFEngine, Puppet, Chef, Ansible, Itamae or anything else even by hand
License: MIT
Group:   Development/Ruby
Url:     https://github.com/mizzy/serverspec

Packager:  Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch: noarch

Source:  %pkgname-%version.tar

BuildRequires(pre): rpm-build-ruby
BuildRequires: ruby-tool-setup

%filter_from_requires /^ruby(\(winrm\|spec_helper\))/d

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
cp -a spec %buildroot%ruby_sitelibdir/%pkgname/
%rdoc lib/
# Remove unnecessary files
rm -f %buildroot%ruby_ri_sitedir/{Object/cdesc-Object.ri,cache.ri,created.rid}

%check
%ruby_test_unit -Ilib:test test

%files
%doc README*
%_bindir/serverspec-init
%ruby_sitelibdir/*

%files doc
%ruby_ri_sitedir/*

%changelog
* Fri May 25 2018 Andrey Cherepanov <cas@altlinux.org> 2.41.3-alt1
- Initial build for Sisyphus
