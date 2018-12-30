# BEGIN SourceDeps(oneline):
BuildRequires: gcc-c++ texinfo
# END SourceDeps(oneline)
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
Name:           malaga
Version:        7.12 
Release:        alt2_25
Summary:        A programming language for automatic language analysis

Group:          Development/Other
License:        GPLv2+
URL:            http://home.arcor.de/bjoern-beutel/malaga/
Source0:        http://home.arcor.de/bjoern-beutel/malaga/%{name}-%{version}.tgz
# Fix map_file symbol conflict with samba. Upstream can be considered
# inactive but as libvoikko >= 2.2 doesn't use libmalaga anymore, these kind
# of problems won't probably come up. The only executables in Fedora which
# link to libmalaga currently are the malaga tools.
Patch0:         malaga-rename-map_file.diff
# Malshow needs to be linked with -lm as Fedora's ld doesn't do implicit
# linking anymore
Patch1:         malaga-malshow-lm.patch
Patch2:         malaga-aarch64.patch

BuildRequires:  gcc
BuildRequires:  gtk-builder-convert gtk-demo libgail-devel libgtk+2-devel libgtk+2-gir-devel readline-devel
Requires: lib%{name} = %{version}-%{release}
Source44: import.info

%description
A software package for the development and application of
grammars that are used for the analysis of words and sentences of natural
languages. It is a language-independent system that offers a programming
language for the modelling of the language-dependent grammatical
information. This language is also called Malaga.

Malaga is based on the grammatical theory of the "Left Associative Grammar"
(LAG), developed by Roland Hausser, professor for Computational Linguistics at
University of Erlangen, Germany.

%package        devel
Summary:        Development files for %{name}
Group:          Development/Other
Requires:       lib%{name} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%package -n	lib%{name}
Summary:        Library files for %{name}
Group:          Development/Other

%description -n	lib%{name}
Library files for %{name}.


%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1
# Remove "@" marks so that the build process is more verbose
sed -i.debug -e 's|^\([ \t][ \t]*\)@|\1|' Makefile.in
# Remove "-s" so binaries won't be stripped
sed -i.strip -e 's| -s | |' Makefile.in
# Make libtool output more verbose
sed -i.silent -e 's|--silent||' Makefile.in

%build
%configure --with-readline
# Remove rpath,
# https://fedoraproject.org/wiki/Packaging/Guidelines#Removing_Rpath
sed -i 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' libtool
sed -i 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' libtool
%make_build


%install
make install DESTDIR=$RPM_BUILD_ROOT INSTALL_INFO=/sbin/install-info INSTALL="install -p"
rm -f $RPM_BUILD_ROOT%{_infodir}/dir
find $RPM_BUILD_ROOT -name '*.la' -exec rm -f {} ';'
# Remove static archive
find $RPM_BUILD_ROOT -name '*.a' -exec rm -f {} ';'
# Change permission of libmalaga.so*
chmod 0755 $RPM_BUILD_ROOT%{_libdir}/libmalaga.so*



%files
%{_infodir}/%{name}*
%{_bindir}/mal*
%{_datadir}/%{name}
%{_mandir}/man1/mal*

%files -n lib%{name}
%doc CHANGES.txt GPL.txt README.txt
%{_libdir}/lib%{name}.so.*

%files devel
%{_libdir}/lib%{name}*.so
%{_includedir}/malaga.h


%changelog
* Sun Dec 30 2018 Igor Vlasenko <viy@altlinux.ru> 7.12-alt2_25
- rebuild with readline7

* Wed Sep 27 2017 Igor Vlasenko <viy@altlinux.ru> 7.12-alt2_23
- update to new release by fcimport

* Thu Mar 16 2017 Igor Vlasenko <viy@altlinux.ru> 7.12-alt2_21
- update to new release by fcimport

* Tue Jul 26 2016 Igor Vlasenko <viy@altlinux.ru> 7.12-alt2_19
- update to new release by fcimport

* Thu Dec 03 2015 Igor Vlasenko <viy@altlinux.ru> 7.12-alt2_18.1
- NMU: added BR: texinfo

* Mon Nov 09 2015 Igor Vlasenko <viy@altlinux.ru> 7.12-alt2_18
- new version

* Mon Aug 12 2013 Igor Vlasenko <viy@altlinux.ru> 7.12-alt2_15
- update to new release by fcimport

* Tue Apr 16 2013 Igor Vlasenko <viy@altlinux.ru> 7.12-alt2_14
- update to new release by fcimport

* Fri Feb 22 2013 Igor Vlasenko <viy@altlinux.ru> 7.12-alt2_13
- update to new release by fcimport

* Fri Jul 27 2012 Igor Vlasenko <viy@altlinux.ru> 7.12-alt2_12
- update to new release by fcimport

* Wed Mar 21 2012 Igor Vlasenko <viy@altlinux.ru> 7.12-alt2_11
- rebuild to get rid of #27020

* Sat Jan 21 2012 Igor Vlasenko <viy@altlinux.ru> 7.12-alt1_11
- update to new release by fcimport

* Sun Dec 18 2011 Igor Vlasenko <viy@altlinux.ru> 7.12-alt1_10
- initial import by fcimport

