Name: dvdbackup
Version: 0.4.2
Release: alt1

Summary: DVD-copy tool
License: GPL
#Group: Video
Group:		Archiving/Cd burning
Packager:	Vlasenko Igor <viy@altlinux.ru>
URL:		http://dvdbackup.sourceforge.net
Source0:	%{name}-%{version}.tar
Source1:	http://ftp.debian.org/debian/pool/main/d/dvdbackup/dvdbackup_0.4.2-4.debian.tar.gz

Requires:       libdvdread
BuildRequires:  libdvdread-devel >= 0.9.6

Summary(ru_RU.UTF-8): Утилита для копирования содержимого DVD на жесткий диск

%description
Copy DVD-content on hard disc.

%description -l ru_RU.UTF-8
Утилита копирования содержимого DVD диска на жесткий диск. 
Поддерживает как выборочное копирование, так и полное.

%prep
%setup -q -a1
for patch in `cat debian/patches/series`; do
    patch -p1 < debian/patches/$patch
done

%build
./configure 
make

%install
install -pD -m755 src/%name $RPM_BUILD_ROOT%_bindir/%name

%files
#doc %name/README %name/INSTALL
%doc README INSTALL
%{_bindir}/%{name}

%changelog
* Sat Nov 18 2017 Igor Vlasenko <viy@altlinux.ru> 0.4.2-alt1
- new version

* Mon Apr 15 2013 Dmitry V. Levin (QA) <qa_ldv@altlinux.org> 0.4.1-alt1.qa1
- NMU: rebuilt for debuginfo.

* Sun Sep 20 2009 Igor Vlasenko <viy@altlinux.ru> 0.4.1-alt1
- new version from http://dvdbackup.sourceforge.net

* Sun Jan 21 2007 Igor Vlasenko <viy@altlinux.ru> 0.1.1-alt2
- removed static linkage with legacy version 0.9.4 of libdvdread
- (debian patch, thanks to thresh@ for hint)

* Wed Jan 17 2007 Igor Vlasenko <viy@altlinux.ru> 0.1.1-alt1
- new version;
- resurrected from orphaned;
- note: starting from 0.9.7, libdvdread no more provide
  UDFFindFile symbol. so we statically link dvdbackup
  with legacy version 0.9.4 of libdvdread.

* Wed Jan 17 2007 Igor Vlasenko <viy@altlinux.ru> 0.1.1-alt0.M30.1
- backport for M30

* Tue Oct 05 2004 ALT QA Team Robot <qa-robot@altlinux.org> 0.1-alt1.1
- Rebuilt with libdvdread.so.3.

* Sun May 18 2003 Gerasimov Dmitry <dmitryg@altlinux.ru> 0.1-alt1
- Initial build for ALT Linux Team
