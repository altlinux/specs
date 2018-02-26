Name: scim-fcitx
Version: 3.1.1
Release: alt1
Summary: FCITX Input Method Engine for SCIM

Group: System/Libraries
License: GPLv2+
Url: http://www.scim-im.org/projects/imengines/
Packager: Ilya Mashkin <oddity@altlinux.ru>
Source0: http://dl.sourceforge.net/scim/%name.%version.tar.bz2

BuildRequires: scim-devel gcc-c++
Requires: scim

Patch0: scim-fcitx-3.1.1-gcc43.patch

%description
scim-fcitx is a port of the fcitx Chinese input method for the SCIM input
method platform.  It provides Wubi, Erbi, Cangjie, and Pinyin styles of input.

%package tools
Summary: Fcitx tables tools
Group: Development/Other

%description tools
This package contains input table tools from fcitx.

%prep
%setup -q -n fcitx
%patch0 -p1 -b .1-gcc43

%build
%configure --disable-static
# doesn't build with %{?_smp_mflags}
make

%install
make DESTDIR=$RPM_BUILD_ROOT install

rm $RPM_BUILD_ROOT/%_libdir/scim-1.0/*/IMEngine/fcitx.la

%files
%doc AUTHORS COPYING README ChangeLog
%_libdir/scim-1.0/*/IMEngine/fcitx.so
%_datadir/scim/fcitx
%_datadir/scim/icons/fcitx

%files tools
%_bindir/*

%changelog
* Tue Dec 21 2010 Ilya Mashkin <oddity@altlinux.ru> 3.1.1-alt1
- Build for ALT Linux

* Fri Feb 29 2008 Huang Peng <phuang@redhat.com> - 3.1.1-9
- Fix build  error with GCC 4.3

* Tue Feb 19 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 3.1.1-8
- Autorebuild for GCC 4.3

* Mon Sep 24 2007 Jens Petersen <petersen@redhat.com> - 3.1.1-7
- update license field to GPLv2+
- remove with_libstdc_preview macro

* Wed Sep 27 2006 Jens Petersen <petersen@redhat.com> - 3.1.1-6
- rebuild for FE6

* Tue Apr  4 2006 Jens Petersen <petersen@redhat.com> - 3.1.1-5.fc6
- rebuild without libstdc++so7

* Thu Mar  2 2006 Jens Petersen <petersen@redhat.com> - 3.1.1-4.fc5
- rebuild for FE5

* Mon Feb 13 2006 Jens Petersen <petersen@redhat.com> - 3.1.1-3
- build conditionally with libstdc++so7 preview library (#166041)
  - add with_libstdc_preview switch and tweak libtool to link against it
- update filelist since moduledir is now api-versioned

* Tue Dec 20 2005 Jens Petersen <petersen@redhat.com> - 3.1.1-2
- package cleanup (John Mahowald)

* Wed Oct  5 2005 Jens Petersen <petersen@redhat.com> - 3.1.1-1
- initial packaging for Fedora Extras.

* Mon Jun 20 2005 Jens Petersen <petersen@redhat.com>
- rebuild against scim-1.3.1

* Tue Jun 14 2005 Jens Petersen <petersen@redhat.com>
- initial build

* Thu May  5 2005 Haojun Bao <baohaojun@yahoo.com>
- first release of scim-fcitx.
