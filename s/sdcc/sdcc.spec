Name: sdcc
Version: 5119
Release: alt1.qa2
Group: Development/C
URL: http://sdcc.sourceforge.net
License: GPL
Summary: Small Device C Compiler
Source: %name.tar
Patch: sdcc-5119-alt-glibc-2.11.3.patch
Patch1: sdcc-5119-alt-SDCCicode.patch
BuildPreReq: flex gcc-c++
%description
SDCC is a retargettable, optimizing ANSI - C compiler that targets the Intel 8051, 
Maxim 80DS390, Zilog Z80 and the Motorola 68HC08 based MCUs. Work is in progress 
on supporting the Microchip PIC16 and PIC18 series. SDCC is Free Open Source Software, 
distributed under GNU General Public License (GPL).
%prep
%setup -q -n %name
%patch -p2
%patch1 -p2
%build
%configure --disable-debug --docdir=%_docdir/%name-%version
%make_build
%install
%make_install DESTDIR=%buildroot install
rm -fr /usr/src/tmp/sdcc-buildroot/usr/share/sdcc/lib/src

%files 
%_bindir/*
%_datadir/%name/*
%_docdir/%name-%version/*
# The package does not own its own docdir subdirectory.
# The line below is added by repocop to fix this bug in a straightforward way. 
# Another way is to rewrite the spec to use relative doc paths.
%dir %_docdir/sdcc-%version 


%changelog
* Wed Jun 20 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 5119-alt1.qa2
- Fixed build with glibc 2.11.3

* Tue Nov 10 2009 Repocop Q. A. Robot <repocop@altlinux.org> 5119-alt1.qa1
- NMU (by repocop): the following fixes applied:
  * docdir-is-not-owned for sdcc
  * postclean-05-filetriggers for spec file

* Fri Mar 28 2008 Yury A. Romanov <damned@altlinux.ru> 5119-alt1
- 5119

* Thu Jan 03 2008 Yury A. Romanov <damned@altlinux.ru> 4988-alt1
- Initial build

