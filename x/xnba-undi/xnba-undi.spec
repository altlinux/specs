Name: xnba-undi
Summary: xCAT Network Boot Agent for x86 PXE hosts
Version: 1.0.2
Release: alt0.1
License: GPL
Group: System/Servers
Packager: Andriy Stepanov <stanv@altlinux.ru>
URL: http://ipxe.org/
BuildArch: noarch

%define tftpdir %{_localstatedir}/tftpboot
%define xcatdir %{tftpdir}/xcat

Source0: ipxe.tar

Patch0: ipxe-branding.patch
Patch1: ipxe-registersan.patch
Patch2: ipxe-config.patch
Patch3: ipxe-droppackets.patch
Patch4: ipxe-xnbaclass.patch
Patch5: ipxe-undinetchange.patch
Patch6: ipxe-expandfilename.patch
Patch7: ipxe-cmdlinesize.patch
Patch8: ipxe-machyp.patch

%description
The xCAT Network Boot Agent is a slightly modified version of ipxe.
It provides enhanced boot features for any UNDI compliant x86 host.
This includes iSCSI, http/ftp downloads, and gPXE script based booting.

%prep

%setup  -n ipxe
%patch -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1
%patch6 -p1
%patch7 -p1
%patch8 -p1

%build

cd src
make NO_WERROR=1 bin/undionly.kkpxe

%install

mkdir -p  %{buildroot}/%{xcatdir}
#Rename to avoid conflicting with potential vanilla undionly.kpxe that user may be using
cp src/bin/undionly.kkpxe %{buildroot}/%{xcatdir}/xnba.kpxe

%files
%{xcatdir}/xnba.kpxe

%changelog
* Mon Nov 22 2010 Andriy Stepanov <stanv@altlinux.ru> 1.0.2-alt0.1
- Update from upstream SVN: trunk@8157

* Mon Sep 20 2010 Andriy Stepanov <stanv@altlinux.ru> 1.0.1-alt0.1
- Update from upstream SVN: trunk@7494

* Mon Jun 21 2010 Andriy Stepanov <stanv@altlinux.ru> 1.0.0-alt0.6
- Update from upstream SVN: trunk@6558

* Tue May 25 2010 Andriy Stepanov <stanv@altlinux.ru> 1.0.0-alt0.5
- Update from upstream SVN: trunk@6210

* Fri Apr 23 2010 Andriy Stepanov <stanv@altlinux.ru> 1.0.0-alt0.4
- Update from upstream SVN: trunk@5766

* Mon Mar 15 2010 Andriy Stepanov <stanv@altlinux.ru> 1.0.0-alt0.3
- rebuild

* Mon Mar 01 2010 Andriy Stepanov <stanv@altlinux.ru> 1.0.0-alt0.2
- Add hdboot patch

* Thu Feb 11 2010 Andriy Stepanov <stanv@altlinux.ru> 1.0.0-alt0.1
- Go away from root tree using

* Tue Nov 17 2009 Andriy Stepanov <stanv@altlinux.ru> 0.9.7-alt0.1
- ALT: initial build

