Name: afuse
Summary: An automounter implemented with FUSE
Version: 0.2
Release: alt1
License: GPLv2+
Group: System/Kernel and hardware
Packager: Mykola Grechukh <gns@altlinux.ru>

Source: http://downloads.sourceforge.net/afuse/%name-%version.tar.gz
Url: http://afuse.sourceforge.net/

BuildRequires: libfuse-devel
# fix CVE-2008-2232
Patch: afuse-template-tokenize.patch

%description
Afuse is an automounting file system implemented in user-space using FUSE.
Afuse currently implements the most basic functionality that can be expected
by an automounter; that is it manages a directory of virtual directories. If
one of these virtual directories is accessed and is not already automounted,
afuse will attempt to mount a filesystem onto that directory. If the mount
succeeds the requested access proceeds as normal, otherwise it will fail
with an error.

%prep
%setup
%patch0 -p1 -b .CVS-2008-2232

%build
%configure
%make_build

%install

%makeinstall_std




%files
%doc AUTHORS ChangeLog COPYING README
%_bindir/afuse

%changelog
* Wed May 25 2011 Mykola Grechukh <gns@altlinux.ru> 0.2-alt1
- initial build for ALT Linux Sisyphus

* Mon Feb 07 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Thu Sep 17 2009 Peter Lemenkov <lemenkov@gmail.com> - 0.2-5
- Rebuilt with new fuse

* Mon Aug 17 2009 Tom "spot" Callaway <tcallawa@redhat.com> - 0.2-4
- fix CVS-2008-2232

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Mon Feb 23 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Fri Nov 21 2008 Tom "spot" Callaway <tcallawa@redhat.com> 0.2-1
- Initial package for Fedora
