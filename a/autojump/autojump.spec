# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-python
# END SourceDeps(oneline)
Requires: bash-completion
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
%global commit 61af2bf4c5a1071f973e661f6145cf606bf30e80
%global owner wting

Name:           autojump
Version:        22.3.2
Release:        alt1_4

Summary:        A fast way to navigate your filesystem from the command line

Group:          Shells
License:        GPLv3+
URL:            http://wiki.github.com/%{owner}/%{name}
Source:         https://github.com/%{owner}/%{name}/archive/%{commit}/%{name}-%{commit}.tar.gz
Patch0:         remove-homebrew-check.patch
Patch1:         install-add-distribution-arg.patch

BuildArch:      noarch

# June 27th, pandoc is broken in rawhide, uncomment when working again
# BuildRequires:  pandoc
BuildRequires:  python-devel
Requires:       python
%if 0%{?rhel} && 0%{?rhel} <= 6
Requires:       python-base
%endif
Requires(pre):  coreutils
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
%patch0 -p1
%patch1 -p1
# Use system argparse
sed -i 's|autojump_argparse|argparse|' bin/%{name}
# Fix shebang
sed -i 's|/usr/bin/env python|/usr/bin/python|' bin/%{name}
sed -i '1{/^#!/d}' bin/%{name}_*.py

%build
# June 27th, pandoc is broken in rawhide, uncomment when working again
# make docs

%install
export SHELL=bash
./install.py --destdir %{buildroot} --prefix usr --zshshare %{buildroot}%{_datadir}/zsh/site-functions --distribution
# Do not need bundled modules
rm %{buildroot}%{_bindir}/%{name}_argparse.py
# Move modules to proper directory
mkdir -p %{buildroot}%{python_sitelibdir_noarch}
mv %{buildroot}%{_bindir}/%{name}_*.py %{buildroot}%{python_sitelibdir_noarch}/

%pre
rm -f %{_bindir}/%{name}_*.pyc

%files
%doc LICENSE
%doc README.md AUTHORS
%{_bindir}/%{name}
%{python_sitelibdir_noarch}/%{name}_data.py*
%{python_sitelibdir_noarch}/%{name}_utils.py*
%dir %{_datadir}/%{name}
%{_datadir}/%{name}/icon.png
%{_mandir}/man1/%{name}.1*
%config(noreplace) %{_sysconfdir}/profile.d/%{name}.sh
%config(noreplace) %{_datadir}/%{name}/%{name}.bash

%files zsh
%config(noreplace) %{_datadir}/%{name}/%{name}.zsh
%{_datadir}/zsh/site-functions/_j

%files fish
%config(noreplace) %{_datadir}/%{name}/%{name}.fish

%changelog
* Tue Oct 10 2017 Igor Vlasenko <viy@altlinux.ru> 22.3.2-alt1_4
- update to new release by fcimport

* Mon Oct 27 2014 Igor Vlasenko <viy@altlinux.ru> 21.7.1-alt1_4
- update to new release by fcimport

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

