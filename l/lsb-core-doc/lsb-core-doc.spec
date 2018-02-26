Name: lsb-core-doc
Version: 3.1.0
Release: alt0.1.qa1

Summary: Linux Standard Base Core Specification %version

License: FDL
Group: Documentation
Url: http://linuxbase.org

Packager: Vitaly Lipatov <lav@altlinux.ru>

BuildArch: noarch

Source: http://refspecs.freestandards.org/LSB_%version/LSB-Core-generic/LSB-Core-generic.html.bz2
Source1: http://refspecs.freestandards.org/LSB_%version/LSB-Core-generic/LSB-Core-generic.pdf.bz2

BuildRequires: bzip2

%description
Linux Standard Base Core Specification %version

%install
%define docdir %buildroot/%_docdir/%name-%version
mkdir -p %docdir
cp %SOURCE0 %SOURCE1 %docdir
bunzip %docdir/*.bz2

%files
%_docdir/%name-%version/*
# The package does not own its own docdir subdirectory.
# The line below is added by repocop to fix this bug in a straightforward way. 
# Another way is to rewrite the spec to use relative doc paths.
%dir %_docdir/lsb-core-doc-%version 

%changelog
* Tue Nov 24 2009 Repocop Q. A. Robot <repocop@altlinux.org> 3.1.0-alt0.1.qa1
- NMU (by repocop): the following fixes applied:
  * docdir-is-not-owned for lsb-core-doc
  * postclean-05-filetriggers for spec file

* Sat Feb 25 2006 Vitaly Lipatov <lav@altlinux.ru> 3.1.0-alt0.1
- initial build for ALT Linux Sisyphus

