Name:		abgraph
Version:	1.1
Release:	alt2_5

Summary:	ABGraph is a simple tool to benchmark webservers

License:	GPLv3+
Group:		Development/Tools
URL:		http://sourceforge.net/projects/abgraph
Source:		http://dl.sf.net/%{name}/%{name}-%{version}.tar.gz

BuildArch:	noarch
Requires:	gnuplot apache-common
Source44: import.info

%description
ABGraph is a simple tool to benchmark webservers.
The program uses ab (apache benchmark) to actually
benchmark the selected remote host. A graph in PNG format
is generated with gnuplot and saved to the selected path/file.

%prep
%setup -q 

%build

%install
install -Dpm 755 abgraph.sh $RPM_BUILD_ROOT%{_bindir}/abgraph


%files
%doc README COPYING
%{_bindir}/abgraph


%changelog
* Wed Mar 21 2012 Igor Vlasenko <viy@altlinux.ru> 1.1-alt2_5
- rebuild to get rid of #27020

* Sat Jan 21 2012 Igor Vlasenko <viy@altlinux.ru> 1.1-alt1_5
- update to new release by fcimport

* Fri Jul 08 2011 Igor Vlasenko <viy@altlinux.ru> 1.1-alt1_4
- initial release by fcimport

