Name:    fluentd
Version: 1.2.5
Release: alt1

Summary: Fluentd: Unified Logging Layer (project under CNCF)
License: Apache-2.0
Group:   Development/Ruby
Url:     https://github.com/fluent/fluentd

Packager:  Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch: noarch

Source:  %name-%version.tar

BuildRequires(pre): rpm-build-ruby

%description
%summary

%package doc
Summary: Documentation files for %name
Group: Documentation

BuildArch: noarch

%description doc
Documentation files for %{name}.

%prep
%setup -n %name-%version
%update_setup_rb

%build
%ruby_config
%ruby_build

%install
%ruby_install
%rdoc lib/
# Remove unnecessary files
rm -f %buildroot%ruby_ri_sitedir/{Object/cdesc-Object.ri,cache.ri,created.rid}
install -pDm 0644 fluent.conf %buildroot%_sysconfdir/fluent/fluent.conf

%files
%doc README*
%_bindir/%name
%_bindir/fluent-*
%ruby_sitelibdir/*
%rubygem_specdir/*
%config(noreplace) %_sysconfdir/fluent/fluent.conf

%files doc
%ruby_ri_sitedir/*

%changelog
* Thu Sep 27 2018 Mikhail Gordeev <obirvalger@altlinux.org> 1.2.5-alt1
- Initial build for Sisyphus
