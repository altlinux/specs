%def_without alsa

%define teaname snack

Name: tcl-snack
Version: 2.2.10
Release: alt4

Summary: Snack - a sound toolkit for scripting languages
License: GPL
Group: Development/Tcl
Url: http://www.speech.kth.se/snack/

Source: %name-%version-%release.tar

Requires: tcl >= 8.4.0-alt1 tcl-sound = %version-%release

BuildRequires: libogg-devel libvorbis-devel tcl-devel >= 8.4.16-alt1 tk-devel >= 8.4.16-alt1
%if_with alsa
BuildRequires: libalsa-devel
%endif

Provides: %teaname
Obsoletes: %teaname

%package -n tcl-sound
Summary: Snack - a sound toolkit for scripting languages
License: GPL
Group: Development/Tcl

%package demos
Summary: A collection of programs to demonstrate the features of the Snack
Group: Development/Tcl
Requires: %name = %version-%release tk >= 8.4.0-alt1
Provides: %teaname-demos
Obsoletes: %teaname-demos

%description
Snack is a sound processing toolkit designed as an extension
to a scripting language. Snack currently works with the scripting
languages Tcl/Tk, Python and Ruby.

This package contains snack Tcl extension.

%description -n tcl-sound
Snack is a sound processing toolkit designed as an extension
to a scripting language. Snack currently works with the scripting
languages Tcl/Tk, Python and Ruby.

This package contains sound Tcl extension.

%description demos
Snack is a sound processing toolkit designed as an extension
to a scripting language. Snack currently works with the scripting
languages Tcl/Tk, Python and Ruby.

This package contains a collection of programs to demonstrate
the features of Snack

%prep
%setup

%build
cd unix
%add_optflags %optflags_debug
%configure \
    --with-tcl=%_libdir \
    --with-tk=%_libdir \
    --with-ogg-lib=%_libdir \
    --with-ogg-include=%_includedir \
    %{?_with_alsa:--enable-alsa} \
    #
%make_build

%install
mkdir -p %buildroot%_tcllibdir
install -pm0644 unix/libs*.so %buildroot%_tcllibdir

sed -i 's/@lib@/%_lib/' unix/pkgIndex.tcl.dll unix/pkgIndex.tcl.sound
install -pm0644 -D unix/pkgIndex.tcl.sound %buildroot%_tcldatadir/sound%version/pkgIndex.tcl
install -pm0644 -D unix/pkgIndex.tcl.dll %buildroot%_tcldatadir/%teaname%version/pkgIndex.tcl
install -pm0644 unix/snack.tcl %buildroot%_tcldatadir/%teaname%version

rm -f demos/tcl/{freewrap,tclkit*,sdx}
find demos/tcl -type f -name '*.tcl' | xargs sed -i '1,3d'
mkdir -p %buildroot%_tcldatadir/%teaname%version/demos
install -pm0644 demos/tcl/* %buildroot%_tcldatadir/%teaname%version/demos/

chmod 0644 doc/*

%files
%doc COPYING README
%doc doc/* 
%_tcllibdir/libsnack.so
%_tcllibdir/libsnackogg.so
%_tcldatadir/%teaname%version
%exclude %_tcldatadir/%teaname%version/demos

%files -n tcl-sound
%_tcllibdir/libsound.so
%_tcldatadir/sound%version/*

%files demos
%_tcldatadir/%teaname%version/demos

%changelog
* Sun May 10 2009 Sergey Bolshakov <sbolshakov@altlinux.ru> 2.2.10-alt4
- rebuilt with new gcc

* Wed Nov 21 2007 Sergey Bolshakov <sbolshakov@altlinux.ru> 2.2.10-alt3
- fixed package index to load sound subpackage before snack

* Fri Oct 19 2007 Sergey Bolshakov <sbolshakov@altlinux.ru> 2.2.10-alt2
- rebuilt according to updated rpm-build-tcl

* Sat Jul 22 2006 Sergey Bolshakov <sbolshakov@altlinux.ru> 2.2.10-alt1
- 2.2.10

* Wed Dec 22 2004 Sergey Bolshakov <sbolshakov@altlinux.ru> 2.2.9-alt1
- 2.2.9

* Fri May 14 2004 Sergey Bolshakov <sbolshakov@altlinux.ru> 2.2.5-alt1
- 2.2.5
- sound subpackage
- eliminated code duplication in snack and sound

* Fri Dec 12 2003 Sergey Bolshakov <sbolshakov@altlinux.ru> 2.2.3-alt1
- 2.2.3

* Sat Jul 12 2003 Sergey Bolshakov <s.bolshakov@sam-solutions.net> 2.2.2-alt1
- 2.2.2

* Tue Mar 11 2003 Sergey Bolshakov <s.bolshakov@sam-solutions.net> 2.2-alt3
- 2.2.1 release

* Mon Sep 30 2002 Sergey Bolshakov <s.bolshakov@belcaf.com> 2.2-alt2
- 2.2b1

* Sat May 18 2002 Sergey Bolshakov <s.bolshakov@belcaf.com> 2.2-alt1
- 2.2a1

* Fri Nov 30 2001 Sergey Bolshakov <s.bolshakov@belcaf.com> 2.1.4-alt2
- fixed requires in demos subpackage

* Wed Nov 28 2001 Sergey Bolshakov <s.bolshakov@belcaf.com>  2.1.4-alt1
- Initial build for ALT Linux distribution.

