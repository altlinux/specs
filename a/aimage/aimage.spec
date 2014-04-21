Name: aimage
Version: 3.2.5
Release: alt3

Summary: Advanced Disk Imager
License: BSD with advertising
Group: File tools

# afflib.org unavailable
Url: http://www.forensicswiki.org/wiki/Aimage
Packager: Michael Shigorin <mike@altlinux.org>

Source: http://www.afflib.org/downloads/aimage-%version.tar.gz

# Automatically added by buildreq on Sat Apr 19 2014
# optimized out: libcloog-isl4 libssl-devel libstdc++-devel libtinfo-devel
BuildRequires: gcc-c++ libaff-devel libexpat-devel libncurses-devel libreadline-devel zlib-devel

%description
Advanced Disk Imager.

NB: it's been obsoleted by guymager,
    at least when GUI is acceptable.

%prep
%setup

%build
%configure
%make_build

%install
%makeinstall_std

%files
%doc ChangeLog
%_bindir/aimage

%changelog
* Mon Apr 21 2014 Michael Shigorin <mike@altlinux.org> 3.2.5-alt3
- bumped Release: to look newer than autoimports package

* Sat Apr 19 2014 Michael Shigorin <mike@altlinux.org> 3.2.5-alt1
- initial build for ALT Linux Sisyphus (based on fedora package)

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.2.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Jul 18 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.2.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Mon Mar 26 2012 Peter Robinson <pbrobinson@fedoraproject.org> - 3.2.5-1
- Update to 3.2.5

* Thu Jan 12 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.2.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Mon Feb 07 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.2.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Fri Nov 27 2009 Nicolas Chauvet <kwizart@fedoraproject.org> - 3.2.4-1
- Update to 3.2.4

* Sun Nov 22 2009 Nicolas Chauvet <kwizart@fedoraproject.org> - 3.2.3-1
- Update to 3.2.3
- Remove upstreamed patch

* Wed Sep  2 2009 kwizart < kwizart at gmail.com > - 3.2.1-1
- Update to 3.2.1
- Update gcc44 patch

* Fri Aug 21 2009 Tomas Mraz <tmraz@redhat.com> - 3.2.0-6
- rebuilt with new openssl

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.2.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Mon Mar  2 2009 kwizart < kwizart at gmail.com > - 3.2.0-4
- Fix for gcc44

* Mon Feb 23 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.2.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Thu Jan 15 2009 Tomas Mraz <tmraz@redhat.com> - 3.2.0-2
- rebuild with new openssl

* Tue Sep 23 2008 kwizart < kwizart at gmail.com > - 3.2.0-1
- Update to 3.2.0

* Thu Sep  4 2008 kwizart < kwizart at gmail.com > - 3.1.2-1
- Update to 3.1.2

* Wed Mar 12 2008 kwizart < kwizart at gmail.com > - 3.1.0-1
- Initial spec file
