Group: System/Libraries
# BEGIN SourceDeps(oneline):
BuildRequires: swig
# END SourceDeps(oneline)
Name:           avl
Version:        3.35
Release:        alt1_5
Summary:        Aerodynamic and flight-dynamic analysis of rigid aircrafts

# Plotlib is LGPLv2+, the rest is GPLv2+
License:        GPLv2+ and LGPLv2+
URL:            http://web.mit.edu/drela/Public/web/avl/
Source0:        http://web.mit.edu/drela/Public/web/avl/avl%{version}.tgz
# The package does not ship a license file
Source1:        LICENSE.GPL
Source2:        LICENSE.LGPL
# Makefile variables and flags
Patch0:         avl3.35-makefile.patch

BuildRequires:  gcc-fortran libX11-devel
Requires:       fonts-bitmap-misc

# There was a previous, now orphaned package called avl in the repos
Conflicts: avl < 3.32-1
Source44: import.info


%description
AVL is a program for the aerodynamic and flight-dynamic analysis of rigid aircraft
of arbitrary configuration. It employs an extended vortex lattice model for
the lifting surfaces, together with a slender-body model for fuselages and nacelles.
General nonlinear flight states can be specified. The flight dynamic analysis
combines a full linearization of the aerodynamic model about any flight state,
together with specified mass properties. 


%prep
%setup -q -n Avl
%patch0 -p1
cp %{SOURCE1} .
cp %{SOURCE2} .


%build
export FFLAGS="%{optflags}"
export CFLAGS="%{optflags}"

make %{?_smp_mflags} -C plotlib
make %{?_smp_mflags} -C eispack
make %{?_smp_mflags} -C bin


%install
%makeinstall_std -C bin BINDIR=%{_bindir}


%files
%doc LICENSE.GPL LICENSE.LGPL version_notes.txt avl_doc.txt session1.txt session2.txt
%{_bindir}/avl


%changelog
* Mon Feb 15 2016 Igor Vlasenko <viy@altlinux.ru> 3.35-alt1_5
- update to new release by fcimport

* Sun Sep 20 2015 Igor Vlasenko <viy@altlinux.ru> 3.35-alt1_4
- update to new release by fcimport

* Wed Aug 27 2014 Igor Vlasenko <viy@altlinux.ru> 3.35-alt1_3
- update to new release by fcimport

* Tue Jul 01 2014 Igor Vlasenko <viy@altlinux.ru> 3.35-alt1_2
- update to new release by fcimport

* Tue Feb 25 2014 Igor Vlasenko <viy@altlinux.ru> 3.35-alt1_1
- update to new release by fcimport

* Tue Sep 24 2013 Igor Vlasenko <viy@altlinux.ru> 3.32-alt1_4
- update to new release by fcimport

* Mon Apr 15 2013 Igor Vlasenko <viy@altlinux.ru> 0.3.5-alt2_2
- fixed build

* Sat Jan 21 2012 Igor Vlasenko <viy@altlinux.ru> 0.3.5-alt1_2
- update to new release by fcimport

* Thu Jul 07 2011 Igor Vlasenko <viy@altlinux.ru> 0.3.5-alt1_1
- initial release by fcimport

