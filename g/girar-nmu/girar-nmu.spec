Name: girar-nmu
Version: 1.45
Release: alt1

Summary: git.alt client utilities for NMU automation
License: GPL
Group: Development/Other
Packager: Igor Vlasenko <viy@altlinux.org>
Url: http://www.altlinux.org/Git.alt/girar-nmu
#BuildArch: noarch

Source: %name-%version.tar

#BuildRequires: help2man
BuildRequires: perl-devel perl-podlators perl(RPM/Header.pm) perl-RPM-Source-Editor perl-RPM-Source-Convert perl(Pod/Usage.pm) perl(Date/Parse.pm) /usr/bin/pod2man perl-Gear-Rules perl(Source/Shared/Utils/GlobList.pm)

Requires: gear
Requires: perl-RPM-Source-Editor >= 0.910

%description
This package contains client utilities for git.alt
for NMU automation.

%prep
%setup
rm *.spec

%build
gcc -O2 %optflags -o girar-nmu-helper-pos-sort pos-sort.c

%install
#make_install install DESTDIR=%buildroot

mkdir -p %buildroot%perl_vendor_privlib/RPM/Source/Tools
install -m 644 GirarWriterPrototype.pm %buildroot%perl_vendor_privlib/RPM/Source/Tools/

mkdir -p %buildroot%_bindir
install -m 755 girar-* rpm-sign-* srpmlschangelog %buildroot%_bindir/

for i in girar-* srpmlschangelog; do
    pod2man  --name $i --center 'girar-nmu utils' --section 1 --release %version $i > $i.1 ||:
done
find . -name '*.1' -size 0 -print -delete
mkdir -p %buildroot%_man1dir
install -m 644 girar-*.1 %buildroot%_man1dir/

%files
%doc README
%_bindir/*
%_man1dir/*
%perl_vendor_privlib/RPM*

%changelog
* Tue Nov 14 2017 Igor Vlasenko <viy@altlinux.ru> 1.45-alt1
- basic support for rpmsign 4.13

* Sat Sep 30 2017 Igor Vlasenko <viy@altlinux.ru> 1.44-alt1
- use Source::Shared::Utils::GlobList

* Sun Apr 02 2017 Igor Vlasenko <viy@altlinux.ru> 1.43-alt1
- new version

* Wed Feb 08 2017 Igor Vlasenko <viy@altlinux.ru> 1.42-alt1
- support for gitery path in girar-nmu-helper-git-push-build

* Mon Jan 30 2017 Igor Vlasenko <viy@altlinux.ru> 1.41-alt1
- new version

* Sat Jan 21 2017 Igor Vlasenko <viy@altlinux.ru> 1.40-alt1
- new version

* Wed Jan 11 2017 Igor Vlasenko <viy@altlinux.ru> 1.39-alt1
- use new CLI

* Tue Jan 10 2017 Igor Vlasenko <viy@altlinux.ru> 1.38-alt1
- use new TransformContainer

* Mon Jan 09 2017 Igor Vlasenko <viy@altlinux.ru> 1.37-alt1
- use new R::S::E interface

* Tue Oct 04 2016 Igor Vlasenko <viy@altlinux.ru> 1.36-alt1
- use RPM::Header

* Sun Jul 03 2016 Igor Vlasenko <viy@altlinux.ru> 1.35-alt1
- updated BR:

* Sat Feb 20 2016 Igor Vlasenko <viy@altlinux.ru> 1.34-alt1
- rest of fixes for interface changes in R::S::E Transform 16

* Sat Feb 20 2016 Igor Vlasenko <viy@altlinux.ru> 1.33-alt1
- fixes for interface changes in R::S::E Transform 16

* Wed Jan 13 2016 Igor Vlasenko <viy@altlinux.ru> 1.32-alt1
- more verbose debug for marked files

* Wed Jan 13 2016 Igor Vlasenko <viy@altlinux.ru> 1.31-alt1
- added buildfrom-rpm-marked opt to girar-nmu-sort-transaction

* Mon Nov 23 2015 Igor Vlasenko <viy@altlinux.ru> 1.30-alt1
- added girar-nmu-helper-task-add-rebuild

* Sun Nov 22 2015 Igor Vlasenko <viy@altlinux.ru> 1.29-alt1
- <before_subtask_id> support in girar-nmu-helper-git-push-build

* Mon Nov 16 2015 Igor Vlasenko <viy@altlinux.ru> 1.28-alt1
- improved debug output in girar-nmu-sort-transaction

* Fri Nov 13 2015 Ivan Zakharyaschev <imz@altlinux.org> 1.27-alt2
- girar-nmu-helper-clone-and-setup-build-commit: configure the remote
  in a standard way (like "git remote add" does; ALT#31482).
- minor tweaks in the code:
  - factored out git://git.altlinux.org/gears and
    git://git.altlinux.org/srpms as variables (to become environment
    parameters in future).
  - typo in documentation.

* Thu Oct 22 2015 Igor Vlasenko <viy@altlinux.ru> 1.27-alt1
- <before_subtask_id> support in girar-nmu-helper-task-add-srpm

* Tue Oct 13 2015 Gleb F-Malinovskiy <glebfm@altlinux.org> 1.26-alt1
- girar-nmu-helper-task-add-git: fixed typo.

* Sat Aug 22 2015 Igor Vlasenko <viy@altlinux.ru> 1.25-alt1
- support for girar and gitery

* Sun Dec 14 2014 Igor Vlasenko <viy@altlinux.ru> 1.24-alt1
- new version

* Thu Dec 11 2014 Igor Vlasenko <viy@altlinux.ru> 1.23-alt1
- new version

* Thu Dec 04 2014 Igor Vlasenko <viy@altlinux.ru> 1.22-alt1
- new version

* Wed Dec 03 2014 Igor Vlasenko <viy@altlinux.ru> 1.21-alt1
- new version

* Wed Nov 26 2014 Igor Vlasenko <viy@altlinux.ru> 1.20-alt1
- bugfix release

* Sun Oct 05 2014 Igor Vlasenko <viy@altlinux.ru> 1.19-alt1
- bugfix release thanks to glebfm@ (closes: #30371)

* Fri Sep 19 2014 Igor Vlasenko <viy@altlinux.ru> 1.18-alt1
- new version

* Sat Jun 14 2014 Igor Vlasenko <viy@altlinux.ru> 1.17-alt1
- use Gear::Rules library

* Thu Apr 17 2014 Igor Vlasenko <viy@altlinux.ru> 1.16-alt1
- new version
