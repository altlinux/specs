Name: spt-profiles-server
Version: 0.4.10
Release: alt1

Summary: spt profiles for building server
Group: Development/Other
License: GPL
Source: %name-%version-%release.tar
BuildArch: noarch
Packager: Dmitry V. Levin <ldv@altlinux.org>

AutoReq: yes, noshell

%description
This package contains spt profiles for building server.

%prep
%setup -n %name-%version-%release

%install
mkdir -p %buildroot/etc/spt/profiles/server
for d in *; do
	cp -a "$d" %buildroot/etc/spt/profiles/server
done

%files
%config(noreplace) /etc/spt/profiles/*

%changelog
* Thu Aug 09 2007 Dmitry V. Levin <ldv@altlinux.org> 0.4.10-alt1
- Updated to 20070809, see git changelog for details.

* Tue Jul 17 2007 Dmitry V. Levin <ldv@altlinux.org> 0.4.9-alt1
- Updated to 20070717, see git changelog for details.

* Thu May 31 2007 Dmitry V. Levin <ldv@altlinux.org> 0.4.8-alt1
- Updated to 20070531, see git changelog for details.

* Tue May 29 2007 Dmitry V. Levin <ldv@altlinux.org> 0.4.7-alt1
- Updated to 20070529, see git changelog for details.

* Thu May 24 2007 Dmitry V. Levin <ldv@altlinux.org> 0.4.6-alt1
- Updated to 20070524, see git changelog for details.

* Fri May 04 2007 Dmitry V. Levin <ldv@altlinux.org> 0.4.5-alt1
- Updated to 20070504, see git changelog for details.

* Thu May 03 2007 Dmitry V. Levin <ldv@altlinux.org> 0.4.4-alt1
- Updated to 20070503, see git changelog for details.

* Wed May 02 2007 Dmitry V. Levin <ldv@altlinux.org> 0.4.3-alt1
- Updated to 20070502, see git changelog for details.

* Sat Apr 28 2007 Dmitry V. Levin <ldv@altlinux.org> 0.4.2-alt1
- Updated to 20070428, see git changelog for details.

* Wed Apr 25 2007 Dmitry V. Levin <ldv@altlinux.org> 0.4.1-alt1
- Updated to 20070424, see git changelog for details.

* Mon Apr 23 2007 Dmitry V. Levin <ldv@altlinux.org> 0.4-alt1
- Updated to 20070423, see git changelog for details.

* Wed Apr 11 2007 Dmitry V. Levin <ldv@altlinux.org> 0.3-alt1
- Updated to 20070411, see git changelog for details.

* Sat Apr 07 2007 Dmitry V. Levin <ldv@altlinux.org> 0.2.2-alt1
- Updated to 20070406, see git changelog for details.

* Thu Apr 05 2007 Dmitry V. Levin <ldv@altlinux.org> 0.2.1-alt1
- Updated to 20070405, see git changelog for details.

* Fri Mar 30 2007 Dmitry V. Levin <ldv@altlinux.org> 0.2-alt1
- Added rescue image.
- Removed cpp and glx from install2.
- Added packages to RPMS.disk based on feedback in devel@lists.

* Thu Mar 15 2007 Dmitry V. Levin <ldv@altlinux.org> 0.1-alt1
- Initial public release.

* Wed Mar 14 2007 Dmitry V. Levin <ldv@altlinux.org> 0.0.1-alt1
- Initial revision, based on spt-profiles-ovz and spt-profile.
