# BEGIN SourceDeps(oneline):
BuildRequires: gcc-c++
# END SourceDeps(oneline)
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
Name:           zzuf
Version:        0.15
Release:        alt1_4
Summary:        Transparent application input fuzzer

Group:          Development/Tools
License:        WTFPL
URL:            http://sam.zoy.org/zzuf/
Source0:        http://github.com/zzuf/%{name}/archive/zzuf-%{version}.tar.gz
#Source0:	http://ftp.debian.org/debian/pool/main/z/zzuf/zzuf_0.13.svn20100215.orig.tar.gz
Patch0:         %{name}-0.13-optflags.patch
# AC_TRY_CFLAGS doesn't honor CFLAGS
# Causes package to produce broken configure results
Patch1:         %{name}-0.13-Remove-AC_TRY_CFLAGS.patch
Source44: import.info

%description
zzuf is a transparent application input fuzzer.  It works by
intercepting file operations and changing random bits in the program's
input.  zzuf's behaviour is deterministic, making it easy to reproduce
bugs.


%prep
%setup -q
%patch0 -p0
%patch1 -p1
touch -r aclocal.m4 configure.*


%build
%configure --disable-dependency-tracking --disable-static
%make_build


%install
make install DESTDIR=$RPM_BUILD_ROOT
rm $RPM_BUILD_ROOT%{_libdir}/zzuf/libzzuf.la



%files
%doc AUTHORS TODO doc/
%doc COPYING
%{_bindir}/zzuf
%{_bindir}/zzat
%dir %{_libdir}/zzuf/
%{_libdir}/zzuf/libzzuf.so
%{_mandir}/man1/zzuf.1*
%{_mandir}/man1/zzat.1*
%{_mandir}/man3/libzzuf.3*


%changelog
* Tue Nov 14 2017 Igor Vlasenko <viy@altlinux.ru> 0.15-alt1_4
- NMU (for oddity@): new version by fcimport

* Sun Mar 30 2014 Ilya Mashkin <oddity@altlinux.ru> 0.13-alt1
- 0.13

* Mon Apr 15 2013 Dmitry V. Levin (QA) <qa_ldv@altlinux.org> 0.12-alt1.qa1
- NMU: rebuilt for debuginfo.

* Thu Aug 14 2008 Pavlov Konstantin <thresh@altlinux.ru> 0.12-alt1
- 0.12 release.

* Tue Nov 06 2007 Pavlov Konstantin <thresh@altlinux.ru> 0.10-alt1
- 0.10 release.

* Wed Aug 22 2007 Pavlov Konstantin <thresh@altlinux.ru> 0.9-alt1
- 0.9 release.

* Sat Mar 31 2007 Pavlov Konstantin <thresh@altlinux.ru> 0.8.1-alt1
- 0.8.1 release.

* Fri Feb 23 2007 Pavlov Konstantin <thresh@altlinux.ru> 0.7-alt1
- Initial build for Sisyphus.

