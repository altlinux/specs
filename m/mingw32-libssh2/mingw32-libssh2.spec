BuildRequires: rpm-build-mingw32
%global __strip %{_mingw32_strip}
%global __objdump %{_mingw32_objdump}

Name:           mingw32-libssh2
Version:        1.1
Release:        alt1_6
Summary:        MinGW Windows library implementation of the SSH2 protocol

License:        BSD
Group:          System/Libraries
URL:            http://www.libssh2.org/
Source0:        http://downloads.sourceforge.net/libssh2/libssh2-%{version}.tar.gz

BuildArch:      noarch

BuildRequires:  mingw32-filesystem >= 49
BuildRequires:  mingw32-gcc
BuildRequires:  mingw32-binutils
BuildRequires:  mingw32-openssl
BuildRequires:  mingw32-zlib

Requires:       pkgconfig
Source44: import.info

%description
libssh2 is a library implementing the SSH2 protocol as defined by
Internet Drafts: SECSH-TRANS(22), SECSH-USERAUTH(25),
SECSH-CONNECTION(23), SECSH-ARCH(20), SECSH-FILEXFER(06)*,
SECSH-DHGEX(04), and SECSH-NUMBERS(10).


%package static
Summary:        Static version of the MinGW Windows SSH2 library
Requires:       %{name} = %{version}-%{release}
Group:          System/Libraries

%description static
Static version of the MinGW Windows SSH2 library.




%prep
%setup -q -n libssh2-%{version}


%build
%{_mingw32_configure} --enable-static --enable-shared
make %{?_smp_mflags}


%install
make DESTDIR=$RPM_BUILD_ROOT install

# Remove man pages which duplicate native Fedora.
rm -r $RPM_BUILD_ROOT%{_mingw32_mandir}/man3


%files
%doc COPYING
%{_mingw32_bindir}/libssh2-1.dll
%{_mingw32_libdir}/libssh2.dll.a
%{_mingw32_libdir}/libssh2.la
%{_mingw32_includedir}/libssh2.h
%{_mingw32_includedir}/libssh2_publickey.h
%{_mingw32_includedir}/libssh2_sftp.h


%files static
%{_mingw32_libdir}/libssh2.a


%changelog
* Wed Aug 17 2011 Igor Vlasenko <viy@altlinux.ru> 1.1-alt1_6
- initial release by fcimport

