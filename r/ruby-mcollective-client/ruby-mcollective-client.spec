%define  pkgname mcollective-client

Name: 	 ruby-%pkgname
Version: 2.11.0 
Release: alt1

Summary: Client libraries for the Mcollective Application Server
License: MIT/Ruby
Group:   Development/Ruby
Url:     https://rubygems.org/gems/mcollective-client/versions/2.11.0

Packager:  Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch: noarch

Source:  %pkgname-%version.tar

%filter_from_requires /^ruby(Win32API)$/d
%filter_from_requires \!^ruby(win32/daemon)$!d
%filter_from_requires \!^ruby(win32/dir)$!d

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
#install -Dm0755 bin/mco %%buildroot%%_bindir/mco
%rdoc lib/
# Remove unnecessary files
rm -f %buildroot%ruby_ri_sitedir/{Object/cdesc-Object.ri,cache.ri,created.rid}

%check
%ruby_test_unit -Ilib:test test

%files
%ruby_sitelibdir/*
#%%_bindir/mco

%files doc
%ruby_ri_sitedir/*

%changelog
* Tue Jul 11 2017 Mikhail Gordeev <obirvalger@altlinux.org> 2.11.0-alt1
- Initial build for Sisyphus
