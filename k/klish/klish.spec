%define _unpackaged_files_terminate_build 1

Name: klish
Version: 2.2.4
Release: alt1

Summary: A framework for implementing a CISCO-like CLI on a UNIX systems

Group: System/Configuration/Other
License: BSD-like
Url: http://libcode.org/projects/klish/

Packager: Paul Wolneykien <manowar@altlinux.org>

Source0: %name-%version.tar
Source1: %name.watch

BuildRequires: libexpat-devel

%description
The klish is a framework for implementing a CISCO-like CLI on a UNIX
systems. It is configurable by XML files. The KLISH stands for Kommand
Line Interface Shell.

%package konfd
Group: System/Configuration/Other
License: BSD-like
Summary: The 'konfd' daemon to store/merge the user configuration commands

%description konfd
The klish is a framework for implementing a CISCO-like CLI on a UNIX
systems. It is configurable by XML files. The KLISH stands for Kommand
Line Interface Shell.

This package contains:

  * 'konfd' daemon to store/merge the user configuration commands;
  * 'konf' util to access the daemon.

%package libclish
Group: System/Configuration/Other
License: BSD-like
Summary: A library for implementing a CISCO-like CLI on a UNIX systems

%description libclish
The klish is a framework for implementing a CISCO-like CLI on a UNIX
systems. It is configurable by XML files. The KLISH stands for Kommand
Line Interface Shell.

This package contains the clish "CLI Shell" library.

The library provides the core functionality for a shell to implement a 
CISCO-like user interface. The look and feel is fully defined by a set of
XML files which are loaded when the shell starts up.

The schema for these XML files can be found in 

http://clish.sourceforge.net/XMLSchema/clish.xsd

and in the %name-doc package.

%package libclish-devel
Group: System/Configuration/Other
License: BSD-like
Summary: A library for implementing a CISCO-like CLI on a UNIX systems (development files)

%description libclish-devel
The klish is a framework for implementing a CISCO-like CLI on a UNIX
systems. It is configurable by XML files. The KLISH stands for Kommand
Line Interface Shell.

This package contains the development files for the clish "CLI Shell"
library.

The library provides the core functionality for a shell to implement a 
CISCO-like user interface. The look and feel is fully defined by a set of
XML files which are loaded when the shell starts up.

The schema for these XML files can be found in 
http://clish.sourceforge.net/XMLSchema/clish.xsd

%package libkonf
Group: System/Configuration/Other
License: BSD-like
Summary: Configuration library for the 'klish' CISCO-like CLI framework

%description libkonf
The klish is a framework for implementing a CISCO-like CLI on a UNIX
systems. It is configurable by XML files. The KLISH stands for Kommand
Line Interface Shell.

This package contains the configuration library for the 'klish'
CISCO-like CLI framework.

%package libkonf-devel
Group: System/Configuration/Other
License: BSD-like
Summary: Configuration library for the 'klish' CISCO-like CLI framework (development files)

%description libkonf-devel
The klish is a framework for implementing a CISCO-like CLI on a UNIX
systems. It is configurable by XML files. The KLISH stands for Kommand
Line Interface Shell.

This package contains the development files for the configuration
library for the 'klish' CISCO-like CLI framework.

%package liblub
Group: System/Configuration/Other
License: BSD-like
Summary: General-purpose library for the 'klish' CISCO-like CLI framework

%description liblub
The klish is a framework for implementing a CISCO-like CLI on a UNIX
systems. It is configurable by XML files. The KLISH stands for Kommand
Line Interface Shell.

This package contains the "Little Useful Bits" library. Is is a general
purpose library of small utilities. The design and implementation are
intended for embedded devices, ie. minimise footprint and maximise
performance.

%package liblub-devel
Group: System/Configuration/Other
License: BSD-like
Summary: General-purpose library for the 'klish' CISCO-like CLI framework (development files)

%description liblub-devel
The klish is a framework for implementing a CISCO-like CLI on a UNIX
systems. It is configurable by XML files. The KLISH stands for Kommand
Line Interface Shell.

This package contains the "Little Useful Bits" library. Is is a general
purpose library of small utilities. The design and implementation are
intended for embedded devices, ie. minimise footprint and maximise
performance.

%package libtinyrl
Group: System/Configuration/Other
License: BSD-like
Summary: A readline replacement library for the 'klish' CISCO-like CLI framework

%description libtinyrl
The klish is a framework for implementing a CISCO-like CLI on a UNIX
systems. It is configurable by XML files. The KLISH stands for Kommand
Line Interface Shell.

This package contains the "Tiny Readline" library.

The library provides a simple replacement of the "readline" functionality.
(The readline interface and implementation has some fundamental flaws when
it comes to try and run it within a single memory space envrioment.)

%package libtinyrl-devel
Group: System/Configuration/Other
License: BSD-like
Summary: A readline replacement library for the 'klish' CISCO-like CLI framework (development files)

%description libtinyrl-devel
The klish is a framework for implementing a CISCO-like CLI on a UNIX
systems. It is configurable by XML files. The KLISH stands for Kommand
Line Interface Shell.

This package contains the "Tiny Readline" library.

The library provides a simple replacement of the "readline" functionality.

%package doc
Group: System/Configuration/Other
License: BSD-like
Summary: Documentation for the 'klish' CISCO-like CLI framework

%description doc
The klish is a framework for implementing a CISCO-like CLI on a UNIX
systems. It is configurable by XML files. The KLISH stands for Kommand
Line Interface Shell.

This package contains the package documentation, the clish XML Schema
file and the example CLI description files. To run the example CISCO-like
CLI use

  clish -x %_docdir/%name-%version/clish

See %_docdir/%name-%version for other examples.

%prep
%setup -q -n %name-%version

%build
%autoreconf
%configure --disable-static
%make_build

%install
%makeinstall_std

%files
%_bindir/clish

%files konfd
%_bindir/konfd
%_bindir/konf
%exclude %_bindir/sigexec

%files libclish
%_libdir/libclish*.so.*
%_libdir/clish_plugin_clish.so
%_libdir/clish_plugin_clish.la

%files libclish-devel
%_includedir/clish/*.h
%_libdir/libclish*.so

%files libkonf
%_libdir/libkonf*.so.*

%files libkonf-devel
%_includedir/konf/*.h
%_libdir/libkonf*.so

%files liblub
%_libdir/liblub*.so.*

%files liblub-devel
%_includedir/lub/*.h
%_libdir/liblub*.so

%files libtinyrl
%_libdir/libtinyrl*.so.*

%files libtinyrl-devel
%_includedir/tinyrl/*.h
%_libdir/libtinyrl*.so

%files doc
%doc README
%doc clish.xsd
%doc xml-examples/clish
%doc xml-examples/klish

%changelog
* Tue Oct 19 2021 Paul Wolneykien <manowar@altlinux.org> 2.2.4-alt1
- New version 2.2.4.
- Update paths of the libraries (now they are in %%_libdir).
- Disable static.

* Mon Jul 28 2014 Paul Wolneykien <manowar@altlinux.org> 1.6.8-alt2
- FR fix: Include the klish-specific examples into the doc package
  (closes #30209).

* Thu Jul 10 2014 Paul Wolneykien <manowar@altlinux.org> 1.6.8-alt1
- Freshed up to v1.6.8 with the help of cronbuild and update-source-functions.

