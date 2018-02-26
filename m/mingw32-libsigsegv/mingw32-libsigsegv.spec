BuildRequires: rpm-build-mingw32
%global __strip %{_mingw32_strip}
%global __objdump %{_mingw32_objdump}

Summary: MinGW library for handling page faults in user mode
Name:    mingw32-libsigsegv
Version: 2.6
Release: alt1_2

License: GPLv2+
URL:     http://libsigsegv.sourceforge.net/
Source0: http://ftp.gnu.org/gnu/libsigsegv/libsigsegv-%{version}.tar.gz
Group:   System/Libraries

## upstream patches
# based on:
# http://git.savannah.gnu.org/cgit/libsigsegv.git/patch/?id=4f14ef87b2fba9718c1a88b9ed9ca7ba111d60da
# http://git.savannah.gnu.org/cgit/libsigsegv.git/patch/?id=54b612e978e26a52b5706272dabf84ed9d895fa7
Patch100: libsigsegv-2.6-mystack.patch

BuildArch:      noarch
BuildRequires:  autoconf automake libtool
BuildRequires:  mingw32-filesystem >= 56
BuildRequires:  mingw32-binutils
BuildRequires:  mingw32-gcc
Source44: import.info


%description
MinGW library for handling memory faults and stack overflows in user mode.

%prep
%setup -q -n libsigsegv-%{version}

%patch100 -p1 -b .mystack
autoreconf


%build
%{_mingw32_configure} --disable-static --enable-shared
make %{?_smp_mflags}


%install
make install DESTDIR=%{buildroot}


%files
%doc AUTHORS COPYING NEWS README
%{_mingw32_bindir}/libsigsegv-0.dll
%{_mingw32_libdir}/libsigsegv.la
%{_mingw32_libdir}/libsigsegv.dll.a
%{_mingw32_includedir}/*.h


%changelog
* Thu Aug 18 2011 Igor Vlasenko <viy@altlinux.ru> 2.6-alt1_2
- initial release by fcimport

