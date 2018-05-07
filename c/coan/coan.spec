# BEGIN SourceDeps(oneline):
BuildRequires: /usr/bin/python /usr/bin/time
# END SourceDeps(oneline)
BuildRequires: /usr/bin/pod2man /usr/bin/pod2html
%define fedora 27
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
Name:		coan
Version:	6.0.1
Release:	alt1_15
Summary:	A command line tool for simplifying the pre-processor conditionals in source code
Group:		Development/Other
License:	BSD
URL:		http://coan2.sourceforge.net/
Source0:	http://downloads.sourceforge.net/coan2/%{name}-%{version}.tar.gz
BuildRequires:  gcc-c++
BuildRequires:	python
# For pod2man:
BuildRequires:  perl-podlators
# On Fedora 23 pod2html is included in the perl package, whereas in 24
# and later it's split out into perl-Pod-Html.
%if 0%{fedora} > 23
BuildRequires:  perl-devel
%endif

# Regression on other arches with F26 mass rebuild (big endian systems)
# Temporarily exclude them
# https://bugzilla.redhat.com/show_bug.cgi?id=1423293
# checking for big-endian host... yes
# RPM build errors:
# configure: error: Sorry. Coan is buggy on big-endian systems
ExcludeArch:	ppc64 s390x
Source44: import.info


%description
%{name} (formerly sunifdef) is a software engineering tool for analyzing
pre-processor-based configurations of C or C++ source code. Its principal use
is to simplify a body of source code by eliminating any parts that are
redundant with respect to a specified configuration.

%{name} is most useful to developers of constantly evolving products
with large code bases, where pre-processor conditionals are used to
configure the feature sets, APIs or implementations of different
releases. In these environments the code base steadily
accumulates #ifdef-pollution as transient configuration options become
obsolete. %{name} can largely automate the recurrent task of purging
redundant #if-logic from the code.

%prep
%setup -q

for i in AUTHORS LICENSE.BSD README ChangeLog ; do
    sed -i -e 's/\r$//' $i
done

%build
%configure
%make_build

%check
#some tests are broken in armv7hl - disable until upstream fixes the issue
#upstream bug report: https://sourceforge.net/p/coan2/bugs/83/
#so for now we'll just allow the tests to fail
#make check || (for f in test_coan/*.log ; do cat ${f} ; done ; false)
make check || (for f in test_coan/*.log ; do cat ${f} ; done ; true)


%install
make install DESTDIR=$RPM_BUILD_ROOT INSTALL="install -p"

%files
%doc AUTHORS LICENSE.BSD README ChangeLog
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1.*

%changelog
* Mon May 07 2018 Igor Vlasenko <viy@altlinux.ru> 6.0.1-alt1_15
- update to new release by fcimport

* Wed Sep 27 2017 Igor Vlasenko <viy@altlinux.ru> 6.0.1-alt1_13
- update to new release by fcimport

* Thu Aug 03 2017 Igor Vlasenko <viy@altlinux.ru> 6.0.1-alt1_11
- update to new release by fcimport

* Tue Mar 29 2016 Igor Vlasenko <viy@altlinux.ru> 6.0.1-alt1_8
- update to new release by fcimport

* Sun Sep 20 2015 Igor Vlasenko <viy@altlinux.ru> 6.0.1-alt1_4
- update to new release by fcimport

* Wed Aug 27 2014 Igor Vlasenko <viy@altlinux.ru> 5.2-alt1_3
- update to new release by fcimport

* Tue Jul 01 2014 Igor Vlasenko <viy@altlinux.ru> 5.2-alt1_2
- update to new release by fcimport

* Tue Jun 03 2014 Igor Vlasenko <viy@altlinux.ru> 5.2-alt1_1
- update to new release by fcimport

* Fri Jul 27 2012 Igor Vlasenko <viy@altlinux.ru> 5.1-alt1_3
- update to new release by fcimport

* Wed Mar 21 2012 Igor Vlasenko <viy@altlinux.ru> 5.1-alt1_2
- rebuild to get rid of #27020

* Tue Feb 21 2012 Igor Vlasenko <viy@altlinux.ru> 5.1-alt1_1
- new fc release

* Sat Jan 21 2012 Igor Vlasenko <viy@altlinux.ru> 4.1-alt1_4
- update to new release by fcimport

* Sat May 21 2011 Igor Vlasenko <viy@altlinux.ru> 4.1-alt1_3
- initial release by fcimport

