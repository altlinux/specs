%define  pkgname ovirt-engine-sdk-ruby

Name:    ruby-ovirt-engine-sdk
Version: 4.2.5
Release: alt1

Summary: This is a mirror from gerrit.ovirt.org http://www.ovirt.org, for issues use http://bugzilla.redhat.com
License: Apache 2.0
Group:   Development/Ruby
Url:     https://github.com/oVirt/ovirt-engine-sdk-ruby

Packager:  Ruby Maintainers Team <ruby@packages.altlinux.org>

Source:  %pkgname-%version.tar
Patch:   alt-remove-absent-modules.patch

BuildRequires(pre): rpm-build-ruby
BuildRequires: ruby-tool-setup
BuildRequires: libruby-devel
BuildRequires: libcurl-devel
BuildRequires: libxml2-devel

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
%patch -p2
%update_setup_rb
echo -e "module OvirtSDK4\nVERSION = \"%version\"\nend" > lib/ovirtsdk4/version.rb

%build
%ruby_config
%ruby_build

%install
%ruby_install
%rdoc lib/
# Remove unnecessary files
rm -f %buildroot%ruby_ri_sitedir/{Object/cdesc-Object.ri,cache.ri,created.rid}

%files
%doc README*
%ruby_sitelibdir/*
%rubygem_specdir/*

%files doc
%ruby_ri_sitedir/*

%changelog
* Mon Oct 08 2018 Andrey Cherepanov <cas@altlinux.org> 4.2.5-alt1
- New version.

* Wed Jul 11 2018 Andrey Cherepanov <cas@altlinux.org> 4.2.4-alt1.2
- Rebuild with new Ruby autorequirements.

* Sat Jun 09 2018 Andrey Cherepanov <cas@altlinux.org> 4.2.4-alt1.1
- Rebuild for aarch64.

* Fri May 25 2018 Andrey Cherepanov <cas@altlinux.org> 4.2.4-alt1
- Initial build for Sisyphus
