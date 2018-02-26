# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-fedora-compat
BuildRequires: /usr/bin/gtkdocize gcc-c++ glib2-devel imlib2-devel libXext-devel libfreetype-devel pkgconfig(freetype2) pkgconfig(gobject-2.0)
# END SourceDeps(oneline)
%add_optflags %optflags_shared
Name:           libhbalinux
Version:        1.0.13
Release:        alt2_3
Summary:        FC-HBAAPI implementation using scsi_transport_fc interfaces
Group:          System/Libraries
License:        LGPLv2
URL:            http://www.open-fcoe.org
Source0:        %{name}-%{version}.tar.gz
Patch0:         libhbalinux-1.0.13-conf.patch
Patch1:         libhbalinux-1.0.13-Set-SerialNumber-to-Unknown-if-not-found.patch
BuildRequires:  libhbaapi-devel libpciaccess-devel libtool automake
Requires:       libhbaapi
Source44: import.info

%description
SNIA HBAAPI vendor library built on top of the scsi_transport_fc interfaces.

%package devel
Summary:        A file needed for libhbalinux application development
Group:          Development/C
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description devel
The libhbalinux-devel package contains the library pkgconfig file.

%prep
%setup -q
%patch0 -p1 -b .conf
%patch1 -p1 -b .sn-unknown

%build
./bootstrap.sh
%configure --disable-static
make %{?_smp_mflags}

%install
make install DESTDIR=%{buildroot}
find %{buildroot} -name '*.la' -exec rm -f {} ';'
find %{buildroot} -name '*.so' -exec rm -f {} ';'

%post
ORG=org.open-fcoe.libhbalinux
LIB=%{_libdir}/libhbalinux.so.2.0.2
STR="$ORG	$LIB"
CONF=%{_sysconfdir}/hba.conf
if test -f $CONF; then
  grep -E -q ^[[:space:]]*$ORG[[:space:]]+$LIB $CONF
  if test $? -ne 0; then
    echo $STR >> $CONF;
  fi
fi

%postun
ORG=org.open-fcoe.libhbalinux
CONF=%{_sysconfdir}/hba.conf
if test -f $CONF; then
  grep -v $ORG $CONF > %{_sysconfdir}/hba.conf.new
  mv %{_sysconfdir}/hba.conf.new %{_sysconfdir}/hba.conf
fi

%files
%doc README COPYING
%{_libdir}/%{name}.so.*

%files devel
%{_libdir}/pkgconfig/%{name}.pc

%changelog
* Tue Feb 21 2012 Igor Vlasenko <viy@altlinux.ru> 1.0.13-alt2_3
- update to new release by fcimport

* Wed Feb 01 2012 Igor Vlasenko <viy@altlinux.ru> 1.0.13-alt2_2
- update to new release by fcimport

* Fri Dec 23 2011 Igor Vlasenko <viy@altlinux.ru> 1.0.13-alt2_1
- spec cleanup thanks to ldv@

* Sat Dec 17 2011 Igor Vlasenko <viy@altlinux.ru> 1.0.13-alt1_1
- initial import by fcimport

