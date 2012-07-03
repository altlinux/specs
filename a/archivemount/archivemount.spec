Name:          archivemount
Version:       0.6.1
Release:       alt2_8
Summary:       FUSE based filesystem for mounting compressed archives

Group:         System/Libraries
License:       LGPLv2+
URL:           http://www.cybernoia.de/software/archivemount/
Source0:       http://www.cybernoia.de/software/archivemount/%{name}-%{version}.tar.gz
Patch0:        archivemount_force-single-threaded.patch
Patch1:        fix-debuginfo.patch

Requires:      fuse
BuildRequires: libfuse-devel
BuildRequires: libarchive-devel
Source44: import.info

%description
Archivemount is a piece of glue code between libarchive and FUSE. It can be
used to mount a (possibly compressed) archive (as in .tar.gz or .tar.bz2)
and use it like an ordinary filesystem.

%prep
%setup -q
%patch0 -p1 -b .single-threaded
%patch1 -p1 -b .fix-debuginfo

%build
%configure
make %{?_smp_mflags}

%install
rm -f archivemount.1
make install DESTDIR=$RPM_BUILD_ROOT

%files
%doc CHANGELOG COPYING README
%{_mandir}/*/*
%{_bindir}/archivemount

%changelog
* Wed Mar 21 2012 Igor Vlasenko <viy@altlinux.ru> 0.6.1-alt2_8
- rebuild to get rid of #27020

* Wed Feb 01 2012 Igor Vlasenko <viy@altlinux.ru> 0.6.1-alt1_8
- update to new release by fcimport

* Wed Jan 11 2012 Igor Vlasenko <viy@altlinux.ru> 0.6.1-alt1_7
- update to new release by fcimport

* Fri Nov 25 2011 Igor Vlasenko <viy@altlinux.ru> 0.6.1-alt1_6
- update to new release by fcimport

* Fri Jul 08 2011 Igor Vlasenko <viy@altlinux.ru> 0.6.1-alt1_5
- initial release by fcimport

