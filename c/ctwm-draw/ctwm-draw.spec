Name:   ctwm-draw
Version:        0.1
Release:        alt1
Summary:        CTWM titile buttons draw companion
Source:         %name-%version.tar
Group:          System/X11
License:        MIT
BuildRequires:  flex bison

%description
A tiny XPM generator based on uneasy input syntax description.
Mainly used for drawing CTWM title buttons.

%prep
%setup

%build
%make

%install
install -D draw %buildroot%_bindir/%name

%files
%_bindir/*

%changelog
* Sun Jun 28 2026 Fr. Br. George <george@altlinux.org> 0.1-alt1
- Initial build
