%define sname acpica-unix
Summary: Intel ASL compiler/decompiler
Summary(ru_RU.UTF-8): Компилятор/декомпилятор ASL от Intel
Name: iasl
Version: 20100806
Release: alt1
License: Distributable
Group: System/Kernel and hardware
URL: http://www.acpica.org/downloads/unix_source_code.php
Source: http://www.acpica.org/download/%sname-%{version}.tar
Conflicts: pmtools < 20071116-alt0.M50.1
# Automatically added by buildreq on Wed Jun 02 2004
BuildRequires: flex

%description

iasl compiles ASL (ACPI Source Language) into AML (ACPI Machine
Language). This AML is suitable for inclusion as a DSDT in system
firmware. It also can disassemble AML, for debugging purposes.

%description -l ru_RU.UTF-8
iasl позволяет компилировать ASL (ACPI Source Language) в AML (ACPI 
Machine Language). Результирующий AML может быть использован для включения в
таблицу DSDT в прошивку. Также iasl может декомпилировать (для отладки) AML.

%prep
%setup -q -n %sname-%version
# convert all UpperCased directories to LowerCase (fix for tarball from Intel)
#for i in `find * -type d|sort -r`;do newi=`echo $i|sed 's,/\?[a-z]*$,\L\0,i'`; [ "$i" = "$newi" ] || mv $i $newi;done


%build
pushd compiler
make
popd
pushd tools/acpixtract
make
popd
pushd tools/acpiexec
make clean
make
popd

%install
mkdir -p %buildroot%_bindir
install -m0755 compiler/iasl %buildroot%_bindir/
install -m0755 tools/acpixtract/acpixtract %buildroot%_bindir/
install -m0755 tools/acpiexec/acpiexec %buildroot%_bindir/

%files
%doc README
%_bindir/iasl
%_bindir/acpixtract
%_bindir/acpiexec

%changelog
* Tue Sep 14 2010 Anton Farygin <rider@altlinux.ru> 20100806-alt1
- new version

* Thu Sep 17 2009 Anton Farygin <rider@altlinux.ru> 20090903-alt1
- new version

* Wed Sep 02 2009 Anton Farygin <rider@altlinux.ru> 20090730-alt1
- new version

* Mon May 04 2009 Anton Farygin <rider@altlinux.ru> 20090422-alt1
- new version

* Tue Apr 07 2009 Anton Farygin <rider@altlinux.ru> 20090320-alt1
- new version

* Thu Mar 05 2009 Anton Farygin <rider@altlinux.ru> 20090220-alt1
- new version

* Mon Feb 09 2009 Anton Farygin <rider@altlinux.ru> 20090123-alt2
- added conflict with pmtools, older than 20071116-alt0.M50.1

* Wed Feb 04 2009 Anton Farygin <rider@altlinux.ru> 20090123-alt1
- new version
- build acpixtract and acpiexec tools

* Wed Feb 21 2007 Anton Farygin <rider@altlinux.ru> 20061109-alt1
- new version

* Tue Jul 04 2006 Anton Farygin <rider@altlinux.ru> 20060608-alt1
- new version

* Wed May 31 2006 Anton Farygin <rider@altlinux.ru> 20060512-alt1
- new version

* Thu Apr 13 2006 Anton Farygin <rider@altlinux.ru> 20060331-alt1
- new version

* Tue Aug 16 2005 Anton Farygin <rider@altlinux.ru> 20050624-alt1
- new version

* Tue Dec 21 2004 Anton Farygin <rider@altlinux.ru> 20041203-alt1
- new version

* Tue Aug 10 2004 Anton Farygin <rider@altlinux.ru> 20040715-alt1
- new version

* Wed Jun 02 2004 Anton Farygin <rider@altlinux.ru> 20040527-alt1
- new version

* Tue Apr 20 2004 Anton Farygin <rider@altlinux.ru> 20040402-alt1
- new version

* Mon Dec 08 2003 Anton Farygin <rider@altlinux.ru> 20031029-alt1
- first build for Sisyphus
