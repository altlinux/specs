%def_disable static

Name: embryo
Version: 1.2.0
%ifdef beta
Release: alt1.%beta
%else
Release: alt1
%endif

Summary: A small virtual machine engine (in a library) and bytecode compiler
License: BSD
Group: System/Libraries
URL: http://www.enlightenment.org/

Source: http://download.enlightenment.org/releases/%name-%version.tar.bz2

BuildRequires: libeina-devel >= 1.2.0
%{?_enable_static:BuildPreReq: glibc-devel-static}

%description
Embryo is primarily a shared library that gives you an API to load and control
interpredted programs compiled into the abstract machine bytecode that it
understands. This abstrac (or virtual) machine is imilar to a real machin
with a CPU, but it is emulated in software. The architecture is simple and is
the same as the abstract machine (AMX) in the
http://www.compuphase.com/small.htm language as it is based
on exactly the same code. Embryo has modified the code for the AMX extensively
and has made it smaller and more portable. It is VERY small. The total size
of the virtual machine code AND header files is less than 2500 lines of code.
It includes the floating point library support by default as well. This makes
it one of the smallest interpreting engines around, and thus makes is very
efficient to use in code.

%package -n %{name}_cc
Summary: Embryo compiler
Group: Development/Other

%description -n %{name}_cc
Embryo is primarily a shared library that gives you an API to load and control
interpredted programs compiled into the abstract machine bytecode that it
understands. This abstrac (or virtual) machine is imilar to a real machin
with a CPU, but it is emulated in software. The architecture is simple and is
the same as the abstract machine (AMX) in the
http://www.compuphase.com/small.htm language as it is based
on exactly the same code. Embryo has modified the code for the AMX extensively
and has made it smaller and more portable. It is VERY small. The total size
of the virtual machine code AND header files is less than 2500 lines of code.
It includes the floating point library support by default as well. This makes
it one of the smallest interpreting engines around, and thus makes is very
efficient to use in code.

This package contains embryo compiler.

%package -n lib%name
Summary: embryo library
Group: System/Libraries

%description -n lib%name
Embryo is primarily a shared library that gives you an API to load and control
interpredted programs compiled into the abstract machine bytecode that it
understands. This abstrac (or virtual) machine is imilar to a real machin
with a CPU, but it is emulated in software. The architecture is simple and is
the same as the abstract machine (AMX) in the
http://www.compuphase.com/small.htm language as it is based
on exactly the same code. Embryo has modified the code for the AMX extensively
and has made it smaller and more portable. It is VERY small. The total size
of the virtual machine code AND header files is less than 2500 lines of code.
It includes the floating point library support by default as well. This makes
it one of the smallest interpreting engines around, and thus makes is very
efficient to use in code.

This package contains shared embryo library.

%package -n lib%name-devel
Summary: embryo headers and development libraries
Group: Development/C
Requires: lib%name = %version

%description -n lib%name-devel
Embryo is primarily a shared library that gives you an API to load and control
interpredted programs compiled into the abstract machine bytecode that it
understands. This abstrac (or virtual) machine is imilar to a real machin
with a CPU, but it is emulated in software. The architecture is simple and is
the same as the abstract machine (AMX) in the
http://www.compuphase.com/small.htm language as it is based
on exactly the same code. Embryo has modified the code for the AMX extensively
and has made it smaller and more portable. It is VERY small. The total size
of the virtual machine code AND header files is less than 2500 lines of code.
It includes the floating point library support by default as well. This makes
it one of the smallest interpreting engines around, and thus makes is very
efficient to use in code.

This package contains embryo headers and development libraries

%package -n lib%name-devel-static
Summary: embryo static libraries
Group: Development/C
Requires: lib%name-devel = %version

%description -n lib%name-devel-static
Embryo is primarily a shared library that gives you an API to load and control
interpredted programs compiled into the abstract machine bytecode that it
understands. This abstrac (or virtual) machine is imilar to a real machin
with a CPU, but it is emulated in software. The architecture is simple and is
the same as the abstract machine (AMX) in the
http://www.compuphase.com/small.htm language as it is based
on exactly the same code. Embryo has modified the code for the AMX extensively
and has made it smaller and more portable. It is VERY small. The total size
of the virtual machine code AND header files is less than 2500 lines of code.
It includes the floating point library support by default as well. This makes
it one of the smallest interpreting engines around, and thus makes is very
efficient to use in code.

This package contains static libraries

%prep
%ifdef beta
%setup -q -n %name-%version.%beta
%else
%setup -q
%endif

%build
%autoreconf
%{?!_enable_static:export lt_cv_prog_cc_static_works=no}
%configure %{subst_enable static}
%make_build

%install
%make_install DESTDIR=%buildroot install

%files -n %{name}_cc
%_bindir/%{name}_cc

%files -n lib%name
%_libdir/*.so.*
%_datadir/%name
%doc AUTHORS COPYING INSTALL README

%files -n lib%name-devel
%_includedir/*
%_pkgconfigdir/*.pc
%_libdir/*.so

%if_enabled static
%files -n lib%name-devel-static
%_libdir/*.a
%endif

%changelog
* Fri May 11 2012 Yuri N. Sedunov <aris@altlinux.org> 1.2.0-alt1
- 1.2.0

* Mon Jan 16 2012 Yuri N. Sedunov <aris@altlinux.org> 1.1.0-alt2
- used %%autoreconf to fix RPATH problem

* Mon Dec 05 2011 Yuri N. Sedunov <aris@altlinux.org> 1.1.0-alt1
- 1.1.0

* Tue May 03 2011 Yuri N. Sedunov <aris@altlinux.org> 1.0.0-alt5
- rebuilt for debuginfo

* Sun Jan 30 2011 Yuri N. Sedunov <aris@altlinux.org> 1.0.0-alt4
- 1.0.0 release

* Thu Nov 18 2010 Yuri N. Sedunov <aris@altlinux.org> 1.0.0-alt3.beta2
- 1.0.0.beta2

* Tue Nov 09 2010 Yuri N. Sedunov <aris@altlinux.org> 1.0.0-alt2.beta
- rebuild for update dependencies

* Fri Oct 29 2010 Yuri N. Sedunov <aris@altlinux.org> 1.0.0-alt1.beta
- 1.0.0.beta

* Mon Jan 04 2010 Yuri N. Sedunov <aris@altlinux.org> 0.9.9.063-alt1
- 0.9.9.063

* Tue Nov 10 2009 Yuri N. Sedunov <aris@altlinux.org> 0.9.9.062-alt1
- new version
- removed obsolete %%post{,un}_ldconfig

* Sat Oct 18 2008 Yuri N. Sedunov <aris@altlinux.org> 0.9.9.050-alt1
- 0.9.9.050

* Thu Apr 03 2008 Igor Androsov <blake@altlinux.org> 0.9.1.042-alt1.20080410
- CVS from 20080410 

* Mon Sep 17 2007 Pavlov Konstantin <thresh@altlinux.ru> 0.9.1.041-alt1.20070917
- CVS from 20070917.

* Thu Sep 06 2007 Pavlov Konstantin <thresh@altlinux.ru> 0.9.1.041-alt1.20070905
- CVS from 20070905.

* Tue Jul 31 2007 Pavlov Konstantin <thresh@altlinux.ru> 0.9.1.040-alt1.20070731
- CVS from 20070731.

* Thu May 10 2007 Pavlov Konstantin <thresh@altlinux.ru> 0.9.1.038-alt2.20070509
- Removed embryo subpackage (it was empty, actually).
- Moved datadir/embryo to libembryo.

* Wed May 09 2007 Pavlov Konstantin <thresh@altlinux.ru> 0.9.1.038-alt1.20070509
- CVS from 20070509.

* Wed Sep 20 2006 Igor Zubkov <icesik@altlinux.org> 0.9.1.032-alt1.20060920
- 20060910 -> 20060920

* Tue Sep 12 2006 Igor Zubkov <icesik@altlinux.org> 0.9.1.032-alt1.20060910
- update from cvs (0.9.1.026 20060412 -> 0.9.1.032 20060910)
- buildreq

* Fri Apr 14 2006 Igor Zubkov <icesik@altlinux.ru> 0.9.1.026-alt1.20060412
- updated from cvs

* Thu Apr 06 2006 Igor Zubkov <icesik@altlinux.ru> 0.9.1-alt0.2_003_20060327
- updated from cvs
- buildreq

* Mon May 30 2005 Denis Klykvin <nikon@altlinux.ru> 0.9.1-alt0.2_003_20050530
- updated from cvs.

* Tue May 24 2005 Denis Klykvin <nikon@altlinux.ru> 0.9.1-alt0.2_003_20050524
- updated from cvs.

* Mon May 16 2005 Denis Klykvin <nikon@altlinux.ru> 0.9.1-alt0.2_003_20050516
- updated from cvs.

* Sat May 14 2005 Denis Klykvin <nikon@altlinux.ru> 0.9.1-alt0.2_003_20050514
- updated from cvs.

* Thu Apr 28 2005 Denis Klykvin <nikon@altlinux.ru> 0.9.1-alt0.2_003_20050428
- updated from cvs.
- minor spec fixes.

* Mon Apr 25 2005 Denis Klykvin <nikon@altlinux.ru> 0.9.1-alt0.2_003_20050425
- updated from cvs.

* Thu Apr 21 2005 Denis Klykvin <nikon@altlinux.ru> 0.9.1-alt0.2_003_20050421
- updated from cvs

* Tue Mar 29 2005 Alex Murygin <murygin@altlinux.ru> 0.9.1-alt0.2_003_20050329
- updated from cvs.

* Sat Jan 22 2005 Alex Murygin <murygin@altlinux.ru> 0.9.1-alt0.1_20050122
- updated from cvs.

* Tue Dec 28 2004 Alex Murygin <murygin@altlinux.ru> 0.9.1-alt0.1_20041228
- updated from cvs.

* Fri Dec 17 2004 Alex Murygin <murygin@altlinux.ru> 0.9.1-alt0.1_20041216
- updated from cvs.

* Sun Oct 24 2004 Alex Murygin <murygin@altlinux.ru> 0.9.1-alt0.1_20041022
- first spec for Sisyphus

