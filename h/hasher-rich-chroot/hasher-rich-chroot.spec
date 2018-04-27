Name: hasher-rich-chroot
Version: 0.02
Release: alt1

Summary: hasher chroot environment for productive work 
License: GPL
Group: Development/Other
Packager: Igor Vlasenko <viy@altlinux.org>
#Url: http://www.altlinux.org/Git.alt/girar-nmu
BuildArch: noarch

Source: %name-%version.tar

Requires: mc vim-console less unzip elfutils rpm-utils
# Andrew Savchenko:
#Лично мне приходится на все системы, где я работаю, ставить
#terminfo-extra, т.к. я использую screen-256color-bce-s; даже внутрь
#хешерницы, т.к. иначе hsh-shell не работает нормально.
Requires: terminfo-extra

%description
This package contains utilities that configure
hasher chroot for comfortable post mortem work.
They should be installed into chroot.

For user-side utils, see %name-utils


%package user-utils
Summary: User-side utils for hasher-rich-chroot
Group: Development/Other

%description user-utils
User-side utils for hasher-rich-chroot -
hasher chroot environment for productive work

%prep
%setup

%build

%install
mkdir -p %buildroot%_bindir
install -m 755 hsh-*  %buildroot%_bindir/

#for i in girar-*; do
#    pod2man  --name $i --center 'girar-nmu utils' --section 1 --release %version $i > $i.1 ||:
#done
#find . -name '*.1' -size 0 -print -delete
#mkdir -p %buildroot%_man1dir
#install -m 644 girar-*.1 %buildroot%_man1dir/

%files
#%doc README
%_bindir/hsh-rich-chroot-create-history
#%_man1dir/*

%files user-utils
%_bindir/hsh-install-rich-chroot

%changelog
* Fri Apr 27 2018 Igor Vlasenko <viy@altlinux.ru> 0.02-alt1
- added terminfo-extra for screen

* Wed May 21 2014 Igor Vlasenko <viy@altlinux.ru> 0.01-alt1
- initial release

* Thu Apr 17 2014 Igor Vlasenko <viy@altlinux.ru> 1.16-alt1
- new version

* Tue Oct 01 2013 Igor Vlasenko <viy@altlinux.ru> 1.15-alt1
- new utility girar-backport-prepare

* Mon May 13 2013 Igor Vlasenko <viy@altlinux.ru> 1.14-alt3
- bugfix release

* Sun May 12 2013 Igor Vlasenko <viy@altlinux.ru> 1.14-alt2
- bugfix release

* Sun May 12 2013 Igor Vlasenko <viy@altlinux.ru> 1.14-alt1
- new version

* Wed Apr 24 2013 Igor Vlasenko <viy@altlinux.ru> 1.13-alt1
- stable release

* Fri Mar 29 2013 Igor Vlasenko <viy@altlinux.ru> 1.12-alt1
- fixes in cycle detection

* Thu Mar 28 2013 Igor Vlasenko <viy@altlinux.ru> 1.11-alt1
- ported --buildreq for new relations set

* Wed Mar 27 2013 Igor Vlasenko <viy@altlinux.ru> 1.10-alt1
- another bugfix in sort-transaction (thanks to aris@)

* Wed Mar 27 2013 Igor Vlasenko <viy@altlinux.ru> 1.07-alt1
- bugfix in sort-transaction (thanks to aris@)

* Sat Dec 08 2012 Igor Vlasenko <viy@altlinux.ru> 1.06-alt1
- better python sypport

* Sat Dec 01 2012 Igor Vlasenko <viy@altlinux.ru> 1.05-alt1
- new version, requires new RPM-Source-Editor

* Thu Sep 27 2012 Igor Vlasenko <viy@altlinux.ru> 1.04-alt1
- maintainance release

* Wed Jun 27 2012 Igor Vlasenko <viy@altlinux.ru> 1.03-alt1
- new version thanks to mithraen@

* Mon Jun 18 2012 Igor Vlasenko <viy@altlinux.ru> 1.02-alt1
- new version thanks to mithraen@

* Mon Jan 30 2012 Igor Vlasenko <viy@altlinux.ru> 1.01-alt1
- new version

* Mon Jan 30 2012 Igor Vlasenko <viy@altlinux.ru> 1.00-alt1
- new version

