Name: codeviz
Version: 1.0.11
Release: alt1.qa1.1

Summary: A call graph generation utility for C/C++

Url: http://www.skynet.ie/~mel/projects/codeviz/
License: distributable
Group: Development/Other

Packager: Vitaly Lipatov <lav@altlinux.ru>

Source: http://www.skynet.ie/~mel/projects/codeviz/%name-%version.tar.bz2
#Patch0: patch.new-options

BuildArch: noarch

# manually removed: rpm-build-mono
# Automatically added by buildreq on Tue Feb 06 2007 (-bi)
BuildRequires: perl-DBM
BuildRequires: perl-Pod-Parser perl-Math-Complex

%description
CodeViz provides the ability to generate call graphs to aid the task
of understanding code. It uses a highly modular set of collection
methods and can be adapted to support any language although only C and
C++ are currently supported.

%prep
%setup

%build
%install
mkdir -p -m 755 %buildroot/%_bindir %buildroot/%perl_vendor_privlib
install -m 755 bin/* %buildroot/%_bindir
cp -pr lib/* %buildroot/%perl_vendor_privlib

# It is the file in the package whose name matches the format emacs or vim uses 
# for backup and autosave files. It may have been installed by  accident.
find $RPM_BUILD_ROOT \( -name '*.swp' -o -name '#*#' -o -name '*~' \) -print -delete

%files
%_bindir/*
%perl_vendor_privlib/CodeViz/
%doc CHANGELOG README compilers graphs

%changelog
* Fri Nov 05 2010 Vladimir Lettiev <crux@altlinux.ru> 1.0.11-alt1.qa1.1
- rebuilt with perl 5.12

* Tue Nov 24 2009 Repocop Q. A. Robot <repocop@altlinux.org> 1.0.11-alt1.qa1
- NMU (by repocop): the following fixes applied:
  * backup-file-in-package for codeviz
  * postclean-05-filetriggers for spec file

* Tue Mar 27 2007 Vitaly Lipatov <lav@altlinux.ru> 1.0.11-alt1
- new version 1.0.11 (with rpmrb script)
- add Url

* Tue Feb 06 2007 Vitaly Lipatov <lav@altlinux.ru> 1.0.6-alt0.1
- initial build for ALT Linux Sisyphus

* Fri Oct 17 2003 Robert Lehr <bozzio@the-lehrs.com>
- initial revision for private RPM
