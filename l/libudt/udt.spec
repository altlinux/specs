# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-fedora-compat
# END SourceDeps(oneline)
Group: Development/C
%add_optflags %optflags_shared
%define oldname udt
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
Name:		libudt
Version:	4.11
Release:	alt1_14
Summary:	UDP based Data Transfer Protocol

License:	BSD
URL:		http://udt.sourceforge.net/
Source0:	http://downloads.sourceforge.net/project/udt/udt/%{version}/udt.sdk.%{version}.tar.gz
Patch:		udt.sdk.4.11-link-as-needed.patch

BuildRequires:	gcc-c++
Source44: import.info
Provides: udt = %{version}-%{release}

%package devel
Group: Development/C
Summary:	UDP based Data Transfer Protocol - development files
Requires:	%{name} = %{version}-%{release}
Provides: udt-devel = %{version}-%{release}

%description
UDT is a reliable UDP based application level data transport protocol
for distributed data intensive applications over wide area high-speed
networks. UDT uses UDP to transfer bulk data with its own reliability
control and congestion control mechanisms. The new protocol can
transfer data at a much higher speed than TCP does. UDT is also a
highly configurable framework that can accommodate various congestion
control algorithms.

%description devel
UDT development files.

%prep
%setup -q -n udt4
%patch -p1

sed 's!-O3!%{optflags}!' -i src/Makefile app/Makefile
sed 's!-shared!& %{?__global_ldflags} -lpthread -Wl,-soname,libudt.so.0!' \
    -i src/Makefile
sed 's!LDFLAGS =!& %{?__global_ldflags}!' -i app/Makefile
sed 's/\r//' -i doc/doc/udtdoc.css

%build
ARCH=
%ifarch %{ix86}
ARCH=IA32
%endif
%ifarch x86_64
ARCH=AMD64
%endif
%ifarch ia64
ARCH=IA64
%endif

# Parallel build fails - no _smp_mflags
make arch=$ARCH

%install
mkdir -p %{buildroot}%{_libdir}
install src/libudt.so %{buildroot}%{_libdir}/libudt.so.0
ln -s libudt.so.0 %{buildroot}%{_libdir}/libudt.so
mkdir -p %{buildroot}%{_includedir}/udt
install -p -m 644 src/*.h %{buildroot}%{_includedir}/udt



%files
%{_libdir}/libudt.so.0
%doc RELEASE_NOTES.txt
%doc --no-dereference LICENSE.txt

%files devel
%{_libdir}/libudt.so
%{_includedir}/udt
%doc doc

%changelog
* Sun Mar 03 2019 Igor Vlasenko <viy@altlinux.ru> 4.11-alt1_14
- new version

