Name:           bcrypt
Version:        1.1
Release:        alt2_6
Summary:        File encryption utility

Group:          File tools
License:        BSD
URL:            http://%{name}.sourceforge.net/
Source0:        http://downloads.sourceforge.net/%{name}/%{name}-%{version}.tar.gz
BuildRequires:  zlib-devel
Source44: import.info


%description
Bcrypt is a cross platform file encryption utility. Encrypted files are
portable across all supported operating systems and processors.
Passphrases must be between 8 and 56 characters and are hashed internally
to a 448 bit key. However, all characters supplied are significant. The
stronger your passphrase, the more secure your data.

In addition to encrypting your data, bcrypt will by default overwrite the
original input file with random garbage three times before deleting it in
order to thwart data recovery attempts by persons who may gain access to
your computer. Bcrypt uses the blowfish encryption algorithm published by 
Bruce Schneier in 1993.


%prep
%setup -q

%{__perl} -pi.orig -e 's|\${PREFIX}/man/man1|\${PREFIX}/share/man/man1|g' Makefile


%build
%{__make} %{?_smp_mflags} CFLAGS="%{optflags}"


%install
%{__make} install PREFIX="%{buildroot}%{_prefix}"


%files
%doc LICENSE README
%doc %{_mandir}/man1/bcrypt.1*
%{_bindir}/bcrypt

%changelog
* Wed Mar 21 2012 Igor Vlasenko <viy@altlinux.ru> 1.1-alt2_6
- rebuild to get rid of #27020

* Sat Jan 21 2012 Igor Vlasenko <viy@altlinux.ru> 1.1-alt1_6
- update to new release by fcimport

* Thu Jul 07 2011 Igor Vlasenko <viy@altlinux.ru> 1.1-alt1_5
- initial release by fcimport

