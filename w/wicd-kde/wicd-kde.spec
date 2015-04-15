Name:           wicd-kde
Version:        0.3.1
Release:        alt2
License:        GPLv3+
Group:          Networking/WWW
Summary:        A Wicd client built on the KDE Development Platform
URL:            https://projects.kde.org/projects/extragear/network/wicd-kde

Source:         http://kde-apps.org/CONTENT/content-files/132366-wicd-kde-0.3.1.tar.gz

Requires:       wicd

BuildRequires(pre): rpm-macros-fedora-compat
BuildRequires:  gcc-c++
BuildRequires:  qt4-devel
BuildRequires:  kde4libs-devel
BuildRequires:  gettext

%description
A Wicd client built on the KDE Development Platform.

%prep
%setup -qn %{name}

%build
mkdir -p %{_target_platform}
pushd %{_target_platform}
%{cmake_kde4} ../
popd
make %{?_smp_mflags} -C %{_target_platform} 

%install
make install/fast DESTDIR=${RPM_BUILD_ROOT} -C %{_target_platform}

%find_lang %{name}

%files -f %{name}.lang
%doc ChangeLog COPYING TODO
%config(noreplace) %{_kde4_sysconfdir}/dbus-1/system.d/org.kde.wicdclient.scripts.conf
%{_kde4_libdir}/kde4/*
%{_kde4_libexecdir}/wicdclient_scripts_helper
%{_kde4_datadir}/dbus-1/system-services/org.kde.wicdclient.scripts.service
%{_kde4_appsdir}/%{name}
%{_kde4_appsdir}/plasma/services/wicd.operations
%{_datadir}/kde4/services/*
%{_kde4_datadir}/polkit-1/actions/org.kde.wicdclient.scripts.policy

%changelog
* Wed Apr 15 2015 Andrey Cherepanov <cas@altlinux.org> 0.3.1-alt2
- Initial build in Sisyphus from Autoimports

* Tue Sep 16 2014 Igor Vlasenko <viy@altlinux.ru> 0.3.1-alt1_5
- update to new release by fcimport

* Mon Jul 07 2014 Igor Vlasenko <viy@altlinux.ru> 0.3.1-alt1_4
- update to new release by fcimport

* Mon Sep 09 2013 Igor Vlasenko <viy@altlinux.ru> 0.3.1-alt1_3
- update to new release by fcimport

* Fri Feb 15 2013 Igor Vlasenko <viy@altlinux.ru> 0.3.1-alt1_2
- update to new release by fcimport

* Wed Jan 16 2013 Igor Vlasenko <viy@altlinux.ru> 0.3.0-alt1_5
- initial fc import

