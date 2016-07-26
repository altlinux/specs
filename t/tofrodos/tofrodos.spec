Group: Text tools
Name:           tofrodos
Version:        1.7.13
Release:        alt1_6
Summary:        Converts text files between MSDOS and Unix file formats
License:        GPLv2
URL:            http://www.thefreecountry.com/tofrodos/
Source0:        http://tofrodos.sourceforge.net/download/tofrodos-%{version}.tar.gz
Source44: import.info

%description
Tofrodos is a text file conversion utility that converts ASCII and Unicode 
UTF-8 files between the MSDOS (or Windows) format, which traditionally have 
CR/LF (carriage return/line feed) pairs as their new line delimiters, and 
the Unix format, which usually have LFs (line feeds) to terminate each line.

It is a useful utility to have around when you have to convert files between 
MSDOS (or Windows) and Unix/Linux/BSD (and her clones and variants). It comes 
standard with a number of systems and is often found on the system as "todos",
"fromdos", "dos2unix" and "unix2dos".

%prep
%setup -qn tofrodos

%build
make -C src/ TFLAG="%{optflags}" LDFLAGS="%{?__global_ldflags}" %{?_smp_mflags}

%install
mkdir -p %{buildroot}%{_bindir} %{buildroot}%{_mandir}/man1
make -C src/ install INSTALL="install -p" BINDIR="%{buildroot}%{_bindir}" MANDIR="%{buildroot}%{_mandir}/man1/" DESTDIR=%{buildroot}

%files
%doc COPYING readme.txt tofrodos.html
%{_bindir}/fromdos
%{_bindir}/todos
%{_mandir}/man1/fromdos.1*
%{_mandir}/man1/todos.1*

%changelog
* Tue Jul 26 2016 Igor Vlasenko <viy@altlinux.ru> 1.7.13-alt1_6
- update to new release by fcimport

* Sun Sep 20 2015 Igor Vlasenko <viy@altlinux.ru> 1.7.13-alt1_5
- update to new release by fcimport

* Wed Aug 27 2014 Igor Vlasenko <viy@altlinux.ru> 1.7.13-alt1_4
- update to new release by fcimport

* Tue Jul 01 2014 Igor Vlasenko <viy@altlinux.ru> 1.7.13-alt1_3
- update to new release by fcimport

* Thu Mar 06 2014 Igor Vlasenko <viy@altlinux.ru> 1.7.13-alt1_2
- moved to Sisyphus as dependency

