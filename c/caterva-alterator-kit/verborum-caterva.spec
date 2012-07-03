Name: caterva-alterator-kit
Version: 2.0
Release: alt1

Source:%name-%version.tar.gz

Packager: Paul Wolneykien <manowar@altlinux.ru>

Summary: Alterator communication library for Verborum Caterva generators
License: GPL
Group: System/Base
BuildArch: noarch

# Automatically added by buildreq on Thu Apr 09 2009
BuildRequires: rpm-macros-alterator rpm-macros-fillup

%description
Verborum Caterva is a simple engine for arbitrary file structure
generation. This library provides a set of functions for communication
with Alterator backends from a Caterva generator script.

%package sh
Summary: Alterator communication library for Verborum Caterva generators
Group: System/Base
BuildArch: noarch

Requires: alterator >= 4.8-alt1
Conflicts: alterator >= 5.0

%description sh
Verborum Caterva is a simple engine for arbitrary file structure
generation. This library provides a set of Shell-scripting functions
for communication with Alterator backends from a Caterva generator script.

%prep
%setup -q

%install
install -p -m0755 -D caterva-alterator.sh %buildroot%_bindir/caterva-alterator.sh

%files sh
%_bindir/caterva-alterator.sh

%changelog
* Fri May 29 2009 Paul Wolneykien <manowar@altlinux.ru> 2.0-alt1
- Do not use obsolete value table framework.

* Wed Apr 15 2009 Paul Wolneykien <manowar@altlinux.ru> 1.0-alt5
- Default value for the status variable.

* Wed Apr 15 2009 Paul Wolneykien <manowar@altlinux.ru> 1.0-alt4
- Fix handler run on an empty object.

* Sun Apr 12 2009 Paul Wolneykien <manowar@altlinux.ru> 1.0-alt3
- Use shell-config to access the value table.

* Fri Apr 10 2009 Paul Wolneykien <manowar@altlinux.ru> 1.0-alt2
- Unset variables after handler has been called.

* Wed Apr 08 2009 Paul Wolneykien <manowar@altlinux.ru> 1.0-alt1
- Initial release.
