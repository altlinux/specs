Name:           ccrypt
Version:        1.10
Release:        alt1
Summary:        Secure encryption and decryption of files and streams

Group:          System/Base
License:        GPLv2+
URL:            http://ccrypt.sourceforge.net/
Source0:        %{name}-%{version}.tar

BuildRequires:  gettext

%description
ccrypt is a utility for encrypting and decrypting files and streams.
It was designed as a replacement for the standard unix crypt utility,
which is notorious for using a very weak encryption algorithm.

%prep
%setup

%build
%configure --disable-static
make %{?_smp_mflags}

%install
%makeinstall_std
##rm %{buildroot}/usr/doc/ccrypt/ccrypt.html
%find_lang %{name}

%check
make check

%files -f %{name}.lang
%doc AUTHORS ChangeLog COPYING NEWS README doc/cypfaq01.txt
%{_mandir}/man*/*.*
%{_bindir}/cc*

%changelog
* Wed Sep 10 2014 Lenar Shakirov <snejok@altlinux.ru> 1.10-alt1
- First build for ALT (based on Fedora 1.10-6.fc21.src)

