# BEGIN SourceDeps(oneline):
BuildRequires: rpm-build-python3
# END SourceDeps(oneline)
Group: Other
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
Name:           zchunk
Version:        1.2.4
Release:        alt1_1
Summary:        Compressed file format that allows easy deltas
License:        BSD and MIT
URL:            https://github.com/zchunk/zchunk
Source0:        https://github.com/zchunk/zchunk/archive/%{version}/%{name}-%{version}.tar.gz
BuildRequires:  gcc
BuildRequires:  pkgconfig(libzstd)
BuildRequires:  pkgconfig(libcurl)
BuildRequires:  pkgconfig(openssl)
BuildRequires:  meson
Requires:       %{name}-libs = %{version}-%{release}
Provides:       bundled(buzhash-urlblock) = 0.1
Source44: import.info

%description
zchunk is a compressed file format that splits the file into independent
chunks.  This allows you to only download the differences when downloading a
new version of the file, and also makes zchunk files efficient over rsync.
zchunk files are protected with strong checksums to verify that the file you
downloaded is in fact the file you wanted.

%package libs
Group: Other
Summary: Zchunk library

%description libs
zchunk is a compressed file format that splits the file into independent
chunks.  This allows you to only download the differences when downloading a
new version of the file, and also makes zchunk files efficient over rsync.
zchunk files are protected with strong checksums to verify that the file you
downloaded is in fact the file you wanted.

This package contains the zchunk library, libzck.

%package devel
Group: Other
Summary: Headers for building against zchunk
Requires: %{name}-libs = %{version}-%{release}

%description devel
zchunk is a compressed file format that splits the file into independent
chunks.  This allows you to only download the differences when downloading a
new version of the file, and also makes zchunk files efficient over rsync.
zchunk files are protected with strong checksums to verify that the file you
downloaded is in fact the file you wanted.

This package contains the headers necessary for building against the zchunk
library, libzck.

%prep
%setup -q

# Remove bundled sha libraries
rm -rf src/lib/hash/sha*

%build
%meson -Dwith-openssl=enabled -Dwith-zstd=enabled
%meson_build -j1

%install
%meson_install
mkdir -p %{buildroot}%{_libexecdir}
install contrib/gen_xml_dictionary %{buildroot}%{_libexecdir}/zck_gen_xml_dictionary

%check
#meson_test -j1



%files
%doc README.md contrib
%{_bindir}/zck*
%{_bindir}/unzck
%{_libexecdir}/zck_gen_xml_dictionary
%{_mandir}/man1/**

%files libs
%doc --no-dereference LICENSE
%doc README.md
%{_libdir}/libzck.so.*

%files devel
%doc zchunk_format.txt
%{_libdir}/libzck.so
%{_libdir}/pkgconfig/zck.pc
%{_includedir}/zck.h

%changelog
* Sat Feb 25 2023 Igor Vlasenko <viy@altlinux.org> 1.2.4-alt1_1
- update to new release by fcimport

* Sat Dec 24 2022 Igor Vlasenko <viy@altlinux.org> 1.2.3-alt1_1
- update to new release by fcimport

* Sat May 07 2022 Igor Vlasenko <viy@altlinux.org> 1.2.2-alt1_1
- update to new release by fcimport

* Tue Sep 21 2021 Igor Vlasenko <viy@altlinux.org> 1.1.15-alt1_3
- update to new release by fcimport

* Thu Jul 08 2021 Igor Vlasenko <viy@altlinux.org> 1.1.15-alt1_1
- update to new release by fcimport

* Tue May 18 2021 Igor Vlasenko <viy@altlinux.org> 1.1.11-alt1_1
- new version

* Mon Jan 25 2021 Igor Vlasenko <viy@altlinux.ru> 1.1.9-alt1_1
- update to new release by fcimport

* Wed Feb 26 2020 Igor Vlasenko <viy@altlinux.ru> 1.1.5-alt1_2
- new version

* Fri Dec 06 2019 Igor Vlasenko <viy@altlinux.ru> 1.1.4-alt1_1
- new version

* Sat May 25 2019 Igor Vlasenko <viy@altlinux.ru> 1.1.2-alt1_2
- update to new release by fcimport

* Thu Feb 14 2019 Igor Vlasenko <viy@altlinux.ru> 1.0.3-alt1_2
- new version

* Sat Dec 29 2018 Igor Vlasenko <viy@altlinux.ru> 1.0.0-alt1_1
- new version

