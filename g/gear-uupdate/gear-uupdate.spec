%define destname gear-uupdate
Name: %destname
Version: 0.05
Release: alt1

Summary: Helper utility to be called by uscan for gear repository update
Source: %name-%version.tar

License: GPL2+
Group: Development/Other

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

for i in gear-uupdate-prepare; do
    pod2man  --name $i --center 'gear-uupdate-prepare' --section 1 --release %version $i > $i.1
done
ln -s gear-uupdate-prepare.1 gear-uupdate.1
mkdir -p %buildroot%_man1dir
install -m 644 gear-*.1 %buildroot%_man1dir/

%files
%_bindir/*
%_man1dir/*

%changelog
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

