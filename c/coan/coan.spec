# BEGIN SourceDeps(oneline):
BuildRequires: gcc-c++
# END SourceDeps(oneline)
BuildRequires: /usr/bin/pod2man /usr/bin/pod2html
Name:		coan
Version: 	5.1
Release: 	alt1_2
Summary: 	A command line tool for simplifying the pre-processor conditionals in source code
Group: 		Development/Tools
License: 	BSD       
URL: 		http://coan2.sourceforge.net/
Source0: 	http://downloads.sourceforge.net/coan2/%{name}-%{version}.tar.gz

# Note: coan was formerly called sunifdef i.e sunifdef was renamed to coan
# with the 4.0 release. This Provides can be removed in F-16.
Provides:      sunifdef = %{version}-%{release}
Obsoletes:     sunifdef < 4.0
Source44: import.info

# Beware: the '#' may never be the first non-blank character on a line,
# it would be interpreted as a comment.
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
make %{?_smp_mflags}

%check
make check

%install
make install DESTDIR=$RPM_BUILD_ROOT INSTALL="install -p"

%files
%doc AUTHORS LICENSE.BSD README ChangeLog
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1.*

%changelog
* Wed Mar 21 2012 Igor Vlasenko <viy@altlinux.ru> 5.1-alt1_2
- rebuild to get rid of #27020

* Tue Feb 21 2012 Igor Vlasenko <viy@altlinux.ru> 5.1-alt1_1
- new fc release

* Sat Jan 21 2012 Igor Vlasenko <viy@altlinux.ru> 4.1-alt1_4
- update to new release by fcimport

* Sat May 21 2011 Igor Vlasenko <viy@altlinux.ru> 4.1-alt1_3
- initial release by fcimport

