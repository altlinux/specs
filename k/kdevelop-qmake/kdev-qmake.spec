%define _unpackaged_files_terminate_build 1
%define unstable 0

%if %unstable
%define pkg_sfx -pre4.7
%define pkg_sfx_other %nil
%define if_unstable() %{expand:%*}
%define if_stable() %nil
%else
%define pkg_sfx %nil
%define pkg_sfx_other -pre4.7
%define if_unstable()  %nil
%define if_stable() %{expand:%*}
%endif

%define kdevplatform kdevplatform%{pkg_sfx}
%define kdevplatform_other kdevplatform%{pkg_sfx_other}
%define kdevelop kdevelop%{pkg_sfx}
%define kdevelop_other kdevelop%{pkg_sfx_other}
%define kdevelop_pg_qt kdevelop-pg-qt

%define kdevelop_qmake kdevelop%{pkg_sfx}-qmake
%define kdevelop_qmake_other kdevelop%{pkg_sfx_other}-qmake

%define build_kdevplatform_ver 1.5.0
%define build_kdevelop_ver 4.5.0
%define build_kdev_pg_qt_ver 1.0.0

%define build_kdelibs_ver 4.6.0

Name: %kdevelop_qmake
Version: 1.6.60
Release: alt1.git

Group: Development/Other
Summary: QMake plugin for KDevelop
Url: https://projects.kde.org/projects/playground/devtools/plugins/kdev-qmake
License: GPL

# Drop the old name
Obsoletes: kdevelop-for-qmake

Requires: %kdevelop-mini >= %build_kdevelop_ver

# Deal with two versions stable and unstable
Conflicts: %{kdevelop_qmake_other}
%if_stable Obsoletes: %{kdevelop_qmake_other} < %version-%release

Source: kdev-qmake-%version.tar.gz

BuildRequires: gcc-c++ glibc-devel kde-common-devel
BuildRequires: kde4libs-devel >= %build_kdelibs_ver
BuildRequires: %kdevplatform-devel >= %build_kdevplatform_ver
BuildRequires: %{kdevelop_pg_qt}-devel >= %build_kdev_pg_qt_ver
BuildRequires: %kdevelop-devel >= %build_kdevelop_ver

%description
This is a plugin for KDevelop to support projects which use QMake
build system.

Please note that the plugin is in early development stage and may
break your KDevelop installation

%prep
%setup -q -n kdev-qmake-%version

%build
%K4build

%install
%K4install

# Don't pack devel-files at the moment
rm -f %buildroot%_K4includedir/kdevelop/qmake/iqmakebuilder.h


%files
%_K4libdir/libkdev4qmake*.so
%_K4lib/kdevqmake*.so
%_K4lib/kcm_kdev_qmake*.so
%_K4apps/kdevappwizard/templates/qmake_qt4*
%_K4apps/kdevqmakebuilder
%_K4srv/kdevqmake*.desktop
%_K4srv/kcm_kdev_qmake*.desktop

%changelog
* Tue Jan 13 2015 Alexey Morozov <morozov@altlinux.org> 1.6.60-alt1.git
- build a pre-release git snapshot (ed465bdc41d2abe7cd581b082bce2ebbdb215254)
  for KDevelop-4.7

* Tue Apr 30 2013 Alexey Morozov <morozov@altlinux.org> 1.4.60-alt0.1.git
- Build a pre-release git snapshot (eba41ae94f3b69595c83dc889b79e44a9e2bd23a)
  for KDevelop-4.5

* Mon Oct 15 2012 Alexey Morozov <morozov@altlinux.org> 1.3.60-alt0.2.git
- New git snapshot (828d773b49bde7646bd9dbdcb50c253f3bb65029)

* Thu Apr 05 2012 Alexey Morozov <morozov@altlinux.org> 1.3.60-alt0.1.git
- a build for an unstable version of KDevelop (pre4.4), git
  snapshot 6f33b8321debc2e09e1e0079046a7f3859fafcfe

* Thu Apr 05 2012 Alexey Morozov <morozov@altlinux.org> 0.1.13-alt1.git
- a build for released KDevelop-4.3.0
- new build of git snapshot (8fac6ac38d4aa24844c45041239fcdb1f87d4be0)
- slightly changed versioning. The version from master already has
  proper versioning (1.3.x) but branch suitable for upcoming 1.3
  kdevplatform still uses 0.1 as "public" version and 13 as internal one.

* Sun Jan 29 2012 Alexey Morozov <morozov@altlinux.org> 0.1-alt0.2.git
- rebuild against fresh kdevelop & Co builds

* Mon Dec 12 2011 Alexey Morozov <morozov@altlinux.org> 0.1-alt0.1.git
- initial build (git snapshot 36da72774d595ec6eab364d2935d75b17ab0ccc2)

