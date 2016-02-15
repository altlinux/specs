# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-python
BuildRequires: gcc-c++
# END SourceDeps(oneline)
%add_optflags %optflags_shared
Name:           libvoikko
Version:        3.7.1
Release:        alt1_4
Summary:        Voikko is a library for spellcheckers and hyphenators

Group:          System/Libraries
License:        GPLv2+
URL:            http://voikko.puimula.org
# The usual format of stable release URLs
Source0:        http://www.puimula.org/voikko-sources/%{name}/%{name}-%{version}.tar.gz
# The usual format of test release URLs
#Source0:        http://www.puimula.org/htp/testing/%%{name}-%%{version}rc1.tar.gz

BuildRequires:  python-devel
# Require the Finnish morphology because Finnish is currently the only language
# supported by libvoikko in Fedora.
Requires:       malaga-suomi-voikko
Source44: import.info

%description
This is libvoikko, library for spellcheckers and hyphenators using Malaga
natural language grammar development tool. The library is written in C.

Currently only Finnish is supported, but the API of the library has been
designed to allow adding support for other languages later. Note however that
Malaga is rather low level tool that requires implementing the whole morphology
of a language as a left associative grammar. Therefore languages that have
simple or even moderately complex morphologies and do not require morphological
analysis in their hyphenators should be implemented using other tools such as
Hunspell.

%package        devel
Summary:        Development files for %{name}
Group:          Development/C
Requires:       %{name}%{?_isa} = %{version}
Requires:       pkgconfig

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%package -n     voikko-tools
Summary:        Test tools for %{name}
Group:          Text tools
Requires:       %{name}%{?_isa} = %{version}

%description -n voikko-tools
This package contains voikkospell and voikkohyphenate, small command line
tools for testing libvoikko. These tools may also be useful for shell
scripts.

%package -n python-module-libvoikko
Summary:        Python interface to %{name}
Group:          Development/C
Requires:       %{name} = %{version}
# Note: noarch subpackage, only works in Fedora >= 11
BuildArch:      noarch

%description -n python-module-libvoikko
Python interface to libvoikko, library of Finnish language tools.
This module can be used to perform various natural language analysis
tasks on Finnish text.


%prep
%setup -q


%build
# The dictionary path must be the same where malaga-suomi-voikko is installed
%configure --with-dictionary-path=%{_libdir}/voikko
# Remove rpath,
# https://fedoraproject.org/wiki/Packaging/Guidelines#Removing_Rpath
sed -i 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' libtool
sed -i 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' libtool
make %{?_smp_mflags}


%install
make install INSTALL="install -p" DESTDIR=$RPM_BUILD_ROOT
find $RPM_BUILD_ROOT -name '*.la' -exec rm -f {} ';'
# Remove static archive
find $RPM_BUILD_ROOT -name '*.a' -exec rm -f {} ';'
# Install the Python interface
install -d $RPM_BUILD_ROOT%{python_sitelibdir_noarch}
install -pm 0644 python/libvoikko.py $RPM_BUILD_ROOT%{python_sitelibdir_noarch}/


%files
%doc ChangeLog COPYING README
%{_libdir}/*.so.*

%files -n voikko-tools
%{_bindir}/voikkospell
%{_bindir}/voikkohyphenate
%{_bindir}/voikkogc
%{_mandir}/man1/voikkohyphenate.1*
%{_mandir}/man1/voikkospell.1*
%{_mandir}/man1/voikkogc.1*

%files devel
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/pkgconfig/libvoikko.pc

%files -n python-module-libvoikko
%{python_sitelibdir_noarch}/%{name}.py*

%changelog
* Mon Feb 15 2016 Igor Vlasenko <viy@altlinux.ru> 3.7.1-alt1_4
- update to new release by fcimport

* Sun Sep 20 2015 Igor Vlasenko <viy@altlinux.ru> 3.7.1-alt1_3
- update to new release by fcimport

* Wed Dec 17 2014 Igor Vlasenko <viy@altlinux.ru> 3.7.1-alt1_1
- update to new release by fcimport

* Wed Aug 27 2014 Igor Vlasenko <viy@altlinux.ru> 3.7-alt1_3
- update to new release by fcimport

* Tue Jul 01 2014 Igor Vlasenko <viy@altlinux.ru> 3.7-alt1_2
- update to new release by fcimport

* Tue Feb 25 2014 Igor Vlasenko <viy@altlinux.ru> 3.7-alt1_1
- update to new release by fcimport

* Tue Oct 22 2013 Igor Vlasenko <viy@altlinux.ru> 3.6.1-alt1_1
- update to new release by fcimport

* Wed Jul 31 2013 Igor Vlasenko <viy@altlinux.ru> 3.6-alt1_3
- update to new release by fcimport

* Tue Apr 16 2013 Igor Vlasenko <viy@altlinux.ru> 3.6-alt1_1
- update to new release by fcimport

* Fri Feb 22 2013 Igor Vlasenko <viy@altlinux.ru> 3.5-alt1_3
- update to new release by fcimport

* Fri Jul 27 2012 Igor Vlasenko <viy@altlinux.ru> 3.5-alt1_2
- update to new release by fcimport

* Thu Jul 19 2012 Igor Vlasenko <viy@altlinux.ru> 3.5-alt1_1
- update to new release by fcimport

* Wed May 09 2012 Igor Vlasenko <viy@altlinux.ru> 3.4.1-alt1_2
- update to new release by fcimport

* Tue Feb 21 2012 Igor Vlasenko <viy@altlinux.ru> 3.4.1-alt1_1
- update to new release by fcimport

* Tue Jan 10 2012 Igor Vlasenko <viy@altlinux.ru> 3.4-alt1_1
- update to new release by fcimport

* Fri Dec 23 2011 Igor Vlasenko <viy@altlinux.ru> 3.3.1-alt2_0.3.rc1
- spec cleanup thanks to ldv@

* Sun Dec 18 2011 Igor Vlasenko <viy@altlinux.ru> 3.3.1-alt1_0.3.rc1
- initial import by fcimport

