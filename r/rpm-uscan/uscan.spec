%define destname rpm-uscan
%define debian_ver 2.11.6
Name: %destname
Version: 0.7.%debian_ver
Release: alt1

Summary: Utility to check watch files
Source: %name-%version.tar

License: %gpl2plus
Group: Development/Other

BuildArch: noarch

BuildRequires: rpm-build-licenses perl-devel perl-RPM perl(LWP/UserAgent.pm)
Requires: perl-Crypt-SSLeay
Requires: gear-uupdate

%description
- uscan: Automatically scan for and download upstream updates.  Uscan can
  also call a program such as girar-nmu to attempt to update the src.rpm 
  or gear repository.  Whilst uscan could be used to release
  the updated version automatically, it is probably better not to without
  testing it first.

%prep
%setup

%build

%install
mkdir -p %buildroot%_bindir
install -Dm755 scripts/uscan.pl %buildroot%_bindir/%destname
sed -i -e 's,###VERSION###,%version-rpm,' %buildroot%_bindir/%destname

install -Dm644 scripts/uscan.1 %buildroot%_man1dir/%destname.1

%files
%_bindir/*
%_man1dir/*

%changelog
* Tue May 08 2012 Igor Vlasenko <viy@altlinux.ru> 0.7.2.11.6-alt1
- more patterns in any-archive

* Tue Apr 24 2012 Igor Vlasenko <viy@altlinux.ru> 0.6.2.11.6-alt1
- sync with debian uscan 2.11.6

* Mon Jan 16 2012 Igor Vlasenko <viy@altlinux.ru> 0.6.2.11.3-alt1
- sync with debian uscan 2.11.3
- added usehttpheaderfilename option (for cas@)

* Fri Nov 11 2011 Igor Vlasenko <viy@altlinux.ru> 0.6.2.11.1-alt1
- new version

* Wed Oct 19 2011 Igor Vlasenko <viy@altlinux.ru> 0.5.2.11.1-alt1
- new version

* Sat Oct 15 2011 Igor Vlasenko <viy@altlinux.ru> 0.4.2.11.1-alt1
- new version

* Sat Oct 15 2011 Igor Vlasenko <viy@altlinux.ru> 0.3.2.11.1-alt1
- new version

* Sat Oct 15 2011 Igor Vlasenko <viy@altlinux.ru> 0.2.2.11.1-alt1
- any-archive option

* Wed Oct 12 2011 Igor Vlasenko <viy@altlinux.ru> 0.1.2.11.1-alt1
- debian uscan, patched to work with rpm and gear.
