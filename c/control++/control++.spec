Name: control++
Version: 0.9.0
Release: alt1

Summary: System configuration tool
License: GPLv3
Group: System/Configuration/Other
Url: https://www.altlinux.org/Control++

Packager: Alexey Appolonov <alexey@altlinux.org>

# http://git.altlinux.org/people/alexey/packages/?p=controlplusplus.git
Source: %name-%version.tar

BuildRequires: gcc-c++

%description
control++ is a simple system configuration tool
that allows administrator to change system ulimits,
set permission modes and, in perspective,
perform other administrative operations.

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# libcontrol++

%package -n libcontrol++
Summary: control++ common classes and functions library
Group: Development/Other

%define libcontrol++_desc \
libcontrol++ provides common classes and functions,\
that can be used in other app\
(such as ini-parser or file-operations).

%description -n libcontrol++
%libcontrol++_desc

%package -n libcontrol++-devel
Summary: libcontrol++ headers
Group: Development/Other
Requires: libcontrol++

%description -n libcontrol++-devel
Development package for libcontrol++.
%libcontrol++_desc

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

%prep
%setup

%build
mkdir -p bin/Release
mkdir -p obj/Release
%make_build -C libcontrol++/ release
export CFLAGS="-iquote ../libcontrol++/src"
%make_build -C control++/ release LDFLAGS="-L../libcontrol++/bin/Release/ -lcontrol++"

%install
mkdir -p %buildroot%_bindir
mkdir -p %buildroot%_libdir
mkdir -p %buildroot%_includedir/libcontrol++
mkdir -p %buildroot%_docdir/%name
mkdir -p %buildroot%_sysconfdir/%name
# Executables
cp control++/bin/Release/%name %buildroot%_bindir
cp libcontrol++/bin/Release/libcontrol++.so %buildroot%_libdir
# Includes
cp libcontrol++/src/*.h %buildroot%_includedir/libcontrol++
# Configuration
cp -r samples/* %buildroot%_sysconfdir/%name
# Documentation
cp COPYING %buildroot%_defaultdocdir/%name/
cp usage.txt %buildroot%_defaultdocdir/%name/

%files
%_bindir/%name
%_sysconfdir/%name
%_defaultdocdir/%name/

%files -n libcontrol++
%_libdir/*.so

%files -n libcontrol++-devel
%_includedir/libcontrol++/

%changelog
* Mon May 21 2018 Alexey Appolonov <alexey@altlinux.org> 0.9.0-alt1
- New libcontrol++ features.

* Fri Mar 16 2018 Alexey Appolonov <alexey@altlinux.org> 0.8.0-alt1
- New libcontrol++ features.

* Mon Feb 26 2018 Alexey Appolonov <alexey@altlinux.org> 0.7.0-alt1
- New libcontrol++ features.

* Wed Feb 14 2018 Alexey Appolonov <alexey@altlinux.org> 0.6.0-alt1
- Common classes and functions that can be used in other projects
  compiled as libcontrol++.so
  therefore libcontrol++ and libcontrol++-devel subpackages.

* Fri Jan 26 2018 Alexey Appolonov <alexey@altlinux.org> 0.5.1-alt1
- Code restyling.
- Minor changes in units handling.

* Mon Dec 11 2017 Alexey Appolonov <alexey@altlinux.org> 0.5.0-alt1
- New unit, that runs script stated in configuration file.

* Mon Dec 4 2017 Alexey Appolonov <alexey@altlinux.org> 0.4.2-alt1
- Handling of values in quotes in configuration files.
- Verbose output with -v param when setting mode.

* Thu Nov 30 2017 Alexey Appolonov <alexey@altlinux.org> 0.4.1-alt1
- Comment lines passing in configuration files.

* Thu Nov 30 2017 Alexey Appolonov <alexey@altlinux.org> 0.4.0-alt1
- Ability to set permission modes.

* Mon Nov 27 2017 Alexey Appolonov <alexey@altlinux.org> 0.3.0-alt1
- Restructure for better extensibility.

* Mon Nov 27 2017 Alexey Appolonov <alexey@altlinux.org> 0.2.0-alt1
- Support of INI file format for the configuration file. 

* Fri Nov 17 2017 Alexey Appolonov <alexey@altlinux.org> 0.1.0-alt1
- Initial ALT Linux release.
