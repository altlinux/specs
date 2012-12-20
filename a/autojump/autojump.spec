Name:           autojump
Version:        21.1.2
Release:        alt1_2

Summary:        A fast way to navigate your filesystem from the command line

Group:          Shells
License:        GPLv3+
URL:            http://wiki.github.com/joelthelion/autojump
Source:         https://github.com/downloads/joelthelion/%{name}/%{name}_v%{version}.tar.gz
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

%prep
%setup -q -n %{name}_v%{version}

# Fix shebang
sed -i 's|/usr/bin/env python|/usr/bin/python|' bin/%{name}
for i in bin/jumpapplet tests/runtests.py; do
    sed -i 's|/usr/bin/env python2|/usr/bin/python|' "$i"
done

%build
make docs

%check
python tests/runtests.py

%install

mkdir -p $RPM_BUILD_ROOT%{_datadir}/%{name}

# There must be a more elegant way to do that
install -p bin/icon.png $RPM_BUILD_ROOT%{_datadir}/%{name}/icon.png
install -Dp bin/%{name} $RPM_BUILD_ROOT%{_bindir}/%{name}
install -p bin/jumpapplet $RPM_BUILD_ROOT%{_bindir}/jumpapplet
install -Dpm 644 bin/_j $RPM_BUILD_ROOT%{_datadir}/zsh/site-functions/_j
install -Dpm 644 bin/%{name}.bash $RPM_BUILD_ROOT%{_sysconfdir}/profile.d/%{name}.bash
install -Dpm 755 bin/%{name}.sh $RPM_BUILD_ROOT%{_sysconfdir}/profile.d/%{name}.sh
install -Dpm 644 bin/%{name}.zsh $RPM_BUILD_ROOT%{_sysconfdir}/profile.d/%{name}.zsh

install -Dpm 644 docs/%{name}.1 $RPM_BUILD_ROOT%{_mandir}/man1/%{name}.1
# jumpapplet needs autojump.py
ln -s %{name} $RPM_BUILD_ROOT%{_bindir}/%{name}.py

%files
%doc LICENSE README.md AUTHORS
%{_bindir}/%{name}
%{_bindir}/%{name}.py
%{_bindir}/jumpapplet
%{_datadir}/%{name}
%{_mandir}/man1/%{name}.1*
%config(noreplace) %{_sysconfdir}/profile.d/%{name}.sh
%config(noreplace) %{_sysconfdir}/profile.d/%{name}.bash

%files zsh
%config(noreplace) %{_sysconfdir}/profile.d/%{name}.zsh
%dir %{_datadir}/zsh/site-functions/
%{_datadir}/zsh/site-functions/_j

%changelog
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

