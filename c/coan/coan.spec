Group: Development/Other
# BEGIN SourceDeps(oneline):
BuildRequires: /usr/bin/time
# END SourceDeps(oneline)
BuildRequires: /usr/bin/pod2man /usr/bin/pod2html
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
Name:		coan
Version:	6.0.1
Release:	alt2_29
Summary:	A command line tool for simplifying the pre-processor conditionals in source code
License:	BSD
URL:		http://coan2.sourceforge.net/
Source0:	http://downloads.sourceforge.net/coan2/%{name}-%{version}.tar.gz
# https://sourceforge.net/p/coan2/bugs/92/
Patch0:         expression_parser.patch
# https://sourceforge.net/p/coan2/bugs/95/
Patch1:         coan-autoconf-c99.patch

BuildRequires:  gcc-c++
BuildRequires:  perl-podlators
BuildRequires:  perl-devel
BuildRequires:  autoconf automake

# removed python2 dependencies and asked upstream to port tests to python3
# https://sourceforge.net/p/coan2/bugs/93/

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
%patch0
%patch1


for i in AUTHORS LICENSE.BSD README ChangeLog ; do
    sed -i -e 's/\r$//' $i
done

%build
export CXXFLAGS="-std=c++14 $RPM_OPT_FLAGS"
autoreconf -vi
%configure
%make_build

# disabling all checks it's broken again on rawhide :(
# some tests are broken in armv7hl and ppc64le - disable until upstream
# fixes the issue upstream bug report:
#     https://sourceforge.net/p/coan2/bugs/83/
# so for now we'll just allow the tests to fail
#
# %ifnarch %{arm} ppc64le
# make check || (for f in test_coan/*.log ; do cat ${f} ; done ; false)
# %else
# make check || (for f in test_coan/*.log ; do cat ${f} ; done ; true)
# %endif


%install
%makeinstall_std

%files
%doc AUTHORS README ChangeLog
%doc --no-dereference LICENSE.BSD
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1*

%changelog
* Sat Dec 24 2022 Igor Vlasenko <viy@altlinux.org> 6.0.1-alt2_29
- update to new release by fcimport

* Sat Feb 27 2021 Igor Vlasenko <viy@altlinux.org> 6.0.1-alt2_25
- update to new release by fcimport

* Mon Jan 13 2020 Igor Vlasenko <viy@altlinux.ru> 6.0.1-alt2_20
- fixed build

* Wed Aug 07 2019 Igor Vlasenko <viy@altlinux.ru> 6.0.1-alt1_20
- update to new release by fcimport

* Wed Oct 10 2018 Igor Vlasenko <viy@altlinux.ru> 6.0.1-alt1_17
- update to new release by fcimport

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

