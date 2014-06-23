%define destname gear-uupdate
Name: %destname
Version: 0.13
Release: alt1

Summary: Helper utility to be called by uscan for gear repository update
Source: %name-%version.tar

License: GPL2+
Group: Development/Other
URL: http://www.altlinux.org/Gear/gear-uupdate

BuildArch: noarch

BuildRequires: perl-devel perl(Pod/Usage.pm) /usr/bin/pod2man perl-Gear-Rules perl-RPM-Source-Editor perl-String-ShellQuote
Requires: gear /usr/bin/srpmnmu perl-Gear-Rules perl-RPM-Source-Editor > 0.73

%description
%summary

%prep
%setup

%build

%install
mkdir -p %buildroot%_bindir
install -Dm755 gear-uupdate* %buildroot%_bindir/

for i in gear-uupdate-prepare gear-uupdate-execute; do
    pod2man  --name $i --center $i --section 1 --release %version $i > $i.1
done
ln -s gear-uupdate-prepare.1 gear-uupdate.1
mkdir -p %buildroot%_man1dir
install -m 644 gear-*.1 %buildroot%_man1dir/

%files
%_bindir/*
%_man1dir/*

%changelog
* Mon Jun 23 2014 Igor Vlasenko <viy@altlinux.ru> 0.13-alt1
- bugfix release

* Sat Jun 14 2014 Igor Vlasenko <viy@altlinux.ru> 0.12-alt1
- new version

* Thu Jun 05 2014 Igor Vlasenko <viy@altlinux.ru> 0.11-alt1
- updated man pages

* Fri Mar 07 2014 Igor Vlasenko <viy@altlinux.ru> 0.10-alt1
- bugfix release

* Sat Aug 17 2013 Igor Vlasenko <viy@altlinux.ru> 0.09-alt1
- now works correctly with depth0 archives

* Mon Jan 21 2013 Igor Vlasenko <viy@altlinux.ru> 0.08-alt2
- git merge --no-edit default behavior

* Mon Jan 21 2013 Igor Vlasenko <viy@altlinux.ru> 0.08-alt1
- bugfix release

* Thu Jan 17 2013 Igor Vlasenko <viy@altlinux.ru> 0.07-alt1
- fixes for upstream branch with sources in root

* Thu Jan 17 2013 Igor Vlasenko <viy@altlinux.ru> 0.06-alt1
- new version

* Thu Jan 17 2013 Igor Vlasenko <viy@altlinux.ru> 0.05-alt2
- bugfix

* Thu Jan 12 2012 Igor Vlasenko <viy@altlinux.ru> 0.05-alt1
- added man page

* Fri Jan 06 2012 Igor Vlasenko <viy@altlinux.ru> 0.04-alt1
- new version

* Thu Oct 20 2011 Igor Vlasenko <viy@altlinux.ru> 0.03-alt1
- new development version

* Wed Oct 19 2011 Igor Vlasenko <viy@altlinux.ru> 0.02-alt1
- new version

* Sat Oct 08 2011 Igor Vlasenko <viy@altlinux.ru> 0.01-alt1
- First draft

