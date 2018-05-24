%define  pkgname ovirt-engine-sdk-ruby

Name:    ruby-ovirt-engine-sdk
Version: 4.2.4
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
%patch -p1
pushd sdk
%update_setup_rb

%build
pushd sdk
%ruby_config
%ruby_build

%install
pushd sdk
%ruby_install
%rdoc lib/
# Remove unnecessary files
rm -f %buildroot%ruby_ri_sitedir/{Object/cdesc-Object.ri,cache.ri,created.rid}

%files
%doc README*
%ruby_sitelibdir/*

%files doc
%ruby_ri_sitedir/*

%changelog
* Fri May 25 2018 Andrey Cherepanov <cas@altlinux.org> 4.2.4-alt1
- Initial build for Sisyphus
