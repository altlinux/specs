%define   pkgname fluentd
Name:    ruby-fluentd
Version: 1.9.3
Release: alt2

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

%package -n %pkgname
Summary: Documentation files for %name
Group: Documentation

BuildArch: noarch

%description -n %pkgname
%summary

%package doc
Summary: Documentation files for %name
Group: Documentation

BuildArch: noarch

%description doc
Documentation files for %{name}.

%prep
%setup -n %name-%version

%build
%gem_build

%install
%gem_show
%gem_install
install -pDm 0644 fluent.conf %buildroot%_sysconfdir/fluent/fluent.conf

%files
%rubygem_gemdir/*
%rubygem_specdir/*

%files -n %pkgname
%doc README*
%_bindir/%pkgname
%_bindir/fluent-*
%config(noreplace) %_sysconfdir/fluent/fluent.conf

%files doc
%ruby_gemdocdir

%changelog
* Mon Mar 30 2020 Mikhail Gordeev <obirvalger@altlinux.org> 1.9.3-alt2
- Change used ruby documentation macro

* Thu Mar 19 2020 Mikhail Gordeev <obirvalger@altlinux.org> 1.9.3-alt1
- new version 1.9.3

* Thu Sep 27 2018 Mikhail Gordeev <obirvalger@altlinux.org> 1.2.5-alt1
- Initial build for Sisyphus
