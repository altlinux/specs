# BEGIN SourceDeps(oneline):
BuildRequires: libarchive-devel
# END SourceDeps(oneline)
Name:           asa
Version:        1.2
Release:        alt1_10
Summary:        Convert Fortran carriage control characters

Group:          Development/Tools
License:        GPLv2+
# version 1.1 is at that url.
URL:            http://www.ibiblio.org/pub/Linux/devel/lang/fortran/!INDEX.short.html
Source0:        http://archive.debian.org/debian-archive/dists/slink/main/source/text/asa_1.2.orig.tar.gz
Patch0:         asa-1.2-declare.patch
Source44: import.info

%description

A POSIX.2 compliant asa(1), for converting Fortran carriage control
characters to line printer control characters.


%prep
%setup -q
%patch0 -p1 -b .declare


%build
make %{?_smp_mflags} CFLAGS="$RPM_OPT_FLAGS" LDFLAGS="$RPM_OPT_FLAGS"


%install

%{__install} -d -m755 $RPM_BUILD_ROOT%{_bindir}/
%{__install} -d -m755 $RPM_BUILD_ROOT%{_mandir}/man1
%{__install} -m755 asa $RPM_BUILD_ROOT%{_bindir}/
%{__install} -m644 -p asa.1 $RPM_BUILD_ROOT%{_mandir}/man1/ 

%files
%doc README COPYING asa-example.doc
%{_bindir}/asa
%{_mandir}/*/asa*


%changelog
* Wed Feb 01 2012 Igor Vlasenko <viy@altlinux.ru> 1.2-alt1_10
- update to new release by fcimport

* Thu Jun 09 2011 Igor Vlasenko <viy@altlinux.ru> 1.2-alt1_9
- converted from Fedora by srpmconvert script

