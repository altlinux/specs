Name:		auto-nng
Version:	1.7
Release:	alt2_2
Summary:	A software for analysis and classification of data, using AI NN

Group:		Engineering
License:	MIT
URL:		http://www.public-software-group.org/auto-nng
Source0:	http://www.public-software-group.org/pub/projects/auto-nng/v%{version}/%{name}.v%{version}.tar.gz
Patch0:		%{name}-cflags.patch

BuildRequires:	ruby
Source44: import.info


%description
auto-nng is a software for analysis and classification of data, using 
artificial neuronal networks.
You can feed an amount of datasets consisting of certain input and output 
parameters into the program, to make it try to find a mathematical correlation 
between the input and output parameters. Afterwards the program tries to 
calculate the output parameters for datasets which only have known input 
parameters.


%prep
%setup -q -n %{name}.v%{version}
# patch0: Not sent upstream, as it is buildsystem related.
%patch0 -p1 -b .cflags


%build
make %{?_smp_mflags} CFLAGS="%{optflags}"


%check
# Test takes at max 3 minutes so do not wonder.
make test


%install
mkdir -p %{buildroot}/%{_bindir}/
install auto-nng %{buildroot}/%{_bindir}/


%files
%doc LICENSE README
%{_bindir}/*

%changelog
* Wed Mar 21 2012 Igor Vlasenko <viy@altlinux.ru> 1.7-alt2_2
- rebuild to get rid of #27020

* Sat Jan 21 2012 Igor Vlasenko <viy@altlinux.ru> 1.7-alt1_2
- update to new release by fcimport

* Fri Jul 08 2011 Igor Vlasenko <viy@altlinux.ru> 1.5-alt1_3
- initial release by fcimport

