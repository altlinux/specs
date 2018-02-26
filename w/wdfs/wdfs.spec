Name: wdfs
Version: 1.4.2
Release: alt1

Summary: WebDAV File System

License: GPLv2+
Group: File tools
Url: http://noedler.de/projekte/wdfs/

Packager: Ilya Shpigor <elly@altlinux.org>

Source: http://noedler.de/projekte/wdfs/wdfs-%version.tar.gz

# Automatically added by buildreq on Wed Jan 20 2010
BuildRequires: glib2-devel libfuse-devel libneon-devel
Patch: wdfs-1.4.2-as-needed.patch

%description
wdfs is a WebDAV filesystem that makes it possible to mount a WebDAV share
under Linux.  wdfs has some special features for accessing subversion
repositiories via WebDAV.

%prep
%setup -q
%patch0 -p1 -b .as-needed

%build
%configure
%make_build

%install
%makeinstall_std

%files
%doc AUTHORS COPYING README TODO
%_bindir/wdfs

%changelog
* Wed Jan 20 2010 Ilya Shpigor <elly@altlinux.org> 1.4.2-alt1
- initial build for ALT Linux Sisyphus

* Thu Sep 17 2009 Peter Lemenkov <lemenkov@gmail.com> - 1.4.2-9
* Mon Jul 27 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4.2-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Mon Feb 18 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 1.4.2-6
- Autorebuild for GCC 4.3

* Tue Jan 22 2008 Adam Jackson <ajax@redhat.com> 1.4.2-5
- Fix License tag. (#428962)

* Mon Sep 24 2007 Adam Jackson <ajax@redhat.com> 1.4.2-4
- Fix spelling error in URL. (#302731)

* Thu Aug 23 2007 Joe Orton <jorton@redhat.com> 1.4.2-3
- rebuild for neon 0.27

* Tue Aug 21 2007 Adam Jackson <ajax@redhat.com> - 1.4.2-2
- Rebuild for build id

* Tue Jun 05 2007 Adam Jackson <ajax@redhat.com> 1.4.2-1
- Initial version.
