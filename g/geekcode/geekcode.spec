Group: Games/Other
Name:           geekcode
Version:        1.7.3
Release:        alt2_18
Summary:        Geek Code generator
Summary(pl):    Generator Geek Code
License:        GPLv2+
URL:            http://sourceforge.net/projects/%{name}/
Source0:        http://downloads.sourceforge.net/%{name}/%{name}-%{version}.tar.gz
# CFLAGS, full RELRO
Patch0:         %{name}-1.7.3-flags.patch
# sf#879355
Patch1:         %{name}-1.7.3-choice.patch
BuildRequires:  binutils
BuildRequires:  coreutils
BuildRequires:  gcc
Source44: import.info

%description
The Geek Code Generator will generate a geek code block for you by asking you a
series of questions about yourself. The generated code can be pasted into your
.sig or anywhere else you would like to display your geekiness.

%description -l pl
Generator ten potrafi wygenerować blok Geek Code po odpowiedzi na serię
pytań. Tak wygenerowany kod można umieścić w swoim podpisie lub
gdziekolwiek indziej, gdzie chcemy się pochwalić swoją geekowatością.

%prep
%setup -q
sed -i 's/\r//' COPYING
%patch0 -p1
%patch1 -p1

%build
make %{?_smp_mflags}

%install
mkdir -p %{buildroot}%{_bindir}
install -m 755 geekcode %{buildroot}%{_bindir}

%files
%doc COPYING
%doc CHANGES README
%{_bindir}/%{name}

%changelog
* Tue Feb 16 2016 Igor Vlasenko <viy@altlinux.ru> 1.7.3-alt2_18
- update to new release by fcimport

* Sun Sep 20 2015 Igor Vlasenko <viy@altlinux.ru> 1.7.3-alt2_17
- update to new release by fcimport

* Wed Aug 27 2014 Igor Vlasenko <viy@altlinux.ru> 1.7.3-alt2_14
- update to new release by fcimport

* Tue Jul 01 2014 Igor Vlasenko <viy@altlinux.ru> 1.7.3-alt2_13
- update to new release by fcimport

* Mon Aug 12 2013 Igor Vlasenko <viy@altlinux.ru> 1.7.3-alt2_12
- update to new release by fcimport

* Sun Feb 24 2013 Igor Vlasenko <viy@altlinux.ru> 1.7.3-alt2_11
- update to new release by fcimport

* Fri Feb 22 2013 Igor Vlasenko <viy@altlinux.ru> 1.7.3-alt2_10
- update to new release by fcimport

* Fri Jul 27 2012 Igor Vlasenko <viy@altlinux.ru> 1.7.3-alt2_9
- update to new release by fcimport

* Fri Mar 02 2012 Igor Vlasenko <viy@altlinux.ru> 1.7.3-alt2_8
- rebuild with fixed sourcedep analyser (#27020)

* Wed Feb 01 2012 Igor Vlasenko <viy@altlinux.ru> 1.7.3-alt1_8
- update to new release by fcimport

* Fri Nov 18 2011 Igor Vlasenko <viy@altlinux.ru> 1.7.3-alt1_7
- update to new release by fcimport

* Thu Jul 07 2011 Igor Vlasenko <viy@altlinux.ru> 1.7.3-alt1_6
- update to new release by fcimport

* Tue Feb 15 2011 Igor Vlasenko <viy@altlinux.ru> 1.7.3-alt1_5
- converted from Fedora by srpmconvert script

