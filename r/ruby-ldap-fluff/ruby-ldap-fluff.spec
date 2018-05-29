%define  pkgname ldap_fluff

Name:    ruby-ldap-fluff
Version: 0.3.7
Release: alt1

Summary: An LDAP gem for querying LDAP in various styles: Active Directory, FreeIPA & POSIX
License: GPLv2
Group:   Development/Ruby
Url:     https://github.com/theforeman/ldap_fluff

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
%ruby_test_unit -Ilib:test test

%files
%doc README*
%ruby_sitelibdir/*

%files doc
%ruby_ri_sitedir/*

%changelog
* Tue May 29 2018 Andrey Cherepanov <cas@altlinux.org> 0.3.7-alt1
- Initial build for Sisyphus
