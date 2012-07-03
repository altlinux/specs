Packager: Repocop Q. A. Robot <repocop@altlinux.org>
%def_enable shared
%def_enable static

%define _name linux-udf
%define prerel %nil
%define cvsdate 20080518

Name: udftools
Version: 1.0.0
Release: alt2.1
Summary: Tools for work with UDF filesystems and CD-R(W)/DVD packet writing drives
Group: Archiving/Cd burning
License: %gpl2plus
Url: http://%_name.sourceforge.net
%ifdef cvsdate
Source: %name-cvs-%cvsdate.tar
%else
Source: %name-%version%prerel.tar
%endif
Patch: %name-cvs-20080518-shared.patch

BuildRequires: libncurses-devel libreadline-devel
BuildRequires: rpm-build-licenses

%description
%name includes:
- mkudffs is a tool to create a UDF(Universal Disk Format) filesystem
  on a device.
- pktsetup to associate packet devices with CD or DVD block devices, so
  that the packet device can then be mounted and potentially used as a
  read/write filesystem. This requires kernel support for the packet
  device, and the UDF filesystem.
- cdwrtool tool that can perform certain actions on a CD-R, CD-RW, or
  DVD-R device. Mainly these are blanking the media, formating it for
  use with the packet-cd device, and applying an UDF filesystem.
- wrudf to maintain a UDF filesystem


%prep
%ifdef cvsdate
%setup -n %name-cvs-%cvsdate
%else
%setup -n %name-%version%prerel
%endif
%patch -p1


%build
%autoreconf
%configure %{subst_enable shared} %{subst_enable static}
%make_build


%install
%make_install DESTDIR=%buildroot install


%files
%doc AUTHORS
%_bindir/*
%_man1dir/*
%_man8dir/*
%{?_enable_shared:%_libdir/*.so.*}


%changelog
* Mon Nov 02 2009 Igor Vlasenko <viy@altlinux.ru> 1.0.0-alt2.1
- NMU (by repocop): the following fixes applied:
  * post_ldconfig for udftools
  * postun_ldconfig for udftools

* Mon May 19 2008 Led <led@altlinux.ru> 1.0.0-alt2
- update from CVS
- removed:
  + %name-wrudf-gcc4.patch (fixed in upstream)
  + %name-1.0.0b3.patch (fixed in upstream)
- added %name-cvs-20080518-shared.patch
- cleaned up spec
- removed init script

* Thu Dec 14 2006 L.A. Kostis <lakostis@altlinux.ru> 1.0.0-alt1.7b3cvs20040826
- remove obsoleted check_kernel from init script.
- cleanup buildrequires.

* Fri Dec 30 2005 ALT QA Team Robot <qa-robot@altlinux.org> 1.0.0-alt1.6b3cvs20040826.1
- Rebuilt with libreadline.so.5.

* Thu Aug 11 2005 LAKostis <lakostis at altlinux.ru> 1.0.0-alt1.6b3cvs20040826
- add missing vars to init script.

* Sat Aug 06 2005 LAKostis <lakostis at altlinux.ru> 1.0.0-alt1.5b3cvs20040826
- more init script rework.

* Fri Aug 05 2005 LAKostis <lakostis at altlinux dot ru> 1.0.0-alt1.4b3cvs20040826
- small init script corrections.
- remove bogus buildreq to gcc-g77.

* Sun Jan 23 2005 LAKostis <lakostis at altlinux dot ru> 1.0.0-alt1.3b3cvs20040826
- add patches from debian (for gcc4.0 compat).
- add init script for automatic setup packet devices 
  (idea & code from debian udftools package).
- adjust udftools.default for proper node names.
- changed group to Archiving/Cd burning cause it more realistic.

* Sun Aug 26 2004 LAKostis <lakostis at altlinux dot ru> 1.0.0-alt0.3b3cvs20040826
- update from cvs.

* Sun Aug 15 2004 LAKostis <lakostis at altlinux dot ru> 1.0.0-alt0.3b3cvs20031102
- update pktsetup.

* Tue Dec 16 2003 Yuri N. Sedunov <aris@altlinux.ru> 1.0.0-alt0.2b3cvs20031102
- /etc/modutils.d/udf added.

* Mon Nov 03 2003 Yuri N. Sedunov <aris@altlinux.ru> 1.0.0-alt0.1b3cvs20031102
- First build for Sisyphus.
- try build cvs snapshot, not release that is too old.
