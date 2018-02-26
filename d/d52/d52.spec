Name: d52
Version: 3.4.1
License: GPL
Group: Development/Other
Release: alt1.qa1
Source: %name.tar
BuildPreReq: gcc
Summary: D52 Microcontroller Disassemblers
%description
8051/8052/8035/8048/Z80 Disassemblers
Disassemblers for 8051/8052/8035/8048/Z80 microcomputers. C
source code released under GNU General Public License. Includes
executable code for DOS/Windows and Linux.

%prep
%setup -q -n %name
%build
mkdir -p obj
%make all
%install
%make DESTDIR=%buildroot install
%files
%_bindir/*
%_docdir/%name-%version/*
# The package does not own its own docdir subdirectory.
# The line below is added by repocop to fix this bug in a straightforward way. 
# Another way is to rewrite the spec to use relative doc paths.
%dir %_docdir/d52-%version 
%changelog
* Wed Feb 03 2010 Repocop Q. A. Robot <repocop@altlinux.org> 3.4.1-alt1.qa1
- NMU (by repocop): the following fixes applied:
  * docdir-is-not-owned for d52
  * postclean-05-filetriggers for spec file

* Sat Jan 05 2008 Yury A. Romanov <damned@altlinux.ru> 3.4.1-alt1
- Initial build

