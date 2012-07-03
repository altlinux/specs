Name: perl-xCAT
Version: 2.5.1
Release: alt0.4.2
License: EPL
Summary: xCAT perl libraries
Url: http://xcat.sourceforge.net/
Group: Development/Perl
Source: perl-xCAT-%{version}.tar
Packager: Andriy Stepanov <stanv@altlinux.ru>
BuildArch: noarch
BuildRequires: perl-DBI perl-Storable perl-Text-Balanced perl-XML-Simple perl-SNMP
BuildRequires: perl-Expect perl-libwww perl-SOAP-Lite
BuildRequires: perl-Math-BigInt
BuildRequires: perl-podlators
BuildRequires: perl-Digest-SHA1
BuildRequires: perl-HTML-Form

%description
Provides perl xCAT libraries for core functionality.  Required for all xCAT installations.
Includes xCAT::Table, xCAT::NodeRange, among others.

# XXX: stanv@
%add_findreq_skiplist %{perl_vendor_privlib}/xCAT/DSHCLI.pm
# XXX: stanv@ see bug: https://sourceforge.net/tracker/?func=detail&aid=2972471&group_id=208749&atid=1006945
%add_findreq_skiplist %{perl_vendor_privlib}/xCAT/Template.pm

%prep
%setup -q

%build

# Modify the Version() function in xCAT/Utils.pm to automatically have the correct version
./modifyUtils %{version}

# Build the pod version of the man pages for each DB table.  It puts them in the man5 and man7 subdirs.
# Then convert the pods to man pages and html pages.
./db2man

install -d -pm 755 %{buildroot}%{perl_vendor_privlib}/xCAT/data

install -D -pm 644 xCAT/*.pm      %{buildroot}%{perl_vendor_privlib}/xCAT

install -D -pm 644 xCAT/data/*.pm %{buildroot}%{perl_vendor_privlib}/xCAT/data

# These were built dynamically in the build phas
install -d -pm 755 %{buildroot}%{_man5dir}
install -d -pm 755 %{buildroot}%{_man7dir}

install -D -pm 644 share/man/man5/* %{buildroot}%{_man5dir}
install -D -pm 644 share/man/man7/* %{buildroot}%{_man7dir}

%files
%doc LICENSE.html README
%doc %_mandir/*/*
%{perl_vendor_privlib}/xCAT

%changelog
* Tue Apr 19 2011 Andriy Stepanov <stanv@altlinux.ru> 2.5.1-alt0.4.2
- Fix rebuild passthrough for Sisyphus #2.

* Thu Mar 10 2011 Andriy Stepanov <stanv@altlinux.ru> 2.5.1-alt0.4.1
- Fix rebuild passthrough for Sisyphus.

* Wed Nov 24 2010 Andriy Stepanov <stanv@altlinux.ru> 2.5.1-alt0.4
- Update from upstream SVN: trunk@8256

* Mon Nov 22 2010 Andriy Stepanov <stanv@altlinux.ru> 2.5.1-alt0.3
- Update from upstream SVN: trunk@8225

* Mon Nov 15 2010 Andriy Stepanov <stanv@altlinux.ru> 2.5.1-alt0.2
- Update from upstream SVN: trunk@8159

* Thu Oct 28 2010 Andriy Stepanov <stanv@altlinux.ru> 2.5.1-alt0.1
- Update from upstream SVN: trunk@7954

* Fri Oct 22 2010 Andriy Stepanov <stanv@altlinux.ru> 2.4.4-alt0.4
- Update from upstream SVN: trunk@7904

* Wed Oct 06 2010 Andriy Stepanov <stanv@altlinux.ru> 2.4.4-alt0.3
- Update from upstream SVN: trunk@7759

* Fri Sep 17 2010 Andriy Stepanov <stanv@altlinux.ru> 2.4.4-alt0.2
- Update from upstream SVN: trunk@7490

* Fri Sep 10 2010 Andriy Stepanov <stanv@altlinux.ru> 2.4.4-alt0.1
- Update from upstream SVN: trunk@7385

* Sun Jun 27 2010 Andriy Stepanov <stanv@altlinux.ru> 2.4.3-alt0.1
- Update from upstream SVN: trunk@6611

* Mon Jun 21 2010 Andriy Stepanov <stanv@altlinux.ru> 2.4.2-alt0.2
- Update from upstream SVN: trunk@6560

* Wed Jun 02 2010 Andriy Stepanov <stanv@altlinux.ru> 2.4.2-alt0.1
- Update from upstream SVN: trunk@6312

* Mon May 24 2010 Andriy Stepanov <stanv@altlinux.ru> 2.3.5-alt0.4
- Update from upstream SVN: trunk@6208

* Wed Apr 21 2010 Andriy Stepanov <stanv@altlinux.ru> 2.3.5-alt0.3
- Update from upstream SVN: trunk@5831

* Thu Mar 25 2010 Andriy Stepanov <stanv@altlinux.ru> 2.3.5-alt0.2
- Merge patches branch.

* Thu Mar 18 2010 Andriy Stepanov <stanv@altlinux.ru> 2.3.5-alt0.1
- Update from upstream SVN: trunk@5517

* Tue Mar 02 2010 Andriy Stepanov <stanv@altlinux.ru> 2.3.3-alt0.6
- Update from upstream SVN: trunk@5320.

* Tue Feb 09 2010 Andriy Stepanov <stanv@altlinux.ru> 2.3.3-alt0.5
- Move to std dir locations

* Thu Jan 21 2010 Andriy Stepanov <stanv@altlinux.ru> 2.3.3-alt0.3
- Update from upstream SVN: trunk@5004.

* Tue Jan 19 2010 Andriy Stepanov <stanv@altlinux.ru> 2.3.3-alt0.2
- Update from upstream SVN: trunk@4978.

* Mon Jan 11 2010 Andriy Stepanov <stanv@altlinux.ru> 2.3.3-alt0.1
- Update from upstream SVN.

* Fri Dec 11 2009 Andriy Stepanov <stanv@altlinux.ru> 2.3.2-alt0.1
- Update from upstream SVN.

* Thu Nov 12 2009 Andriy Stepanov <stanv@altlinux.ru> 2.3-alt0.3
- Update from upstream SVN.

* Tue Nov 03 2009 Andriy Stepanov <stanv@altlinux.ru> 2.3-alt0.2
- Update from upstream SVN.

* Wed Oct 28 2009 Andriy Stepanov <stanv@altlinux.ru> 2.3-alt0.1
- Package for ATL Linux.

