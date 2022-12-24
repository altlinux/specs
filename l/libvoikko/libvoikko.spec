# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-python3
BuildRequires: libtinyxml2-devel
# END SourceDeps(oneline)
Group: System/Libraries
%add_optflags %optflags_shared
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
%global _hardened_build 1

Name:           libvoikko
Version:        4.3.1
Release:        alt1_6
Summary:        Voikko is a library for spellcheckers and hyphenators

License:        GPL-2.0-or-later
URL:            https://voikko.puimula.org
# The usual format of stable release URLs
Source0:        https://www.puimula.org/voikko-sources/%{name}/%{name}-%{version}.tar.gz
# The usual format of test release URLs
#Source0:        https://www.puimula.org/htp/testing/%%{name}-%%{version}rc1.tar.gz

# See https://voikko.puimula.org/sources.html for the key fingerprint.
# I did
#  gpg --recv-keys "AC5D 65F1 0C85 96D7 E2DA  E263 3D30 9B60 4AE3 942E"
# and then
#  gpg2 --export --export-options export-minimal AC5D65F10C8596D7E2DAE2633D309B604AE3942E > gpgkey-AC5D65F10C8596D7E2DAE2633D309B604AE3942E.gpg
Source1:        http://www.puimula.org/voikko-sources/%{name}/%{name}-%{version}.tar.gz.asc
Source2:        gpgkey-AC5D65F10C8596D7E2DAE2633D309B604AE3942E.gpg

Requires: voikko-fi
BuildRequires:  gcc-c++
BuildRequires:  python3-devel
BuildRequires: gnupg2
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
Group: Development/Other
Summary:        Development files for %{name}
Requires:       %{name} = %{version}-%{release}
Requires:       pkgconfig

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%package -n     voikko-tools
Group: Text tools
Summary:        Test tools for %{name}
Requires:       %{name} = %{version}-%{release}

%description -n voikko-tools
This package contains voikkospell and voikkohyphenate, small command line
tools for testing libvoikko. These tools may also be useful for shell
scripts.

%package -n python3-module-libvoikko
Group: Development/Other
Summary:        Python interface to %{name}
Requires:       %{name} = %{version}-%{release}
BuildArch:      noarch

%description -n python3-module-libvoikko
Python interface to libvoikko, library of Finnish language tools.
This module can be used to perform various natural language analysis
tasks on Finnish text.

%prep

%setup -q



%build
# Use vfst for now, no hfst yet. We need to package hfst-ospell for the hfst dictionaries.
# Use /usr/lib/voikko for the dictionaries, this is where the voikko-fi package will put them.
# The dictonary path has been agreed on in reviews and fedora-devel discussions.
# This way the voikko-fi package can be noarch.
%configure --disable-hfst --with-dictionary-path=%{_prefix}/lib/voikko
# Remove rpath,
# https://fedoraproject.org/wiki/Packaging/Guidelines#Removing_Rpath
sed -i 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' libtool
sed -i 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' libtool
%make_build CXXFLAGS="$CXXFLAGS"


%install
make install INSTALL="install -p" DESTDIR=$RPM_BUILD_ROOT
find $RPM_BUILD_ROOT -name '*.la' -exec rm -f {} ';'
# Remove static archive
find $RPM_BUILD_ROOT -name '*.a' -exec rm -f {} ';'
# Install the Python interface
install -d $RPM_BUILD_ROOT%{python3_sitelibdir_noarch}
install -pm 0644 python/libvoikko.py $RPM_BUILD_ROOT%{python3_sitelibdir_noarch}/
# Make the directory for the dictionary data files, so this package can own it.
mkdir -p %{buildroot}%{_prefix}/lib/voikko


%files
%doc ChangeLog README
%doc --no-dereference COPYING
%dir %{_prefix}/lib/voikko
%{_libdir}/libvoikko.so.1*

%files -n voikko-tools
%{_bindir}/voikkospell
%{_bindir}/voikkohyphenate
%{_bindir}/voikkogc
%{_bindir}/voikkovfstc
%{_mandir}/man1/voikkohyphenate.1*
%{_mandir}/man1/voikkospell.1*
%{_mandir}/man1/voikkogc.1*
%{_mandir}/man1/voikkovfstc.1*

%files devel
%{_includedir}/*
%{_libdir}/libvoikko.so
%{_libdir}/pkgconfig/libvoikko.pc

%files -n python3-module-libvoikko
%{python3_sitelibdir_noarch}/%{name}.py
%{python3_sitelibdir_noarch}/__pycache__/%{name}.cpython-3*.pyc
%{python3_sitelibdir_noarch}/__pycache__/%{name}.cpython-3*.opt-?.pyc

%changelog
* Sat Dec 24 2022 Igor Vlasenko <viy@altlinux.org> 4.3.1-alt1_6
- update to new release by fcimport

* Fri Dec 17 2021 Igor Vlasenko <viy@altlinux.org> 4.3.1-alt1_2
- update to new release by fcimport

* Sat Jul 24 2021 Igor Vlasenko <viy@altlinux.org> 4.3.1-alt1_0
- bootstrap w/o voikko-fi dependency

* Thu Oct 17 2019 Igor Vlasenko <viy@altlinux.ru> 4.1.1-alt1_5
- update to new release by fcimport

* Wed Oct 10 2018 Igor Vlasenko <viy@altlinux.ru> 4.1.1-alt1_1
- update to new release by fcimport

* Sat Jul 14 2018 Igor Vlasenko <viy@altlinux.ru> 3.8-alt1_10
- update to new release by fcimport

* Fri May 25 2018 Igor Vlasenko <viy@altlinux.ru> 3.8-alt1_9
- update to new release by fcimport

* Mon May 07 2018 Igor Vlasenko <viy@altlinux.ru> 3.8-alt1_8
- update to new release by fcimport

* Wed Sep 27 2017 Igor Vlasenko <viy@altlinux.ru> 3.8-alt1_6
- update to new release by fcimport

* Wed Sep 21 2016 Igor Vlasenko <viy@altlinux.ru> 3.8-alt1_2
- update to new release by fcimport

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

