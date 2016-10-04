%define vala_api 0.34

Name: xfce4-vala
Version: 4.10.0
Release: alt8

Summary: Vala bindings for the Xfce framework
License: %lgpl2only
Group: Development/Other
URL: http://xfce.org/
Packager: Xfce Team <xfce@packages.altlinux.org>

# git://git.xfce.org/bindings/xfce4-vala
Source: %name-%version.tar
Patch: %name-%version-%release.patch

BuildRequires(pre): rpm-build-licenses

BuildPreReq: rpm-build-xfce4 >= 0.1.0 xfce4-dev-tools
BuildRequires: libxfce4util-devel libgarcon-devel libxfconf-devel libxfce4ui-devel
BuildRequires: libxfce4panel-devel libexo-devel
BuildRequires: libvala-devel

Requires: libxfce4util-devel libgarcon-devel libxfconf-devel libxfce4ui-devel
Requires: libxfce4panel-devel libexo-devel

%define _unpackaged_files_terminate_build 1

%description
%name offers Vala bindings to Xfce

%prep
%setup
%patch -p1

%xfce4reconf
%configure \
	--with-vala-api=%vala_api
%make_build

%install
%makeinstall_std

%files
%doc AUTHORS NEWS README
%_pkgconfigdir/*.pc
/usr/share/vala-%vala_api/vapi/*

%changelog
* Tue Oct 04 2016 Mikhail Efremov <sem@altlinux.org> 4.10.0-alt8
- Rebuild with vala-0.34.

* Mon Apr 04 2016 Mikhail Efremov <sem@altlinux.org> 4.10.0-alt7
- Rebuild with vala-0.32.

* Tue Sep 29 2015 Mikhail Efremov <sem@altlinux.org> 4.10.0-alt6
- Rebuild with vala-0.30.

* Mon Apr 20 2015 Mikhail Efremov <sem@altlinux.org> 4.10.0-alt5
- Rebuild with vala-0.28.

* Mon Nov 10 2014 Mikhail Efremov <sem@altlinux.org> 4.10.0-alt4
- Rebuild with vala-0.26.

* Fri Apr 04 2014 Mikhail Efremov <sem@altlinux.org> 4.10.0-alt3
- Fix Xfce name (XFCE -> Xfce).
- Rebuild with vala-0.24.

* Thu Oct 03 2013 Mikhail Efremov <sem@altlinux.org> 4.10.0-alt2
- Rebuild with vala-0.22.

* Thu Jul 25 2013 Mikhail Efremov <sem@altlinux.org> 4.10.0-alt1
- Updated from upstream git (6d0ef92197b9).
- Initial build.

