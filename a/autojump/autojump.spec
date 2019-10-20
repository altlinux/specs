Group: Shells
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-python3
BuildRequires: /usr/bin/pathfix.py
# END SourceDeps(oneline)
Requires: bash-completion
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
%global owner wting

Name:           autojump
Version:        22.5.1
Release:        alt1_8

Summary:        A fast way to navigate your filesystem from the command line

License:        GPLv3+
URL:            http://wiki.github.com/%{owner}/%{name}
Source:         https://github.com/%{owner}/%{name}/archive/release-v%{version}/%{name}-%{version}.tar.gz
Patch0:         remove-homebrew-check.patch
Patch1:         install-add-distribution-arg.patch

BuildArch:      noarch

BuildRequires:  pandoc
BuildRequires:  python3-devel
BuildRequires:  python3-module-mock
BuildRequires:  pytest python-module-pytest python3-module-pytest
Source44: import.info

%description
autojump is a faster way to navigate your filesystem. It works by maintaining 
a database of the directories you use the most from the command line.


%package zsh
Group: Shells
Requires:       %{name} = %{version}-%{release}
Summary:        Autojump for zsh

%description zsh
autojump is a faster way to navigate your filesystem. It works by maintaining 
a database of the directories you use the most from the command line.
autojump-zsh is designed to work with zsh.


%package fish
Group: Office
Requires:       %{name} = %{version}-%{release}
Summary:        Autojump for fish shell

%description fish
autojump is a faster way to navigate your filesystem. It works by maintaining 
a database of the directories you use the most from the command line.
autojump-fish is designed to work with fish shell.


%prep
%setup -q -n %{name}-release-v%{version}
%patch0 -p1
%patch1 -p1


# Use system argparse
sed -i 's|autojump_argparse|argparse|' bin/%{name}
# Fix shebangs, non .py files need to be specified manually, so we provide bin/* as well as .
pathfix.py -i %{__python3} -pn . ./bin/*
sed -i '1{/^#!/d}' bin/%{name}_*.py

%build
make docs

%install
export SHELL=bash
./install.py --destdir %{buildroot} --prefix usr --zshshare %{buildroot}%{_datadir}/zsh/site-functions --distribution
# Do not need bundled modules
rm %{buildroot}%{_bindir}/%{name}_argparse.py
# Move modules to proper directory
mkdir -p %{buildroot}%{python3_sitelibdir_noarch}
mv %{buildroot}%{_bindir}/%{name}_*.py %{buildroot}%{python3_sitelibdir_noarch}/

%check
%{__python3} -m pytest tests -vv

%files
%doc --no-dereference LICENSE
%doc README.md AUTHORS
%{_bindir}/%{name}
%{python3_sitelibdir_noarch}/%{name}_data.py
%{python3_sitelibdir_noarch}/%{name}_match.py
%{python3_sitelibdir_noarch}/%{name}_utils.py
%{python3_sitelibdir_noarch}/__pycache__/%{name}*.pyc
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
* Thu Oct 17 2019 Igor Vlasenko <viy@altlinux.ru> 22.5.1-alt1_8
- update to new release by fcimport

* Fri Apr 19 2019 Igor Vlasenko <viy@altlinux.ru> 22.5.1-alt1_5
- update to new release by fcimport

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

