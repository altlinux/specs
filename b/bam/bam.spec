# BEGIN SourceDeps(oneline):
BuildRequires: gcc-c++
# END SourceDeps(oneline)
Name:           bam
Version:        0.4.0

Release:        alt2_2
Summary:        A build-system

Group:          Games/Other
License:        zlib
URL:            http://matricks.github.com/bam/
Source0:        http://github.com/downloads/matricks/bam/%{name}-%{version}.tar.bz2
Source44: import.info


%description
A tool that controls process of producing executables of 
software from its source code. Used to build the Teeworlds game.


%prep
%setup -q 


%build
sh -x make_unix.sh %{optflags}


%install

install -D -m 0755 %{name} \
        %{buildroot}%{_bindir}/%{name}


%files
%doc docs/ examples/
%{_bindir}/%{name}


%changelog
* Fri Mar 02 2012 Igor Vlasenko <viy@altlinux.ru> 0.4.0-alt2_2
- rebuild with fixed sourcedep analyser (#27020)

* Fri Jan 20 2012 Igor Vlasenko <viy@altlinux.ru> 0.4.0-alt1_2
- update to new release by fcimport

* Thu May 19 2011 Igor Vlasenko <viy@altlinux.ru> 0.4.0-alt1_1
- new origin release

* Tue Feb 15 2011 Igor Vlasenko <viy@altlinux.ru> 0.2.0-alt1_4
- converted from Fedora by srpmconvert script

