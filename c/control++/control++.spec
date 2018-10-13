%define libcontrolppver 0.14

Name: control++
Version: 0.11.0
Release: alt1

Summary: System configuration tool
License: GPLv3
Group: System/Configuration/Other
Url: https://www.altlinux.org/Control++

Packager: Alexey Appolonov <alexey@altlinux.org>

# http://git.altlinux.org/people/alexey/packages/?p=controlplusplus.git
Source: %name-%version.tar

BuildRequires: gcc-c++
BuildRequires: libcontrol++-devel >= %libcontrolppver

ExcludeArch: aarch64

%description
control++ is a simple system configuration tool
that allows administrator to change system ulimits,
set permission modes and, in perspective,
perform other administrative operations.

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

%prep
%setup

%build
mkdir -p bin/Release
mkdir -p obj/Release
%make_build -C control++/ release

%install
mkdir -p %buildroot%_bindir
mkdir -p %buildroot%_docdir/%name
mkdir -p %buildroot%_sysconfdir/%name
# Executables
cp control++/bin/Release/%name %buildroot%_bindir
# Configuration
cp -r samples/* %buildroot%_sysconfdir/%name
# Dirs for generated files
mkdir -p %buildroot%_localstatedir/%name/ulimits
mkdir %buildroot%_localstatedir/%name/permissions
# Documentation
cp COPYING %buildroot%_defaultdocdir/%name/
cp usage.txt %buildroot%_defaultdocdir/%name/
cp readme.txt %buildroot%_defaultdocdir/%name/

%files
%_bindir/%name
%_sysconfdir/%name
%_localstatedir/%name
%_defaultdocdir/%name

%changelog
* Mon Oct 15 2018 Alexey Appolonov <alexey@altlinux.org> 0.11.0-alt1
- Pass setting/checking mode for non existent files;
- It's OK to not have 'reset' file if current mode is not stated;
- Terminating if main or internal conf are not accessible;
- Generated files are stored in /var/lib/control++;
- New functionality of the libcontrol++ TPrinter;
- Adjusted dialogs.

* Mon Oct 1 2018 Alexey Appolonov <alexey@altlinux.org> 0.10.0-alt1
- Units can have many config files;
- Determining available modes by the units themselves;
- Ability to not specify some of the submodes;
- Ability to state '*' bit (that means don't change) in permission mode
  or as owner or group, not stated owner/group is '*' owner/group;
- Ability to change mode for all files of the dir, ability to state different
  modes for nested dirs, ability to change mode for the dir recursively;
- Implementation of the black/white list concept;
- Every unit can reset it's mode (restore the state that held before
  the current mode was set);
- Every unit must reset the current mode before setting up the new one;
- Every unit can check current mode compliance;
- Storing current mode and all the submodes in the internal configuration file
  used for compliance-checking;
- Starter unit is running 'do' file when setting up a mode;
- There is no default mode anymore;
- Term 'corrupted mode' is discarded;
- Proper feedback by all units;
- Delegating some of the functions and classes to the libcontol++;
- Russian manual.

* Wed Aug 08 2018 Alexey Appolonov <alexey@altlinux.org> 0.9.2-alt2
- libcontrol++ is a separate package now.

* Wed Aug 08 2018 Alexey Appolonov <alexey@altlinux.org> 0.9.2-alt1
- Fix of the "starter" unit;
- Excluding aarch64.

* Sat Jun 02 2018 Alexey Appolonov <alexey@altlinux.org> 0.9.1-alt1
- Memory leakage fix.

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
