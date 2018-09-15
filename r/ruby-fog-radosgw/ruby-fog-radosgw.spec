%define  pkgname fog-radosgw

Name:    ruby-%pkgname
Version: 0.0.5
Release: alt1

Summary: Fog backend for provisioning Ceph Radosgw - the Swift and S3 compatible REST API for Ceph.
Summary(ru_RU.UTF8): Затынка для резервирования Ceph Radosgw, Ceph REST API совместимый с Swift и S3
License: MIT
Group:   Development/Ruby
Url:     https://github.com/fog/fog-radosgw

Packager:  Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch: noarch

Source:  %pkgname-%version.tar

BuildRequires(pre): rpm-build-ruby
BuildRequires: ruby-tool-setup

%description
Fog backend for provisioning Ceph Radosgw - the Swift and S3 compatible REST API
for Ceph. Currently, the gem only supports the S3 API, not Swift. Based on the
Riak CS backend.

%description -l ru_RU.UTF8
Затынка для резервирования Ceph Radosgw, Ceph REST API совместимый с Swift и S3.
Ныне в бисере поддерживается только S3 API, но не Swift. Основан на затынке Riak CS.

%package doc
Summary: Documentation files for %name
Group: Documentation

BuildArch: noarch

%description doc
Documentation files for %{name}.

%description doc -l ru_RU.UTF8
Файлы сведений для %name

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

#%check
#%ruby_test_unit -Ilib:test test

%files
%doc README*
%ruby_sitelibdir/*
%rubygem_specdir/*

%files doc
%ruby_ri_sitedir/*

%changelog
* Thu Aug 30 2018 Pavel Skrylev <majioa@altlinux.org> 0.0.5-alt1
- Initial build for Sisyphus
