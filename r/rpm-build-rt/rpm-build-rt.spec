Name: rpm-build-rt
Url: http://sisyphus.ru/srpm/Sisyphus/rpm-build-rt
Version: 0.01
Release: alt1

Summary: helper to build rt extensions
License: LGPL2+
Group: Development/Other

Requires(post,preun): rt

BuildArch: noarch

%description
The package makes rt config files readable to help build rt extensions.
Use this package in chroot builds only. Never install this package into a living system.

!!! Do not install this package into a living system !!!

%install
mkdir -p %buildroot

%post
chmod o+r %{_sysconfdir}/rt/RT_*.pm
#%{_sysconfdir}/rt/RT_SiteConfig.d ?

%postun
if [ "$1" -eq 0 ]; then
    chmod o-r %{_sysconfdir}/rt/RT_*.pm ||:
fi

%files

%changelog
* Thu Feb 14 2019 Igor Vlasenko <viy@altlinux.ru> 0.01-alt1
- Initial build for Sisyphus
