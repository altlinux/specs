Name: control++
Version: 0.5.1
Release: alt1

Summary: System configuration tool
License: GPLv3
Group: System/Configuration/Other
Url: https://www.altlinux.org/Control%2B%2B

Packager: Alexey Appolonov <alexey@altlinux.org>

# http://git.altlinux.org/people/alexey/packages/?p=controlplusplus.git
Source: %name-%version.tar

BuildRequires: gcc-c++

%description
control++ is a simple system configuration tool
that allows administrator to change system ulimits,
set permission modes and, in perspective,
perform other administrative operations.

%prep
%setup

%build
mkdir -p bin/Release
mkdir -p obj/Release
%make_build release

%install
mkdir -p %buildroot%_bindir
mkdir -p %buildroot%_docdir/%name
mkdir -p %buildroot%_sysconfdir/%name
cp bin/Release/%name %buildroot%_bindir
cp -r samples/* %buildroot%_sysconfdir/%name
cp COPYING %buildroot%_defaultdocdir/%name/
cp usage.txt %buildroot%_defaultdocdir/%name/

%files
%_bindir/%name
%_sysconfdir/%name
%_defaultdocdir/%name/

%changelog
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
