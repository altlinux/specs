Name: xmount
Version: 0.7.6
Release: alt2
Summary: A on-the-fly convert for multiple hard disk image types

Group: Archiving/Other
License: GPLv3+
Url: https://www.pinguin.lu/index.php
Packager: Artyom Bystrov <arbars@altlinux.org>

Source: %name-%version.tar.gz
Patch0: xmount-suffix.patch
Patch1: xmount-cflags.patch

BuildRequires: gcc-c++
BuildRequires: libfuse-devel
BuildRequires: libewf-devel
BuildRequires: libaff-devel
BuildRequires: zlib-devel
BuildRequires: ctest cmake

%description
xmount allows you to convert on-the-fly between multiple input
and output hard disk image types. xmount creates a virtual file
system using FUSE (Filesystem in Userspace) that contains a virtual
representation of the input image. The virtual representation can
be in raw DD, VirtualBox's virtual disk file format or in VmWare's
VMDK file format. Input images can be raw DD, EWF (Expert Witness
Compression Format) or AFF (Advanced Forensic Format) files. In
addition, xmount also supports virtual write access to the output
files that is redirected to a cache file. This makes it possible
to boot acquired hard disk images using QEMU, KVM, VirtualBox,
VmWare, or alike.

%prep -n %name-%version
%setup
%patch0 -p1
%patch1 -p1

# Fix perm
chmod -x src/xmount.*

%build

%cmake \
    -DCMAKE_BUILD_TYPE=Release \
    -DCMAKE_SKIP_RPATH=ON \
    ..

cd BUILD
%make_build

%install
cd BUILD
%makeinstall_std

%files
%doc AUTHORS ChangeLog NEWS README ROADMAP TODO COPYING
%_mandir/man*/%name.*
%_bindir/%name
%_libdir/xmount


%changelog
* Fri Nov 15 2019 Artyom Bystrov <arbars@altlinux.org> 0.7.6-alt2
- initial build for ALT Sisyphus

* Tue Aug 06 2019 Igor Vlasenko <viy@altlinux.ru> 0.7.6-alt1_5
- update to new release by fcimport

* Fri Mar 01 2019 Igor Vlasenko <viy@altlinux.ru> 0.7.6-alt1_4
- update to new release by fcimport

* Sun Sep 02 2018 Igor Vlasenko <viy@altlinux.ru> 0.7.6-alt1_3
- update to new release by fcimport

* Mon Sep 09 2013 Igor Vlasenko <viy@altlinux.ru> 0.5.0-alt1_5
- update to new release by fcimport

* Thu Mar 14 2013 Igor Vlasenko <viy@altlinux.ru> 0.5.0-alt1_4
- update to new release by fcimport

* Wed Feb 27 2013 Igor Vlasenko <viy@altlinux.ru> 0.5.0-alt1_3
- update to new release by fcimport

* Wed Jan 16 2013 Igor Vlasenko <viy@altlinux.ru> 0.5.0-alt1_2
- initial fc import
