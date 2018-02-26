Name: xCAT-nbroot-core
Summary: xCAT-nbroot-core provides opensource components of the netboot image
Version: 2.5.1
Release: alt0.4
License: EPL
Group: System/Servers
Packager: Andriy Stepanov <stanv@altlinux.ru>
BuildArch: noarch

Source1: xcat-nbrootoverlay.tar
Source2: reboot

# Do not find any requirements and providings
%description
xcat-nbroot-core provides the xCAT scripts for the mini-root environment
All files included are as they were downloadable on 4/7/2007

%package x86
AutoReq: false
AutoProv: false
Group: System/Servers
Summary: xCAT-nbroot-core provides opensource components of the netboot image

%description x86
xcat-nbroot-core provides the xCAT scripts for the mini-root environment
for x86 architecture

%package x86_64
AutoReq: false
AutoProv: false
Group: System/Servers
Summary: xCAT-nbroot-core provides opensource components of the netboot image

%description x86_64
xcat-nbroot-core provides the xCAT scripts for the mini-root environment
for x86_64 architecture

%package ppc64
AutoReq: false
AutoProv: false
Group: System/Servers
Summary: xCAT-nbroot-core provides opensource components of the netboot image

%description ppc64
xcat-nbroot-core provides the xCAT scripts for the mini-root environment
for ppc64 architecture

%install
for i in x86 x86_64 ppc64; do
  tdir="%{buildroot}%{_datadir}/xcat/netboot/$i/nbroot"
  install -d -pm 755 "$tdir"
  tar xvf %{SOURCE1} -C "$tdir"
  chmod 755 "$tdir/"{etc/init.d/S40network,bin/getdestiny,bin/getdestiny.awk,bin/getipmi,bin/getipmi.awk}
  cp %{S:2} "$tdir/bin/"
done

%files x86
%{_datadir}/xcat/netboot/x86/nbroot/*

%files x86_64
%{_datadir}/xcat/netboot/x86_64/nbroot/*

%files ppc64
%{_datadir}/xcat/netboot/ppc64/nbroot/*

%changelog
* Wed Nov 24 2010 Andriy Stepanov <stanv@altlinux.ru> 2.5.1-alt0.4
- Update from upstream SVN: trunk@8256.

* Mon Nov 22 2010 Andriy Stepanov <stanv@altlinux.ru> 2.5.1-alt0.3
- Update from upstream SVN: trunk@8225.

* Mon Nov 15 2010 Andriy Stepanov <stanv@altlinux.ru> 2.5.1-alt0.2
- Update from upstream SVN: trunk@8159.

* Thu Oct 28 2010 Andriy Stepanov <stanv@altlinux.ru> 2.5.1-alt0.1
- Update from upstream SVN: trunk@7954.

* Fri Oct 22 2010 Andriy Stepanov <stanv@altlinux.ru> 2.4.4-alt0.4
- Update from upstream SVN: trunk@7904.

* Wed Oct 06 2010 Andriy Stepanov <stanv@altlinux.ru> 2.4.4-alt0.3
- Update from upstream SVN: trunk@7759.

* Fri Sep 17 2010 Andriy Stepanov <stanv@altlinux.ru> 2.4.4-alt0.2
- Update from upstream SVN: trunk@7490.

* Fri Sep 10 2010 Andriy Stepanov <stanv@altlinux.ru> 2.4.4-alt0.1
- Update from upstream SVN: trunk@7385.

* Sun Jun 27 2010 Andriy Stepanov <stanv@altlinux.ru> 2.4.3-alt0.1
- Update from upstream SVN: trunk@6611.

* Mon Jun 21 2010 Andriy Stepanov <stanv@altlinux.ru> 2.4.2-alt0.2
- Update from upstream SVN: trunk@6560.

* Wed Jun 02 2010 Andriy Stepanov <stanv@altlinux.ru> 2.4.2-alt0.1
- Update from upstream SVN: trunk@6312.

* Mon May 24 2010 Andriy Stepanov <stanv@altlinux.ru> 2.3.5-alt0.4
- Update from upstream SVN: trunk@6208.

* Thu Apr 22 2010 Andriy Stepanov <stanv@altlinux.ru> 2.3.5-alt0.3
- Update from upstream SVN: trunk@5831.

* Tue Mar 23 2010 Andriy Stepanov <stanv@altlinux.ru> 2.3.5-alt0.2
- Fixes in nbroot scripts

* Thu Mar 18 2010 Andriy Stepanov <stanv@altlinux.ru> 2.3.5-alt0.1
- Update from upstream SVN: trunk@5517.

* Tue Mar 02 2010 Andriy Stepanov <stanv@altlinux.ru> 2.3.3-alt0.5
- Update from upstream SVN: trunk@5320.

* Fri Feb 05 2010 Andriy Stepanov <stanv@altlinux.ru> 2.3.3-alt0.4
- Update from upstream SVN.

* Thu Jan 21 2010 Andriy Stepanov <stanv@altlinux.ru> 2.3.3-alt0.3
- Update from upstream SVN: trunk@5004.

* Tue Jan 19 2010 Andriy Stepanov <stanv@altlinux.ru> 2.3.3-alt0.2
- Update from upstream SVN: trunk@4978.

* Mon Jan 11 2010 Andriy Stepanov <stanv@altlinux.ru> 2.3.3-alt0.1
- Update from upstream SVN.

* Fri Dec 11 2009 Andriy Stepanov <stanv@altlinux.ru> 2.3.2-alt0.1
- Update from upstream SVN.

* Wed Nov 18 2009 Andriy Stepanov <stanv@altlinux.ru> 2.3-alt0.1
- ALT: initial build

