%define _unpackaged_files_terminate_build 1
%define soname 1

Name: libhangul
Version: 0.2.0
Release: alt1

License: LGPLv2+
Url: https://github.com/libhangul/libhangul
Vcs: https://github.com/libhangul/libhangul

Source:  %name-%version.tar.gz

BuildRequires: chrpath

Summary: Hangul input library
Group:   System/Libraries
%description
libhangul provides common features for Hangul input method programs.

%package devel
Summary: Development files for libhangul
Group:   Development/Other
Requires: pkgconfig
%description devel
This package contains development files necessary to develop programs
providing Hangul input.

%package -n %name%soname
Group: System/Libraries
Summary: %name library
%description -n %name%soname
%name library.

%prep
%setup
#created missing file
touch ChangeLog

%build
%autoreconf
%configure --disable-static

make %{?_smp_mflags}

%install
%makeinstall_std

rm %buildroot%_libdir/%name.la
chrpath -d %buildroot%_bindir/hangul

%find_lang %name

%files -f %name.lang
%doc AUTHORS COPYING ChangeLog NEWS README
%_bindir/hangul
%_datadir/%name

%files -n %name%soname
%_libdir/%name.so.%soname
%_libdir/%name.so.%{soname}.*

%files devel
%_includedir/hangul-*
%_libdir/pkgconfig/*.pc
%_libdir/*.so

%changelog
* Tue Nov 03 2026 Aleksandr Shamaraev <shad@altlinux.org> 0.2.0-alt1
- 0.1.0 -> 0.2.0
- changed URL && VCS
- builded in accordance with SharedLibsPolicy

* Fri May 30 2014 Andrey Cherepanov <cas@altlinux.org> 0.1.0-alt1
- New version
- Disable hardcoded rpath with standard library path
- Package hangul utility and localization

* Sun Apr 14 2013 Dmitry V. Levin (QA) <qa_ldv@altlinux.org> 0.0.11-alt1.qa1
- NMU: rebuilt for debuginfo.

* Sun Jan 02 2011 Ilya Mashkin <oddity@altlinux.ru> 0.0.11-alt1
- Build for ALT Linux

* Mon Oct  4 2010 Daiki Ueno <dueno@redhat.com> - 0.0.11-1
- update to 0.0.11

* Thu Dec 10 2009 Jens Petersen <petersen@redhat.com> - 0.0.10-1
- update to 0.0.10
- drop buildroot field and removal

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.0.9-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Jun 10 2009 Jens Petersen <petersen@redhat.com> - 0.0.9-1
- update to 0.0.9 (fixes #501212)
- hanjac and hanja.txt are gone

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.0.8-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Tue Oct 28 2008 Jens Petersen <petersen@redhat.com> - 0.0.8-2
- add hanjac and hanja.bin to filelists

* Tue Oct 28 2008 Jens Petersen <petersen@redhat.com> - 0.0.8-1
- update to 0.0.8 (#468817)

* Wed Aug  6 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 0.0.6-5
- fix license tag

* Wed Feb 20 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 0.0.6-4
- Autorebuild for GCC 4.3

* Tue Aug 28 2007 Fedora Release Engineering <rel-eng at fedoraproject dot org> - 0.0.6-3
- Rebuild for selinux ppc32 issue.

* Wed Jul 25 2007 Jesse Keating <jkeating@redhat.com> - 0.0.6-2
- Rebuild for RH #249435

*Tue Jul 24 2007 Hu Zheng <zhu@redhat.com> - 0.0.6-1
- New upstream release.

* Mon Feb 19 2007 Akira TAGOH <tagoh@redhat.com> - 0.0.4-2
- Better descriptions.

* Fri Feb 16 2007 Akira TAGOH <tagoh@redhat.com> - 0.0.4-1
- New upstream release.
- cleanup spec.

* Wed Nov 29 2006 Akira TAGOH <tagoh@redhat.com> - 0.0.3-1
- Initial package.

