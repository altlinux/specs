Name: Nuklear
Version: 4.13.3
Release: alt1
Summary: Immediate-mode graphical user interface toolkit
License: MIT
Group: System/Libraries
BuildRequires: python3-dev

Source: %name-%version.tar
BuildArch: noarch
%description
This is a minimal-state, immediate-mode graphical
user interface toolkit written in ANSI C and
licensed under public domain. It was designed as a simple
embeddable user interface for application and
does not have any dependencies, a default render backend
or OS window/input handling but instead provides a highly modular,
library-based approach, with simple input state for input and draw
commands describing primitive shapes as output.
So instead of providing a layered library that tries to abstract
over a number of platform and render backends, it focuses only on the actual UI.

%prep
%setup -n %name-%version

%build

make nuke

%install

mkdir -p %buildroot{%_includedir,%_docdir}
install -m644 nuklear.h %buildroot%_includedir
install -m644 Readme.md %buildroot%_docdir/Readme.md

%files
%_docdir/Readme.md
%_includedir/nuklear.h

%changelog
* Thu May  7 2026 Artyom Bystrov <arbars@altlinux.org> 4.13.3-alt1
- Update to new version

* Thu Apr  9 2026 Artyom Bystrov <arbars@altlinux.org> 4.13.2-alt1
- Initial build for ALT
