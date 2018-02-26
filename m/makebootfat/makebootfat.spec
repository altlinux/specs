Summary: Utility for creation bootable FAT disk
Name: makebootfat
Version: 1.4
Release: alt1
Group: 	System/Kernel and hardware
License: %gpl2plus
URL: http://advancemame.sourceforge.net/doc-makebootfat.html

Source0: http://dl.sourceforge.net/sourceforge/advancemame/%{name}-%{version}.tar.gz
## from syslinux-3.86
Source2: ldlinux.bss
Source3: ldlinux.sys

BuildPreReq: rpm-build-licenses

%description
This utility creates a bootable FAT filesystem and populates it
with files and boot tools.

It was mainly designed to create bootable USB and Fixed disk
for the AdvanceCD project (http://advancemame.sourceforge.net), but
can be successfully used separately for any purposes.


%prep
%setup -q

%build
%configure
%make_build

%install
%makeinstall

install -d $RPM_BUILD_ROOT%{_libdir}/%{name}/x86
install -p -m644 mbrfat.bin $RPM_BUILD_ROOT%{_libdir}/%{name}/x86

install -p -m644 %{SOURCE2} $RPM_BUILD_ROOT%{_libdir}/%{name}/x86
install -p -m644 %{SOURCE3} $RPM_BUILD_ROOT%{_libdir}/%{name}/x86

%files
%defattr(-,root,root)
%doc AUTHORS COPYING HISTORY README
%{_bindir}/*
%{_libdir}/%{name}
%{_mandir}/*/*


%changelog
* Thu May 27 2010 Mykola Grechukh <gns@altlinux.ru> 1.4-alt1
- initial build for ALT Linux

* Sat Jul 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Mon Feb 18 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 1.4-7
- Autorebuild for GCC 4.3

* Thu Sep 27 2007 Dmitry Butskoy <Dmitry@Butskoy.name> - 1.4-6
- always distribute own ldlinux.sys as well as ldlinux.bss
- add conditional macro %%{new_ldlinux} (default off) to build the package
  with ldlinux.bss and ldlinux.sys taken from some syslinux source directly.
- Update README.usbboot .

* Fri Aug 17 2007 Dmitry Butskoy <Dmitry@Butskoy.name>
- Change License tag to GPLv2+

* Fri Sep  1 2006 Dmitry Butskoy <Dmitry@Butskoy.name> - 1.4-5
- rebuild for FC6

* Tue Aug  1 2006 Dmitry Butskoy <Dmitry@Butskoy.name> - 1.4-4
- avoid world-writable docs (#200829)

* Wed Feb 15 2006 Dmitry Butskoy <Dmitry@Butskoy.name> - 1.4-3
- rebuild for FC5

* Mon Dec 26 2005 Dmitry Butskoy <Dmitry@Butskoy.name> - 1.4-2
- place mbrfat.bin and ldlinux.bss under %%{_datadir}/%%{name}/x86

* Mon Dec 24 2005 Dmitry Butskoy <Dmitry@Butskoy.name> - 1.4-1
- accepted for Fedora Extra (review by John Mahowald <jpmahowald@gmail.com>)

* Mon Oct  3 2005 Dmitry Butskoy <Dmitry@Butskoy.name> - 1.4-1
- initial release
- install mbrfat.bin and ldlinux.bss binary files, they are
  actually needed to create something useful here.
- add README.usbboot -- instruction how to make diskboot.img more helpful
  (written by me).

