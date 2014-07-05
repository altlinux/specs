Requires: bash-completion
%global commit dabc177bbd2a6728f94ad013ab581dd44437d5ab
%global owner joelthelion

Name:           autojump
Version:        21.7.1
Release:        alt1_3

Summary:        A fast way to navigate your filesystem from the command line

Group:          Shells
License:        GPLv3+
URL:            http://wiki.github.com/joelthelion/autojump
Source:         https://github.com/%{owner}/%{name}/archive/%{commit}/%{name}-%{commit}.tar.gz
Patch1:         fix-bash-completion.patch

# pandoc doesnt build on arm, so lets build on intel arch only
ExclusiveArch:  %{ix86} noarch
BuildArch:      noarch

BuildRequires:  pandoc python-devel
Source44: import.info

%description
autojump is a faster way to navigate your filesystem. It works by maintaining 
a database of the directories you use the most from the command line.


%package zsh
Requires:       %{name} = %{version}-%{release}
Group:          Shells
Summary:        Autojump for zsh

%description zsh
autojump is a faster way to navigate your filesystem. It works by maintaining 
a database of the directories you use the most from the command line.
autojump-zsh is designed to work with zsh.


%package fish
Requires:       %{name} = %{version}-%{release}
Group:          Office
Summary:        Autojump for fish shell

%description fish
autojump is a faster way to navigate your filesystem. It works by maintaining 
a database of the directories you use the most from the command line.
autojump-fish is designed to work with fish shell.


%prep
%setup -q -n %{name}-%{commit}
%patch1 -p1

# Fix shebang
sed -i 's|/usr/bin/env python|/usr/bin/python|' bin/%{name}

%build
make docs

%install
./install.sh --destdir %{buildroot} --prefix usr
# deprecated file
rm -f %{buildroot}/_j

%files
%doc LICENSE README.md AUTHORS
%{_bindir}/%{name}
%{_bindir}/%{name}_argparse.py
%{_datadir}/%{name}
%{_mandir}/man1/%{name}.1*
%config(noreplace) %{_sysconfdir}/profile.d/%{name}.sh
%config(noreplace) %{_sysconfdir}/profile.d/%{name}.bash

%files zsh
%config(noreplace) %{_sysconfdir}/profile.d/%{name}.zsh

%files fish
%config(noreplace) %{_sysconfdir}/profile.d/%{name}.fish

%changelog
* Tue Jul 01 2014 Igor Vlasenko <viy@altlinux.ru> 21.7.1-alt1_3
- update to new release by fcimport

* Wed Mar 13 2013 Igor Vlasenko <viy@altlinux.ru> 21.1.2-alt3_3
- 755 for all profile files (closes: #28500)

* Fri Feb 22 2013 Igor Vlasenko <viy@altlinux.ru> 21.1.2-alt2_3
- update to new release by fcimport

* Sat Feb 02 2013 Igor Vlasenko <viy@altlinux.ru> 21.1.2-alt2_2
- added R: bash-completion (closes: 28500)

* Fri Dec 21 2012 Igor Vlasenko <viy@altlinux.ru> 21.1.2-alt1_2
- update to new release by fcimport

* Fri Jul 27 2012 Igor Vlasenko <viy@altlinux.ru> 20-alt1_2
- update to new release by fcimport

* Fri May 11 2012 Igor Vlasenko <viy@altlinux.ru> 20-alt1_1
- update to new release by fcimport

* Wed Mar 21 2012 Igor Vlasenko <viy@altlinux.ru> 19-alt2_3
- rebuild to get rid of #27020

* Sat Jan 21 2012 Igor Vlasenko <viy@altlinux.ru> 19-alt1_3
- update to new release by fcimport

* Tue Dec 13 2011 Igor Vlasenko <viy@altlinux.ru> 19-alt1_2
- update to new release by fcimport

* Thu Nov 24 2011 Igor Vlasenko <viy@altlinux.ru> 15-alt2_1
- bugfix release

* Tue Oct 25 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 15-alt1_1.1
- Rebuild with Python-2.7

* Fri Jul 08 2011 Igor Vlasenko <viy@altlinux.ru> 15-alt1_1
- initial release by fcimport

