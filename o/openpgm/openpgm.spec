Group: System/Libraries
# BEGIN SourceDeps(oneline):
BuildRequires: /usr/bin/patch gcc-c++ perl(IO/File.pm) perl(IO/Handle.pm) perl(IPC/Open2.pm) perl(JSON.pm) perl(Net/SSH.pm) perl(Sys/Hostname.pm) perl(Time/HiRes.pm) python3-devel rpm-build-perl
# END SourceDeps(oneline)
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
Name:          openpgm
Version:       5.2.122
%global name_alias        pgm
%global version_main      5.2
%global version_dash_main 5-2
%global version_dash      %{version_dash_main}-122
Release:       alt1_21
Summary:       An implementation of the PGM reliable multicast protocol

# The license is LGPLv2.1
License:       LGPLv2
# New URL is https://github.com/steve-o/openpgm
# The files are now on https://code.google.com/archive/p/openpgm/downloads
URL:           https://github.com/steve-o/%{name}
Source0:       https://github.com/steve-o/%{name}/archive/release-%{version_dash}.tar.gz#/%{name}-%{version}.tar.gz

# All the following patches have been submitted upstream
# as a merge request: https://github.com/steve-o/openpgm/pull/64
Patch2:        openpgm-02-c-func.patch
Patch3:        openpgm-03-pkgconfig.patch
Patch4:        openpgm-04-py-version-gen.patch
Patch5:        openpgm-05-fix-setgid.patch

BuildRequires: libtool automake autoconf
BuildRequires: gcc
BuildRequires: python3
BuildRequires: dos2unix
BuildRequires: perl-devel
Source44: import.info


%description
OpenPGM is an open source implementation of the Pragmatic General
Multicast (PGM) specification in RFC 3208.


%package devel
Group: System/Libraries
Summary:       Development files for openpgm
Requires:      %{name} = %{version}-%{release}

%description devel
This package contains OpenPGM related development libraries and header files.


%prep
%setup -q -n %{name}-release-%{version_dash}/%{name}/%{name_alias}
%patch2 -p3
%patch3 -p3
%patch4 -p3
%patch5 -p3
dos2unix examples/getopt.c examples/getopt.h

libtoolize --force --copy
aclocal
autoheader
automake --copy --add-missing
autoconf
%configure

%build
%make_build

%install
%makeinstall_std

# Remove the static libraries and the temporary libtool artifacts
rm -f %{buildroot}%{_libdir}/lib%{name_alias}.{a,la}

# Move the header files into /usr/include
mv -f %{buildroot}%{_includedir}/%{name_alias}-%{version_main}/%{name_alias} %{buildroot}%{_includedir}/

%files
%doc COPYING LICENSE
%{_libdir}/*.so.*


%files devel
%doc examples/
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/pkgconfig/openpgm-5.2.pc


%changelog
* Mon Jan 13 2020 Igor Vlasenko <viy@altlinux.ru> 5.2.122-alt1_21
- fixed build

* Thu Mar 22 2018 Igor Vlasenko <viy@altlinux.ru> 5.2.122-alt1_3
- new version

